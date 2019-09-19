# coding=utf-8
import time

__author__ = "Junpeng Chen"


class Bounds:
    """
    Attributes:
        Element在屏幕上显示的位置和大小，(x,y)为中心点坐标系以屏幕左上角为坐标原点
        __________ X
        |
        |
        |
        Y
        X:element与屏幕左侧的距离
        Y:element与屏幕上边的距离
        Width:element的宽
        Height:element的高
    """

    def __init__(self, dictionary):
        if dictionary == None:
            pass
        else:
            self.X = dictionary["X"]
            self.Y = dictionary["Y"]
            self.Width = dictionary["Width"]
            self.Height = dictionary["Height"]
            self.centre_x = self.X + self.Width / 2
            self.centre_y = self.Y + self.Height / 2

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()


class Element:
    def __init__(self, dictionary, engine):
        self.Name = dictionary["Name"]
        self.Id = dictionary["Id"]
        self.Components = dictionary["Components"]
        self.Txt = dictionary["Txt"]
        self.Img = dictionary["Img"]
        self.Visible = bool(dictionary["Visible"])
        self.Bounds = Bounds(dictionary["Bounds"])
        self.engine = engine  # get_element中已导入Element,python中两模块互相引用是不允许的

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, element):
        return isinstance(element, Element) and hasattr(element, 'Id') and self.Id == element.Id

    def __ne__(self, element):
        return not self.__eq__(element)

    def click(self, sleep=1):
        self.engine.click(self.Bounds.centre_x, self.Bounds.centre_y)
        time.sleep(sleep)

    def click_right(self, sleep=1):
        self.engine.click_right(self.Bounds.centre_x, self.Bounds.centre_y)
        time.sleep(sleep)

    def click_double(self, sleep=1):
        self.engine.click_double(self.Bounds.centre_x, self.Bounds.centre_y)
        time.sleep(sleep)

    def press(self, press_time, sleep=1):
        self.engine.press(self.Bounds.centre_x, self.Bounds.centre_y, press_time)
        time.sleep(sleep)

    def input(self, text, sleep=1):
        self.engine.input(self, text)
        time.sleep(sleep)

    def get_field(self, component, attribute):
        if component not in self.Components:
            return None
        return self.engine.get_component_field(self, component, attribute)

    def get_property(self, property_name):
        """
            s3引擎专用
        :param property_name:
        :return:
        """
        if not isinstance(property_name, str):
            return None
        return self.engine.get_property(self, property_name)


class ImageElement:
    def __init__(self, dictionary, engine, src_image="", tmp_image="", target_image=""):
        self.src_image = src_image
        self.tmp_image = tmp_image
        self.target_image = target_image
        self.accurate = dictionary["maxVal"]
        self.centre_x = dictionary["maxLocX"]
        self.centre_y = dictionary["maxLocY"]
        self.scale_x = dictionary["scaleX"]
        self.scale_y = dictionary["scaleY"]
        self.engine = engine

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def click(self, sleep=1):
        self.engine.click(self.centre_x, self.centre_y)
        time.sleep(sleep)

    def press(self, press_time, sleep=1):
        self.engine.press(self.centre_x, self.centre_y, press_time)
        time.sleep(sleep)


class ElementPath:
    def __init__(self, name, index=-1, txt="", img=""):
        self.Name = name
        self.Index = index
        self.Txt = txt
        self.Img = img

    def add_child(self, child):
        if not isinstance(child, ElementPath):
            raise TypeError
        if self.has_attribute() or child.has_attribute():
            return child
        else:
            if self.Name:
                self.Name += "/" + child.Name
            else:
                self.Name = child.Name
        return self

    def has_attribute(self):
        return self.Index != -1 or self.Txt or self.Img

    def __str__(self):
        """
            Txt可能含有中文字符，采用dict会产生编码格式转换
        :return: 
        """
        return "{'Index': %s, 'Txt': '%s', 'Name': '%s', 'Img': '%s'}" % (self.Index, self.Txt, self.Name, self.Img)

    def __repr__(self):
        return self.__str__()


class TouchEvent:
    ACTION_DOWN = 0
    ACTION_UP = 1
    ACTION_MOVE = 2

    def __init__(self, x, y, sleep, action):
        self.X = round(x, 2)
        self.Y = round(y, 2)
        self.Sleep = int(sleep * 1000)
        self.Action = action

    def __str__(self):
        return "{'X':%s,'Y':%s,'Sleep':%s,'Action':%s}" % (self.X, self.Y, self.Sleep, self.Action)

    def __repr__(self):
        return self.__str__()


class Version:
    def __init__(self, dictionary):
        self.Engine = dictionary["Engine"]
        self.SdkVersion = dictionary["SdkVersion"]
        self.engineVersion = dictionary["engineVersion"]
        self.SdkUi = dictionary["SdkUi"]


class WorldBounds(object):
    def __init__(self, dictionary):
        self.Id = dictionary["Id"]
        self.Existed = dictionary["Existed"]
        self.CenterX = dictionary["CenterX"]
        self.CenterY = dictionary["CenterY"]
        self.CenterZ = dictionary["CenterZ"]
        self.ExtentsX = dictionary["ExtentsX"]
        self.ExtentsY = dictionary["ExtentsY"]
        self.ExtentsZ = dictionary["ExtentsZ"]


class MemoryData:
    def __init__(self, dictionary):
        self.MonoUsedSize = int(dictionary["MonoUsedSize"])
        self.MonoHeapSize = int(dictionary["MonoHeapSize"])
        self.TotalAllocatedMemory = int(dictionary["TotalAllocatedMemory"])
        self.TotalUnusedReservedMemory = int(dictionary["TotalUnusedReservedMemory"])
        self.TotalReservedMemory = int(dictionary["TotalReservedMemory"])


class Performance:
    def __init__(self, dictionary):
        self.Memory = MemoryData(dictionary["Memory"])
        self.CpuUsage = float(dictionary["CpuUsage"])
        # self.GpuUsage = float(dictionary["GpuUsage"])
        self.Fps = int(dictionary["Fps"])
