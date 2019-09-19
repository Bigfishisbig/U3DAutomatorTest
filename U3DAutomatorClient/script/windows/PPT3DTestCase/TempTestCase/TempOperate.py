# coding=utf-8

import shutil
import codecs
import re, os, time
from PIL import ImageGrab
#from xlutils.copy import copy
from main.utils.xlsx_writer import XlsxWriter
from main.object.enum import *


class TempOperation:
    global xls_3dpx
    global xls_pptx

    xls_3dpx = XlsxWriter()
    xls_pptx = XlsxWriter()
    def __init__(self):
        global CapPath
        global m
        CapPath = os.getcwd()
        # imgP = ImageRecognize()
        # m = PyMouse()

        # self.x.write_line("start_time", "end_time", "start_spend_time", "run_times", "break_times", "isBreak",
        #              "analyse_time", "analyse_break", "rendering_time", "rendering_break")

    def getSaveTimeXLS(self, start_time, end_time, start_spend_time, break_times=0, isBreak=0):
        # xls_3dpx.set_line(int(os.environ[Environment.XlsRow]))
        xls_3dpx.write_line(start_time, end_time, start_spend_time, break_times, isBreak)

    def getSaveTimeXLSClose(self, path):
        xls_3dpx.close(path)

    def getSavePPTXTimeXLS(self, start_time, end_time, start_spend_time, break_times=0, isBreak=0):
        # xls_3dpx.set_line(int(os.environ[Environment.XlsRow]))
        xls_pptx.write_line(start_time, end_time, start_spend_time, break_times, isBreak)

    def getSavePPTXTimeXLSClose(self, path):
        xls_pptx.close(path)
    
    def cmd_os(self, cmd_str):
        # cmd_str = ""
        os.system(cmd_str)

    
    def getPathValue1(self, path, s):
        """
        获取所插入元素路径中的特定值
        :param str:
        :return:
        """
        # '"actual":"([\d.]+)"'
        # '"解析器返回:页FODP文件消息/s","TimeSpan":"([\d.]+)"'
        xml = self.read_file_as_str(path)
        # for k in xml:
        #     txt = xml[k]
        # s = re.findall(r'%s(\w+)*'%str, txt)
        value = re.findall(s, xml)
        if value is None:
            value[0] = 0
        print value[-1]
        return value[-1]

    
    def getPathValue2(self, path, s1, s2):
        """
        获取所插入元素路径中的特定值
        :param str:
        :return:
        """
        xml = open(path)
        sum = 0
        # print xml.read()
        for line in xml.readlines():
            # print line
            if s1 in line:
                s = re.findall(s2, line)
                sum = float(s[-1]) + sum
        print sum
        return sum

    
    def isExist(self, path, key):
        try:
            with open(path, 'r') as foo:
                for line in foo.readlines():
                    if key in line:
                        # print line
                        return True
        except Exception, e:
            print str(e)
        return False

    
    def read_file_as_str(self, file_path):
        # 判断路径文件存在
        if not os.path.isfile(file_path):
            raise TypeError(file_path + " does not exist")

        all_the_text = open(file_path).read()
        # print type(all_the_text)
        return all_the_text

    
    def getFiles(self, dir, suffix):  # 查找根目录，文件后缀
        res = []
        for root, directory, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
            for filename in files:
                name, suf = os.path.splitext(filename)  # =>文件名,文件后缀
                if suf == suffix:
                    # print os.path.join(root, filename.decode('utf-8'))
                    res.append(os.path.join(root, filename))  # =>吧一串字符串组合成路径
        return res

    
    def deleteFile(self, path):
        """
        删除指定文件
        :param path:
        :return:
        """
        try:
            if os.path.exists(path):
                os.remove(path)
        except Exception, e:
            print str(e)

    
    def write_file(self, filePath, cmd):
        f = open(filePath, 'w')
        f.write(cmd)
        f.close()

    
    def convertUTF8ToANSI(self, oldfile, newfile):
        # 打开UTF8文本文件
        f = codecs.open(oldfile, 'r', 'utf8')
        utfstr = f.read()
        f.close()

        # 把UTF8字符串转码成ANSI字符串
        outansestr = utfstr.encode('mbcs')

        # 使用二进制格式保存转码后的文本
        f = open(newfile, 'wb')
        f.write(outansestr)
        f.close()

    
    def copy2Path(self, oldPath, newPath):
        # 拷贝指定文件到指定路径
        try:
            if os.path.exists(oldPath):
                shutil.copyfile(oldPath, newPath)
            else:
                pass
        except Exception, e:
            print u"拷贝日志失败", str(e)
            pass

    
    # def imgPair(self, pngModelName, x, y, Accurate=0.6):
    #     try:
    #         imgTimename = TempOperation.timeImageName()
    #         TempOperation.Screen_cap(imgTimename)
    #         imgdict = ImageRecognize.proxy(  # self.CapPath + ur"\image\tmp\windows\sample\%s.png"% pngModelName ,
    #             pngModelName,
    #             CapPath + ur"\image\source\%s.png" % imgTimename,
    #             CapPath + ur"\image\target\%s.png" % imgTimename,
    #             srcX=x, srcY=y, defaultAccurate=Accurate)
    #         # print ("imgPairSuccess")
    #         print "Image Match:", imgdict["match"], imgdict["maxVal"], imgdict["maxLocX"], imgdict["maxLocY"]
    #         return imgdict["match"], imgdict["maxLocX"], imgdict["maxLocY"]
    #     except Exception, e:
    #         print u"图片匹配失败：", str(e)
    #         return False
    #         # get_logger().info("%s-imgPair:%s-%s" % (imgTimename, str(e), pngModelName))

    #
    # def imgClick(self, pngModelName, x, y, Accurate=0.6):
    #     result, dx, dy = TempOperation.imgPair(pngModelName, x, y, Accurate=0.6)
    #     if result is not False:
    #         try:
    #             print "success"
    #             m.click(dx, dy, 1)  # x坐标，y坐标， 1为左键2为右键， 默认点击一次
    #         except Exception, e:
    #             print str(e)

    
    # def Screen_cap(self, CapName="Test"):
    #     try:
    #         TestCapPath = CapPath + r"\image\source"
    #         print TestCapPath
    #         if not os.path.isdir(TestCapPath):
    #             os.mkdir(TestCapPath)
    #         im = ImageGrab.grab()
    #         im.save(TestCapPath + "\\" + CapName + ".png")
    #     except Exception, e:
    #         print str(e)
    #         pass
    #
    #
    # def timeImageName(self):
    #     return time.strftime("%Y%m%d%H%M%S", time.localtime())