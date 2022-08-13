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
from .primitives2D import (
    sortrecpoints,
    iif,
    isinrectbnd,
    regpolygonvert
    )

from math import (
    sin as sine,
    cos as cosine,
    pi
)

from cmath import (
    sin,
    cos,
    tan,
    exp
)

from .mathlib import (
    addvect,
    subvect,
    newtonmethod,
    scalarmulvect,
    roundvect,
    sign
    )

_2pij = 2 * pi * 1j

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
        3: (lambda z: z * z * z - 1.0,
            lambda z: 3.0 * (z * z)),
        4: (lambda z: z * z * z * z - 1.0,
            lambda z: 4.0 * (z * z * z)),
      4.1: (lambda z: z * z * z * z - z,
            lambda z: 4.0 * (z * z * z) - 1),
        5: (lambda z: (z * z * z * z * z) - 1,
            lambda z: 5.0 * (z * z * z * z)),
      5.1: (lambda z: (z * z * z * z * z) - (z),
            lambda z: 5.0 * (z * z * z * z) - 1),
      5.3: (lambda z: (z * z * z * z * z) - (z * z * z),
            lambda z: 5.0 * (z * z * z * z) - 3.0 * (z * z)),
        6: (lambda z: (z * z * z * z * z * z) - 1,
            lambda z: 6.0 * (z * z * z * z * z)),
      6.3: (lambda z: (z * z * z * z * z * z) - (z * z * z) -  1,
            lambda z: 6.0 * (z * z * z * z * z) - 3 * (z * z))
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
        IFStransparam   : see line 26 of fractals.py
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
    (af, p) = IFStransparam
    x = x1
    y = y1
    dy = y2 - y1
    (p0, p1, p2) = p[0:3]
    for _ in range(maxiter):
        j = random()
        (a, b, c, d, e, f) = \
            af[iif(j < p0, 0,
               iif(j < p1, 1,
               iif(j < p2, 2, 3)))]
        nx = a * x + b * y + e
        y  = c * x + d * y + f
        x = nx
        px = int(x * xscale + xoffset + x1)
        py = int((dy - y * yscale + yoffset) + y1)
        if isinrectbnd(px, py, x1, y1, x2, y2):
          	  yield (px, py)


def tetrationfn(P: float, Q: float,
        d: int, maxiter: int) -> int:
    """Tetration Function

    Args:
        P : real part as float
        Q : imaginary part as float
        d : int Threshold
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = complex(P, Q)
    y = 0
    for i in range(d):
        try:
            if abs(y := y + (z := z**z).imag) > d:
                return i % maxiter
        except OverflowError:
            return i % maxiter
    return maxiter


def sinjulia(P: float, Q: float,
        c: complex, maxiter: int,
        lim: int = 50) -> int:
    """Sin(z) Julia  Function

    Args:
        P : real part as float
        Q : imaginary part as float
        c : complex number
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = complex(P, Q)
    s = 0
    for i in range(lim):
        if abs(s := s + (z := c * sin(z)).imag) > lim:
            return i % maxiter
    return maxiter


def cosjulia(P: float, Q: float,
        c: complex, maxiter: int,
        lim: int = 50) -> int:
    """Cos(z) Julia Function

    Args:
        P : real part as float
        Q : imaginary part as float
        c : complex number
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = complex(P, Q)
    s = 0
    for i in range(lim):
        if abs(s := s + (z := c * cos(z)).imag) > lim:
            return i % maxiter
    return maxiter


def spiraljulia(P: float, Q: float,
        c: complex, maxiter: int) -> int:
    """Spiral Julia Function

    Args:
        P : real part as float
        Q : imaginary part as float
        c : complex number
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = complex(P, Q)
    for i in range(maxiter):
        if abs(z := tan(z*z + c)) > 2:
            return i
    return maxiter


def lambdafn(P: float, Q: float,
        c: complex, maxiter: int) -> int:
    """Lambda fractal Function

    Args:
        P : real part as float
        Q : imaginary part as float
        c : complex number
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = complex(P, Q)
    for i in range(maxiter):
        if abs(z := c * z * (1 - z)) > 2:
            return i
    return maxiter


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
        if abs(z := z**d + c) > 2:
            return i
    return maxiter


def multicircle(
        P: float, Q: float,
        d: float, maxiter: int) -> int:
    """Multicircle Function

    Args:
        P : real part as float
        Q : imaginary part as float
        d : exponent
        maxiter : color limit

    Returns:
        int
    """
    return abs(complex(P, Q)**d) % maxiter


def xorfn(
        P: float, Q: float,
        d: int, maxiter: int) -> int:
    """Xor Function

    Args:
        P : real part as float
        Q : imaginary part as float
        d : int modulo
        maxiter : color limit

    Returns:
        int
    """
    return ((int(P) ^ int(Q)) % d) % maxiter


def xordivfn(
        P: float, Q: float,
        d: int, maxiter: int) -> int:
    """Xor Function with integer div

    Args:
        P : real part as float
        Q : imaginary part as float
        d : int div
        maxiter : color limit

    Returns:
        int
    """
    return ((int(P) ^ int(Q)) // d) % maxiter


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
    return newtonmethod(complex(P, Q), f := d[0], fp := d[1], maxiter)


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


def multibiomorphvariant(P: float, Q: float,
        c: complex,
        d: float,
        maxiter: int,
        a: float = 5) -> int:
    """Multi Biomorph Variant Function

    Args:
        P : real part as float
        Q : imaginary part as float
        c : complex number
        d : exponent
        maxiter : when to break
                  color compute
        a : optional limit as float

    Returns:
        int
    """
    z = complex(P, Q)
    for _ in range(maxiter):
        z = z**d + c
        if abs(z.real) > a or abs(z.imag) > a:
            return abs(z)
    return maxiter


def ngonfunc(P: float, Q: float,
        c: float,
        n: float, maxiter: int) -> int:
    """n-gon Function

    Args:
        P : real part as float
        Q : imaginary part as float
        c : float constant
        n : float exponent (sides)
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = complex(P, Q)
    for i in range(maxiter):
        if z == 0 + 0j:
            return i
        if abs(z := (z**n + c) / z) > 2:
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
        if abs(z := z.conjugate()**d + c) > 2:
            return i
    return maxiter


def barnsleytree(P: float, Q: float,
        d: complex, maxiter: int) -> int:
    """Barnsley Tree Function

    Args:
        P : real part as float
        Q : imaginary part as float
        d : complex number
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = complex(P, Q)
    for i in range(maxiter):
        if abs(z := d * (z - sign(z.real))) > 2:
            return i
    return maxiter


def marekdragon(P: float, Q: float,
        d: float, maxiter: int, lim: int = 65) -> int:
    """Marek Dragon Function

    Args:
        P : real part as float
        Q : imaginary part as float
        d : float
        maxiter : when to break
                  color compute

    Returns:
        int
    """
    z = complex(P, Q)
    s = 0
    for i in range(lim):
        z *= d + z
        s += abs(z.imag)
        if s > lim:
            return i % maxiter
    return maxiter


def mapfractaldomain(
    x1: int, y1: int,
    x2: int, y2: int,
    domain: list[float, float, float, float]
    ) ->list[list, list]:
    """Returns coordinate mapping between the complex plane
    and screen coordinates

    Args:
        x1, y1, x2, y2: rectangular screen area
                        to draw in
        domain        : coordinates in real
                        and imaginary plane
    Returns:
        Coordinate system mapping between screen
        and the complex plane (P -> real,  Q -> imag)
        [[(P: float, x: int), ...],
         [(Q: float, y: int), ...]]
    """
    (Pmax, Pmin, Qmax, Qmin) = domain
    x1, y1, x2, y2 = \
        sortrecpoints(x1, y1, x2, y2)
    dp = (Pmax - Pmin) / (x2 - x1)
    dq = (Qmax - Qmin) / (y2 - y1)
    return [[(Pmin + (x - x1) * dp, x) for x in range(x1, x2)],
            [(Qmin + (y - y1) * dq, y) for y in range(y1, y2)]]


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
        (x: int, y: int, c: int)
    """
    (mp, mq) = mapfractaldomain(x1, y1, x2, y2, domain)
    for (Q, y) in mq:
        for (P, x) in mp:
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
        (x: int, y: int, c: int)
    """
    (mp, mq) = mapfractaldomain(x1, y1, x2, y2, domain)
    for (Q, y) in mq:
        for (P, x) in mp:
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
        (x: int, y: int, c: int)
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
        (x: int, y: int, c: int)
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
        (x: int, y: int, c: int)
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
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        multibrot, mandelparam, maxiter):
        yield p


def itermulticircle(
        x1: int, y1: int,
        x2: int, y2: int,
        d: float,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Multicircle set

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : power to raise z to
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : color limit

    Yields:
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        multicircle, domain, maxiter):
        yield p


def itertetration(
        x1: int, y1: int,
        x2: int, y2: int,
        d: float,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Tetration Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : threshold
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        tetrationfn, domain, maxiter):
        yield p


def iterxorfractal(
        x1: int, y1: int,
        x2: int, y2: int,
        d: int,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Xor Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : int modulo
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        xorfn, domain, maxiter):
        yield p


def iterxordivfractal(
        x1: int, y1: int,
        x2: int, y2: int,
        d: int,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Xor int div Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : int div
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        xordivfn, domain, maxiter):
        yield p


def itersinjulia(
        x1: int, y1: int,
        x2: int, y2: int,
        c: complex,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Sin(z) Julia Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        c             : Complex Number
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, c,
        sinjulia, domain, maxiter):
        yield p


def itercosjulia(
        x1: int, y1: int,
        x2: int, y2: int,
        c: complex,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Cos(z) Julia Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        c             : Complex Number
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, c,
        cosjulia, domain, maxiter):
        yield p


def iterspiraljulia(
        x1: int, y1: int,
        x2: int, y2: int,
        c: complex,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Spiral Julia Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        c             : Complex Number
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, c,
        spiraljulia, domain, maxiter):
        yield p


def iterlamdbafractal(
        x1: int, y1: int,
        x2: int, y2: int,
        c: complex,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Lambda Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        c             : Complex Number
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, c,
        lambdafn, domain, maxiter):
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
        (x: int, y: int, c: int)
    """
    for p in itermultifractalcomplexpar(x1, y1, x2, y2, c, d,
        multijulia, domain, maxiter):
        yield p


def iterngonfractal(
        x1: int, y1: int,
        x2: int, y2: int,
        c: float,
        n: float,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a n-gon fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        c             : float constant
        n             : floatexponent (sides)
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x: int, y: int, c: int)
    """
    for p in itermultifractalcomplexpar(x1, y1, x2, y2, c, n,
        ngonfunc, domain, maxiter):
        yield p


def itermultibiomorphvariant(
        x1: int, y1: int,
        x2: int, y2: int,
        c: complex,
        d: float,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Multi Biomorph Variant fractal

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
        (x: int, y: int, c: int)
    """
    for p in itermultifractalcomplexpar(x1, y1, x2, y2, c, d,
        multibiomorphvariant, domain, maxiter):
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
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        multicorn, domain, maxiter):
        yield p


def iterbarnsleytree(
        x1: int, y1: int,
        x2: int, y2: int,
        d: complex,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Barnsley Tree Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : a complex number
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x: int, y: int, c: int)
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        barnsleytree, domain, maxiter):
        yield p


def itermarekdragon(
        x1: int, y1: int,
        x2: int, y2: int,
        d: float,
        domain: list[float, float, float, float],
        maxiter: int):
    """Yields a Marek Dragon Fractal

    Args:
        x1, y1, x2, y2: rectangular area
                        to draw in
        d             : irrational number
        domain        : coordinates in real
                        and imaginary plane
        rgbfactors    : [r, g, b] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Yields:
        (x: int, y: int, c: int)
    """
    d = exp(_2pij * d)
    for p in itermultifractal(x1, y1, x2, y2, d,
        marekdragon, domain, maxiter):
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
    """Yields Newtons Fractal

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
        (x: int, y: int, (itercount: int, root: float))
    """
    for p in itermultifractal(x1, y1, x2, y2, d,
        newton, domain, maxiter):
        yield p


def koch(u: list[float, float],
         v: list[float, float],
         h: float = 0.28867513459481288225457439025098
         ) -> list[list[float, float],
                   list[float, float],
                   list[float, float]]:
    """Returns new points for a Koch Curve

    Args:
        u: origin point (x, y)
        v: end point (x, y)
        h: optional param to
           control angle and height

    Returns:
        ((x1, y1), (x2, y2), (x3, y3))
    """
    d = subvect(v, u)
    e = scalarmulvect(d, 1/3)
    d = scalarmulvect(d, h)
    return (addvect(u, e),
            addvect(scalarmulvect(addvect(u, v), 0.5),
                    (-d[1], d[0])),
            subvect(v, e)
            )


def kochcurvevert(u: list[int, int],
                  v: list[int, int],
                  n: int
               ) -> list[list[float, float]]:
    """Returns list of 2D points for a Koch curve

    Args:
        u: origin point (x: int, y: int)
        v: end point (x: int, y: int)
        n: number of recursions
           or order of the curve

    Returns:
        list of 2D vertices for a Koch curve
        [(x: int, y: int),...]
    """
    size = 4 ** n + 1
    p = [(0, 0)] * size
    p[0] =  u
    p[-1] = v
    size -= 1
    l = size
    for _ in range(n):
        seg = size // l
        for s in range(seg):
            i = s * l
            j = l >> 2
            (p[i + j],
             p[i + (l >> 1)],
             p[i + (j * 3)]) = koch(p[i],
                                    p[i + l])
        l = j
    return p


def kochsnowflakevert(
    x: int, y: int, r: int,
    angle: float, n: int
    ) -> list[list[float, float]]:
    """Returns list of 2D points for a Koch snowflake

    Args:
        x, y : center coordinates
        r    : radius
        angle: rotation of snowflake
               in degrees
        n: number of recursions
           or order of the curve

    Returns:
        list of 2D vertices for a Koch snowflake
        [(x: int, y: int),...]
    """
    (a, b, c) = regpolygonvert(x, y, r, 3, angle)
    return  kochcurvevert(a, b, n) + \
            kochcurvevert(b, c, n) + \
            kochcurvevert(c, a, n)


def ikedaattractorlist(
        a: float, b: float,
        k: float, p: float,
        n: int) -> list[complex]:
    """Returns list of complex numbers for an Ikeda Attractor

    Args:
        a, b, k, p: float coefficients
        n: number of terms to compute

    Returns:
        list of complex numbers for an Ikeda Attractor
        [z: complex,...]
    """
    z = complex(0, 0)
    return [z := a + b * z * exp(1j * k - (1j * p / (1 + abs(z * z)))) for _ in range(n)]


def nattractorlist(
        a: float, b: float,
        c: float, d: float,
        n: int) -> list[list[float, float]]:
    """Returns list of [x,y] coordinate pairs for a n attractor

    Args:
        a, b, c, d: float coefficients
        n: number of terms to compute

    Returns:
        list of x,y pairs for a n attractor
        [[x: float, y: float],...]
    """
    x = y = 0
    return [[x := a * sine(a * y) + b * cosine(b * x),
             y := c * sine(c * x) + d * cosine(d * y)] for _ in range(n)]


def gumowskimiraattractorlist(
        x: float, y: float,
        a: float, b: float,
        n: int) -> list[list[float, float]]:
    """Returns list of [x,y] coordinate pairs for a
    Gumowski-Mira attractor

    Args:
        x, y: starting coordinates
        a, b: float coefficients
        n   : number of terms to compute

    ox and oy -> any floating point
    value between -20 and +20

    The a and b -> any floating point
    value between -1 and +1.

    Returns:
        list of x,y pairs for a Gumowski-Mira attractor
        [[x: float, y: float],...]
    """
    k = 2 * (1 - a)
    f = lambda x: a * x + k * x * x * (1 + x * x) ** -2
    g = f(x)
    v = [(0,0)] * n
    for i in range(n):
        z = x
        v[i] = (x := b * y + g,
                y := (g := f(x)) - z)
    return v


def peterdejongattractorlist(
        a: float, b: float,
        c: float, d: float,
        n: int) -> list[list[float, float]]:
    """Returns list of [x,y] coordinate pairs for a
    Peter de Jong Attractor

    Args:
        a, b, c, d: float coefficients
        n: number of terms to compute

    Returns:
        list of x,y pairs for a Peter de Jong Attractor
        [[x: float, y: float],...]
    """
    x = y = 0
    v = [(0,0)] * n
    for i in range(n):
         (x, y) = v[i] = \
         (sine(a * y) - cosine(b * x),
          sine(c * x) - cosine(d * y))
    return v


def cliffordattractorlist(
        a: float, b: float,
        c: float, d: float,
        n: int) -> list[list[float, float]]:
    """Returns list of [x,y] coordinate pairs for a
    Clifford Attractor

    Args:
        a, b, c, d: float coefficients
        n: number of terms to compute

    Returns:
        list of x,y pairs for a Clifford Attractor
        [[x: float, y: float],...]
    """
    x = y = 0
    v = [(0,0)] * n
    for i in range(n):
         (x, y) = v[i] = \
         (sine(a * y) + c * cosine(a * x),
          sine(b * x) + d * cosine(b * y))
    return v


def wallpaperattractorlist(
        a: float, b: float,
        c: float,
        n: int) -> list[list[float, float]]:
    """Returns list of [x,y] coordinate pairs for a
    Wallpaper Attractor

    Args:
        a, b, c: float coefficients
        n: number of terms to compute

    Returns:
        list of x,y pairs for a Wallpaper Attractor
        [[x: float, y: float],...]
    """
    x = y = 0
    v = [(0,0)] * n
    for i in range(n):
         (x, y) = v[i] = \
         (y - sign(x) * (abs(b * x - c) ** .5),
          a - x)
    return v