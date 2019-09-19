# coding=utf-8
import os, time, socket
from main.object.enum import *
from main.utils.unittest_handler import UnittestHandler
import sys
from script.windows.PPT3DSetting import DataBaseSet
from main.utils.xml_reader import get_config
import subprocess

__author__ = ""


class ScriptHandler(UnittestHandler):
    """
        用于单元测试启动
    """

    def __init__(self, environ=None):
        UnittestHandler.__init__(self)
        if environ:
            os.environ.update(environ)
            return

        os.environ[Environment.VERSION] = Version.Debug
        os.environ[Environment.PLATFORM] = Platform.Windows
        # os.environ[Environment.MODULE] = ""

        # Windows设置项
        os.environ[Environment.TEST_PATH] = get_config().exe_path
        os.environ[Environment.WINDOWS_TITLE] = "演示文稿"
        os.environ[Environment.DataFlag] = "Y"
        # S3Windows设置项
        # os.environ[Environ.TEST_PATH] = r"D:\91und\91UU\415415\RecvFile\彭彬_981203\Debug_qatest_20161205\cosapp.exe"
        # os.environ[Environ.WINDOWS_TITLE] = "cos"

        # Android设置项
        # os.environ["DEVICE_ID"] = "UCEY6L6T99999999"
        # os.environ["PACKAGE"] = "com.nd.argame"
        # os.environ[Environ.DEVICE_ID] = ""
        # os.environ[Environ.APK_PATH] = ""
        # os.environ[Environ.PACKAGE] = ""
        # os.environ[Environ.SRC_SCREEN_WIDTH] = ""
        # os.environ[Environ.SRC_SCREEN_HEIGHT] = ""

    def set_up(self):
        UnittestHandler.set_up(self)

    def tear_down(self):
        UnittestHandler.tear_down(self)


    def settingScripts(self, nums, path, path2, Script):
        d = DataBaseSet.DataBase()

        module = []
        for num in range(nums):
            for i in range(len(path2)):
                for j in Script[i]:
                    for m in range(1):  # 一次性测试的次数
                        module.append(path + path2[i] + j)
                    # 数据库操作
                    sql = "INSERT IGNORE INTO t_CaseName (TestCaseName) VALUES ('" + j + "')"

                    d.databaseOperate(sql)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        except:
            ip = "0.0.0.0"
        finally:
            s.close()
        sql_ip = "INSERT IGNORE INTO t_IPs (ip) VALUES ('" + ip + "')"
        # d = DataBaseSet.DataBase()
        d.databaseOperate(sql_ip)
        # sql_ip = "select IP_id from t_IPs where ip='" + ip + "'"
        # __IP_id = d.getData(sql_ip)
        sql_result = "INSERT INTO t_Result (Detail) VALUES (null)"  # 插入一条结果
        d.databaseOperate(sql_result)
        sql_lastId = "SHOW TABLE STATUS where Name = 't_Result'"
        __Result_id = d.getData(sql_lastId)
        if __Result_id is None:
            os.environ[Environment.Result_id] = "0"
        else:
            os.environ[Environment.Result_id] = str(__Result_id[10])
        # os.environ[Environment.MODULE] = ",".join(module)

        os.environ[Environment.IP] = ip
        os.environ[Environment.isTransSTAF] = "Y"
        modules = ",".join(module)
        return modules

if __name__ == "__main__":

    path = "script.windows.PPT3DTestCase."
    path2 = ["TextTestCase.", "FirstStageTestCase.", "ImageTestCase.", "PlayingTestCase.", "TransitionsTestCase.",
             "MediaTestCase.", "ThumbnailTestCase.", "ShapeTestCase.", "MainStage.", "MainWindow.",
             "ThreeDChart.", "TempTestCase."]
    # Script = [
        # [],
        # [],
        # [],
        # [],
        # [],
        # [],
        # [],
        # [],
        # [],
        # [],
        # [],
        # ["SaveAsPPTXTestCase","OpenPPTXTestCase","StartRightTestCase", "StartDoubleClickTestCase", "SaveAs3dpxTestCase","Open3DPXTestCase",]
    # ]

    Script = [
        [
            # 文本格式设置
        ],
        [
            "Start3DPPTTestCase", "NewPageTestCase",
            "ExitPlayingEscTestCase", "ExitPlayingRightTestCase",
    
            # 插入元素
    
            # 选中元素
            "SelectOneTextTestCase", "SelectOneImageTestCase", "SelectOnePageTestCase",
            "SelectOneAudioTestCase", "SelectOneVideoTestCase", "SelectOne3DModelTestCase",
            "SelectOneChartTestCase", "SelectOneTableTestCase", "SelectOneShapeTestCase",
            # 复制粘贴元素
    
            # 超链接
            "HyperLinkTextBoxTestCase", "HyperLinkTextWordTestCase", "HyperLinkTextSpaceTestCase",
            "HyperLinkImageTestCase", "HyperLinkShapeTestCase", "HyperLinkShapeWebTestCase",
            # 图片设置边框
            "ImageBorderPanelTestCase", "ImageBorderEditTestCase", "ImageBorderClearTestCase",
            "ImageBorderTestCase",
            # 设置场景
            "ChangeThemesTestCase",
            # 剪切元素
    
        ],
        [
    
        ],
        [
            # 放映设置
            "PlayingFromCurrentTestCase", "PlayingFromFirstTestCase", "PlayingF5TestCase",
            # 上下页
            "PlayingSwitchPageArrowTestCase", "PlayingSwitchPagePgTestCase", "PlayingSwitchPageMouseWheelTestCase",
            # 拖动元素
            "SwipeTextTestCase", "SwipeImageTestCase", "SwipeAudioTestCase",
            "SwipeVideoTestCase", "Swipe3DModelTestCase",
            # 放映态菜单按钮功能
            "MenuFuncTextTestCase",
            "MenuFuncImageTestCase", "MenuFuncVideoTestCase", "MenuFuncAudioTestCase",
            "MenuFunc3DModelTestCase", "MenuFuncChartTestCase", "MenuFuncShapeTestCase",
            # 放映态复制粘贴
            "PlayingCopyPasteTextTestCase",
            "PlayingCopyPasteImageBMPTestCase", "PlayingCopyPasteImageGIFTestCase",
            "PlayingCopyPasteImageJPEGTestCase", "PlayingCopyPasteImageJPGTestCase",
            "PlayingCopyPasteImagePNGTestCase",
            "PlayingCopyPasteVideo3GPTestCase", "PlayingCopyPasteVideoASFTestCase",
            "PlayingCopyPasteVideoAVITestCase", "PlayingCopyPasteVideoFLVTestCase",
            "PlayingCopyPasteVideoMOVTestCase", "PlayingCopyPasteVideoMP4TestCase",
            "PlayingCopyPasteVideoMPEGTestCase", "PlayingCopyPasteVideoRMTestCase",
            "PlayingCopyPasteVideoRMVBTestCase", "PlayingCopyPasteVideoWMVTestCase",
            "PlayingCopyPasteAudioAPETestCase", "PlayingCopyPasteAudioM4ATestCase",
            "PlayingCopyPasteAudioM4RTestCase", "PlayingCopyPasteAudioMP3TestCase",
            "PlayingCopyPasteAudioWAVTestCase", "PlayingCopyPasteAudioWMATestCase",
            "PlayingCopyPasteChartHistogramTestCase", "PlayingCopyPasteChartLineTestCase",
            "PlayingCopyPasteChartPieTestCase", "PlayingCopyPasteShapeAddTestCase",
            "PlayingCopyPasteShapeArrowTestCase", "PlayingCopyPasteShapeCircleTestCase",
            "PlayingCopyPasteShapeLineTestCase", "PlayingCopyPasteShapeProcessTestCase",
            "PlayingCopyPasteShapeRectangleTestCase", "PlayingCopyPasteShapeStartTestCase",
            "PlayingCopyPaste3DModelTestCase",
        ],
        [],
        [
            # 视频播放设置
            "VideoPlayAutoTestCase", "VideoPlayClickTestCase",
            "VideoPlayCycleTestCase", "VideoPlayerHideTestCase",
            "VideoShowHidePageTestCase", "VideoShowPlayTestCase",
            "VideoShowStillPageTestCase", "VideoWindowNoTransTestCase",
            # 音频播放设置
            "AudioBSSettingTestCase", "AudioPlayClickTestCase",
            "AudioPlayAutoTestCase", "AudioPlayCycleTestCase",
            "AudioPlayHideTestCase",
        ],
        [
            # 缩略图验证
            "ThumbnailMouseCoverTestCase", "ThumbnailMove2TestCase", "ThumbnailMove3TestCase",
            "ThumbnailMoveTestCase", "ThumbnailNewPageButtonTestCase", "ThumbnailNewPageEnterTestCase",
            "ThumbnailRightStageTestCase", "ThumbnailSelectMoreTestCase", "ThumbnailSelectMuchTestCase",
            "ThumbnailSelectRightTestCase", "ThumbnailZoomTestCase",
        ],
        [
            # 形状属性设置
            "ShapeColorTestCase", "ShapeFormatTestCase", "ShapeLineTestCase",
            "ShapeLineTypeCircleTestCase", "ShapeLineTypeLongLineTestCase", "ShapeLineTypeLongSquareSquareTestCase",
            "ShapeLineTypeLongSquareTestCase", "ShapeLineTypeShortLineTestCase", "ShapeLineTypeShortSquareTestCase",
            "ShapeLineTypeSquareTestCase", "ShapeRectangleStyleTestCase", "ShapeRectangleTestCase",
            "ShapeTransparentTestCase",
        ],
        [
            "FarAndNearImageTestCase", "RotateXImageTestCase", "RotateYImageTestCase", "RotateZImageTestCase",
            "FarAndNearShapeTestCase", "RotateXShapeTestCase", "RotateYShapeTestCase", "RotateZShapeTestCase",
            "FarAndNearTextTestCase", "RotateXTextTestCase", "RotateYTextTestCase", "RotateZTextTestCase",
            "FarAndNearAudioTestCase", "RotateXAudioTestCase", "RotateYAudioTestCase", "RotateZAudioTestCase",
            "FarAndNearVideoTestCase", "RotateXVideoTestCase", "RotateYVideoTestCase", "RotateZVideoTestCase",
            "FarAndNear3DModelTestCase", "RotateX3DModelTestCase", "RotateY3DModelTestCase", "RotateZ3DModelTestCase",
            "Delete3DModelTestCase", "DeleteAudioTestCase", "DeleteChartTestCase",
            "DeleteImageTestCase", "DeleteShapeTestCase", "DeleteTableTestCase",
            "DeleteTextTestCase", "DeleteVideoTestCase", "DeletePageTestCase",
            "ZoomOriginLeftImageTestCase", "ZoomOriginLeftTextTestCase", "ZoomOriginLeftAudioTestCase",
            "ZoomOriginLeftVideoTestCase", "ZoomOriginLeftShapeTestCase", "ZoomOriginLeft3DModelTestCase",
        ],
        [
    
            # 保存提醒
            "CloseFileRemindTestCase", "NewFileRemindTestCase",
    
            "CheckCacheTestCase", "ScaleAddTestCase", "ScaleSubTestCase",
            "ScaleNormalBtnTestCase", "ScaleNormalChangePageTestCase", "ScaleNormalQuitPlayingTestCase",
        ],
        [
    
        ],
        []
    ]

    # Script = [
    #     [
    #         # 文本格式设置
    #         "TextBGTestCase", "TextDefWordTestCase", "TextTypeWordTestCase",
    #         "TextNewTextXTestCase", "TextNewTextYTestCase", "TextTypeWord2TestCase",
    #         "TextCutTestCase", "TextChangeFontTestCase", "TextChangeSizeTestCase",
    #         "TextChangeSize2TestCase", "TextChangeBoldTestCase", "TextChangeItalicTestCase",
    #         "TextChangeShadowTestCase", "TextChangeUnderlineTestCase", "TextChangeStrikeTestCase",
    #         "TextChangeDropDownTestCase", "TextChangeWordColorTestCase", "TextChangeRowSpaceTestCase",
    #         "TextChangeSpaceTestCase", "TextParaNoSymTestCase", "TextParaSymSaveTestCase",
    #         "TextParaSymOpenTestCase", "TextParaSymPreviewTestCase", "TextParaIndentTestCase",
    #         "TextParaIncIndentTestCase", "TextParaIncIndentSaveTestCase", "TextParaIncIndentOpenTestCase",
    #         "TextParaIncIndentTimesTestCase", "TextParaIndentSym1TestCase", "TextParaIndentSym2TestCase",
    #         "TextParaDefSpaceTestCase", "TextParaChange2SpaceTestCase", "TextParaChange3SpaceTestCase",
    #         "TextParaChange3SpaceSaveTestCase", "TextParaChange3SpaceOpenTestCase",
    #         "TextParaChangeFontTestCase", "TextParaLineSpaceSettingTestCase", "TextParaSettingAlignTestCase",
    #         "TextParaSettingAlign2TestCase", "TextParaSettingIndentTestCase", "TextParaSettingIndentAddTestCase",
    #         "TextParaSettingIndentMaxTestCase", "TextParaSettingIndentSubTestCase",
    #         "TextParaSettingIndentMinTestCase",
    #         "TextParaSettingIndentSpeTestCase", "TextParaSettingIndentSpe2TestCase",
    #         "TextParaSettingIndentSpe3TestCase",
    #         "TextParaSettingIndentSpe4TestCase", "TextParaSettingIndentSpe5TestCase",
    #         "TextParaSettingIndentSpe6TestCase",
    #         "TextParaSettingIndentSpe7TestCase", "TextParaSettingIndentSpeSymTestCase",
    #         "TextParaSettingIndentSpeSym2TestCase",
    #         "TextParaSettingIndentSpeSym3TestCase", "TextParaSettingIndentSpaceQianTestCase",
    #         "TextParaSettingIndentSpaceQian2TestCase",
    #         "TextParaSettingIndentSpaceQian3TestCase", "TextParaSettingIndentSpaceQian4TestCase",
    #         "TextParaSettingIndentSpaceQian5TestCase",
    #         "TextParaSettingIndentSpaceRowTestCase",
    #         "TextParaSettingIndentSpaceRow1TestCase", "TextParaSettingIndentSpaceRow2TestCase",
    #         "TextParaSettingIndentSpaceRow3TestCase",
    #         "TextParaSettingIndentSpaceRow4TestCase", "TextParaSettingIndentSpaceRow5TestCase",
    #         "TextParaSettingIndentSpaceRow6TestCase",
    #         "TextParaSettingIndentSpaceRow7TestCase", "TextParaSettingIndentSpaceRow8TestCase",
    #         "TextParaSettingIndentSpaceRow9TestCase",
    #         "TextParaSettingIndentSpaceRow10TestCase", "TextParaSettingCloseTestCase",
    #         "TextParaSettingCancleTestCase",
    #         "TextParaSettingSaveTestCase", "TextParaSettingOpenTestCase",
    #     ],
    #     [
    #         "Start3DPPTTestCase", "OpenPPTTestCase",
    #         "Open3DPPTTestCase", "NewPageTestCase", "SavepptxAs3dpxTestCase",
    #         "ExitPlayingEscTestCase", "ExitPlayingRightTestCase",
    #         "NewFileEditNoSaveTestCase", "NewFileEditSaveTestCase", "NewFileNoEditTestCase",
    #
    #         # 插入元素
    #         "InsertTextXTestCase", "InsertTextYTestCase",
    #         "InsertTextBGTestCase", "InsertWordArtTestCase",
    #         "InsertVideo3GPTestCase", "InsertVideoASFTestCase",
    #         "InsertVideoAVITestCase", "InsertVideoFLVTestCase",
    #         "InsertVideoMOVTestCase", "InsertVideoMP4TestCase",
    #         "InsertVideoMPEGTestCase", "InsertVideoRMTestCase",
    #         "InsertVideoRMVBTestCase", "InsertVideoWMVTestCase",
    #         "InsertAudioAPETestCase", "InsertAudioM4ATestCase",
    #         "InsertAudioM4RTestCase", "InsertAudioMP3TestCase",
    #         "InsertAudioWAVTestCase", "InsertAudioWMATestCase",
    #         "InsertChart3DHistogramTestCase", "InsertChart3DLineTestCase",
    #         "InsertChart3DPieTestCase", "InsertImageBMPTestCase",
    #         "InsertImageGIFTestCase", "InsertImageJPEGTestCase",
    #         "InsertImageJPGTestCase", "InsertImagePNGTestCase",
    #         "InsertShapeAddTestCase", "InsertShapeArrowTestCase",
    #         "InsertShapeCircleTestCase", "InsertShapeLabelTestCase",
    #         "InsertShapeLineTestCase", "InsertShapeProcessTestCase",
    #         "InsertShapeRectangleTestCase", "InsertShapeStartTestCase",
    #         "Insert3DModelTestCase", "InsertTableQuickTestCase", "InsertTableCustomTestCase",
    #         # 选中元素
    #         "SelectOneTextTestCase", "SelectOneImageTestCase", "SelectOnePageTestCase",
    #         "SelectOneAudioTestCase", "SelectOneVideoTestCase", "SelectOne3DModelTestCase",
    #         "SelectOneChartTestCase", "SelectOneTableTestCase", "SelectOneShapeTestCase",
    #         # 复制粘贴元素
    #         "CopyPasteImageBMPTestCase", "CopyPasteImageGIFTestCase",
    #         "CopyPasteImageJPEGTestCase", "CopyPasteImageJPGTestCase",
    #         "CopyPasteImagePNGTestCase",
    #         "CopyPasteVideo3GPTestCase", "CopyPasteVideoASFTestCase",
    #         "CopyPasteVideoAVITestCase", "CopyPasteVideoFLVTestCase",
    #         "CopyPasteVideoMOVTestCase", "CopyPasteVideoMP4TestCase",
    #         "CopyPasteVideoMPEGTestCase", "CopyPasteVideoRMTestCase",
    #         "CopyPasteVideoRMVBTestCase", "CopyPasteVideoWMVTestCase",
    #         "CopyPasteAudioAPETestCase", "CopyPasteAudioM4ATestCase",
    #         "CopyPasteAudioM4RTestCase", "CopyPasteAudioMP3TestCase",
    #         "CopyPasteAudioWAVTestCase", "CopyPasteAudioWMATestCase",
    #         "CopyPasteChartHistogramTestCase", "CopyPasteChartLineTestCase",
    #         "CopyPasteChartPieTestCase", "CopyPasteShapeAddTestCase",
    #         "CopyPasteShapeArrowTestCase", "CopyPasteShapeCircleTestCase",
    #         "CopyPasteShapeLineTestCase", "CopyPasteShapeProcessTestCase",
    #         "CopyPasteShapeRectangleTestCase", "CopyPasteShapeStartTestCase",
    #         "CopyPastePageTestCase", "CopyPaste3DModelTestCase", "CopyPasteTableQuickTestCase",
    #         "CopyPasteTableCustomTestCase", "CopyPasteTextTestCase",
    #         # 超链接
    #         "HyperLinkTextBoxTestCase", "HyperLinkTextWordTestCase", "HyperLinkTextSpaceTestCase",
    #         "HyperLinkImageTestCase", "HyperLinkShapeTestCase", "HyperLinkShapeWebTestCase",
    #         # 图片设置边框
    #         "ImageBorderPanelTestCase", "ImageBorderEditTestCase", "ImageBorderClearTestCase",
    #         "ImageBorderTestCase",
    #         # 设置场景
    #         "ChangeThemesTestCase",
    #         # 剪切元素
    #         "CutTextTestCase", "CutImageTestCase", "CutAudioTestCase",
    #         "CutVideoTestCase", "CutShapeTestCase", "Cut3DModelTestCase",
    #         "CutChartTestCase", "CutTableTestCase", "CutPasteElementTestCase", "CutPageTestCase",
    #     ],
    #     [
    #
    #     ],
    #     [
    #         # 放映设置
    #         "PlayingFromCurrentTestCase", "PlayingFromFirstTestCase", "PlayingF5TestCase",
    #         # 上下页
    #         "PlayingSwitchPageArrowTestCase", "PlayingSwitchPagePgTestCase", "PlayingSwitchPageMouseWheelTestCase",
    #         # 拖动元素
    #         "SwipeTextTestCase", "SwipeImageTestCase", "SwipeAudioTestCase",
    #         "SwipeVideoTestCase", "Swipe3DModelTestCase",
    #         # 放映态菜单按钮功能
    #         "MenuFuncTextTestCase",
    #         "MenuFuncImageTestCase", "MenuFuncVideoTestCase", "MenuFuncAudioTestCase",
    #         "MenuFunc3DModelTestCase", "MenuFuncChartTestCase", "MenuFuncShapeTestCase",
    #         # 放映态复制粘贴
    #         "PlayingCopyPasteTextTestCase",
    #         "PlayingCopyPasteImageBMPTestCase", "PlayingCopyPasteImageGIFTestCase",
    #         "PlayingCopyPasteImageJPEGTestCase", "PlayingCopyPasteImageJPGTestCase",
    #         "PlayingCopyPasteImagePNGTestCase",
    #         "PlayingCopyPasteVideo3GPTestCase", "PlayingCopyPasteVideoASFTestCase",
    #         "PlayingCopyPasteVideoAVITestCase", "PlayingCopyPasteVideoFLVTestCase",
    #         "PlayingCopyPasteVideoMOVTestCase", "PlayingCopyPasteVideoMP4TestCase",
    #         "PlayingCopyPasteVideoMPEGTestCase", "PlayingCopyPasteVideoRMTestCase",
    #         "PlayingCopyPasteVideoRMVBTestCase", "PlayingCopyPasteVideoWMVTestCase",
    #         "PlayingCopyPasteAudioAPETestCase", "PlayingCopyPasteAudioM4ATestCase",
    #         "PlayingCopyPasteAudioM4RTestCase", "PlayingCopyPasteAudioMP3TestCase",
    #         "PlayingCopyPasteAudioWAVTestCase", "PlayingCopyPasteAudioWMATestCase",
    #         "PlayingCopyPasteChartHistogramTestCase", "PlayingCopyPasteChartLineTestCase",
    #         "PlayingCopyPasteChartPieTestCase", "PlayingCopyPasteShapeAddTestCase",
    #         "PlayingCopyPasteShapeArrowTestCase", "PlayingCopyPasteShapeCircleTestCase",
    #         "PlayingCopyPasteShapeLineTestCase", "PlayingCopyPasteShapeProcessTestCase",
    #         "PlayingCopyPasteShapeRectangleTestCase", "PlayingCopyPasteShapeStartTestCase",
    #         "PlayingCopyPaste3DModelTestCase",
    #     ],
    #     [],
    #     [
    #         # 视频播放设置
    #         "VideoPlayAutoTestCase", "VideoPlayClickTestCase",
    #         "VideoPlayCycleTestCase", "VideoPlayerHideTestCase",
    #         "VideoShowHidePageTestCase", "VideoShowPlayTestCase",
    #         "VideoShowStillPageTestCase", "VideoWindowNoTransTestCase",
    #         # 音频播放设置
    #         "AudioBSSettingTestCase", "AudioPlayClickTestCase",
    #         "AudioPlayAutoTestCase", "AudioPlayCycleTestCase",
    #         "AudioPlayHideTestCase",
    #     ],
    #     [
    #         # 缩略图验证
    #         "ThumbnailMouseCoverTestCase", "ThumbnailMove2TestCase", "ThumbnailMove3TestCase",
    #         "ThumbnailMoveTestCase", "ThumbnailNewPageButtonTestCase", "ThumbnailNewPageEnterTestCase",
    #         "ThumbnailRightStageTestCase", "ThumbnailSelectMoreTestCase", "ThumbnailSelectMuchTestCase",
    #         "ThumbnailSelectRightTestCase", "ThumbnailZoomTestCase",
    #     ],
    #     [
    #         # 形状属性设置
    #         "ShapeColorTestCase", "ShapeFormatTestCase", "ShapeLineTestCase",
    #         "ShapeLineTypeCircleTestCase", "ShapeLineTypeLongLineTestCase", "ShapeLineTypeLongSquareSquareTestCase",
    #         "ShapeLineTypeLongSquareTestCase", "ShapeLineTypeShortLineTestCase", "ShapeLineTypeShortSquareTestCase",
    #         "ShapeLineTypeSquareTestCase", "ShapeRectangleStyleTestCase", "ShapeRectangleTestCase",
    #         "ShapeTransparentTestCase",
    #     ],
    #     [
    #         "FarAndNearImageTestCase", "RotateXImageTestCase", "RotateYImageTestCase", "RotateZImageTestCase",
    #         "FarAndNearShapeTestCase", "RotateXShapeTestCase", "RotateYShapeTestCase", "RotateZShapeTestCase",
    #         "FarAndNearTextTestCase", "RotateXTextTestCase", "RotateYTextTestCase", "RotateZTextTestCase",
    #         "FarAndNearAudioTestCase", "RotateXAudioTestCase", "RotateYAudioTestCase", "RotateZAudioTestCase",
    #         "FarAndNearVideoTestCase", "RotateXVideoTestCase", "RotateYVideoTestCase", "RotateZVideoTestCase",
    #         "FarAndNear3DModelTestCase", "RotateX3DModelTestCase", "RotateY3DModelTestCase", "RotateZ3DModelTestCase",
    #         "Delete3DModelTestCase", "DeleteAudioTestCase", "DeleteChartTestCase",
    #         "DeleteImageTestCase", "DeleteShapeTestCase", "DeleteTableTestCase",
    #         "DeleteTextTestCase", "DeleteVideoTestCase", "DeletePageTestCase",
    #         "ZoomOriginLeftImageTestCase", "ZoomOriginLeftTextTestCase", "ZoomOriginLeftAudioTestCase",
    #         "ZoomOriginLeftVideoTestCase", "ZoomOriginLeftShapeTestCase", "ZoomOriginLeft3DModelTestCase",
    #     ],
    #     [
    #         "SettingLogViewerTestCase", "SettingAboutUsTestCase", "SettingCheckUpdateTestCase",
    #         "SettingContractUsTestCase", "SettingFloatTestCase", "SettingLanguageTestCase",
    #         "SettingQuickOperateTestCase", "MaxWindowedTestCase", "RestoreWindowTestCase",
    #         #保存提醒
    #         "CloseFileRemindTestCase", "NewFileRemindTestCase",
    #
    #           "CheckCacheTestCase", "ScaleAddTestCase", "ScaleSubTestCase",
    #           "ScaleNormalBtnTestCase", "ScaleNormalChangePageTestCase", "ScaleNormalQuitPlayingTestCase",
    #     ],
    #     [
    #         "ChartPreviewTestCase", "ChartSettingTestCase", "ChartRightStageTestCase",
    #         "ChartColumnTestCase", "ChartColumnChangeTestCase","ChartNumChangeTestCase",
    #         "ChartNameChangeTestCase", "ChartDeleteTestCase", "ChartTableAddRowTestCase", "ChartTableAddColumnTestCase",
    #     ],
    #     []
    #
    # ]

    #print "第4个点"
    #print "启动java虚拟机123"

    # subprocess.Popen("D:\\Program Files (x86)\\PCPA ASSISTENT\\AutoImport\\ProAutoImport.exe --STARTTASK('test_201908211643')")

    os.environ[Environment.StartTime] = time.strftime('%Y_%m_%d-%H_%M_%S', time.localtime())
    for i in range(1):  # 执行轮数,且按照ABCD形式执行
        print "The test ", i
        os.environ[Environment.XlsRow] = str(i+1)
        modules = ScriptHandler().settingScripts(1, path, path2, Script)  # para1:执行轮数
        ScriptHandler().run(modules)
        time.sleep(5)
    # subprocess.Popen("D:\\Program Files (x86)\\PCPA ASSISTENT\\AutoImport\\ProAutoImport.exe --ENDTASK('test_201908211643')")
