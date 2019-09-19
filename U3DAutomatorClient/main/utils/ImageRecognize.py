# coding=utf-8

import cv2
import numpy as np
from PIL import Image
import os,shutil, sys
from win32api import GetSystemMetrics
from main.utils.path import delete_file
from main.log.logger import get_logger

reload(sys)
sys.setdefaultencoding('UTF-8') # 将脚本编码格式转化为指定的编码格式

class ImageRecognize:
    """
        Image.resize can not  satisfy me ,maybe change another way.
    """
    
    def __init__(self):
        pass

    @staticmethod
    def __unite_resolution( sourcePath, srcX, srcY, orientation, targetPath=None,suffix="png"):
        """
        将图片处理成对应分辨率
        :param sourcePath:
        :param srcX:
        :param srcY:
        :param orientation:
        :param targetPath:
        :param suffix:
        :return:
        """
        #ImageRecognize.copypng(sourcePath,targetPath)
        img = Image.open(sourcePath)
        size = img.size
        sizes = [size[0], size[1]]  # 获取图片的宽高

        re_img = None
        if orientation == 1:  # 旋转方向90度
            re_img = img.transpose(Image.ROTATE_90)
            temp = sizes[0]
            sizes[0] = sizes[1]
            sizes[1] = temp
            if srcX != size[1] or srcY != size[0]:
                re_img = re_img.resize((srcX, srcY))
        else:
            if srcX != size[0] or srcY != size[1]:  # 如果图片大小与给定分辨率不一样则将图片变成对应分辨率
                # tmp = int(float(srcX) / size[0] * size[1])
                re_img = img.resize((srcX, srcY))
        if re_img:
            re_img.save(sourcePath, suffix)
        return sizes

    @staticmethod
    def __unite_resolution2( sourcePath, srcX, srcY, orientation, targetPath, suffix="png"):
        """
        将图片处理成对应分辨率
        :param sourcePath:
        :param srcX:
        :param srcY:
        :param orientation:
        :param targetPath:
        :param suffix:
        :return:
        """
        # ImageRecognize.copypng(sourcePath,targetPath)
        img = Image.open(sourcePath)
        size = img.size
        sizes = [size[0], size[1]]  # 获取图片的宽高

        re_img = None
        re_img = img.resize((1680/1920)*size[0], (1680/1920)*size[1],)
        if orientation == 1:  # 旋转方向90度
            re_img = img.transpose(Image.ROTATE_90)
            temp = sizes[0]
            sizes[0] = sizes[1]
            sizes[1] = temp
            if srcX != size[1] or srcY != size[0]:
                re_img = re_img.resize((srcX, srcY))
        else:
            if srcX != size[0] or srcY != size[1]:  # 如果图片大小与给定分辨率不一样则将图片变成对应分辨率
                # tmp = int(float(srcX) / size[0] * size[1])
                re_img = img.resize((srcX, srcY))
        if re_img:
            re_img.save(sourcePath, suffix)
        return sizes

    @staticmethod
    def __unite_resolution_template( templatePath, srcX, srcY, orientation, targetPath=None, suffix="png"):
        """
        将图片处理成对应分辨率
        :param sourcePath:l
        :param srcX:
        :param srcY:
        :param orientation:
        :param targetPath:
        :param suffix:
        :return:
        """
        # ImageRecognize.copypng(sourcePath,targetPath)
        img = Image.open(templatePath)
        size = img.size
        sizes = [size[0], size[1]]  # 获取图片的宽高

        screen_x = GetSystemMetrics(0)
        screen_y = GetSystemMetrics(1)
        # print "分辨率为：", screen_x, "*", screen_y
        x_compare = screen_x / 1920
        y_compare = screen_y / 1080

        # if srcX != size[0] or srcY != size[1]:  # 如果图片大小与给定分辨率不一样则将图片变成对应分辨率
            # tmp = int(float(srcX) / size[0] * size[1])
        re_img = img.resize((size[0]*x_compare, size[1]*y_compare))
        if re_img:
            re_img.save(templatePath, suffix)
        return sizes

    @staticmethod
    def __image_comparison( templatePath, sourcePath, targetPath, defaultAccurate, defaultMethod="cv2.TM_CCOEFF_NORMED"):
        """
        在大图片中圈出小图片
        :param templatePath:
        :param sourcePath:
        :param targetPath:
        :param defaultAccurate:
        :param defaultMethod:methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        :return:
        """
        result = {"match": False, "maxVal": 0, "maxLocX": 0, "maxLocY": 0, "scaleX": 0, "scaleY": 0}
        img_rgb = cv2.imread(sourcePath)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img_template = cv2.imread(templatePath, 0)

        w, h = img_template.shape[::-1]
        # img_template = cv2.imread(templatePath)
        # img_template = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)
        method = eval(defaultMethod)
        res = cv2.matchTemplate(img_gray, img_template, method)  # 模板匹配方法
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 最大值和最小值
        # 		print min_val, max_val, min_loc, max_loc
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.putText(img_rgb, str(max_val), top_left, cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)  # 显示名字
        cv2.rectangle(img_rgb, top_left, bottom_right, (0, 0, 255), 4)
        cv2.imwrite(sourcePath, img_rgb)

        result["match"] = max_val >= defaultAccurate
        # result["minVal"] = min_val
        result["maxVal"] = max_val
        result["maxLocX"] = max_loc[0] + w / float(2)
        result["maxLocY"] = max_loc[1] + h / float(2)
        # try:
        #     if result["match"] == False:
        #         print "删除"
        #         delete_file(sourcePath)
        # except Exception, e:
        #     print "删除图片失败"
        #     get_logger().info("%s-imgPair:%s-%s" % ("删除匹配不成功图片失败", str(e), sourcePath))

        return result

    @staticmethod
    def img_comparison( templatePath, sourcePath, defaultAccurate=0.5,defaultMethod='cv2.TM_CCOEFF_NORMED'):

        result = {'match': False, 'maxVal': 0, 'maxLocX': 0, 'maxLocY': 0}
        img_rgb = cv2.imread(sourcePath)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img_template = cv2.imread(templatePath, 0)
        method = eval(defaultMethod)
        res = cv2.matchTemplate(img_gray, img_template, method)
        max_val = cv2.minMaxLoc(res)[1]
        result['match'] = max_val >= defaultAccurate
        result['maxVal'] = max_val
        return result

    @staticmethod
    def proxy( templatePath, sourcePath, targetPath, srcX, srcY, orientation=0, defaultAccurate=0.5, isDel=False):
        """
        判断给定的小图片在大图片中存在的概率(圈出一个)
        :param templatePath: 小图片
        :param sourcePath: 大图片
        :param targetPath: 在大图片中圈出小图片
        :param srcX: 当前分辨率X
        :param srcY: 当前分辨率Y
        :param orientation: 方向  1—》旋转90， 0-》不变
        :param defaultAccurate: 相似度
        :return:
        """
        target_x, target_y = ImageRecognize.__unite_resolution(sourcePath, srcX, srcY, orientation)
        template_x, template_y = ImageRecognize.__unite_resolution_template(templatePath, srcX, srcY, orientation)
        result = ImageRecognize.__image_comparison(templatePath, sourcePath, targetPath, defaultAccurate)
        try:
            if isDel == True:
                delete_file(sourcePath)
            else:
                if result["match"] == False:
                    print "删除"
                    print delete_file(sourcePath)
        except Exception, e:
            print "删除图片失败", str(e)
            get_logger().info("%s-imgPair:%s-%s" % ("删除匹配不成功图片失败", str(e), sourcePath))

        result["maxLocX"] = int(target_x / float(srcX) * result["maxLocX"])
        result["maxLocY"] = int(target_y / float(srcY) * result["maxLocY"])
        result["scaleX"] = target_x / float(srcX)
        result["scaleY"] = target_y / float(srcY)

        return result

    @staticmethod
    def __image_multi_comparison(templatePath, sourcePath, targetPath, defaultAccurate,defaultMethod="cv2.TM_CCOEFF_NORMED"):
        """
        在大图片中圈出小图片(多个)
        :param templatePath:
        :param sourcePath:
        :param targetPath:
        :param defaultAccurate:
        :param defaultMethod:
        :return:
        """
        result = {"match": False, "maxVal": 0, "maxLocX": 0, "maxLocY": 0, "scaleX": 0, "scaleY": 0}
        img_rgb = cv2.imread(sourcePath)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(templatePath, 0)
        w, h = template.shape[::-1]

        method = eval(defaultMethod)
        res = cv2.matchTemplate(img_gray, template, method)

        loc = np.where(res >= defaultAccurate)
        print loc
        print zip(*loc[::-1])
        for pt in zip(*loc[::-1]):
            print pt
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv2.imwrite(targetPath, img_rgb)

    @staticmethod
    def proxy_multi( templatePath, sourcePath, targetPath, srcX, srcY, orientation=0, defaultAccurate=0.5):
        ImageRecognize.__unite_resolution(sourcePath, srcX, srcY, targetPath, orientation)
        ImageRecognize.__image_multi_comparison(templatePath, sourcePath, targetPath, defaultAccurate)

if __name__=="__main__":
    moban = r"D:\YCY\u3d\U3DAutomatorClient\image\tmp\windows\sample\test1.png"
    source = r"D:\YCY\u3d\U3DAutomatorClient\image\tmp\windows\sample\test2.png"
    result = r"D:\YCY\u3d\U3DAutomatorClient\image\tmp\windows\sample\source_result.png"
    moban2 = r"D:\YCY\u3d\U3DAutomatorClient\image\tmp\windows\sample\test3.png"
    source2 = r"D:\YCY\u3d\U3DAutomatorClient\image\tmp\windows\sample\test4.png"
    result2 = r"D:\YCY\u3d\U3DAutomatorClient\image\tmp\windows\sample\source_result2.png"
    moban3 = r"D:\YCY\u3d\U3DAutomatorClient\image\tmp\windows\sample\test5.png"
    source3 = r"D:\YCY\u3d\U3DAutomatorClient\image\tmp\windows\sample\test6.png"
    result3 = r"D:\YCY\u3d\U3DAutomatorClient\image\tmp\windows\sample\source_result3.png"
    print ImageRecognize.proxy(templatePath=moban, sourcePath=source, targetPath=result,srcX=1920, srcY=1080 ,defaultAccurate=0.8)
    print ImageRecognize.proxy(templatePath=moban2, sourcePath=source2, targetPath=result2,srcX=1920, srcY=1080 ,defaultAccurate=0.9)
    print ImageRecognize.proxy(templatePath=moban3, sourcePath=source3, targetPath=result3, srcX=1920, srcY=1080,
                               defaultAccurate=0.5)
