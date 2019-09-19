#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextParaSettingIndentSpaceRow2TestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/28 10:29
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath
import win32api, win32con

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式


class TextParaSettingSaveTestCase(Action, Operation, SystemDiaglog):
    '''段落-行距-双倍行距'''
    def test_main(self):
        '''段落-行距-双倍行距'''
        # 段落-行距-双倍行距
        self.OperationSetting()
        self.Init3DPPT()
        self.OpenParaSetting()
        # 对齐方式
        self.OneClick("AlignBar")
        self.OneClick("AlignRight")
        # 文本之前缩进
        self.OneClick("InputFieldIndent")
        self.InputStr("14")
        # 首行缩进
        self.OneClick("LabelSpecialFormat")
        time.sleep(3)
        self.OneClick("SpecialFormat_1")
        #段前
        self.OneClick("ParaQianAdd")
        # 段后
        self.OneClick("ParaHouAdd")
        # 设置行距
        # self.WaitForElementText("LabelSpecialFormat", "（无）", 5, "特殊格式设置错误")
        self.OneClick("InputFieldParaSpace")
        time.sleep(1)
        self.OneClick("RowSpace3")

        self.OneClick("BtnParaOK")
        self.OneClick("BtnStart")
        save_path = SourcePath.File_PPTOpenTestSave_3dpx  # 保存
        if os.path.exists(save_path):
            os.remove(save_path)
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)
        self.SaveAs3DPPTFile(save_path)
        # self.LoadingWait("Slider")
        # time.sleep(120)
        self.fileExist(save_path, "文件120s内保存失败")
        self.endScene(tag)
        time.sleep(3)




