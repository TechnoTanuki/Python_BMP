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
from .primitives2D import sortrecpoints, iif, isinrectbnd

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


def mandelparamdict() -> dict:
    return {'maxdefault':(1.75,-1.75,1.5,-1.5),
              'maxeqdim':(1.75,-1.75,1.75,-1.75),
            'middefault':(.75,-1.25,1.25,-1.25),
            'mindefault':(.75,-.75,.5,-.5),
              'mineqdim':(.5,-.5,.5,-.5),
               'custom1':(-.5,-.7,-.5,-.7)}


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


def itermandelbrot(
        x1: int, y1: int,
        x2: int, y2: int,
        mandelparam: list[float, float, float, float],
        maxiter: int):
    """Yields a Mandelbrot set

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: rectangular area
                        to draw in
        mandelparam   : see fractals.py
        rgbfactors    : [r, b, g] values
                        range from
                        0.0 to 1.0
        maxiter       : when to break
                        color compute

    Returns:
        (x:int, y: int, c: int)
    """
    (Pmax, Pmin, Qmax, Qmin) = \
                 mandelparam
    x1, y1, x2, y2 = \
        sortrecpoints(x1, y1, x2, y2)
    maxx = x2 - x1
    maxy = y2 - y1
    dp = (Pmax - Pmin) / maxx
    dq = (Qmax - Qmin) / maxy
    max_size = 4
    for y in range(y1, y2):
        Q = Qmin + (y - y1) * dq
        for x in range(x1, x2):
            P = Pmin + (x - x1) * dp
            xp = yp = c= Xsq = Ysq = 0
            while (Xsq + Ysq) < max_size:
                 xp, yp = Xsq - Ysq + P, \
                       2 * xp * yp + Q
                 Xsq = xp * xp
                 Ysq = yp * yp
                 c += 1
                 if c > maxiter:
                     break
            yield (x, y, c)