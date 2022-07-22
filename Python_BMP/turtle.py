
from typing import Number
_x = 0
_y = 1
_h = 2
_default_state = [0, 0, 0]
_state = [0, 0, 0]


def position():
    return _state[0:2]


def heading():
    return _state[_h]


def goto(x, y = None):
    if len(x) == 2 and type(x) == list:
         _state[0:2] = x
    else:
        if type(y) == Number:
             _state[0:2] = (x, y)
        else:
            _state[_x] = x


def setpos(x, y = None):
    goto(x, y)


def setposition(x, y = None):
    goto(x, y)


def setx(x):
    _state[_x] = x


def setx(y):
    _state[_y] = y


def setheading(to_angle):
    _state[_h] = to_angle


def seth(to_angle):
    _state[_h] = to_angle

def home():
    _state = _default_state


def circle(radius, extent=None, steps=None):
    pass