# coding=utf-8
import re

from main.log.logger import get_logger
from main.object.enum import Cmd, Environment
from main.object.enum import Platform
from main.object.objects import *
from main.utils.adb_handler import get_adb_handler
from main.utils.image_recognize import ImageRecognize
from main.utils.path import *
from main.utils.socket_handler import SocketHandler
from main.utils.windows_handler import get_windows_handler
from main.utils.xml_reader import get_config
from main.utils.socket_handler import *

__author__ = "Junpeng Chen"
__all__ = ["get_application", "get_image_engine", "get_engine"]


class BasicEngine:
    def __init__(self, host=os.getenv(Environment.HOST), port=os.getenv(Environment.SERVER_PORT)):
        self.host = host or get_config().host
        self.port = port or get_config().server_port
        self._socket = SocketHandler(self.host, int(self.port))

    def get_sdk_version(self):
        """
            获取版本
        :return:
        """
        return self._socket.send_command(Cmd.GetVersion)

    def dumpTree(self):
        return self._socket.send_command(Cmd.DumpTree)

    def find_element(self, name):
        """
            通过GameObject.Find查找对应的GameObject
        :param name:
            GameObject.Find的参数
        :return:
            a instance of Element if find the GameObject,else return  None
            example:
            {"object_name":"/Canvas/Panel/Button",
            "instance":4257741}
        :rtype: Element
        """
        get_logger().info("find_element >>> name = %s" % name)

        response = self._socket.send_command(Cmd.FindElements, "['%s']" % name)
        if response:
            dic = response[0]
            if dic["Id"] != -1:
                return Element(dic, get_engine())
        return None

    def find_elements_path(self, path):
        """
            表达式匹配获取符合的所有节点
            第一个节点"/"代表从根节点，如果不是代表可以从任意位置开始

        index：代表节点的位置。
             parent
           /      \
         index[0]  index[1]

         name:代表节点名称，"*"代表任意名称
         text:代表节点的文字内容（当前GameObject的挂载的Compenent）
         img:图片名称,sprite或者texture名称

         /Canvas/Panel/Button
         Canvas[0]{txt="hello"}/Button
         /Canvas/Panel/*[1]/Button
        :param path:
            需要查找的路径,/Canvas/Button[0]{txt=Button,img=img}
        :return:包含instance的Elements对象列表
            example:
            [{"objectName":"/Canvas/Panel/Button",
            "Instance":4257741},{"objectName":"/Canvas/Panel/Button",
            "Instance":4257742}]
        """
        get_logger().info("find_elements_path  >>> path = %s" % path)
        element_paths = self.__parse_path(path)
        print "Analysis Path：", element_paths
        if element_paths is None:
            raise Exception("Error path")

        response = self._socket.send_command(Cmd.FindElementPath, element_paths)
        elements = []
        if response:
            for e in response:
                element = Element(e, get_engine())
                elements.append(element)
        #print "Elements:", elements
        return elements

    def __parse_path(self, path):
        """
            解析路径
        :param path:
        :return:
        """
        if path is None or not isinstance(path, str):
            print "this is none"
            return None

        paths = path.split("/")
        element_paths = []
        if len(paths) == 0:
            return None
        elif paths[0] == '':
            paths = paths[1:]

        name_re = re.compile(r"(?P<name>[^[{]+)")
        txt_re = re.compile(r"(txt\s*=\s*(?P<txt>[^,\}]*))")
        img_re = re.compile(r"(img\s*=\s*(?P<img>[^,\}]*))")
        index_re = re.compile(r"\[(?P<index>\d+)\]")
        for node in paths:
            result = name_re.search(node)
            if result:
                name = result.groupdict().get("name", "")
            else:
                name = ""
            result = txt_re.search(node)
            if result:
                txt = result.groupdict().get("txt", "")
            else:
                txt = ""
            result = img_re.search(node)
            if result:
                img = result.groupdict().get("img", "")
            else:
                img = ""
            result = index_re.search(node)
            if result:
                index = result.groupdict().get("index", "-1")
                index = int(index)
            else:
                index = -1
            element_paths.append(str(ElementPath(name, index, txt, img)))

        return "[%s]" % (",".join(element_paths))

    def get_fps(self):
        """
            获取FPS
        :return:
        """
        return self._socket.send_command(Cmd.GetFps)

    def get_cpu(self):
        """
            获取cpu占用
        :return:
        """
        return self._socket.send_command(Cmd.GetCpu)

    def get_gpu(self):
        """
            获取gpu占用
        :return:
        """
        return self._socket.send_command(Cmd.GetGpu)

    def get_memory(self):
        """
            获取内存占用
        :return:
        """
        response = self._socket.send_command(Cmd.GetMemory)
        if response:
            return MemoryData(response)
        return None

    def get_performance(self):
        """
            获取性能数据，包括FPS,CPU，MEMORY
        :return:
        """
        response = self._socket.send_command(Cmd.GetPerformance)
        if response:
            # print response
            return Performance(response),response['Fps'],response['CpuUsage'],response['Memory']['TotalAllocatedMemory']
        return None


    def get_registered_handlers(self):
        """
            获取用户当前注册的自定义的函数集合
        :return: []注册的自定义函数名称序列
        """
        return self._socket.send_command(Cmd.GetRegisteredHandlers)

    def call_registered_handler(self, name, args):
        """
            调用指定的注册的函数，并返回返回值
        :param name:已经注册的函数名称
        :param args:传入函数中的参数，一个不超过1024个字符的参数
        :return:
            自定义注册函数的返回值
        """
        return self._socket.send_command(Cmd.CallRegisterHandler, {"name": name, "args": args})

    def get_scene(self):
        """
            获取当前界面的scene名称
        :return:当前scene的名称
        """
        return self._socket.send_command(Cmd.GetCurrentScene)

    def get_touchable_elements(self):
        """
            获取当前界面的可点击节点的列表
        :return:
            [(element1,point1),(element2,point2)]
            [({"object_name":"/Canvas/Panel/Button","Instance":4257741},{"x":250,"y":300}),.....]
        """
        response = self._socket.send_command(Cmd.GetTouchableElements)
        elements = []
        if response:
            for e in response:
                element = Element(e, get_engine())
                elements.append(element)
        return elements

    def get_element_world_bounds(self, elements):
        """
            查找节点对应的世界坐标。世界坐标包含，节点的中心位置的x,y,z坐标，及物体离中心点在在x,y,z轴上的大小。
            具体详见：http://docs.unity3d.com/ScriptReference/Bounds.html
        :param elements: 一个Element或者Element[]，节点应该至少包含Renderer、MeshFilter或Collider组件
        :return: WorldBound[]
        """
        if elements is None:
            raise Exception("Invalid Instance")
        if isinstance(elements, Element):
            elements = [elements]

        if len(elements) == 0:
            raise Exception("Invalid Instance,search node is error")

        req = [e.instance for e in elements]
        dicts = self._socket.send_command(Cmd.GetElementWorldBound, req)

        world_bounds = []
        for dic in dicts:
            world_bound = WorldBounds(dic)
            if world_bound.Existed:
                world_bounds.append(world_bound)
        return world_bounds

    def get_component_field(self, element, component, attribute):
        """
            通过反射的方式获取到GameObject上面组件的属性值。反射查看是否存在Property或者Field名称为attribute
        :param element:已经找到的GameObject对象
        :param component:组件名称
        :param attribute:字段或者属性名称
        :return: 字段或者属性名称toString()之后的string值
        """
        if element is None or component is None or attribute is None:
            raise Exception("Invalid Instance")
        get_logger().info("get_component_field  >>> attribute = %s.%s.%s" % (element.Name, component, attribute))
        return self._socket.send_command(Cmd.GetObjectField,
                                         {"Id": element.Id, "ComponentName": component, "AttributeName": attribute})

    def get_property(self, element, property_name):
        """
            S3引擎获取属性值
        :param element:
        :param property_name:
        :return:
        """
        if isinstance(element, str):
            name = element
        elif isinstance(element, Element):
            if element.Id == 0:
                name = element.Name
            else:
                raise Exception("Invalid Instance")
        else:
            return None
        # get_logger().info("get_property >>> property_name = %s.%s" % (name, property_name))
        return self._socket.send_command(Cmd.GetObjectField,
                                         "{'Name': '%s', 'Property': '%s'}" % (name, property_name))

    def set_property(self, element, property_name, content):
        """
            S3引擎设置属性值
        :param element:
        :param property_name:
        :param content:
        :return:
        """
        if isinstance(element, str):
            name = element
        elif isinstance(element, Element):
            if element.Id == 0:
                name = element.Name
            else:
                raise Exception("Invalid Instance")
        else:
            return None
        return self._socket.send_command(Cmd.SetObjectField, "{'Name': '%s', 'Property': '%s', 'Content': '%s'}" % (
            name, property_name, content))

    def custom_command(self, command):
        """
            S3引擎自定义命令发送
        :param command:
        :return:
        """
        if isinstance(command, str):
            return self._socket.send_command(Cmd.CustomCommand, "{'Command': '%s'}" % command)

    def input(self, element, text):
        """
            input 文本
        :param element: is an element locator
        :param text: input的内容
        :return: "hello world"input控件上原有的内容
        """
        if element and isinstance(element, Element):
            get_logger().info("input >>> %s set %s" % (element.Name, text))
            if element.Id != 0:
                result = self._socket.send_command(Cmd.SetInputText, "{'Id': %d, 'Content': '%s'}" % (element.Id, text))
            else:
                result = self._socket.send_command(Cmd.SetInputText,
                                                   "{'Name': '%s', 'Content': '%s'}" % (element.Name, text))
            return result
        else:
            raise Exception(
                "Input locator = {0},text = {1},valid argument is Element or ElementBound".format(element, text))

    def move_pos(self, x, y):
        pass

    def click_double(self, x, y):
        pass

    def click(self, x, y):
        pass

    def press(self, x, y, press_time):
        pass

    def swipe(self, start_x, start_y, end_x, end_y, steps, duration):
        pass

    def swipe_press(self, start_x, start_y, end_x, end_y, steps, duration, sleep_time=0):
        pass

    def screen_cap(self, path):
        pass


class WindowsEngine(BasicEngine):
    def __init__(self):
        self.handler = get_windows_handler()
        print "self.handler ",self.handler
        BasicEngine.__init__(self)

    def key_code(self, key_name, sleep_time=0):
        """
            键盘功能键
        :param key_name:
        :param sleep_time:
        :return:
        """
        if not isinstance(key_name, str):
            raise Exception("text not str")
        get_logger().info("key_code >>> key_name = %s, sleep_time = %d" % (key_name, sleep_time))
        self.handler.key_code_input(key_name, sleep_time)

    def input_text(self, text, x=None, y=None):
        """
            输入文字
        """
        if not isinstance(text, str):
            raise Exception("text not str")
        if x and y:
            get_logger().info("input >>> (%f ,%f), text=%s" % (x, y, text))
            x, y = self.handler.client_to_screen(x, y)
        self.handler.key_input(text, x, y,)

    def key_press(self, key, sleep_time=0):
        """
            长按键盘
        """
        if not isinstance(key, str):
            raise Exception("text not str")
        get_logger().info("key_press >>>  key = %s, sleep_time = %d" % (key, sleep_time))
        self.handler.key_click(key, sleep_time)

    def move_pos(self, x, y):
        """
            移动
        """
        get_logger().info("move >>> (%f ,%f)" % (x, y))
        x, y = self.handler.client_to_screen(x, y)
        self.handler.mouse_move(x, y)

    def move_pos2(self, x, y, x2, y2):
        """
            移动
        """
        get_logger().info("move >>> (%f ,%f)" % (x, y))
        x, y = self.handler.client_to_screen(x, y)
        self.handler.mouse_absolute(x, y, x2, y2)

    def click(self, x, y, isClientPos=True):
        """
            点击鼠标左键
        """
        self.press(x, y, press_time=0.05, isClientPos=isClientPos)

    def click_double(self, x, y, isClientPos=True):
        """
            鼠标左键双击
        :param x:
        :param y:
        :return:
        """
        get_logger().info("click_double >>> (%f ,%f)" % (x, y))
        if isClientPos:
            x, y = self.handler.client_to_screen(x, y)
        self.handler.mouse_click_double(x, y)

    def click_three(self, x, y, isClientPos=True):
        """
            鼠标左键三击
        :param x:
        :param y:
        :return:
        """
        get_logger().info("click_double >>> (%f ,%f)" % (x, y))
        if isClientPos:
            x, y = self.handler.client_to_screen(x, y)
        self.handler.mouse_click_three(x, y)

    def click_right(self, x, y, isClientPos=True):
        """
            点击鼠标右键
        """
        get_logger().info("click_right >>> (%f ,%f)" % (x, y))
        if isClientPos:
            x, y = self.handler.client_to_screen(x, y)
        self.handler.mouse_click_right(x, y)

    def press(self, x, y, press_time, isClientPos=True):
        """
            鼠标左键长按
        """
        get_logger().info("press >>> (%f ,%f), time = %f" % (x, y, press_time))
        if isClientPos:
            x, y = self.handler.client_to_screen(x, y)
        self.handler.mouse_press(x, y, press_time)

    def wheel_roll(self, data):
        """
            鼠标滑轮滚动
        """
        get_logger().info("wheel_roll >>> %d" % data)
        self.handler.mouse_wheel_roll(data)

    def swipe(self, start_x, start_y, end_x, end_y, steps, duration, isClientPos=True):
        """
            鼠标左键拖动
        """
        self.swipe_press(start_x, start_y, end_x, end_y, steps, duration, sleep_time=0, isClientPos=isClientPos)

    def swipe_press(self, start_x, start_y, end_x, end_y, steps, duration, sleep_time=0.2, isClientPos=True):
        """
            鼠标左键拖动，并长按
        """
        get_logger().info("swipe (%d,%d)=>(%d,%d), steps = %d, swipe_time = %d, press_time = %d" % (
            start_x, start_y, end_x, end_y, steps, duration, sleep_time))
        if isClientPos:
            start_x, start_y = self.handler.client_to_screen(start_x, start_y)
            end_x, end_y = self.handler.client_to_screen(end_x, end_y)
        self.handler.mouse_swipe_press(start_x, start_y, end_x, end_y, steps, duration, sleep_time)

    def swipe_right(self, start_x, start_y, end_x, end_y, steps, duration):
        """
            鼠标右键拖动      
        """
        self.swipe_press_right(start_x, start_y, end_x, end_y, steps, duration, sleep_time=0)

    def swipe_press_right(self, start_x, start_y, end_x, end_y, steps, duration, sleep_time=0.2):
        """
            鼠标右键拖动，并长按
        """
        get_logger().info("swipe_right (%d,%d)=>(%d,%d), steps = %d, swipe_time = %d, press_time = %d" % (
            start_x, start_y, end_x, end_y, steps, duration, sleep_time))
        start_x, start_y = self.handler.client_to_screen(start_x, start_y)
        end_x, end_y = self.handler.client_to_screen(end_x, end_y)
        self.handler.mouse_swipe_press_right(start_x, start_y, end_x, end_y, steps, duration, sleep_time)

    def get_client_centre(self):
        """
            获取客户端中心点
        :return:
        """
        return self.handler.get_client_centre()

    def screen_cap(self, path):
        """
            截图并保存到pc端
        """
        self.handler.screen_cap(path)
        return path_exists(path)


class AndroidEngine(BasicEngine):
    def __init__(self, device_id=None):
        self.adb = get_adb_handler(device_id)

        host = os.getenv(Environment.HOST) or get_config().host
        server_port = os.getenv(Environment.SERVER_PORT) or get_config().server_port
        adb_port = os.getenv(Environment.ADB_PORT) or get_config().server_port

        if host == "localhost":
            # 如果配置文件的host项的内容是"localhost"则通过adb转发数据包
            self.adb.forward_list()
            self.adb.forward(adb_port, server_port)
            BasicEngine.__init__(self, host, adb_port)
        else:
            # 如果配置文件的host项不是"localhost",则这个项的内容是手机的ip，直接连接手机的监听端口
            BasicEngine.__init__(self, host, server_port)

    def _inject_touch_actions(self, actions):
        """
            发送touch序列号，touch事件结束之后，才会返回。同步函数
        """
        return self._socket.send_command(Cmd.TouchEvents, actions)

    def press(self, x, y, press_time):
        """
            长按动作
        """
        x = float(x)
        y = float(y)
        get_logger().info("press >>> (%f ,%f), press_time = %f" % (x, y, press_time))

        actions = [TouchEvent(x, y, press_time, TouchEvent.ACTION_DOWN).__dict__,
                   TouchEvent(x, y, 0, TouchEvent.ACTION_UP).__dict__]
        self._inject_touch_actions(actions)
        return True

    def click(self, x, y):
        """
            在屏幕的某个位置进行点击
        """
        return self.press(x, y, 0.05)

    def swipe(self, start_x, start_y, end_x, end_y, steps, duration=0):
        """
            滑动坐标
        """
        return self.swipe_press(start_x, start_y, end_x, end_y, steps, duration, press_time=0)

    def swipe_press(self, start_x, start_y, end_x, end_y, steps, duration, press_time=0.2):
        """
            滑动并在结束的地方一直按压
        """
        if steps <= 0:
            raise Exception("steps = {0} is invalid, steps must more than 0".format(steps))
        get_logger().info("swipe_press >>> (%f ,%f)=>(%f ,%f), steps = %d, duration = %d, press_time = %f" % (
            start_x, start_y, end_x, end_y, steps, duration, press_time))
        start_x = float(start_x)
        start_y = float(start_y)
        end_x = float(end_x)
        end_y = float(end_y)
        actions = [TouchEvent(start_x, start_y, 0, TouchEvent.ACTION_DOWN).__dict__]

        x_distance = (end_x - start_x) / steps
        y_distance = (end_y - start_y) / steps
        move_x, move_y = start_x, start_y
        step_sleep = 0 if duration <= 0 else float(duration) / steps

        for i in xrange(steps):
            move_x += x_distance
            move_y += y_distance
            actions.append(TouchEvent(move_x, move_y, step_sleep, TouchEvent.ACTION_MOVE).__dict__)
        actions.append(TouchEvent(end_x, end_y, press_time, TouchEvent.ACTION_MOVE).__dict__)
        actions.append(TouchEvent(end_x, end_y, 0, TouchEvent.ACTION_UP).__dict__)
        self._inject_touch_actions(actions)
        return True

    def screen_cap(self, path):
        """
            截图并保存到pc端
        """
        self.adb.screen_cap_pull(path)
        return path_exists(path)


class S3Engine(BasicEngine):
    def __init__(self):
        BasicEngine.__init__(self)

    def _inject_touch_actions(self, actions):
        """
            发送touch序列号，touch事件结束之后，才会返回。同步函数
        """
        return self._socket.send_command(Cmd.TouchEvents, actions)

    def press(self, x, y, press_time):
        """
            长按动作
        """
        x = float(x)
        y = float(y)
        get_logger().info("press >>> (%f ,%f), press_time = %f" % (x, y, press_time))
        actions = [TouchEvent(x, y, press_time, TouchEvent.ACTION_DOWN).__dict__,
                   TouchEvent(x, y, 0, TouchEvent.ACTION_UP).__dict__]
        self._inject_touch_actions(actions)
        return True

    def click(self, x, y):
        """
            在屏幕的某个位置进行点击
        """
        return self.press(x, y, 0.05)

    def swipe(self, start_x, start_y, end_x, end_y, steps, duration=0):
        """
            滑动坐标
        """
        return self.swipe_press(start_x, start_y, end_x, end_y, steps, duration)

    def swipe_press(self, start_x, start_y, end_x, end_y, steps, duration, press_time=0.2):
        """
            滑动并在结束的地方一直按压
        """
        if steps <= 0:
            raise Exception("steps = {0} is invalid, steps must more than 0".format(steps))
        get_logger().info("swipe_press >>> (%f ,%f)=>(%f ,%f), steps = %d, duration = %d, press_time = %f" % (
            start_x, start_y, end_x, end_y, steps, duration, press_time))
        start_x = float(start_x)
        start_y = float(start_y)
        end_x = float(end_x)
        end_y = float(end_y)
        actions = [TouchEvent(start_x, start_y, 0, TouchEvent.ACTION_DOWN).__dict__]

        x_distance = (end_x - start_x) / steps
        y_distance = (end_y - start_y) / steps
        move_x, move_y = start_x, start_y
        step_sleep = 0 if duration <= 0 else float(duration) / steps

        for i in xrange(steps):
            move_x += x_distance
            move_y += y_distance
            actions.append(TouchEvent(move_x, move_y, step_sleep, TouchEvent.ACTION_MOVE).__dict__)
        actions.append(TouchEvent(end_x, end_y, press_time, TouchEvent.ACTION_MOVE).__dict__)
        actions.append(TouchEvent(end_x, end_y, 0, TouchEvent.ACTION_UP).__dict__)
        self._inject_touch_actions(actions)
        return True

    def find_elements_path(self, path):
        pass

    def screen_cap(self, path):
        get_windows_handler().screen_cap(path)
        return path_exists(path)


class ImageEngine:
    gAccurate = 0.5

    def __init__(self, screen_width=None, screen_height=None):
        self.screen_width = int(screen_width or os.getenv(Environment.SRC_SCREEN_WIDTH) or 720)
        self.screen_height = int(screen_height or os.getenv(Environment.SRC_SCREEN_HEIGHT) or 1280)

    def find_image(self, image_name, accurate=gAccurate):
        get_logger().info("find_image >>> image_name = %s" % image_name)
        source_image = self.__get_image_path("source", image_name)
        tmp_image = self.__get_image_path("tmp", image_name)
        target_image = self.__get_image_path("target", image_name)

        get_engine().screen_cap(tmp_image)
        dictionary = ImageRecognize.proxy(source_image, tmp_image, target_image, default_accurate=accurate,
                                          src_x=self.screen_width, src_y=self.screen_height, orientation=0)
        if dictionary["match"]:
            return ImageElement(dictionary, get_engine(), source_image, tmp_image, target_image)
        return None

    def swipe(self, image1, image2, steps, duration, accurate=gAccurate):
        self.swipe_press(image1, image2, steps, duration, 0, accurate)

    def swipe_press(self, image1, image2, steps, duration, sleep_time, accurate=gAccurate):
        element1 = self.find_image(image1, accurate)
        element2 = self.find_image(image2, accurate)
        get_engine().swipe_press(element1.centre_x, element1.centre_y, element2.centre_x, element2.centre_y, steps,
                                 duration, sleep_time)

    def __get_image_path(self, image_type, image_name):
        path = get_root_path("image", image_type, os.getenv(Environment.PLATFORM), "%s.png" % image_name)
        create_file(os.path.split(path)[0])
        return path


class Application:
    def __init__(self):
        pass

    def open_application(self, sleep_time):
        pass

    def close_application(self):
        pass


class WindowsApplication(Application):
    def __init__(self):
        Application.__init__(self)

    def open_application(self, sleep_time=5):
        get_windows_handler().open_process()
        time.sleep(sleep_time)

    def close_application(self):
        get_windows_handler().close_process()


class AndroidApplication(Application):
    def __init__(self, package=None):
        Application.__init__(self)
        self.pid = -1
        self.package = package or os.getenv(Environment.PACKAGE)
        if not self.package:
            raise EnvironmentError("AndroidApplication package error!")

    def open_application(self, sleep_time):
        get_logger().info("open_application >>> package = %s, sleep_time =%d" % (self.package, sleep_time))
        get_adb_handler().start_by_monkey(self.package)
        time.sleep(sleep_time)
        self.pid = get_adb_handler().get_pid(os.environ["PACKAGE"])

    def close_application(self):
        get_logger().info("close_application >>> package = %s " % self.package)
        get_adb_handler().force_stop(self.package)
        mutex.release()



def get_engine():
    get_engine.instance = None
    if not get_engine.instance:
        platform = os.getenv(Environment.PLATFORM)
        if platform == Platform.Windows:
            get_engine.instance = WindowsEngine()
        elif platform == Platform.Android:
            get_engine.instance = AndroidEngine()
        elif platform == Platform.S3Windows:
            get_engine.instance = S3Engine()
        else:
            get_engine.instance = WindowsEngine()
    return get_engine.instance





def get_image_engine():
    get_image_engine.instance = None
    if not get_image_engine.instance:
        get_image_engine.instance = ImageEngine()
    return get_image_engine.instance





def get_application():
    get_application.instance = None
    if not get_application.instance:
        platform = os.getenv(Environment.PLATFORM)
        if platform == Platform.Windows:
            get_application.instance = WindowsApplication()
        elif platform == Platform.Android:
            get_application.instance = AndroidApplication()
        elif platform == Platform.S3Windows:
            get_application.instance = WindowsApplication()
        else:
            get_application.instance = WindowsApplication()
    return get_application.instance



