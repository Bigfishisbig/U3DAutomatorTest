# coding=utf-8
import os
import shutil,time

__author__ = "Junpeng Chen"


def create_file(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
    return path


def copy_file(from_path, to_path):
    if os.path.exists(from_path):
        shutil.copy(from_path, to_path)
    return from_path, to_path


def path_exists(path):
    return os.path.exists(path)


def get_root_path(*file_args):
    """
        获取根文件，调用处需进行绝对导入
    :return:
    """
    path = ""
    filename = ""
    if file_args:
        if "." in file_args[-1]:
            path = os.sep.join(file_args[:-1])  # os.sep 根据当前平台获取对应的路径分隔符
            filename = file_args[-1]
        else:
            path = os.sep.join(file_args)

    abspath = os.path.join(__file__.split(__package__.replace(".", os.sep))[0] if __package__ else ".", path)
    return create_file(abspath) if not filename else os.path.join(create_file(abspath), filename)

####################################################################################

class Path:
    def __init__(self):
        pass

    @staticmethod
    def create_file(path):#创建路径 文件夹路径（以文件夹结尾）
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def delete_file(path):#删除文件
        if os.path.exists(path):
            os.remove(path)

    @staticmethod
    def copy_file(from_path,to_path):
        if os.path.exists(from_path):
            shutil.copy(from_path,to_path)

    @staticmethod
    def path_exists(path):
        return os.path.exists(path)

    @staticmethod
    def get_root_path(filename):
        """
            获取根文件，调用处需进行绝对导入
        :param filename:
        :return:
        """
        return os.path.join(__file__.split(__package__.replace(".", os.sep))[0],
                            filename) if __package__ else os.path.join(".", filename)

    @staticmethod
    def path(path,dirPath = "/data"):
        '''
        @Title:path
        @Description:指引到/auto/data的绝对路径
        @param:     path:/auto/data/下的路径
        @return:str
        '''
        #splitvar = r"\main" if r"\main" in os.path.abspath(".") else r"\data"
        splitvar = ""
        if r"\main" in os.path.abspath("."):
            splitvar=r"\main"
        elif r"\data" in os.path.abspath("."):
            splitvar=r"\data"
        elif r"\script" in os.path.abspath("."):
            splitvar=r"\script"
        else:
            splitvar=r""
        if splitvar!=r"":
            return os.path.abspath(os.path.join(os.path.abspath(".").split(splitvar)[0] + dirPath,path))
        else:
            return os.path.abspath(os.path.join(os.path.abspath(".")+os.sep+ splitvar+os.sep+ dirPath,path))

    @staticmethod
    def mainPath(filename,dirPath= "/main"):
        '''
        @Title:mainPath
        @Description:auto/main下的文件路径
        @param:     appname:安装包名字
        @return:str
        '''
        return Path.path(filename,dirPath)

    @staticmethod
    def sysLogPath():
        '''
        @Title:appPath
        @Description:系统log所在路径
        @param:
        @return:str
        '''
        Path.create_file(Path.path("syslog"))
        return Path.path("syslog" + os.sep +"%s.log" % time.strftime("%Y-%m-%d",time.localtime(time.time())))

    @staticmethod
    def windowsPath(file):
        return Path.path("windows","/script")+ os.sep + file

    @staticmethod
    def caseTempPath(file):
        Path.create_file(Path.windowsPath("temp"))
        return Path.windowsPath("temp"+ os.sep + file)

    @staticmethod
    def resultPath(file):
        Path.create_file(Path.path("result"))
        return Path.path("result" + os.sep + file)

    @staticmethod
    def resultImagePath(scriptname,file):
        Path.create_file(Path.resultPath("image" + os.sep + scriptname))
        return Path.resultPath("image" + os.sep + scriptname + os.sep + file)

    @staticmethod
    def deleteDir(Dir):
        '''
        @Description:   删除文件
        @param:     path
        @return:    None
        '''
        if os.path.exists(Dir):
            #print "删除文件夹"
            shutil.rmtree(Dir)
    
if __name__ == "__main__":
    pass
    # os.environ["PLATFORM"] =Platform.Windows
    # print Path.sysLogPath()
    # print Path.mainPath("utils")
    # print Path.windowsPath("loginvisitor.py")
    # print Path.caseTempPath("123")
    # print Path.resultPath("123")
    # print Path.resultImagePath("123","1.png")
    # Path.deleteDir(r"F:\autotestU3D\U3DAutomatorClient\data\result\image\123")
