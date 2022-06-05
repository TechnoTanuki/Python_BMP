from typing import Callable
from inspect import signature


def getfuncmetastr(f: Callable):
    return f'def {f.__name__}{signature(f)}\n\n{f.__doc__}'
