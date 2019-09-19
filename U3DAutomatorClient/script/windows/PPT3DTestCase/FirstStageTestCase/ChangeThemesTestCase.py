#!/usr/bin/env python
# coding=utf-8
"""
文件名称：ChangeThemesTestCase.py
作者：ycy
版本：PPTPro
创建时间：2019/1/17 19:07
修改时间：
软件：PyCharm
"""
from script.windows.Operation import *
from script.windows.SystemDialog import SystemDiaglog
from script.windows.PPT3DTestCase.Action import Action
from script.windows.PPT3DSetting.SourcePath import SourcePath

reload(sys)
sys.setdefaultencoding('UTF-8')  # 将脚本编码格式转化未置顶的编码格式


class ChangeThemesTestCase(Action, Operation, SystemDiaglog):
    '''更换主题'''
    def test_main(self):
        '''更换主题'''
        self.OperationSetting()
        self.Init3DPPT()
        self.SetTag("更换主题", time.time())

        # self.TimesClick(["BtnNewPage", "BtnNewPage", "BtnNewPage"], 1)
        # self.ClickRight_XY()
        # self.ListClick("BtnStageRightChangeBK")
        tag = (self.__class__.__doc__ or u"测试") + "_" + self.__class__.__name__  
        self.startScene(tag)

        self.OneClick("BtnChangeBK")
        # self.OneClick("LocalSceneCtgText")
        i=1
        bk_array = []
        # time.sleep()
        while True:
            if self.isVisibleV("Canvas/DlgScenePreview(Clone)/Scroll View/Viewport/Content/%s/Title"%i, 2):
                themeName = self.ElementTxt("Canvas/DlgScenePreview(Clone)/Scroll View/Viewport/Content/%s/Title"%i,var=1)
                bk_array.append(themeName)
                print "场景名：", themeName
                i = i + 1
            else:
                break
        print "i:", i
        # scene_num = self.ElementNum("SceneItemNameText")
        for bk in bk_array:
            print "bk:", bk
            if bk == "城市场景" or bk == "湖泊":
                print "the theme is bad"
                continue
            for j in range(i):
                if self.ElementTxt("Canvas/DlgScenePreview(Clone)/Scroll View/Viewport/Content/%s/Title" % j, var=1) == bk:
                    self.Click("Canvas/DlgScenePreview(Clone)/Scroll View/Viewport/Content/%s/Title" % j)
                    # self.DoubleClick("DoubleClickTip")  # 双击下载
                    self.OneClickL("Canvas/DlgScenePreview(Clone)/Scroll View/Viewport/Content/%s/Title" % j, -50, o=-50)
                    # self.LoadingWait("NoResource")
                    self.isNotElementVisible("NoResource", "主题场景不在线")
                    self.OneClick("BtnApplyBk")
                    time.sleep(3)
                    self.LoadingWait("BtnApplyBk", 3)
                    # self.WaitForElementText("FileName", "演示文稿", 30, "更换主题失败")
                    time.sleep(2)
                    self.OneClick("BtnChangeBK")
                    self.WaitForElementText("BtnFirstBk", bk, 10, "更换主题失败")
                    break
                else:
                    pass
        for m in range(i):
            if self.ElementTxt("Canvas/DlgScenePreview(Clone)/Scroll View/Viewport/Content/%s/Title" % m, var=1) == "南极科考站":
                self.Click("Canvas/DlgScenePreview(Clone)/Scroll View/Viewport/Content/%s/Title" % m)
                # self.DoubleClick("DoubleClickTip")  # 双击下载
                self.OneClickL("Canvas/DlgScenePreview(Clone)/Scroll View/Viewport/Content/%s/Title" % m, -50, o=-50)
                # self.LoadingWait("NoResource")
                self.isNotElementVisible("NoResource", "主题场景不在线")
                self.OneClick("BtnApplyBk")
                self.LoadingWait("BtnApplyBk", 2)
                # self.WaitForElementText("FileName", "演示文稿", 30, "更换主题失败")
                time.sleep(2)
                self.OneClick("BtnChangeBK")
                self.WaitForElementText("BtnFirstBk", "南极科考站", 10, "更换主题失败")
                break
            else:
                pass

        self.endScene(tag)
        time.sleep(1)
        self.EndTag()
