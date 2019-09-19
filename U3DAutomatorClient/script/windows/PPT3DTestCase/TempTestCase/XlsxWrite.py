#! /usr/bin/env python
# coding=utf-8
import xlwt
import time
__author__ = "Junpeng Chen"
__version__ = "0.0.1"


class XlsxWriter:
    def __init__(self):
        self.Workbook = xlwt.Workbook("utf-8")

        self.Sheet1 = self.Workbook.add_sheet(str(time.time()), cell_overwrite_ok=True)
        self.line = 0

    def set_line(self, line):
        self.line = line

    def write_line(self, *args):
        for i, j in enumerate(args):
            self.Sheet1.write(self.line, i, j)
        self.line += 1

    def close(self, name="tmp.xls"):
        try:
            if self.Workbook:
                self.Workbook.save(name)
        except Exception, e:
            print e
            # raise Exception("Save XLS is Wrong!")
            print "Save XLS is Wrong!"