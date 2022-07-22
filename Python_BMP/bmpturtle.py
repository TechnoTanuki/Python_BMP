
import inspect
import functools
from typing import Number


def logaction(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        _state[_cmd] += [f'{f.__name__}({args})']
        return f(*args, **kwargs)
    return wrapper

_x = 0
_y = 1
_h = 2
_cmd = 3
_default_state = [0, 0, 0 , []]
_state = [0, 0, 0, []]

def position():
    return _state[0:2]


def heading():
    return _state[_h]

@logaction
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

@logaction
def setx(x):
    _state[_x] = x

@logaction
def setx(y):
    _state[_y] = y

@logaction
def setheading(to_angle):
    _state[_h] = to_angle


def seth(to_angle):
    setheading(to_angle)

@logaction
def home():
    _state = _default_state
    _state[_cmd] += [f'home()']

@logaction
def circle(radius, extent=None, steps=None):
    pass

@logaction
def dot(size=None, *color):
    pass

@logaction
def undo():
    if len(_state[_cmd]) > 0:
        del _state[_cmd][-1]

@logaction
def towards(x, y=None):
    if len(x) == 2 and type(x) == list:
         (x0, y0) = _state[0:2]
    else:
        if type(y) == Number:
            (x0, y0) = _state[0:2]
        else:
            x0 = _state[_x]

