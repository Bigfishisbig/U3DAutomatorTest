import re

__author__ = "Junpeng Chen"


def search(pattern, string):
    model_re = re.compile(pattern)
    result = model_re.search(string)
    if result:
        return result.groups()
    return None
