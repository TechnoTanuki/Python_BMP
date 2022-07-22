
import functools
from typing import Number
from math import degrees, radians

def logaction(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        _state[_cmd] += [f'{f.__name__}({args})']
        return f(*args, **kwargs)
    return wrapper

_p = 0
_h = 1
_cmd = 2
_default_state = [complex(0, 0), 0 , []]
_state = [complex(0, 0), 0, []]

def _goto(x, y = None):
    if len(x) == 2 and type(x) == list:
         _state[_p] = complex(x[0], x[1])
    else:
        if type(y) == Number:
            _state[_p] = complex(x, y)
        else:
            _state[_p].real = x


@logaction
def position():
    return (_state[_p].real, _state[_p].imag)


@logaction
def heading():
    return _state[_h]


@logaction
def goto(x, y = None):
    _goto(x, y)


@logaction
def setpos(x, y = None):
    _goto(x, y)


@logaction
def setposition(x, y = None):
    _goto(x, y)


@logaction
def setx(x):
    _state[_p].real = x


@logaction
def setx(y):
    _state[_p].imag = y


@logaction
def setheading(to_angle):
    _state[_h] = to_angle


@logaction
def seth(to_angle):
    _state[_h] = to_angle


@logaction
def home():
    _state = _default_state


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
        p = complex(*x)
    else:
        if type(y) == Number:
            p = complex(x, y)
        else:
            p = (x, _state[_p].imag)
    d = p - _state[_p]
    return degrees(d.phase)


@logaction
def xcor():
    return _state[_p].real


@logaction
def ycor():
    return _state[_p].imag


@logaction
def heading():
    return _state[_h]


@logaction
def distance(x, y=None):
    if len(x) == 2 and type(x) == list:
        p = complex(*x)
    else:
        if type(y) == Number:
            p = complex(x, y)
        else:
            p = (x, _state[_p].imag)
    d = p - _state[_p]
    return abs(d)

