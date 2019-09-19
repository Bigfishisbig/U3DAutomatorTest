# coding=utf-8
import urllib as request
import datetime
import json


class Holiday(object):

    def __init__(self):
        self.url = "http://192.168.239.202:1340/holiday/"

    def is_holiday(self, query_date):
        resp = request.urlopen(self.url + query_date)
        content = json.loads(resp.read())
        return content["isHoliday"]

    def today_isholiday(self):
        query_date = datetime.datetime.strftime(datetime.datetime.today(), '%Y%m%d')
        return self.is_holiday(query_date)


if __name__ == '__main__':
    holiday = Holiday()
