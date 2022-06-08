from typing import Callable
from inspect import signature


def getfuncmetastr(f: Callable):
    _d= '"'*3
    return f'def {f.__name__}{signature(f)}\n    {_d}{f.__doc__}{_d}'
