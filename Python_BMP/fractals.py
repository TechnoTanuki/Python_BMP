"""    Fractal Numerics Module
 -----------------------------------
| Copyright 2022 by Joel C. Alcarez |
| [joelalcarez1975@gmail.com]       |
|-----------------------------------|
|    We make absolutely no warranty |
| of any kind, expressed or implied |
|-----------------------------------|
|   Contact primary author          |
|   if you plan to use this         |
|   in a commercial product at      |
|   joelalcarez1975@gmail.com       |
 -----------------------------------
"""

from random import random
from typing import Callable
from .primitives2D import sortrecpoints, iif, isinrectbnd
from .mathlib import (
    addvect,
    newtonmethod,
    scalarmulvect,
    roundvect
    )

def getIFSparams() -> dict:
    return {'fern':(((0, 0, 0, .16, 0, 0),
                    (.2, -.26, .23, .22, 0, 1.6),
                    (-.15, .28, .26, .24, 0, .44),
                    (.85, .04, -.04, .85, 0, 1.6)),
                    (.009, .073, .137, 1)),
            'tree':(((0, .2, 0, .5, 0, 0),
                     (.1, 0, 0, .1, 0, .2),
                     (.42, -.42, .42, .42, 0, .2),
                     (.42, .42, -.42, .42, 0, .2)),
                     (.05, .2, .6, 1)),
      'cantortree':(((1/3, 0, 0, 1/3, 0, 0),
                     (1/3, 0, 0, 1/3, 1, 0),
                     (2/3, 0, 0, 2/3, 0.5, 0.5),
                     (0, 0, 0, 0, 0, 0)),
                     (1/3, 2/3, 1, 1)),
'sierpinskitriangle':(((.5, 0, 0, .5, 0, 0),
                       (.5, 0, 0, .5, 1, 0),
                       (.5, 0, 0, .5, .5, .5),
                       (0, 0, 0, 0, 0, 0)),
                       (1/3, 2/3, 1, 1))}


def fractaldomainparamdict() -> dict:
    return {'maxdefault':(1.75, -1.75, 1.5, -1.5),
              'maxeqdim':(1.75, -1.75, 1.75, -1.75),
            'middefault':(.75, -1.25, 1.25, -1.25),
            'mindefault':(.75, -.75, .5, -.5),
              'mineqdim':(.5, -.5, .5, -.5),
               'custom1':(-.5, -.7, -.5, -.7)}


def funcparamdict() -> dict:
    return {
        3: (lambda z: z * z * z - 1.0, lambda z: 3.0 * (z * z)),
        4: (lambda z: z * z * z * z - 1.0, lambda z: 4.0 * (z * z * z)),
        5: (lambda z: (z * z *z * z * z) - (z), lambda z: 5.0 * (z * z * z * z) - 1),
        6: (lambda z: (z * z *z * z * z * z) - 1, lambda z: 6.0 * (z * z * z * z * z))
    }


def iterIFS(
        IFStransparam: tuple,
        x1: int, y1: int,
        x2: int, y2: int,
        xscale: int, yscale: int,
        xoffset: int, yoffset: int,
        maxiter: int):
    """Yield 2D points for an Interated Function System Fractal

    Args:
        IFStransparam   : see line 19
        x1, y1, x2, y2  : rectangular
                          region
                          to draw in
        xscale, yscale  : scaling factors
        xoffset, yoffset: used to move
                          the fractal
        maxiter         : when to break
                          color compute

    Yields:
        (x: int, y: int)
    """
    x1, y1, x2, y2 = \
        sortrecpoints(x1, y1, x2, y2)
    af = IFStransparam[0]
    p = IFStransparam[1]
    x = x1
    y = y1
    dy = y2 - y1
    for _ in range(maxiter):
        j = random()
        t = af[iif(j < p[0], 0,
               iif(j < p[1], 1,
               iif(j < p[2], 2, 3)))]
        nx = t[0] * x + t[1] * y + t[4]
        y  = t[2] * x + t[3] * y + t[5]
        x = nx
        px = int(x * xscale + xoffset + x1)
        py = int((dy - y * yscale + yoffset) + y1)
        if isinrectbnd(px, py, x1, y1, x2, y2):
          	  yield (px, py)


def multibrot(
        P: float, Q: float,
        d: float, maxiter: int) -> int:
    """Multibrot Function

    Args:
        P : real part as float
        Q : imaginary part as float
        d : exponent
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = 0
    c = complex(P, Q)
    for i in range(maxiter):
        z = z**d + c
        if abs(z) > 2:
            return i
    return maxiter


def newton(P: float, Q: float,
        d: float, maxiter: int) -> tuple:
    """Newton Function

    Args:
        P : real part as float
        Q : imaginary part as float
        d : function and derivative pair
        maxiter : when to break
                  color compute

    Returns:
        list[root, iteration]
    """
    f, fp =  d
    return newtonmethod(complex(P, Q), f, fp, maxiter)


def multijulia(P: float, Q: float,
        c: complex,
        d: float, maxiter: int) -> int:
    """Multijulia Function

    Args:
        P : real part as float
        Q : imaginary part as float
        c : complex number
        d : exponent
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = complex(P, Q)
    for i in range(maxiter):
        z = z**d + c
        if (z * z.conjugate()).real > 4:
            return i
    return maxiter


def multicorn(P: float, Q: float,
        d: float, maxiter: int) -> int:
    """Multicorn Function

    Args:
        P : real part as float
        Q : imaginary part as float
        d : exponent
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = complex(0, 0)
    c = complex(P, Q)
    for i in range(maxiter):
        z = z.conjugate()**d + c
        if abs(z) > 2:
            return i
    return maxiter


def itermultifractal(
        x1: int, y1: int,
        x2: int, y2: int,
        d: any,
        func: Callable,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Multi Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : any paramater
        func          : fractal function
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x:int, y: int, c: int)
    """
    (Pmax, Pmin, Qmax, Qmin) = domain
    x1, y1, x2, y2 = \
        sortrecpoints(x1, y1, x2, y2)
    dp = (Pmax - Pmin) / (x2 - x1)
    dq = (Qmax - Qmin) / (y2 - y1)
    for y in range(y1, y2):
        Q = Qmin + (y - y1) * dq
        for x in range(x1, x2):
            P = Pmin + (x - x1) * dp
            yield (x, y, func(P, Q, d, maxiter))


def itermultifractalcomplexpar(
        x1: int, y1: int,
        x2: int, y2: int,
        c: complex,
        d: float,
        func: Callable,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Multi Fractal with a complex number parameter

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : power to raise z to
        func          : fractal function
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x:int, y: int, c: int)
    """
    (Pmax, Pmin, Qmax, Qmin) = domain
    x1, y1, x2, y2 = \
        sortrecpoints(x1, y1, x2, y2)
    dp = (Pmax - Pmin) / (x2 - x1)
    dq = (Qmax - Qmin) / (y2 - y1)
    for y in range(y1, y2):
        Q = Qmin + (y - y1) * dq
        for x in range(x1, x2):
            P = Pmin + (x - x1) * dp
            yield (x, y, func(P, Q, c, d, maxiter))


def itermandelbrot(
        x1: int, y1: int,
        x2: int, y2: int,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Mandelbrot set

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x:int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, 2,
        multibrot, domain, maxiter):
        yield p


def iterjulia(
        x1: int, y1: int,
        x2: int, y2: int,
        c: complex,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Julia set

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        domain        : coordinates in real
                        and imaginary plane
        c             : complex number
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x:int, y: int, c: int)
    """
    for p in itermultifractalcomplexpar(x1, y1, x2, y2, c, 2,
        multijulia, domain, maxiter):
        yield p


def itertricorn(
        x1: int, y1: int,
        x2: int, y2: int,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Tricorn set

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x:int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, 2,
        multicorn, domain, maxiter):
        yield p


def itermultibrot(
        x1: int, y1: int,
        x2: int, y2: int,
        d: float,
        mandelparam: list[float, float, float, float],
        maxiter: int):
    """Yields a Multibrot set

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : power to raise z to
        mandelparam   : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x:int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        multibrot, mandelparam, maxiter):
        yield p


def itermultijulia(
        x1: int, y1: int,
        x2: int, y2: int,
        c: complex,
        d: float,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Multijulia set

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        c             : complex number
        d             : power to raise z to
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x:int, y: int, c: int)
    """
    for p in itermultifractalcomplexpar(x1, y1, x2, y2, c, d,
        multijulia, domain, maxiter):
        yield p


def itermulticorn(
        x1: int, y1: int,
        x2: int, y2: int,
        d: float,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Multicorn set

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : power to raise z to
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x:int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        multicorn, domain, maxiter):
        yield p


def hilbertvert(l: list,
                u: list[int, int],
                v: list[int, int, int, int],
                n: int):
    """Returns list of 2D points for a Hilbert curve

    Args:
        l: Empty list for return value
        u: origin point (x: int, y: int)
        v: sets orientation and extent
           of the Hilbert Curve
        n: number of recursions
           or order of the curve

    Returns:
        byref list of 2D vertices for
        a Hilbert curve
        [(x: int, y: int),...]
    """
    if n <= 0:
        (v0, v1, v2, v3) = v
        l += [roundvect(
              addvect(u, ((v0 + v2) / 2,
                          (v1 + v3) / 2)))]
    else:
        i = v[2]
        j = v[3]
        v = scalarmulvect(v, 0.5)
        (v0, v1, v2, v3) = v
        n -= 1
        w = (v2, v3, v0, v1)
        hilbertvert(l, u, w, n)
        hilbertvert(l,
          addvect(u, (v0, v1)), v, n)
        hilbertvert(l,
          addvect(u, (v0 + v2, v1 + v3)),
                                   v, n)
        hilbertvert(l,
          addvect(u, (v0 + i, v1 + j)),
                 scalarmulvect(w, -1), n)


def iternewtonsfractal(
        x1: int, y1: int,
        x2: int, y2: int,
        d: list[Callable, Callable],
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields Netwons Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : function and derivative pair
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x:int, y: int, (itercount: int, root: float))
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        newton, domain, maxiter):
        yield p
