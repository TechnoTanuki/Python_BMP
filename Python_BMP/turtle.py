
from typing import Number
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


def goto(x, y = None):
    if len(x) == 2 and type(x) == list:
         _state[0:2] = x
         _state[_cmd] += [f'goto({_state[_x]},{_state[_y]})']
    else:
        if type(y) == Number:
            _state[0:2] = (x, y)
            _state[_cmd] += [f'goto({_state[_x]},{_state[_y]})']
        else:
            _state[_x] = x
            _state[_cmd] += [f'goto({_state[_x]})']


def setpos(x, y = None):
    goto(x, y)


def setposition(x, y = None):
    goto(x, y)


def setx(x):
    _state[_x] = x
    _state[_cmd] += [f'setx({_state[_x]})']


def setx(y):
    _state[_y] = y
    _state[_cmd] += [f'sety({_state[_y]})']


def setheading(to_angle):
    _state[_h] = to_angle
    _state[_cmd] += [f'setheading({_state[_y]})']


def seth(to_angle):
    setheading(to_angle)

def home():
    _state = _default_state
    _state[_cmd] += [f'home()']


def circle(radius, extent=None, steps=None):
    _state[_cmd] += [f'circle({radius})']

def dot(size=None, *color):
    _state[_cmd] += [f'dot({color})']


def undo():
    if len(_state[_cmd]) > 0:
        del _state[_cmd][-1]


def towards(x, y=None):
    if len(x) == 2 and type(x) == list:
         (x0, y0) = _state[0:2]
         _state[_cmd] += [f'towards({_state[_x]},{_state[_y]})']
    else:
        if type(y) == Number:
            (x0, y0) = _state[0:2]
            _state[_cmd] += [f'towards({_state[_x]},{_state[_y]})']
        else:
            x0 = _state[_x]
            _state[_cmd] += [f'towards({_state[_x]})']

