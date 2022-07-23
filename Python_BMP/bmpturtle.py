
import functools
from typing import Number
from math import degrees as deg, radians as rad, pi

def logaction(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        _state[_cmd] += [f'{f.__name__}({args})']
        return f(*args, **kwargs)
    return wrapper
_2pi = 2 * pi
_p = 0
_h = 1
_cmd = 2
_au = 3
_pen = 4


_default_state = [complex(0, 0), 0 , [] ,'d', [True, 1]]
_state = _default_state

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
    _state[_h] = rad(to_angle) if _state[_au] == 'd' else to_angle

@logaction
def seth(to_angle):
    _state[_h] = rad(to_angle) if _state[_au] == 'd' else to_angle


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
    phase = d.phase
    _state[_h] = phase
    h = phase if _state[_au] == 'R' else deg(phase)
    return h


@logaction
def xcor():
    return _state[_p].real


@logaction
def ycor():
    return _state[_p].imag


@logaction
def heading():
    return  degrees(_state[_h]) if _state[_au] == 'd' else _state[_h]


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


@logaction
def degrees(fullcircle=360.0):
    if fullcircle == 360.0:
        _state[_au] == 'd'
    else :
        _state[_au] == fullcircle


@logaction
def radians():
    _state[_au] == 'r'


@logaction
def pendown():
    _state[_pen][0] =  True


@logaction
def pd():
    _state[_pen][0] =  True


@logaction
def down():
    _state[_pen][0] =  True


@logaction
def penup():
    _state[_pen][0] =  False


@logaction
def pu():
    _state[_pen][0] =  False


@logaction
def up():
    _state[_pen][0] =  False



