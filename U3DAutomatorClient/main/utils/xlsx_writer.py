#! /usr/bin/env python
# coding=utf-8
import xlwt, xlrd
import time,os
from xlutils.copy import copy

__author__ = "Junpeng Chen"
__version__ = "0.0.1"


class XlsxWriter:
    def __init__(self):
        self.Workbook = xlwt.Workbook("utf-8")
        self.Sheet1 = self.Workbook.add_sheet("data", cell_overwrite_ok=True)
        self.line = 0
        self.name = ""

    def set_line(self, line):
        self.line = line

    def write_line(self, *args):
        for i, j in enumerate(args):
            self.Sheet1.write(self.line, i, str(j))
        self.line += 1

    def close(self, name="tmp.xls"):
        if self.name is not "":
            name = self.name
            try:
                if self.newBK:
                    self.newBK.save(name)
                return
            except Exception, e:
                print e
                # raise Exception("Save XLS is
                # Wrong!")
                print "Save XLS is Wrong!"
        try:
            if self.Workbook:
                self.Workbook.save(name)
        except Exception, e:
            print e
            # raise Exception("Save XLS is
            # Wrong!")
            print "Save XLS is Wrong!"

    def getOldData(self, name="tmp.xls"):
        # dir = os.path.abspath('.').split('src')[0]
        '''主要逻辑实现'''

        try:
            if os.path.exists(name):
                pass
            else:
                return
            oldWb = xlrd.open_workbook(name)  # 先打开已存在的表
            self.newBK = copy(oldWb)
            self.Sheet1 = self.newBK.get_sheet(0)
        except Exception, e:
            print str(e)
        self.line = oldWb.sheet_by_index(0).nrows
        # self.Sheet1 = self.Sheet.get_sheet(0)

        # self.line = self.Sheet1.nrows
        print "Line:", self.line
        self.name = name

