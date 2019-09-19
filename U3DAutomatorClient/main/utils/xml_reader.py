import os
import sys
from xml.dom import minidom
from main.utils.path import get_root_path

__author__ = "Junpeng Chen"
__all__ = ["get_config"]


class XmlReader(object):
    def __init__(self, xml_path):
        self.path = xml_path
        self.is_exist()
        self.root = minidom.parse(self.path).documentElement

    def is_exist(self):
        if not os.path.exists(self.path):
            # #print "%s is not exist" % self.path
            sys.exit()

    def read(self, tag, param=None):
        nodes = self.root.getElementsByTagName(tag)
        if not param:
            return nodes[0].childNodes[0].data
        else:
            return nodes[0].getAttribute(param)

    def __getattr__(self, item):
        return self.read(item)

def get_config():
    if not get_config.instance:
        # get config file
        config_file = "config.xml"
        for arg in sys.argv:
            if arg[0:7] == "config:":
                config_file = arg[7:]
        get_config.instance = XmlReader(get_root_path(config_file))
    return get_config.instance


get_config.instance = None
