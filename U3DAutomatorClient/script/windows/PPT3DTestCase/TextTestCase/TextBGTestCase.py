#!/usr/bin/env python
# coding=utf-8
"""
文件名称：TextBGTestCase.py
作者：ycy
版本：PPTPro_1007 Q6
创建时间：2018/11/12 16:37
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化为指定的编码格式

class TextBGTestCase(Action, Operation, SystemDiaglog):
    '''插入文本框'''
    def test_main(self):
        '''插入文本框_文字背景'''
        self.OperationSetting()
        self.Init3DPPT()
        # 查找settag正则 self.SetTag\([\s\S]*time.time\(\)\)$
        # tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  ("文字背景", time.time())

        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__
        self.startScene(tag)

        self.OneClick("BtnInsert")
        self.OneClick("BtnInsertTextBar")
        self.OneClick("BtnInsertTextBG")
        self.OneClick("BG_Text_1")
        # self.s_witForImg(SourcePath.File_Img_Text_BGEditor, 5, "文字背景创建失败")
        fileroot = self.getPathValue("File")  # 获取可变路径
        PageID = self.getPathValue("Page")  # 获取可变路径
        itemTextID = self.getPathValue("ItemText")
        Xpath = "3DP Root/File" + fileroot[0] +"/3DP Root/Page" + PageID[0] + "/ItemText/ItemText" + itemTextID[
            1] + "/TextRoot/CharRoot"

        self.isElementExistPageID(Xpath)
        self.isElementExist("TextFormatShow")

        self.endScene(tag)

        # self.EndTag("", time.time())
        time.sleep(2)
        self.EndTag("")
        # self.s_witForImg(SourcePath.File_Img_Text_BGSetting, 5, "文字背景创建失败")



    # def test_mai2(self):
    #     '''插入文本框-文字背景'''
    #     self.OperationSetting()
    #     self.Init3DPPT()
    #     # tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
    #     tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__ 
    #
    #     self.OneClick("BtnInsert")
    #     self.OneClick("BtnInsertTextBar")
    #
    #     self.OneClick("BtnInsertTextBG")
    #     self.OneClick("BG_Text_1")
    #     # self.s_witForImg(SourcePath.File_Img_Text_BGEditor, 5, "文字背景创建失败")
    #     fileroot = self.getPathValue("File")  # 获取可变路径
    #     PageID = self.getPathValue("Page")  # 获取可变路径
    #     itemTextID = self.getPathValue("ItemText")
    #     Xpath = "3DP Root/File" + fileroot[0] +"/3DP Root/Page" + PageID[0] + "/ItemText/ItemText" + itemTextID[
    #         1] + "/TextRoot/CharRoot"
    #
    #     self.isElementExistPageID(Xpath)
    #     self.isElementExist("TextFormatShow")
    #
    #     self.cmdCommand("'" + SourcePath.File_PCPA + " --ENDSCENE(\"Insert_Text\")" + "'")
    #     # self.cmdSubprocess(str(SourcePath.File_PCPA + " --ENDSCENE('插入文本框-文字背景')"))
    #     # subprocess.Popen('"D:\Program Files (x86)\PCPA ASSISTENT\AutoImport\ProAutoImport.exe" --ENDSCENE("test1658")')
    #
    #     self.EndTag("", str(time.time()))
    #     time.sleep(2)
    #     self.EndTag("")
    #     # self.s_witForImg(SourcePath.File_Img_Text_BGSetting, 5, "文字背景创建失败")