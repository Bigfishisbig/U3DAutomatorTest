import cv2
import numpy as np
from PIL import Image

__author__ = "Wei Li"


class ImageRecognize:
    """
        Image.resize can not  satisfy me ,maybe change another way.
    """

    def __init__(self):
        pass

    @staticmethod
    def __unite_resolution(source_path, src_x, src_y, orientation, suffix="png"):
        img = Image.open(source_path)
        size = img.size
        sizes = [size[0], size[1]]

        re_img = None
        if orientation == 1:
            re_img = img.transpose(Image.ROTATE_90)
            temp = sizes[0]
            sizes[0] = sizes[1]
            sizes[1] = temp
            if src_x != size[1] or src_y != size[0]:
                re_img = re_img.resize((src_x, src_y))
        else:
            if src_x != size[0] or src_y != size[1]:
                # tmp = int(float(src_x) / size[0] * size[1])
                re_img = img.resize((src_x, src_y))
        if re_img:
            re_img.save(source_path, suffix)
        return sizes

    @staticmethod
    def __image_comparison(template_path, source_path, target_path, default_accurate,
                           default_method="cv2.TM_CCOEFF_NORMED"):
        result = {"match": False, "maxVal": 0, "maxLocX": 0, "maxLocY": 0, "scaleX": 0, "scaleY": 0}
        img_rgb = cv2.imread(source_path)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img_template = cv2.imread(template_path, 0)

        w, h = img_template.shape[::-1]
        method = eval(default_method)
        res = cv2.matchTemplate(img_gray, img_template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # 		print min_val, max_val, min_loc, max_loc
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(img_rgb, top_left, bottom_right, (0, 0, 255), 4)
        cv2.imwrite(target_path, img_rgb)

        result["match"] = max_val >= default_accurate
        result["maxVal"] = max_val
        result["maxLocX"] = max_loc[0] + w / float(2)
        result["maxLocY"] = max_loc[1] + h / float(2)
        return result

    @staticmethod
    def img_comparison(template_path, source_path, default_accurate=0.5,
                       default_method='cv2.TM_CCOEFF_NORMED'):

        result = {'match': False, 'maxVal': 0, 'maxLocX': 0, 'maxLocY': 0}
        img_rgb = cv2.imread(source_path)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img_template = cv2.imread(template_path, 0)
        method = eval(default_method)
        res = cv2.matchTemplate(img_gray, img_template, method)
        max_val = cv2.minMaxLoc(res)[1]
        result['match'] = max_val >= default_accurate
        result['maxVal'] = max_val
        return result

    @staticmethod
    def proxy(template_path, source_path, target_path, src_x=720, src_y=1280, orientation=0, default_accurate=0.5):
        if src_x != 0 and src_y != 0:
            target_x, target_y = ImageRecognize.__unite_resolution(source_path, src_x, src_y, orientation)
            result = ImageRecognize.__image_comparison(template_path, source_path, target_path, default_accurate)
            result["maxLocX"] = int(target_x / float(src_x) * result["maxLocX"])
            result["maxLocY"] = int(target_y / float(src_y) * result["maxLocY"])
            result["scaleX"] = target_x / float(src_x)
            result["scaleY"] = target_y / float(src_y)
        else:
            result = ImageRecognize.__image_comparison(template_path, source_path, target_path, default_accurate)
            result["scaleX"] = 1
            result["scaleY"] = 1
        return result

    @staticmethod
    def __image_multi_comparison(template_path, source_path, target_path, default_accurate,
                                 default_method="cv2.TM_CCOEFF_NORMED"):
        img_rgb = cv2.imread(source_path)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_path, 0)
        w, h = template.shape[::-1]

        method = eval(default_method)
        res = cv2.matchTemplate(img_gray, template, method)

        loc = np.where(res >= default_accurate)
        print loc
        print zip(*loc[::-1])
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        cv2.imwrite(target_path, img_rgb)

    @staticmethod
    def proxy_multi(template_path, source_path, target_path, src_x=720, src_y=1280, orientation=0,
                    default_accurate=0.5):
        ImageRecognize.__unite_resolution(source_path, src_x, src_y, orientation)
        ImageRecognize.__image_multi_comparison(template_path, source_path, target_path, default_accurate)
