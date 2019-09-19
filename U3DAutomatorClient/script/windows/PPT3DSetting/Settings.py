# coding=utf-8
"""
    3DPPT脚本配置Setting
    版本: 3DPPT Final.2017.1225.1314
    创建日期：2017.12.26
    修改日期：2017.12.26
"""
from script.windows.PPT3DSetting.SourcePath import SourcePath


class PPT3DPath:

    def __init__(self):
        # PageID = self.getPageID( )
        self.PPT3DPath = {
            # 顶部操作
            "FileName": "Canvas/DlgMain(Clone)/Titlebar/FilesPanel/FileTabList/FileTab(Clone)/Container/TitleText", # 文件名
            "FileName1": "Canvas/DlgMain(Clone)/Titlebar/FilesPanel/FileTabList/FileTab(Clone)[1]/Container/TitleText",
            "FileName2": "Canvas/DlgMain(Clone)/Titlebar/FilesPanel/FileTabList/FileTab(Clone)[2]/Container/TitleText",
            "BtnStart": "Canvas/DlgMain(Clone)/ToggleMenuPanel/StartToggle/Label", # 开始
            "BtnInsert": "Canvas/DlgMain(Clone)/ToggleMenuPanel/InsertToggle/Label", # 插入
            "BtnFormat": "Canvas/DlgMain(Clone)/ToggleMenuPanel/FormatToggle/Label", # 格式
            "BtnAction": "Canvas/DlgMain(Clone)/ToggleMenuPanel/ActionToggle/Label", # 动画
            "BtnCloseTab": "Canvas/DlgMain(Clone)/Titlebar/FilesPanel/FileTabList/FileTab(Clone)/Container/BtnCloseFile", # 关闭标签
            "BtnNewTab": "Canvas/DlgMain(Clone)/Titlebar/FilesPanel/BtnAddPanel/BtnAddFile", # 新建标签

            "BtnMaxmize": "Canvas/DlgMain(Clone)/Titlebar/TitleRightBtnPanel/BtnMaxmize",  # 最大化
            "BtnWindowmize": "Canvas/DlgMain(Clone)/Titlebar/TitleRightBtnPanel/BtnWindowmize", # 窗口化
            "BtnMinimize": "Canvas/DlgMain(Clone)/Titlebar/TitleRightBtnPanel/BtnMinimize", # 最小化
            "BtnCloseApp": "Canvas/DlgMain(Clone)/Titlebar/TitleRightBtnPanel/BtnCloseApp", # 关闭

            "BtnSetting": "Canvas/DlgMain(Clone)/Titlebar/LogoPanel", #3DPPT设置
            "BtnPublicSetup": "Canvas/Dlg3DPPTSetting(Clone)/container/BtnPublicSetup", # 常规设置
            "BtnBackup": "Canvas/Dlg3DPPTSetting(Clone)/container/BtnBackup", # 备份恢复
            "BtnCheckUpdate": "Canvas/Dlg3DPPTSetting(Clone)/container/BtnCheckUpdate", # 检查更新
            "BtnUpdateLog": "Canvas/Dlg3DPPTSetting(Clone)/container/BtnUpdateLog", # 更新日志
            "BtnAboutUs": "Canvas/Dlg3DPPTSetting(Clone)/container/BtnAboutUs", #关于我们
            "BtnContractUs": "Canvas/Dlg3DPPTSetting(Clone)/container/BtnContractUs", # 联系我们
            "BtnLogViewer": "Canvas/Dlg3DPPTSetting(Clone)/container/BtnLogViewer", # 性能查看

            # 常规设置
            "CommonSetup": "Canvas/DlgPublicSetup(Clone)/Panel/OptionBar/CommonSetup", # 基本设置
            "AutoBackupSetup": "Canvas/DlgPublicSetup(Clone)/Panel/OptionBar/AutoBackupSetup", # 备份设置
            "DownloadSetup": "Canvas/DlgPublicSetup(Clone)/Panel/OptionBar/DownloadSetup", # 下载设置
            "LanguageSetup": "Canvas/DlgPublicSetup(Clone)/Panel/OptionBar/LanguageSetup", # 语言设置
            "ResourceSetup": "Canvas/DlgPublicSetup(Clone)/Panel/OptionBar/ResourceSetup", # 资源设置
            "FrameRateSetup": "Canvas/DlgPublicSetup(Clone)/Panel/OptionBar/FrameRateSetup", # 流畅度设置
            "RecorderSetup": "Canvas/DlgPublicSetup(Clone)/Panel/OptionBar/RecorderSetup", # 录制设置

            "STEnableBySelect": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/CommonSetupPanel/TextSettingBlock/Container/STEnableBySelect", # 选择显示浮动工具栏
            "STEnableByRightMenu": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/CommonSetupPanel/TextSettingBlock/Container/STEnableByRightMenu", # 右键显示浮动工具栏

            "BasicOperationOption": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/CommonSetupPanel/BasicOperationSettingBlock/BasicOperationOption", # 快捷操作

            "BtnSettingOK": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/BottomBar/BtnOk", #
            "BtnSettingCancle": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/BottomBar/BtnCancel",
            "BtnSettingApply": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/BottomBar/BtnApply",

            "LanguageDropDown": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/LanguageSetupPanel/LanguageBlock/ChooseLanguageText/LanguageDropDown", # 语言下拉
            "SimpleChinese": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/LanguageSetupPanel/LanguageBlock/ChooseLanguageText/LanguageDropDown/Dropdown List/Viewport/Content/Item 0: 简体中文",
            "HardChinese": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/LanguageSetupPanel/LanguageBlock/ChooseLanguageText/LanguageDropDown/Dropdown List/Viewport/Content/Item 1: 繁體中文",
            "English": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/LanguageSetupPanel/LanguageBlock/ChooseLanguageText/LanguageDropDown/Dropdown List/Viewport/Content/Item 2: English",

            "LanguageText": "Canvas/DlgMain(Clone)/ToggleMenuPanel/StartToggle/Label", # 开始文本

            "BtnClearCache": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/DownloadSetupPanel/FileCacheBlock/BtnClearCache/Text", # 清除缓存
            "ClearCacheTip": "Canvas/DlgPublicSetup(Clone)/Panel/SetupPanel/DownloadSetupPanel/FileCacheBlock/ClearCacheTip", # 清除缓存提示

            # 关于我们
            "AboutUsTitle": "Canvas/DlgAboutUs(Clone)/Background/Top/TxtTitle", # 关于我们标题
            "AboutUsClose": "Canvas/DlgAboutUs(Clone)/Background/BtnClose",

            # 联系我们
            "ContractUsTitle": "Canvas/DlgContractUs(Clone)/Panel/Head/Title",
            "WeixinToggle": "Canvas/DlgContractUs(Clone)/Panel/LeftPanel/WeixinToggle", # 微信公众号
            "QQToggle": "Canvas/DlgContractUs(Clone)/Panel/LeftPanel/QQToggle", # QQ群
            "AddQQ": "Canvas/DlgContractUs(Clone)/Panel/RightPanel/QqPanel/QqPanel1/QqQunGroup/QqQunElement(Clone)/Button", # 加入QQ群

            # dingbu菜单栏按钮-开始
            "BtnOpenFile": "Canvas/DlgMain(Clone)/Titlebar/BtnMenuPanel/BtnOpen", # 打开文件按钮
            "BtnSave": "Canvas/DlgMain(Clone)/Titlebar/BtnMenuPanel/BtnSavePanel/BgSave", # 直接保存
            "BtnSaveMenu": "Canvas/DlgMain(Clone)/Titlebar/BtnMenuPanel/BtnSavePanel/BtnSaveMore", # 下拉保存菜单
            "BtnSaveAs": "Canvas/DlgSaveMenu(Clone)/BtnSaveAs", # 下拉另存为

            "BtnRevert": "Canvas/DlgMain(Clone)/Titlebar/BtnMenuPanel/BtnUndo",# 撤销
            "BtnRecover": "Canvas/DlgMain(Clone)/Titlebar/BtnMenuPanel/BtnRedo", # 恢复
            "BtnCreateNewFile": "Canvas/DlgMain(Clone)/Titlebar/FilesPanel/BtnAddPanel/BtnAdd", # 新建文件

            "BtnChangeBK": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/StartMenuBar/RightContainer/EditBackgroundPanel/Text",
            "BtnApplyBk": "Canvas/DlgScenePreview(Clone)/Bottom/ApplyBtn/Text", # 应用当前主题按钮
            "BtnBkLoadSlider": "Canvas/DlgScenePreview(Clone)/Preview/Loading/Text", # 应用主题加载
            "BtnFirstBk": "Canvas/DlgScenePreview(Clone)/Scroll View/Viewport/Content/0/Title",
            "DoubleClickTip": "Canvas/DlgScenePreview(Clone)/Scroll View/Viewport/Content/1/DownloadTip", # 双击下载提示
            "NoResource": "Canvas/DlgScenePreview(Clone)/Preview/NoRes/Image", # 主题场景暂无资源


            #菜单栏按钮-插入
            "BtnInsertText": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/InsertText/BtnInsertText",
            "BtnInsertTextBar": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/InsertText/BtnMoreText", # 文本下拉
            "BtnInsertTextX": "Canvas/DlgMoreText(Clone)/container/items/BtnInsertHoriontalText",  #横排文字
            "BtnInsertTextY": "Canvas/DlgMoreText(Clone)/container/items/BtnInsertVerticalText",  # 竖排文字
            "BtnInsertTextBG": "Canvas/DlgMoreText(Clone)/container/items/BtnInsertTextBG",  # 文字背景
            "BtnInsertImage": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/InsertImage/BtnInsertImage/nor_Img",
            "BtnInsertImageBar": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/InsertImage/BtnMoreImage",  # 图片下拉
            "BtnInsertImageListImage": "Canvas/DlgMoreImage(Clone)/Items/BtnInsertImageListImage",  #图片
            #"Canvas/DlgMoreImage(Clone)/container/Items/BtnInsertImageListImage"
            "BtnInsertImageListImageWall": "Canvas/DlgMoreImage(Clone)/container/Items/BtnInsertImageListImageWall",  #
            "BtnInsertPanoram": "Canvas/DlgMoreImage(Clone)/container/Items/BtnInsertPanorama", # 全景图
            "BtnInsertAudio": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/InsertAudio/BtnInsertAudio",
            "BtnInsertVideo": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/InsertVedio",
            "BtnInsertShape": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/InsertShape/BtnInsertShape",

            "BtnInsertTable": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/InsertTable/BtnInsertTable",
            "BtnInsertMath": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/InsertMath",
            "BtnInsertChart": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/Insert3DChart",
            "BtnInsert3DModel": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/InsertMenuBar/InsertPanel/Top/Insert3DModel",

            "BtnHistogram": "Canvas/DlgInsertChartPanel(Clone)/TabContent/HistogramToggle/HistogramToggleTitle",
            "BtnLine": "Canvas/DlgInsertChartPanel(Clone)/TabContent/LineToggle/LineToggleTitle",
            "BtnPie": "Canvas/DlgInsertChartPanel(Clone)/TabContent/PieToggle/PieToggleTitle",
            "BtnChart": "Canvas/DlgInsertChartPanel(Clone)/ChartTemplate/ChartTemplateContent/ChartTemplateItem(Clone)/ChartTemplateImg/InsertBtn/Text",


            "BtnShape_Line": "Canvas/DlgGeometryView(Clone)/Containter/Main/Scroll View/Viewport/Content/PresetPart/ShapeExpandPart_Line/ItemGroup/1_1/icon",
            "BtnShape_Rectangle": "Canvas/DlgGeometryView(Clone)/Containter/Main/Scroll View/Viewport/Content/PresetPart/SHAPE_TITLE_RECTANGLE/ItemGroup/2_4/icon",
            "BtnShape_Circle": "Canvas/DlgGeometryView(Clone)/Containter/Main/Scroll View/Viewport/Content/PresetPart/SHAPE_TITLE_BASESHAPE/ItemGroup/3_13/icon",
            "BtnShape_Arrow": "Canvas/DlgGeometryView(Clone)/Containter/Main/Scroll View/Viewport/Content/PresetPart/SHAPE_TITLE_ARROW/ItemGroup/4_31/icon",
            "BtnShape_Add": "Canvas/DlgGeometryView(Clone)/Containter/Main/Scroll View/Viewport/Content/PresetPart/SHAPE_TITLE_SYMBOL/ItemGroup/5_35/icon",
            "BtnShape_Process": "Canvas/DlgGeometryView(Clone)/Containter/Main/Scroll View/Viewport/Content/PresetPart/SHAPE_TITLE_FLOWCHART/ItemGroup/6_41/icon",
            "BtnShape_Start": "Canvas/DlgGeometryView(Clone)/Containter/Main/Scroll View/Viewport/Content/PresetPart/Shape_Title_Star/ItemGroup/7_44/icon",
            "BtnShape_Label": "Canvas/DlgGeometryView(Clone)/Containter/Main/Scroll View/Viewport/Content/PresetPart/Shape_Title_Label/ItemGroup/8_50/icon",

            "BtnImageBack": "Canvas/ImagePanel(Clone)/BtnReturn/Text",
            "BtnImageWallBack": "Canvas/PhotoWallPanel(Clone)/BtnReturn/Text",
            "BtnVideoBack": "Canvas/TestVideoPanel(Clone)/BtnReturn/Text",
            "BtnAudioBack": "Canvas/TestAudioPanel(Clone)/BtnReturn/Text",
            "BtnShapeBack": "Canvas/ShapeUIPanel(Clone)/ButtonReturn/Text",
            "BtnExitChart": "Canvas/DlgChartEdit(Clone)/Tab/ButtonExit/Text",

            "BtnTableCustom": "Canvas/DlgFormEdit(Clone)/Container/Button/Text",
            "SureInsertTable": "Canvas/DlgFormInsert(Clone)/Container/BtnSure/Text",

            # 文本格式
            "BtnFontBar": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/UITextFontStyle/ArrowDown", # 字体
            "BtnFontSong": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/UITextFontStyle/Dropdown List/Viewport/Content/Item 18: 宋体", # 宋体

            "BtnSizeBar": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/UITextFontSize/ArrowDown", # 大小
            "BtnSize28": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/UITextFontSize/Dropdown List/Viewport/Content/Item 14: 28", # 字体大小28号

            "BtnBold": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/BtnBold", # 加粗
            "BtnItalic": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/BtnItalic", # 倾斜
            "BtnUnderLine": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/BtnUnderline", # 下划线
            "BtnShadow": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/BtnShadow", # 阴影
            "BtnStrike": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/BtnStrike", # 删除线

            "BtnDropdown": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/DropdownChangeCase", # 大小写切换
            "BtnDrop": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/DropdownChangeCase/Dropdown List/Viewport/Content/Item 2: 全部大写", # 全部大写

            "BtnIncreaseFontSize": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/BtnIncreaseFontSize", #字体增大
            "BtnDecreaseFontSize": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/BtnDecreaseFontSize",

            "BtnSpacing": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/DropdownKerning", # 字间距
            "BtnLoose": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/DropdownKerning/Dropdown List/Viewport/Content/Item 4: 很松", # 字间距：很松

            "BtnWordColor": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextMenuBar(Clone)/Top/SelectColor", # 字体颜色
            "BtnOrange": "Canvas/DlgColorEdit(Clone)/CommonColor/GroupColor/ThemeColorGrid/Button105/Color", # 字体橙色

            "BtnRowSpacing": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextParagraphMenuBar(Clone)/Top/Rowspacing", # 行间距
            "BtnSpace2": "Canvas/DlgLineSpacing(Clone)/Container/BtnPrefab(Clone)/Text{txt=2.0}", # 行间距2.0
            "BtnSpace1": "Canvas/DlgLineSpacing(Clone)/Container/BtnPrefab(Clone)/Text{txt=1.0}",  # 行间距2.0
            "BtnSpace1.5": "Canvas/DlgLineSpacing(Clone)/Container/BtnPrefab(Clone)/Text{txt=1.5}",
            "BtnSpace2.5": "Canvas/DlgLineSpacing(Clone)/Container/BtnPrefab(Clone)/Text{txt=2.5}",
            "BtnSpace3.0": "Canvas/DlgLineSpacing(Clone)/Container/BtnPrefab(Clone)/Text{txt=3.0}",

            "BtnSpace": "Canvas/DlgLineSpacing(Clone)/Container/BtnPrefab(Clone)/Text{txt=行距选项}",

            "BtnMarksBar": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextParagraphMenuBar(Clone)/Top/Marks/BtnMore", # 段落符号
            "BtnMarksNull": "Canvas/DlgTextNumber(Clone)/Container/Mark/ItemNull", # 段落符号为空
            "BtnMarks": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextParagraphMenuBar(Clone)/Top/Marks/BtnMarks", # 快速段落符号marks
            "BtnMarks1": "Canvas/DlgTextNumber(Clone)/Container/Mark/Item1", # 符号

            "BtnIdentifierBar": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextParagraphMenuBar(Clone)/Top/Identifier/BtnMore", # 段落符号
            "BtnIdentifierNull": "Canvas/DlgTextNumber(Clone)/Container/Identifier/ItemNull",
            "BtnIdentifier": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextParagraphMenuBar(Clone)/Top/Identifier/BtnIdentifier", # 快速段落符号数字
            "BtnIdentifier1": "Canvas/DlgTextNumber(Clone)/Container/Identifier/Item1", # 数字符号

            "BtnDecIndent": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextParagraphMenuBar(Clone)/Top/BtnDecreaseIndent", # 减少缩进
            "BtnIncIndent": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextParagraphMenuBar(Clone)/Top/BtnIncreaseIndent",  # 增加缩进

            "TextFormatShow": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextParagraphMenuBar(Clone)/Top/BtnAlignLeft/Image", # 判断文字格式显示

            # 艺术字格式
            "WordArtStyle": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextWordArtMenuBar(Clone)/Top/WordArt/Group/WordArtPrefab(Clone)/Icon", # 艺术字样式
              "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/TextFormatMenuBar(Clone)/TextWordArtMenuBar(Clone)/Top/WordArt/Group/WordArtPrefab(Clone)/Icon"

            # 音频格式
            "NoTypeLabel": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/AudioMenuBar(Clone)/AudioMainPanel/NoneStyleToggle/NoTypeLabel",  # 无样式
            "HideOnPlayLabel": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/AudioMenuBar(Clone)/AudioMainPanel/HideOnPlayToggle/HideOnPlayLabel",  #放映时隐藏
            "LoopLabel": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/AudioMenuBar(Clone)/AudioMainPanel/LoopToggle/LoopLabel",  # 循环播放
            "BackgroundLabel": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/AudioMenuBar(Clone)/AudioMainPanel/BackgroundToggle/BackgroundLabel",  # 在后台播放
             "AlwaysPlayLabel": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/AudioMenuBar(Clone)/AudioMainPanel/AcrossSliderToggle/AlwaysPlayLabel",  # 跨幻灯片播放


            # 文字背景
            "BG_Text_1": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgTextBackground(Clone)/Root/TabPage/StaticPage/ScrollView/Viewport/Content/TextBackgroundItem(Clone)/root",  # 文字背景1

            # 舞台左侧缩略图
            "BtnNewPage": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Bottom/BottomContainer/Btn_AddNewPage", # 新建幻灯片按钮
            "PageNum": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)/LeftContainer/Top/Number",# PPT页编号

            "BtnPlaying": "Canvas/DlgMain(Clone)/Titlebar/BtnMenuPanel/BtnPlay/BackImage",  # 首页播放
            "BtnPlayFirst": "Canvas/DlgMain(Clone)/BottomPanel/BtnPlayFirst", # 当前页播放

            "PageItem": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)", # 幻灯片
            "PageItem1": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)[1]",
        # 幻灯片
            "PageItem2": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)[2]",
            "PageItem3": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)[3]",

            # 幻灯片
            "BtnPageDelete": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)/Icon/BtnDelete",
            "BtnTransition": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)/LeftContainer/Bottom/BtnTransition",  # 转场效果按钮
            "ImgLoading": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)/BG_Black/Load",
            "IsPageSelected": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)/RightContainer/ViewContainer/BG", # 选中态
            "IsPageSelected1": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)[1]/RightContainer/ViewContainer/BG",
        # 选中态
            "IsPageSelected2": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/PageViewList(Clone)/Scroll View/Viewport/Content/Item(Clone)[2]/RightContainer/ViewContainer/BG",

            "BtnCloseTransition": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/DlgTransition(Clone)/Container/Title/BtnClose",
            "DlgTransition": "Canvas/DlgMain(Clone)/OptionPanel/Left/LeftContainer/DlgTransition(Clone)/Container",  # 转场动效弹窗


            # 舞台中央
            "SliderTip": "Canvas/DlgProgressBar(Clone)/Content",  # 提示进度条
            "ParaContainer": "Canvas/DlgParagraph(Clone)/Container", # 段落行距设置界面
            "ParaContainerClose": "Canvas/DlgParagraph(Clone)/Container/Title/BtnClose",  # 关闭设置界面
            "AudioTitle": "UIFollow(Clone)/AudioControlPanel(Clone)/middle/Title",  # 音频名称
            "FloatTool": "Canvas/DlgTextShortcutTool(Clone)", # 浮动工具栏

            "CloseDlgConfirm": "Canvas/DlgAlertBox(Clone)/DlgConfirm", # 关闭文件提示框
            "DlgConfirmTxt": "Canvas/DlgAlertBox(Clone)/DlgConfirm/PnlContent/TxtCenter", # 文件保存提示
            "TxtLeftButton": "Canvas/DlgAlertBox(Clone)/DlgConfirm/PnlContent/PnlButton/BtnConfirmLeft/TxtLeftButton", # 是（弹窗）
            "TxtCenterButton": "Canvas/DlgAlertBox(Clone)/DlgConfirm/PnlContent/PnlButton/BtnConfirmCenter/TxtCenterButton", # 否
            "TxtRightButton": "Canvas/DlgAlertBox(Clone)/DlgConfirm/PnlContent/PnlButton/BtnConfirmRight/TxtRightButton", # 取消

            "BtnMoveStep": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/MoveStep", # 遠近調整按鈕
            "BtnRotateByXAxis": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/RotateByXAxis",
            "BtnRotateByYAxis": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/RotateByYAxis",
            "BtnRotateByZAxis": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/RotateByZAxis",
            "BtnDragball0": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/Dragball0", # 等比缩放左上角
            "BtnDragball5": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/Dragball5", # 左

            "BtnRotateByXAxisDown": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/RotateByXAxisDown", # 快捷出现

            # 舞台底部
            "SliderFileSave": "Canvas/DlgMain(Clone)/BottomPanel/SliderFileSave",
            "TxtSaveStatus": "Canvas/DlgMain(Clone)/BottomPanel/TxtSaveStatus",
            "SliderFileOpen": "Canvas/DlgMain(Clone)/Titlebar/FilesPanel/FileTabList/FileTab(Clone)/SliderProgress/Handle Slide Area/Handle",
            "SliderFileOpen2": "Canvas/DlgMain(Clone)/Titlebar/FilesPanel/FileTabList/FileTab(Clone)[3]/SliderProgress/Handle Slide Area/Handle", # 打开文件进度条


            # 幻灯片背景
            "LocalSceneCtgText": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/SceneTitlePanel/LocalSceneCtgButton/LocalSceneCtgText", # 当前主题
            "ServerSceneCtgText": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/SceneTitlePanel/ServerSceneCtgButton/ServerSceneCtgText", # 更多主题
            "CurrentSceneNameText": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/SelectionScenePanel/CurrentSceneNameText", # 当前场景名称
            "HoverSceneItemImage": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/LocalScenePanel/LocalSceneItemGroup/Container/SceneItem(Clone)/SceneItemButton/HoverSceneItemImage", # 场景缩略图
            "CurrentSceneItemImage": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/LocalScenePanel/LocalSceneItemGroup/Container/SceneItem(Clone)/SceneItemButton/CurrentSceneItemImage", # 已应用标志
            "SceneItemButton": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/LocalScenePanel/LocalSceneItemGroup/Container/SceneItem(Clone)/SceneItemButton", #
            "SceneItemApplyText": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/LocalScenePanel/LocalSceneItemGroup/Container/SceneItem(Clone)/SceneItemApplyButton/SceneItemApplyText", # 应用场景
            "SceneItemNameText": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/LocalScenePanel/LocalSceneItemGroup/Container/SceneItem(Clone)/SceneItemNameButton/SceneItemNameText", # 场景名称
            "HoverSceneItemImage1": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/LocalScenePanel/LocalSceneItemGroup/Container/SceneItem/SceneItemButton/HoverSceneItemImage",
        # 场景缩略图
            "CurrentSceneItemImage1": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/LocalScenePanel/LocalSceneItemGroup/Container/SceneItem/SceneItemButton/CurrentSceneItemImage",
        # 已应用标志
            "SceneItemButton1": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/LocalScenePanel/LocalSceneItemGroup/Container/SceneItem/SceneItemButton",
        #
            "SceneItemApplyText1": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/LocalScenePanel/LocalSceneItemGroup/Container/SceneItem/SceneItemApplyButton/SceneItemApplyText",
        # 应用场景
            "SceneItemNameText1": "Canvas/DlgMain(Clone)/OptionPanel/Right/dlg3dpptscene(Clone)/PanelBottom/LocalScenePanel/LocalSceneItemGroup/Container/SceneItem/SceneItemNameButton/SceneItemNameText",
        # 场景名称


            #--段落设置界面
            "AlignBar": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Common/Options/Option1/Dropdown", # 对齐方式下拉
            "AlignLabel": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Common/Options/Option1/Dropdown/Label", # 已选对齐方式
            "AlignLeft": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Common/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 0: 左对齐",  # 左对齐
            "AlignRight": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Common/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 1: 右对齐", # 右对齐
            "AlignDouble": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Common/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 2: 两端对齐",
            "AlignMiddle": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Common/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 3: 居中",
            "AlignSep": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Common/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 4: 分散对齐",
            "BtnParaOK": "Canvas/DlgParagraph(Clone)/Container/BottomBar/BtnOk",  # 确定段落设置
            "BtnParaCancle": "Canvas/DlgParagraph(Clone)/Container/BottomBar/BtnCancel",  # 取消段落设置

            "InputFieldIndent": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Indentation/Options/Option0/InputField/Text", # 文本之前缩进大小
            "BtnAddIndent": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Indentation/Options/Option0/InputField/BtnAdd", # 增加缩进按钮
            "BtnSubIndent": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Indentation/Options/Option0/InputField/BtnSub", # 减少缩进按钮

            "LabelSpecialFormat": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Indentation/Options/Option1/Dropdown/Label", # 缩进特殊格式
            "SpecialFormat_0": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Indentation/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 0: （无）",  # 特殊格式：无
            "SpecialFormat_1": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Indentation/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 1: 首行缩进",
            "SpecialFormat_2": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Indentation/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 2: 悬挂缩进",
            "InputFieldSpe": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Indentation/Options/Option2/InputField/Text",# 悬挂缩进大小

            "InputFieldPara1": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option0/InputField/Text", #段前输入
            "InputFieldPara2": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option3/InputField/Text", # 段后输入
            "ParaQianAdd": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option0/InputField/BtnAdd", # 段前增加
            "ParaQianSub": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option0/InputField/BtnSub", #段前减少
            "ParaHouAdd": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option3/InputField/BtnAdd", # 段后增加
            "ParaHouSub": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option3/InputField/BtnSub",# 段后减少
            "InputFieldParaSpace": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option1/Dropdown/Label",# 行距输入
            "RowSpace1": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 0: 单倍行距",
            "RowSpace2": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 1: 1.5倍行距",
            "RowSpace3": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 2: 双倍行距",
            "RowSpace4": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 3: 固定值",
            "RowSpace5": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option1/Dropdown/Dropdown List/Viewport/Content/Item 4: 多倍行距",
            "InputFieldParaSpace2": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option2/InputField/Text", #固定值设置
            "ParaSpaceAdd": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option2/InputField/BtnAdd", # 设置值增加
            "ParaSpaceSub": "Canvas/DlgParagraph(Clone)/Container/SetupPanel/Spacing/Options/Option2/InputField/BtnSub",

            # 临时按钮
            "BtnNewFile": "Canvas/DlgMain(Clone)/Demo/BtnCreate/Text", # 新建文件

            # 放映状态
            "BtnNextPage": "Canvas/DlgPlayMode(Clone)/PlayerControlPanel/LeftBtnContainer/LeftNextPageBtn", # 下一页
            "BtnLastPage": "Canvas/DlgPlayMode(Clone)/PlayerControlPanel/LeftBtnContainer/LeftPrevPageBtn", # 上一页
            "BtnExitPlaying": "Canvas/DlgPlayMode(Clone)/BtnClose", # 放映态关闭

            "Tip": "Canvas/DlgHyperlinkShowTip(Clone)/Container/Text", # 超链接提示

            "BtnPlayingRight": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container", # 右键
            "BtnElementOption": "Canvas/DlgPlayItemMenu(Clone)/Container",
            "BtnElementOptionOpen": "Canvas/DlgPlayItemMenu(Clone)/Container/BtnOpen",
            "BtnElementOptionClose": "Canvas/DlgPlayItemMenu(Clone)/Container/BtnClose",
            "TextMenuFunc": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name",

            "PlayingPage": "Canvas/DlgPlayMode(Clone)/ThumbnailPanel/Index/Text",


            # 舞台右键
            "BtnStageRight": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name", # 舞台右键元素列表
            "BtnStageRightCut": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=剪切}",
            "BtnStageRightCut2": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Icon{img=ContextMenu_Cut_nor}",
            "BtnStageRightCopy": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=复制}",
            "BtnStageRightCopy2": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Icon{img=ContextMenu_Copy_nor}",
            "BtnStageRightPaste": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=粘贴}}",
            "BtnStageRightPaste2": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Icon{img=ContextMenu_Paste_dis}",
            "BtnStageRightDel": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=删除}",
            "BtnStageRightDel2": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Icon{img=ContextMenu_DeleteItem_nor}",
            "BtnStageRightReplace": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=替换}",
            "BtnStageRightHyperLink": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=超链接}",
            "BtnStageRightHyperLink2": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=<color=#BEBEBEFF>超链接</color>}",
            "BtnStageRightNewPage": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=新建幻灯片}",
            "BtnStageRightEditTrans": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Icon{img=ContextMenu_ChangeState_dis}",
            "BtnStageRightEditTrans2": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Icon{img=ContextMenu_ChangeState_nor}",
            "BtnStageRightChangeBK": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=背景更换}",
            "BtnStageRightImageWallSetting": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=图片墙设置}",
            "BtnStageRightDelTable": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=删除表格}",
            "BtnStageRightChartSet": "Canvas/DlgContextMenu(Clone)/ContextMenuItemPrefabWithoutChildMenu(Clone)/Container/Name{txt=图表设置}",

            # 图片墙
            "BtnImageWallConfirm": "Canvas/DlgSelectPhotoWall(Clone)/Panel/footer/BtnConfirm/Text",
            "BtnImageWallCancle": "Canvas/DlgSelectPhotoWall(Clone)/Panel/footer/BtnCancle/Text",

            # tmp

            # 超链接
            "BtnDisk": "Canvas/DlgHyperlinkMain(Clone)/Container/Content/RightPanel/Content/FileMidPanel/MainScrollRect/Viewport/Content/FileBaseTemp(Clone)",
            "BtnLinkSubmit": "Canvas/DlgHyperlinkMain(Clone)/Container/Content/RightPanel/BottomPanel/BtnSubmit",
            "BtnPPTToggle": "Canvas/DlgHyperlinkMain(Clone)/Container/Content/LeftPanel/LeftPanelTglGroup/LinkPPTToggle",

            "TglPreviousPPT": "Canvas/DlgHyperlinkMain(Clone)/Container/Content/RightPanel/Content/PPTMidPanel/PPTList/Scroll View/Viewport/Content/TglPreviousPPT", # 上一页幻灯片
            "ScreenShowTextBtn": "Canvas/DlgHyperlinkMain(Clone)/Container/Content/RightPanel/Title/ScreenShowTextBtn",
            "TipInputField": "Canvas/DlgHyperlinkTip(Clone)/Container/Bottom/TipInputField",
            "BtnTipSubmit": "Canvas/DlgHyperlinkTip(Clone)/Container/Bottom/BtnSubmit",
            "WebPathInputField": "Canvas/DlgHyperlinkMain(Clone)/Container/Content/RightPanel/Content/FileMidPanel/PathContainer/PathInputField", # 网页地址

            "BtnOpenDisk": "Canvas/DlgHyperlinkMain(Clone)/Container/Content/RightPanel/Content/FileMidPanel/GotoParentBtn/Icon",  # 打开本地磁盘

            # 图片格式
            "BorderStyleItem": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ImageMenuBar(Clone)/BorderStyleGroupPanel/BorderStyleGroup/BorderStyleItem(Clone)", # 图片边框
            "BtnClearBorder": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ImageMenuBar(Clone)/BtnClearBorder",  # 清除图片边框
            "BtnBorderFactor": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ImageMenuBar(Clone)/BtnBorderFactor", # 边框粗细设置
            "BorderPercent": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ImageMenuBar(Clone)/BtnBorderFactor/Percent", # 边框粗细百分比
            "ThickPanel": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ImageMenuBar(Clone)/ThickPanel", # 粗细面板
            "BtnBorderSub": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ImageMenuBar(Clone)/ThickPanel/BtnSub",
            "BtnBorderAdd": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ImageMenuBar(Clone)/ThickPanel/BtnAdd",
            "BorderSlider": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ImageMenuBar(Clone)/ThickPanel/Slider/Handle Slide Area/Handle", # 滑块

            "ImageWallWarn": "Canvas/DlgSimpleAlert(Clone)/Panel/Body/TextCenter", # 圖片墻數量提示
            "BtnImageWallMore": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/StartMenuBar/LeftContainer/TextParagraphMenuBar(Clone)/Top/Marks", # 圖片墻圖片菜單
            "BtnAddImage": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemImage/PanelItemImage/GroupItemImage/BtnAddImage", # 添加圖片
            "ItemImageWall": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemImage/PanelItemImage/GroupItemImage/ItemImage(Clone)", # 圖片墻圖片
            "ItemImageWallClose": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemImage/PanelItemImage/GroupItemImage/ItemImage(Clone)/BtnClose",

            "ImageWallShowEdit": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemAction/ItemActionShowEdit", # 图片墙播放设置
            "TextImageCount": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemImage/TextImageCount", #图片墙图片数量

            "ItemActionPlayMode": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemAction/ItemActionPlayMode",
            "CurrentPlayMode": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemAction/ItemActionPlayMode/DropDown/TextCurrentAction",
            "ManualMode": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemAction/ItemActionPlayMode/PanelDown/Group/Item/Text (1)", # 下拉列表
            "AutoMode": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemAction/ItemActionPlayMode/PanelDown/Group/Item (1)/Text (1)", # 下拉列表

            "ImageWallShowType": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemShowType/PanelItemShowType/Left/Viewport/Content/ItemShowType(Clone)", # 图片墙展示方式(设置界面)
            "ShowTypeListDown": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemShowType/PanelItemShowType/TurnPage/BtnDown", # 向下
            "ShowTypeListUp": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemShowType/PanelItemShowType/TurnPage/BtnUp", #
            "ShowTypeListMore": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemShowType/PanelItemShowType/TurnPage/BtnMore",

            "ImageListUp": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemImage/DivTurnPage/BtnUp", # 图片上拉
            "ImageListDown": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemImage/DivTurnPage/BtnDown",
            "ImageListMore": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/PhotoWallBar(Clone)/DivItemImage/DivTurnPage/BtnMore",


            "ImageWallSelectTitle": "Canvas/DlgSelectPhotoWall(Clone)/Panel/Head/Title", # 图片墙弹窗标题
            "ShowTypeAll": "Canvas/DlgSelectPhotoWall(Clone)/Panel/Body/LeftPanel/Toggle",  # 全部
            "ShowTypeOrder": "Canvas/DlgSelectPhotoWall(Clone)/Panel/Body/LeftPanel/Toggle (1)",  # 顺序关系
            "ShowTypeCompared": "Canvas/DlgSelectPhotoWall(Clone)/Panel/Body/LeftPanel/Toggle (2)",  # 对比关系
            "ShowTypeMain": "Canvas/DlgSelectPhotoWall(Clone)/Panel/Body/LeftPanel/Toggle (3)",  # 主次关系
            "NoModeTips": "Canvas/DlgSelectPhotoWall(Clone)/Panel/Body/PanelCenter/ModeTips/Text", # 暂无样式
            "ItemShowType": "Canvas/DlgSelectPhotoWall(Clone)/Panel/Body/PanelCenter/Center/Viewport/Content/ItemShowType(Clone)", # 展示方式列表

            # 音频
            "AudioControlPanel": "UIFollow(Clone)/AudioControlPanel(Clone)",

            "ToggleCourse": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/EduResList(Clone)/EduResTypesContainer/EduResTypesMask/EduResTypesContent/ToggleCourse",
        # 插入课件
            "Toggle3DResource": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/EduResList(Clone)/EduResTypesContainer/EduResTypesMask/EduResTypesContent/Toggle3DResource",
        # 插入3D资源
            "ToggleSubjectTool": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/EduResList(Clone)/EduResTypesContainer/EduResTypesMask/EduResTypesContent/ToggleSubjectTool",
        # 插入学科工具
            "ToggleMedia": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/EduResList(Clone)/EduResTypesContainer/EduResTypesMask/EduResTypesContent/ToggleMedia",
        # 插入多媒体
            "ToggleExercise": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/EduResList(Clone)/EduResTypesContainer/EduResTypesMask/EduResTypesContent/ToggleExercise",
        # 插入基础习题
            "ToggleInteractExercise": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/EduResList(Clone)/EduResTypesContainer/EduResTypesMask/EduResTypesContent/ToggleInteractExercise",
        # 插入趣味习题

            #课件
            "InsertWholeResource": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/ResourcesList(Clone)/DataPanel/GridDataWidget(Clone)/Viewport/Content/CommonListItem(Clone)/Bottom/Menu/InsertBtn",
        # 插入整个课件
            "InsertOneCourse": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/ResourcesList(Clone)/ResourcesSubList(Clone)/DataPanel/Scroll View/Viewport/Content/CommonListItem2(Clone)/Bottom/Menu/InsertBtn", # 插入单个课件
            "ItemCourse": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/ResourcesList(Clone)/CategoryPanel/SubCategory/Viewport/Content/SubCategoryItem(Clone)", # 类别
            "AllResource": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/ResourcesList(Clone)/CategoryPanel/TagPanel/ResourceTagWidget(Clone)/ResourceTagRect(Clone)/全部", #类别全部
            "CoursePageShow": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/ResourcesList(Clone)/DataPanel/GridDataWidget(Clone)/Viewport/Content/CommonListItem(Clone)/Mask/Thumbnail", # 打开课件列表

            # 3D资源

            # 学科工具
            "CefWordShow": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/ResourcesList(Clone)/DataPanel/GridDataWidget(Clone)/Viewport/Content/CommonListItem(Clone)/Bottom/Menu/SingleBtn", # 展开生字卡
            "BtnInsertCefWord": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/ResourcesList(Clone)/DataPanel/WordcardList(Clone)/Scroll View/Viewport/Content/CommonListItem(Clone)/Bottom/Menu/InsertBtn", # 生字卡插入

            # 多媒体
            "InsertAudioResource": "Canvas/DlgMain(Clone)/OptionPanel/Right/RightContainer/ResourcesList(Clone)/DataPanel/GridDataWidget(Clone)/Viewport/Content/AudioListItem(Clone)/Right/InsertBtn/Text", # 音频插入按钮

            # 选中


            # 音视频播放设置
            "MediaPlayerCtrlPanel": "UIFollow(Clone)/MediaPlayerCtrlPanel_UI(Clone)", # 播放控件
            "BtnMediaPlay": "UIFollow(Clone)/MediaPlayerCtrlPanel_UI(Clone)/Left/BtnPlay", # 播放按钮

            "BtnVideoStyleMore": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoStylePanel/StylePart/TurnPage/BtnMore",
            "VideoPlayModeDropdown": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/PlayModePanel/PlayModeText/PlayModeDropdown", # 播放设置
            "VideoPlayClick": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/PlayModePanel/PlayModeText/PlayModeDropdown/Dropdown List/Viewport/Content/Item 0: 点击时播放",
            "VideoPlayAuto": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/PlayModePanel/PlayModeText/PlayModeDropdown/Dropdown List/Viewport/Content/Item 1: 自动播放",
            "VideoPlayCurrentTime": "UIFollow(Clone)/MediaPlayerCtrlPanel_UI(Clone)/Middle/ProgressText/TotalTime/textSeparator/CurTime",
            "VideoShowTypeLabel": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/ShowTypePanel/ShowTypeText/ShowTypeDropdown/Label",
            "VideoShowTypeStill": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/ShowTypePanel/ShowTypeText/ShowTypeDropdown/Dropdown List/Viewport/Content/Item 0: 首帧静止展示",
            "VideoShowTypeMute": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/ShowTypePanel/ShowTypeText/ShowTypeDropdown/Dropdown List/Viewport/Content/Item 1: 静音播放展示",
            "VideoShowTypeHide": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/ShowTypePanel/ShowTypeText/ShowTypeDropdown/Dropdown List/Viewport/Content/Item 2: 隐藏画面展示",
            "VideoPanelPlay": "UIFollow(Clone)/MediaPlayerCtrlPanel_UI(Clone)/Left/BtnPlay",

            "BtnVideoPlayFullScreen": "UIFollow(Clone)/MediaPlayerCtrlPanel_UI(Clone)/Right/BtnFullScreen", # 视频全屏
            "BtnVideoPlayWindow": "UIFollow(Clone)/MediaPlayerCtrlPanel_UI(Clone)/Right/BtnWindowPlay", # 更多3D化样式
            "WindowPlayToggle": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/WindowPlayToggle", # 是否窗口播放
            "LoopToggle": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/LoopToggle", # 是否循环播放
            "SwitchEffectToggle": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/SwitchEffectToggle", # 是否转场效果
            "HidePlayerToggle": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/VideoMenuBar(Clone)/VideoMainPanel/HidePlayerToggle", # 是否隐藏播放器

            "PlayFillArea": "UIFollow(Clone)/MediaPlayerCtrlPanel_UI(Clone)/Middle/Progress/Fill Area", # 播放进度条
            "PlayHandle": "UIFollow(Clone)/MediaPlayerCtrlPanel_UI(Clone)/Middle/Progress/Handle Slide Area/Handle", # 播放点
            "PlayedFillArea": "UIFollow(Clone)/MediaPlayerCtrlPanel_UI(Clone)/Middle/Progress/Fill Area/Fill", # 已播放进度条

            "NoStyleItem": "Canvas/DlgVideoStyleList(Clone)/Container/NoneStyleGroup/GroupContent/StyleItem(Clone)", # 无样式类
            "EntityItem": "Canvas/DlgVideoStyleList(Clone)/Container/EntityGroup/GroupContent/StyleItem(Clone)", # 视频3D化3D实物类
            "ConceptItem": "Canvas/DlgVideoStyleList(Clone)/Container/ConceptGroup/GroupContent/StyleItem(Clone)", # 3D概念类

            "AudioPlayCurrentTime": "UIFollow(Clone)/AudioControlPanel(Clone)/middle/TimeContainer/AudioLength/textSeparator/AudioPlayerTimer", # 音频播放时间
            "BtnAudioPlay": "UIFollow(Clone)/AudioControlPanel(Clone)/left/BtnPlayAudio",
            "AudioPlayerCtrlPanel": "UIFollow(Clone)/AudioControlPanel(Clone)",
            "AudioPlayHandle": "UIFollow(Clone)/AudioControlPanel(Clone)/middle/ProgressSlider/Handle Slide Area/Handle",
            "AudioPlayedFillArea": "UIFollow(Clone)/AudioControlPanel(Clone)/middle/ProgressSlider/Fill Area/Fill",
            "AudioPlayFillArea": "UIFollow(Clone)/AudioControlPanel(Clone)/middle/ProgressSlider",
            "AudioPlayModeDropdown": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/AudioMenuBar(Clone)/AudioMainPanel/PlayModePanel/PlayModeText/PlayModeDropdown",
            "AudioPlayClick": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/AudioMenuBar(Clone)/AudioMainPanel/PlayModePanel/PlayModeText/PlayModeDropdown/Dropdown List/Viewport/Content/Item 0: 点击时播放",
            "AudioPlayAuto": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/AudioMenuBar(Clone)/AudioMainPanel/PlayModePanel/PlayModeText/PlayModeDropdown/Dropdown List/Viewport/Content/Item 1: 自动播放",
            "AudioLoopToggle": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/AudioMenuBar(Clone)/AudioMainPanel/LoopToggle",
            "AudioBackgroundToggle": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/AudioMenuBar(Clone)/AudioMainPanel/BackgroundToggle",

            "BtnShapeChange": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ShapeMenuBar(Clone)/ChangeShape/BtnShapeChange/Text", # 更改形状按钮
            "ShapeChangeDlg": "Canvas/DlgGeometryView(Clone)/Containter/Main", # 更改形状的列表
            "ShapeStyleItem01": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ShapeMenuBar(Clone)/ChangeStyle/StylePart/DefaultStyleGroup/StyleItem(Clone)/Image{img=style_rect_01}", # 形状样式
            "BtnShapeFillMore": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ShapeMenuBar(Clone)/ChangeStyle/StyleBtns/Btn_FillMore/Text", # 形状填充
            "TransparentText": "Canvas/DlgColorEdit(Clone)/CommonColor/Setalpha/InputField/Text", # 透明度文本框
            "BtnShapeOutlineMore": "Canvas/DlgMain(Clone)/EditPanelMask/EditPanel/FormatMenuBar/ShapeMenuBar(Clone)/ChangeStyle/StyleBtns/Btn_OutlineMore", # 更改形状轮廓
            "OutlineBlack": "Canvas/DlgColorEdit(Clone)/CommonColor/GroupColor/ThemeColorGrid/Button101", # 形状轮廓黑色
            "OutlineType": "Canvas/DlgColorEdit(Clone)/CommonColor/MiddleAnchor/ColorItemPrefab(Clone)/Text{txt=线段类型}", # 轮廓线条类型
            "OutlineWidth": "Canvas/DlgColorEdit(Clone)/CommonColor/MiddleAnchor/ColorItemPrefab(Clone)/Text{txt=线宽}", # 轮廓线条宽
            "OutlineArrow": "Canvas/DlgColorEdit(Clone)/CommonColor/MiddleAnchor/ColorItemPrefab(Clone)/Text{txt=箭头样式}",
            "LineWidthItem6":"Canvas/DlgLineWidth(Clone)/LineWidthPanel/LineWidthGroup/LineWidthItem/Text{txt=6 磅}", # 线条宽度类型
            "LineTypeItem1": "Canvas/DlgLineType(Clone)/LineTypePanel/LineTypeGroup/LineTypeItem/Image{img=形状轮廓-线段类型1-实线}",
            "LineTypeItem2": "Canvas/DlgLineType(Clone)/LineTypePanel/LineTypeGroup/LineTypeItem/Image{img=形状轮廓-线段类型2-圆点}", # 线条类型
            "LineTypeItem3": "Canvas/DlgLineType(Clone)/LineTypePanel/LineTypeGroup/LineTypeItem/Image{img=形状轮廓-线段类型3-方点}",
            "LineTypeItem4": "Canvas/DlgLineType(Clone)/LineTypePanel/LineTypeGroup/LineTypeItem/Image{img=形状轮廓-线段类型4-短划线}",
            "LineTypeItem5": "Canvas/DlgLineType(Clone)/LineTypePanel/LineTypeGroup/LineTypeItem/Image{img=形状轮廓-线段类型5-划线-点}",
            "LineTypeItem6": "Canvas/DlgLineType(Clone)/LineTypePanel/LineTypeGroup/LineTypeItem/Image{img=形状轮廓-线段类型6-长划线}",
            "LineTypeItem7": "Canvas/DlgLineType(Clone)/LineTypePanel/LineTypeGroup/LineTypeItem/Image{img=形状轮廓-线段类型7-长划线-点}",
            "LineTypeItem8": "Canvas/DlgLineType(Clone)/LineTypePanel/LineTypeGroup/LineTypeItem/Image{img=形状轮廓-线段类型8-长划线-点-点}",

            # 旋转
            "RotateByYAxisNor": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/RotateByYAxis",
            "RotateByYAxisHov": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/RotateByYAxis{img=rotate_y_hov}",
            "RotateByXAxisNor": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/RotateByXAxis",
            "RotateByXAxisHov": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/RotateByXAxis{img=rotate_x_hov}",
            "RotateByZAxisNor": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/RotateByZAxis",
            "RotateByZAxisHov": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/RotateByZAxis{img=rotate_z_hov}",
            "MoveStepNor": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/MoveStep",
            "MoveStepHov": "(singleton) BasicOperation.EasyGizmoManager/GizmoHandles(Clone)/MoveStep{img=move_step_hov}",

            # 表格
            "ItemPrefab": "Canvas/DlgFormEdit(Clone)/Container/Content/ItemPrefab(Clone)", # 单元格
            "TableRowInput": "Canvas/DlgFormInsert(Clone)/Container/InputGroup/RowInputField",
            "TableColumnInput": "Canvas/DlgFormInsert(Clone)/Container/InputGroup/ColumnInputField",

            # 幻灯片比例设置
            "BtnAddScale": "Canvas/DlgMain(Clone)/BottomPanel/Tool/BtnAddScale", # 放大
            "BtnDecScale":"Canvas/DlgMain(Clone)/BottomPanel/Tool/BtnDecScale", # 缩小
            "SacleHandle": "Canvas/DlgMain(Clone)/BottomPanel/Tool/SliderScale/Handle Slide Area/Handle", # 比例滑动
            "SliderScale": "Canvas/DlgMain(Clone)/BottomPanel/Tool/SliderScale", # 滑动条
            "TextScaleValue": "Canvas/DlgMain(Clone)/BottomPanel/Tool/TextScaleValue", # 比例百分比
            "BtnNormalScale": "Canvas/DlgMain(Clone)/BottomPanel/BtnNormalScale", # 还原比例

            # 3D图表
            "ChartData": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData", # 图表数据界面
            "ChartOption": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartOption", # 图表设置界面
            "ChartTemplate": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartTemplate", # 更换模板界面
            "ChartRow": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData/Mask/ChartDataContent/ChartTable/Viewport/ChartTableContent/ChartTableBody/ChartRow(Clone)", #表格行数
            "ChartColumn": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData/Mask/ChartDataContent/ChartTable/Viewport/ChartTableContent/ChartTableBody/ChartRow(Clone)[7]/ChartTableCell(Clone)",
            "ChartTableCell_6": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData/Mask/ChartDataContent/ChartTable/Viewport/ChartTableContent/ChartTableBody/ChartRow(Clone)[7]/ChartTableCell(Clone)[2]/Text", # 3D图表第六行单元格
            "ChartTableCell_5": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData/Mask/ChartDataContent/ChartTable/Viewport/ChartTableContent/ChartTableBody/ChartRow(Clone)[6]/ChartTableCell(Clone)[2]/Text",
            "ChartTableCell_4": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData/Mask/ChartDataContent/ChartTable/Viewport/ChartTableContent/ChartTableBody/ChartRow(Clone)[5]/ChartTableCell(Clone)[2]/Text",
        # 3D图表第4行单元格

            "ChartConfirmBtn": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData/Mask/ChartDataContent/ChartTable/ConfirmBtn/Text", # 图表数据确定
            "ChartOptionToggleTitle": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Tab/TabContent/ChartOptionToggle/ChartOptionToggleTitle", # 图表设置tab
            "ChartTitleInputField": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartOption/Mask/ChartOptionContent/ChartTitleInputField/Text", # 图表标题输入框
            "ChartConfirmAll": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartOption/Mask/ChartOptionContent/ConfirmAll/Text", # 图表设置全部应用
            "AddTypeDropdown": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData/Mask/ChartDataContent/ChartTable/AddPanel/AddTypeDropdown/Label", # 添加类型
            "AddBtn": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData/Mask/ChartDataContent/ChartTable/AddPanel/AddBtn", #添加
            "AddTypeRow": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData/Mask/ChartDataContent/ChartTable/AddPanel/AddTypeDropdown/Dropdown List/Viewport/Content/Item 0: 行",
            "AddTypeColumn": "Canvas/DlgMain(Clone)/OptionPanel/Right/DlgChartEdit(Clone)/Content/ChartData/Mask/ChartDataContent/ChartTable/AddPanel/AddTypeDropdown/Dropdown List/Viewport/Content/Item 1: 列",


        }
