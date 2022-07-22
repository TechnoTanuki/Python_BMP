
from typing import Number


_position = [0, 0]

def position():
    return _position

def goto(x, y = None):
    if len(x) == 2 and type(x) == list:
        _position = x
    else:
        if type(y) == Number:
            _position = (x, y)
        else:
            _position[0] = x

def setx(x):
    _position[0] = x


def setx(y):
    _position[1] = y
