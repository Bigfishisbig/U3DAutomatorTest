# coding=utf-8
"""
Open3DPPT
作者: qa-wang
版本: 3DPPT Final.2017.1225.1314
创建日期：2017.12.26
修改日期：2017.12.26
"""

import os, sys, inspect

class SourcePath(object):

    def current_file_directory():
        path = os.path.realpath(sys.path[0])
        if os.path.isfile(path):
            path = os.path.dirname(path)
            return os.path.abspath(path)
        else:
            caller_file = inspect.stack()[1][1]
            return os.path.abspath(os.path.dirname(caller_file))

    File_PCPA = "D:\Program Files (x86)\PCPA ASSISTENT\AutoImport\ProAutoImport.exe"
    File_Source = current_file_directory() + "\\Source\\"

    # File_3DPPT_EXE_PATH = "E:/Program Files (x86)/3DPPT/3DPPT.exe"  # 3DPPT安装位置
    File_3DPPT_Kill = current_file_directory() +"\\Source\\kill3dppt.bat"
    File_Log_Analysis_PPTX = current_file_directory() + "\\Source\\Log_Analysis_PPTX.log"
    File_Log_Analysis_3DPX = current_file_directory() + "\\Source\\Log_Analysis_3DPX.log"
    File_Log_Insert_Course = current_file_directory() + "\\Source\\Log_Course.log"
    File_Image_Icon_3DPPT = current_file_directory() + "\\Source\\Img\\img_icon_3DPPT.png"
    File_Image_Icon_Close_3DPPT = current_file_directory() + "\\Source\\Img\\img_icon_close_3DPPT.png"

    File_3DPPTOpenTest_3dpx = current_file_directory() + "\\Source\\3DPPTOpenTest.3dpx"
    File_3DPPTOpenTestSave_3dpx = current_file_directory() + "\\Source\\3DPPTOpenTestSave.3dpx"
    File_PPTOpenTest_3dpx = current_file_directory() + "\\Source\\PPTOpenTest.3dpx"
    File_PPTOpenTestSave_3dpx = current_file_directory() + "\\Source\\PPTOpenTestSave.3dpx"
    File_PPTOpenTestSave_pptx = current_file_directory() + "\\Source\\PPTOpenTestSave.pptx"
    File_PPTOpenTest_pptx = current_file_directory() + "\\Source\\PPTOpenTest.pptx"
    File_PPTSaveTestForm_3dpx = current_file_directory() + "\\Source\\PPTSaveTestFrom.3dpx"
    File_PPTSaveTestTo_3dpx = current_file_directory() + "\\Source\\PPTSaveTestTo.3dpx"
    File_YSWG_3dpx = current_file_directory() + "\\Source\\3DPPTOpenTest.3dpx"

    File_3DPPTCopy_3dpx = current_file_directory() + "\\Source\\3DPPTCopy.3dpx"

    File_Image_bmp = current_file_directory() + "\\Source\\Image\\BMP.bmp"
    File_Image_jpg = current_file_directory() + "\\Source\\Image\\JPG.jpg"
    File_Image_jpeg = current_file_directory() + "\\Source\\Image\\JPEG.jpeg"
    File_Image_png = current_file_directory() + "\\Source\\Image\\PNG.png"
    File_Image_gif = current_file_directory() + "\\Source\\Image\\GIF.gif"
    File_Image_panorama = current_file_directory() + "\\Source\\Image\\Panorama.jpg"
    File_Image = current_file_directory() + "\\Source\\Image\\"


    File_Video_3gp = current_file_directory() + "\\Source\\Video\\3GP.3gp"
    File_Video_asf = current_file_directory() + "\\Source\\Video\\ASf.asf"
    File_Video_avi = current_file_directory() + "\\Source\\Video\\AVI.avi"
    File_Video_flv = current_file_directory() + "\\Source\\Video\\FLV.flv"
    File_Video_mov = current_file_directory() + "\\Source\\Video\\MOV.mov"
    File_Video_mp4 = current_file_directory() + "\\Source\\Video\\MP4.mp4"
    File_Video_mpeg = current_file_directory() + "\\Source\\Video\\MPEG.mpeg"
    File_Video_rm = current_file_directory() + "\\Source\\Video\\RM.rm"
    File_Video_rmvb =current_file_directory() + "\\Source\\Video\\RMVB.rmvb"
    File_Video_wmv = current_file_directory() + "\\Source\\Video\\WMV.wmv"

    File_Audio_ape = current_file_directory() + "\\Source\\Audio\\APE.ape"
    File_Audio_m4a = current_file_directory() + "\\Source\\Audio\\M4A.m4a"
    File_Audio_m4r = current_file_directory() + "\\Source\\Audio\\M4R.m4r"
    File_Audio_mp3 = current_file_directory() + "\\Source\\Audio\\MP3.mp3"
    File_Audio_wav = current_file_directory() + "\\Source\\Audio\\WAV.wav"
    File_Audio_wma = current_file_directory() + "\\Source\\Audio\\WMA.wma"

    File_Insert_3DModel = current_file_directory() + "\\Source\\3DModel\\spider.fbx"

    File_Card_K = current_file_directory() + "\\Source\\单页知识卡.card"
    File_Card = current_file_directory() + "\\Source\\Card\\"

    File_View_xml = 'D:\YCY\Code\U3D Viewer\dump.xml'

    File_Jvm_18 = current_file_directory() + "\\Source\\JVM\\jdk1.8\\jdk1.8.171\\bin\\server\\jvm.dll"
    File_Jar_sikuli = current_file_directory() + "\\Source\\Jar\\sikulixapi.jar"
    File_Jar_mysikuli = current_file_directory() + "\\Source\\Jar\\mySikuli_20181107.jar"

    File_Performance_xls = os.path.join(current_file_directory(), os.path.pardir,  os.path.pardir, os.path.pardir) + '\\performance\\'

    # ------------------------sikuli------------------------
    File_Img_RightStart = current_file_directory() + "\\Source\\Img\\Start\\img_rightstart.png"
    File_Img_PPTXThumbnail = current_file_directory() + "\\Source\\Img\\Start\\img_pptxThumbnail.png"

    File_Img_FullScreen = current_file_directory() + "\\Source\\Img\\img_fullScreen2.png"
    File_Img_FullScreen2 = current_file_directory() + "\\Source\\Img\\img_fullScreen2.png"
    File_Img_FullScreen3 = current_file_directory() + "\\Source\\Img\\img_fullScreen3.png"
    File_Img_Text = current_file_directory() + "\\Source\\Img\\Text.png"
    File_Img_test = current_file_directory() + "\\Source\\Img\\Test.png"
    # File_Img_Text_newX = current_file_directory() + "\\Source\\Img\\Text\\img_new_textX.png"
    # File_Img_Text_newY = current_file_directory() + "\\Source\\Img\\Text\\img_new_textY.png"
    File_Img_TextX = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X.png"
    # File_Img_TextX_2 = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_2.png"
    File_Img_TextX_Song = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_Song.png"
    File_Img_TextX_Size28 = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_size28.png"
    File_Img_TextX_Add3 = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_size_add3.png"
    File_Img_TextX_Sub3 = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_size_sub3.png"

    File_Img_TextX_Bold = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_bold.png"
    File_Img_TextX_Italic = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_italic.png" # 倾斜
    File_Img_TextX_UnderLine = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_underline.png"
    File_Img_TextX_Shadow = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_shadow.png"
    File_Img_TextX_Strike = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_strike.png"
    File_Img_TextX_DropDown = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_dropdown.png" # 切换大小写
    File_Img_TextX_Spacing = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_spacing.png"
    File_Img_TextX_Color = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_color.png"  # 间距：很松
    File_Img_TextX_RowSpacing = current_file_directory() + "\\Source\\Img\\Text\\img_newText_X_rowspacing.png"  # 间距：很松

    File_Img_TextY = current_file_directory() + "\\Source\\Img\\Text\\img_newText_Y.png"
    File_Img_Text_BGEditor = current_file_directory() + "\\Source\\Img\\Text\\img_textBG_editor.png"
    File_Img_Text_BGSetting = current_file_directory() + "\\Source\\Img\\Text\\img_textBG_setting.png"
    File_Img_Text_DefWord = current_file_directory() + "\\Source\\Img\\Text\\img_textBG_defWord.png"
    File_Img_Text_typeWord = current_file_directory() + "\\Source\\Img\\Text\\img_textBG_typeWord.png"

    # 艺术字
    File_Img_WordArt_Text_1 = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_wordArtText_1.png"
    File_Img_WordArt_Text_2 = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_wordArtText_2.png"
    File_Img_WordArt_Text_3 = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_wordArtText_3.png"

    # 段落
    File_Img_Text_Para_Sym_NoSym = current_file_directory() + "\\Source\\Img\\Text\\img_para_sym_nosym.png"
    File_Img_Text_Para_Setting = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting.png"
    File_Img_Text_Para_Sym_Marks = current_file_directory() + "\\Source\\Img\\Text\\img_para_sym_marks.png"
    File_Img_Text_Para_Sym_Identifier = current_file_directory() + "\\Source\\Img\\Text\\img_para_sym_identifier.png"

    File_Img_Text_Para_LineSpace_1 = current_file_directory() + "\\Source\\Img\\Text\\img_para_linespace_1.png"
    File_Img_Text_Para_LineSpace_Change = current_file_directory() + "\\Source\\Img\\Text\\img_para_linespace_change.png"
    File_Img_Text_Para_LineSpace_Change_30 = current_file_directory() + "\\Source\\Img\\Text\\img_para_linespace_change_3.0.png"
    File_Img_Text_Para_LineSpace_Setting = current_file_directory() + "\\Source\\Img\\Text\\img_para_linespace_setting.png"
    File_Img_Text_Para_LineSpace_Move1 = current_file_directory() + "\\Source\\Img\\Text\\img_para_linespace_move1.png"
    File_Img_Text_Para_LineSpace_Move2 = current_file_directory() + "\\Source\\Img\\Text\\img_para_linespace_move2.png"
    File_Img_Text_Para_LineSpace_Move3 = current_file_directory() + "\\Source\\Img\\Text\\img_para_linespace_move3.png"


    File_Img_Text_Para_Indent_1 = current_file_directory() + "\\Source\\Img\\Text\\img_para_indent_1.png"
    File_Img_Text_Para_Indent_2 = current_file_directory() + "\\Source\\Img\\Text\\img_para_indent_2.png"
    File_Img_Text_Para_Indent_3 = current_file_directory() + "\\Source\\Img\\Text\\img_para_indent_3.png"
    File_Img_Text_Para_Indent_4 = current_file_directory() + "\\Source\\Img\\Text\\img_para_indent_inc_4.png"
    File_Img_Text_Para_Indent_5 = current_file_directory() + "\\Source\\Img\\Text\\img_para_indent_inc_5.png"
    File_Img_Text_Para_Indent_6 = current_file_directory() + "\\Source\\Img\\Text\\img_para_indent_inc_6.png"
    # File_Img_Text_Para_Indent_7 = current_file_directory() + "\\Source\\Img\\Text\\img_para_indent_inc_7.png"
    File_Img_Text_Para_Indent_8 = current_file_directory() + "\\Source\\Img\\Text\\img_para_indent_inc_8.png"

    File_Img_Text_Para_Indent_Inc = current_file_directory() + "\\Source\\Img\\Text\\img_para_indent_inc.png"
    File_Img_Text_Para_Indent_Inc_8Times = current_file_directory() + "\\Source\\Img\\Text\\img_para_indent_inc_8times.png"

    File_Img_Text_Para_Font = current_file_directory() + "\\Source\\Img\\Text\\img_para_font_song.png"

    File_Img_Text_Para_Setting_Align_Right = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_align_right.png"
    File_Img_Text_Para_Setting_Indent_14cm = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_14cm.png"
    File_Img_Text_Para_Setting_Indent_Max = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_max.png"
    File_Img_Text_Para_Setting_Indent_Spe = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_spe.png"
    File_Img_Text_Para_Setting_Indent_Spe2 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_spe2.png"
    File_Img_Text_Para_Setting_Indent_Spe3 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_spe3.png"
    File_Img_Text_Para_Setting_Indent_Spe4 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_spe4.png"
    File_Img_Text_Para_Setting_Indent_Spe5 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_spe5.png"
    File_Img_Text_Para_Setting_Indent_Spe6 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_spe6.png"
    File_Img_Text_Para_Setting_Indent_Spe7 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_spe7.png"
    File_Img_Text_Para_Setting_Indent_Para1 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_para1.png"
    File_Img_Text_Para_Setting_Indent_Para2 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_para2.png"
    File_Img_Text_Para_Setting_Indent_Para3 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_para3.png"
    File_Img_Text_Para_Setting_Indent_Space1 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_space1.png"
    File_Img_Text_Para_Setting_Indent_Space2 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_space2.png"
    File_Img_Text_Para_Setting_Indent_Space3 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_space3.png"
    File_Img_Text_Para_Setting_Indent_Space4 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_space4.png"
    File_Img_Text_Para_Setting_Indent_Space5 = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_indent_space5.png"
    File_Img_Text_Para_Setting_Save = current_file_directory() + "\\Source\\Img\\Text\\img_para_setting_save.png"

    File_Img_Open3DPPT = current_file_directory() + "\\Source\\Img\\Insert\\img_open3DPPT.png"
    File_Insert_BMP = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_bmp.png"
    File_Insert_GIF = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_gif.png"
    File_Insert_JPEG = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_jpeg.png"
    File_Insert_JPG = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_jpg.png"
    File_Insert_PNG = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_png.png"
    File_Insert_IMAGEWALL = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_imagewall.png"

    File_Insert_3GP = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_3GP.png"
    File_Insert_ASF = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_ASF.png"
    File_Insert_AVI = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_AVI.png"
    File_Insert_FLV = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_FLV.png"
    File_Insert_MOV = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_MOV.png"
    File_Insert_MP4 = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_MP4.png"
    File_Insert_MPEG = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_MPEG.png"
    File_Insert_RM = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_RM.png"
    File_Insert_RMVB = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_RMVB.png"
    File_Insert_WMV = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_WMV.png"

    File_Insert_VIDEO = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_video.png"
    File_Insert_AUDIO = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_audio.png"
    File_Img_3DModel = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_3dmodel.png"

    File_Insert_Shape_Line = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_shape_line.png"
    File_Insert_Shape_Rectangle = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_shape_rectangle.png"
    File_Insert_Shape_Circle = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_shape_circle.png"
    File_Insert_Shape_Arrow = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_shape_arrow.png"
    File_Insert_Shape_Add = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_shape_add.png"
    File_Insert_Shape_Process = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_shape_process.png"
    File_Insert_Shape_Start = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_shape_start.png"
    File_Insert_Shape_Label = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_shape_label.png"

    File_Insert_Table_Quick = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_table_quick.png"

    File_Image_Border_1 = current_file_directory() + "\\Source\\Img\\Format\\img_image_border_1.png"
    File_Image_Border_2 = current_file_directory() + "\\Source\\Img\\Format\\img_image_border_2.png"
    File_Image_Border_3 = current_file_directory() + "\\Source\\Img\\Format\\img_image_border_3.png"
    File_Image_Border_Clear = current_file_directory() + "\\Source\\Img\\Format\\img_image_border_clear.png"
    File_ImageWall_WallShow = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_wallsshow.png"
    File_ImageWall_ShowEdit = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_showedit.png"
    File_ImageWall_AfterDelete = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_afterdelete.png"
    File_ImageWall_SmallImg = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_smallimg.png"

    File_ImageWall_SelectImage = current_file_directory() + "\\Source\\Img\\Playing\\img_imagewall_selectimage.png"
    File_ImageWall_ShowType = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_showtype.png"
    File_ImageWall_ShowType1 = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_showtype1.png"
    File_ImageWall_ShowType2 = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_showtype2.png"
    File_ImageWall_ShowType3 = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_showtype3.png"
    File_ImageWall_ImageList_Down = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_imagelist_down.png"
    File_ImageWall_ImageList_Up = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_imagelist_up.png"
    File_ImageWall_ImageList_More = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_imagelist_more.png"
    File_ImageWall_ImageList_Swipe = current_file_directory() + "\\Source\\Img\\Format\\img_imagewall_imagelist_swipe.png"


    File_ImageWall_Dlg = current_file_directory() + "\\Source\\Img\\ImageWall\\img_imagewall_dlg.png"
    File_ImageWall_Dlg_ShowTypes_All = current_file_directory() + "\\Source\\Img\\ImageWall\\img_imagewall_showtypes_all.png"
    File_ImageWall_Dlg_ShowTypes_Main = current_file_directory() + "\\Source\\Img\\ImageWall\\img_imagewall_showtypes_main.png"
    File_ImageWall_Dlg_ShowTypes_Order = current_file_directory() + "\\Source\\Img\\ImageWall\\img_imagewall_showtypes_order.png"



    File_Insert_UI = current_file_directory() + "\\Source\\Img\\Insert\\img_insert_UI.png"
    File_Dlg_CheckUpdate = current_file_directory() + "\\Source\\Img\\img_dlg_checkupdate.png"
    File_BtnOk_CheckUpdate = current_file_directory() + "\\Source\\Img\\img_btnok_checkupdate.png"
    File_ContractUs_Weixin = current_file_directory() + "\\Source\\Img\\img_weixin_contractus.png"
    File_ContractUs_QQ1 = current_file_directory() + "\\Source\\Img\\img_QQ1_contractus.png"
    File_ContractUs_QQ2 = current_file_directory() + "\\Source\\Img\\img_QQ2_contractus.png"
    File_Dlg_LogViewer = current_file_directory() + "\\Source\\Img\\img_dlg_logviewer.png"

    File_ScreenShoot_Path = current_file_directory() + "\\Source\\ScreenShoot\\"
    File_Minimize = current_file_directory() + "\\Source\\Img\\img_minimize.png"

    File_Insert_Exercise = current_file_directory() + "\\Source\\Img\\insert\\img_insert_btnexercise.png"
    #视频3D化
    File_Video_Playing_Button_Pause = current_file_directory() + "\\Source\\Img\\Playing\\img_video_button_pause.png"
    File_Video_Playing_Show_Still = current_file_directory() + "\\Source\\Img\\Playing\\img_video_show_still.png"
    File_Video_Playing_Show_Hide = current_file_directory() + "\\Source\\Img\\Playing\\img_video_show_hide.png"
    File_Video_3D_PhotoFrame1 = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_photoframe1.png"
    File_Video_3D_PhotoFrame2 = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_photoframe2.png"
    File_Video_3D_PhotoFrame3 = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_photoframe3.png"
    File_Video_3D_NoStyle = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_nostyle.png"
    File_Video_3D_BillBoard = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_billboard.png"
    File_Video_3D_ExBoard = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_exboard.png"
    File_Video_3D_LDBillBoard = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_ldbillboard.png"
    File_Video_3D_Monitor = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_monitor.png"
    File_Video_3D_OldTV = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_oldtv.png"
    File_Video_3D_Paint = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_paint.png"
    File_Video_3D_Reel = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_Reel.png"
    File_Video_3D_TV = current_file_directory() + "\\Source\\Img\\Playing\\img_video_3d_tv.png"

    File_Audio_BSSetting = current_file_directory() + "\\Source\\Img\\Playing\\img_audio_bssetting.png"
    File_Shape_Style = current_file_directory() + "\\Source\\Img\\Shape\\img_shape_style.png"
    File_Shape_Transparent = current_file_directory() + "\\Source\\Img\\Shape\\img_shape_transparent.png"
    File_Shape_Color = current_file_directory() + "\\Source\\Img\\Shape\\img_shape_color.png"
    File_Shape_LineType_Circle = current_file_directory() + "\\Source\\Img\\Shape\\img_shape_linetype_circle.png"
    File_Shape_LineType_LongLine = current_file_directory() + "\\Source\\Img\\Shape\\img_shape_linetype_longline.png"
    File_Shape_LineType_LongSquare = current_file_directory() + "\\Source\\Img\\Shape\\img_shape_linetype_longsquare.png"
    File_Shape_LineType_LongSquare2 = current_file_directory() + "\\Source\\Img\\Shape\\img_shape_linetype_longsquare2.png"
    File_Shape_LineType_ShortSquare = current_file_directory() + "\\Source\\Img\\Shape\\img_shape_linetype_shortsquare.png"
    File_Shape_LineType_Square = current_file_directory() + "\\Source\\Img\\Shape\\img_shape_linetype_square.png"
    File_Shape_LineType_ShortLine = current_file_directory() + "\\Source\\Img\\Shape\\img_shape_linetype_shortline.png"

    # 检查更新
    File_MainWindow_Update_Latest = current_file_directory() + "\\Source\\Img\\Shape\\img_mainwindow_update_latest.png"

    # 秀英截屏点击
    File_Phone_Click = current_file_directory() + "\\Source\\PhoneClick.png"

if __name__ == "__main__":
    print SourcePath.File_3DPPTOpenTest_3dpx