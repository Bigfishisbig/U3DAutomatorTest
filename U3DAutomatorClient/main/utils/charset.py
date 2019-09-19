# coding=utf-8
import chardet

__author__ = "Junpeng Chen"


def convert(string, encoding):
    # fixme 转换类型有存在差异，待研究。python3.0+无编码格式问题，是否考虑转3.0+
    if not isinstance(string, basestring):
        raise Exception("%s isn't string" % string)
    dic = chardet.detect(string)
    tmp = dic.get("encoding")

    if tmp == encoding:
        return string
    if encoding == 'unicode':
        return string.decode(tmp)
    if tmp == 'unicode':
        return string.encode(encoding)
    return string.decode(tmp).encode(encoding)
