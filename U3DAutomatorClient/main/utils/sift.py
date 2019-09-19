#!/usr/bin/env python
# coding=utf-8
import cv2

def find_sift(im_source, im_search, threshold=0.8, rgb=True, good_ratio=FILTER_RATIO):
    """基于sift进行图像识别，只筛选出最优区域."""
    # 第一步：检验图像是否正常：
    if not check_image_valid(im_source, im_search):
        return None

    # 第二步：获取特征点集并匹配出特征点对: 返回值 good, pypts, kp_sch, kp_src
    kp_sch, kp_src, good = _get_key_points(im_source, im_search, good_ratio)

    # 第三步：根据匹配点对(good),提取出来识别区域:
    if len(good) == 0:
        # 匹配点对为0,无法提取识别区域：
        return None
    elif len(good) == 1:
        # 匹配点对为1，可信度赋予设定值，并直接返回:
        return _handle_one_good_points(kp_src, good, threshold) if ONE_POINT_CONFI >= threshold else None
    elif len(good) == 2:
        # 匹配点对为2，根据点对求出目标区域，据此算出可信度：
        origin_result = _handle_two_good_points(im_source, im_search, kp_src, kp_sch, good)
        if isinstance(origin_result, dict):
            return origin_result if ONE_POINT_CONFI >= threshold else None
        else:
            middle_point, pypts, w_h_range = _handle_two_good_points(im_source, im_search, kp_src, kp_sch, good)
    elif len(good) == 3:
        # 匹配点对为3，取出点对，求出目标区域，据此算出可信度：
        origin_result = _handle_three_good_points(im_source, im_search, kp_src, kp_sch, good)
        if isinstance(origin_result, dict):
            return origin_result if ONE_POINT_CONFI >= threshold else None
        else:
            middle_point, pypts, w_h_range = _handle_three_good_points(im_source, im_search, kp_src, kp_sch, good)
    else:
        # 匹配点对 >= 4个，使用单矩阵映射求出目标区域，据此算出可信度：
        middle_point, pypts, w_h_range = _many_good_pts(im_source, im_search, kp_sch, kp_src, good)

    # 第四步：根据识别区域，求出结果可信度，并将结果进行返回:
    # 对识别结果进行合理性校验: 小于5个像素的，或者缩放超过5倍的，一律视为不合法直接raise.
    _target_error_check(w_h_range)
    # 将截图和识别结果缩放到大小一致,准备计算可信度
    x_min, x_max, y_min, y_max, w, h = w_h_range
    target_img = im_source[y_min:y_max, x_min:x_max]
    resize_img = cv2.resize(target_img, (w, h))
    confidence = _cal_sift_confidence(im_search, resize_img, rgb=rgb)

    best_match = generate_result(middle_point, pypts, confidence)
    print("[aircv][sift] threshold=%s, result=%s" % (threshold, best_match))
    return best_match if confidence >= threshold else None




def _get_key_points(im_source, im_search, good_ratio):
    """根据传入图像,计算图像所有的特征点,并得到匹配特征点对."""
    # 准备工作: 初始化sift算子
    sift = _init_sift()
    # 第一步：获取特征点集，并匹配出特征点对: 返回值 good, pypts, kp_sch, kp_src
    kp_sch, des_sch = sift.detectAndCompute(im_search, None)
    kp_src, des_src = sift.detectAndCompute(im_source, None)
    # When apply knnmatch , make sure that number of features in both test and
    #       query image is greater than or equal to number of nearest neighbors in knn match.
    if len(kp_sch) < 2 or len(kp_src) < 2:
        raise NoSiftMatchPointError("Not enough feature points in input images !")

    # 匹配两个图片中的特征点集，k=2表示每个特征点取出2个最匹配的对应点:
    matches = FLANN.knnMatch(des_sch, des_src, k=2)
    good = []
    # good为特征点初选结果，剔除掉前两名匹配太接近的特征点，不是独特优秀的特征点直接筛除(多目标识别情况直接不适用)
    for m, n in matches:
        if m.distance < good_ratio * n.distance:
            good.append(m)
    # good点需要去除重复的部分，（设定源图像不能有重复点）去重时将src图像中的重复点找出即可
    # 去重策略：允许搜索图像对源图像的特征点映射一对多，不允许多对一重复（即不能源图像上一个点对应搜索图像的多个点）
    good_diff, diff_good_point = [], [[]]
    for m in good:
        diff_point = [int(kp_src[m.trainIdx].pt[0]), int(kp_src[m.trainIdx].pt[1])]
        if diff_point not in diff_good_point:
            good_diff.append(m)
            diff_good_point.append(diff_point)
    good = good_diff

    return kp_sch, kp_src, good