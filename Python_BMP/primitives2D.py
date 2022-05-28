""" Math for 2D Graphics Primitives
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


from math import(
    sin,
    cos,
    radians,
    comb
    )

from numbers import Number

from .conditionaltools import(
    iif,
    swapif
    )

from .mathlib import (
    addvect,
    computerotvec,
    isinrange,
    mirror1stquad,
    pivotlist,
    rect2polarcoord2Dwithcenter,
    rotvec2D,
    roundvect,
    roundvectlist,
    scalarmulvect,
    setmax,
    sign,
    subvect,
    )


def itercirclepart(r: int
       ) -> list[int, int]:
    """Yields (int, int) 2D vertices
        along a path defined by
        radius r as it traces
        one fourth of a circle
        with origin set at (0, 0)

    Args:
        r: int radius

    Yields:
        [x: int, y: int]
    """
    row = r
    col = 0
    r_sqr = r * r
    _2r_sqr = r_sqr << 1
    _4r_sqr = r_sqr << 2
    d = _2r_sqr * ((row -1 ) * (row)) + \
        r_sqr + _2r_sqr * (1 - r_sqr)
    while row >= col:
        yield([col, row])
        if row != col:
            yield([row,col])
        if d >= 0:
            row -= 1
            d -= _4r_sqr * row
        d += _2r_sqr * (3 + (col << 1))
        col += 1


def itercirclepartlineedge(
        r: int) -> list[int, int]:
    """Yields (int, int) 2D vertices
        along a path defined by
        radius r as it traces
        one fourth of a circle
        with origin set at (0, 0)
        tuned for generating
        filled circles with
        horizontal lines and other
        tasks involving a circular
        area

    Args:
        r: int radius

    Yields:
        [x: int, y: int]
    """
    row = r
    col = 0
    r_sqr = r * r
    _2r_sqr = r_sqr << 1
    _4r_sqr = r_sqr << 2
    d = _2r_sqr * ((row - 1) *(row)) + \
        r_sqr+ _2r_sqr * (1 - r_sqr)
    y = []
    while row >= col:
        if col not in y:
            yield([row, col])
            y += [col]
        if d >= 0:
            if row not in y:
                yield([col, row])
                y += [row]
            row -= 1
            d -= _4r_sqr * row
        d += _2r_sqr * (3 + (col << 1))
        col += 1


def itercirclepartvertlineedge(
        r: int) -> list[int, int]:
    """Yields (int, int) 2D vertices
        along a path defined by
        radius r as it traces
        one fourth of a circle
        with origin set at (0, 0)
        tuned for generating
        filled circles with
        vertical lines and other
        tasks involving a circular
        area

    Args:
        r: int radius

    Yields:
        [x: int, y: int]
    """
    row = r
    col = 0
    r_sqr = r * r
    _2r_sqr = r_sqr << 1
    _4r_sqr = r_sqr << 2
    d = _2r_sqr * ((row - 1) * (row)) + \
        r_sqr + _2r_sqr * (1 - r_sqr)
    x = []
    while row >= col:
        if col not in x:
            yield([col, row])
            x += [col]
        if row not in x:
            yield([row, col])
            x += [row]
        if d >= 0:
            row -= 1
            d -= _4r_sqr * row
        d += _2r_sqr *(3 + (col << 1))
        col += 1


def iterline(
        p1: list[int,int],
        p2: list[int,int]) -> list[int,int]:
    """Yields (int, int) 2D vertices
        along a line segment defined
        by endpoints p1 and p2

    Args:
        p1, p2: line endpoints
                both [x:int, y:int]

    Yields:
        [x:int, y:int]
    """
    (dx, dy) = subvect(p2, p1)
    sdx = sign(dx)
    sdy = sign(dy)
    dxabs = abs(dx)
    dyabs = abs(dy)
    x = y = 0
    (px, py) = p1
    if dxabs >= dyabs:
        ilim = dxabs + 1
        for i in range(0, ilim):
            y += dyabs
            if y >= dxabs:
                y -= dxabs
                py += sdy
            yield([px, py])
            px += sdx
    else:
        ilim = dyabs + 1
        for i in range(0, ilim):
            x += dxabs
            if x >= dyabs:
                x -= dyabs
                px += sdx
            yield([px, py])
            py += sdy
    yield p2


def iterparallelogram(
        p1: list, p2: list, p3: list
        ) -> list[int, int]:
    p = lineseg(p1, p3)
    q = lineseg(p2, addvect(p3,
                    subvect(p2, p1)))
    for u, v in zip(p, q):
        yield [u,v]


def lineseg(p1: list[int, int],
            p2: list[int, int]
      ) -> list[list[int, int]]:
    """Generates a list of (int, int)
        2D vertices along
        a line segment defined
        by endpoints p1 and p2

    Args:
        p1, p2: line endpoints
                both [x:int, y:int]

    Returns:
        [[x:int, y:int],..]

    """
    return [p for p in \
            iterline(p1, p2)]


def iterellipsepart(b: int, a: int):
    """Yields (int, int) 2D vertices
        along a path defined by
        major and minor axes
        b and a as it traces
        one fourth of an ellipse
        with origin set at (0, 0)

    Args:
        b, a: major and minor axes

    Yields:
        [x: int, y: int]
    """
    row = b
    col = 0
    a_sqr = a * a
    b_sqr = b * b
    _2a_sqr = a_sqr << 1
    _4a_sqr = a_sqr << 2
    _2b_sqr = b_sqr << 1
    _4b_sqr = b_sqr << 2
    d= _2a_sqr * ((row - 1) * row) + \
        a_sqr + _2b_sqr * (1 - a_sqr)
    while row * a_sqr >= col * b_sqr:
        yield [col, row]
        if d >= 0:
            row -= 1
            d -= _4a_sqr * row
        d += _2b_sqr * (3 + (col << 1))
        col += 1
    d = _2b_sqr * ((col - 1) * col) + \
        _2a_sqr * (row * (row - 2) + 1) + \
        (1 - _2a_sqr) * b_sqr
    while (row + 1) > 0:
        yield [col, row]
        if d >= 0:
            col += 1
            d -= _4b_sqr * col
        d += _2a_sqr * (3 + (row << 1))
        row -= 1


def iterellipse(x: int, y: int,
                b: int, a: int):
    """Yields (int, int) 2D vertices
        along a path defined by
        major and minor axes
        b and a as it traces
        an ellipse with origin
        set at (x, y)

    Args:
        b, a: major and minor axes

    Yields:
        [x: int, y: int]
    """
    for p in iterellipsepart(b,a):
         for v in mirror1stquad(x,y,p):
             yield v


def iterellipserot(
        x: int, y: int,
        b: int, a: int,
        degrot: float):
    """Yields (int, int) 2D vertices
        along a path defined by
        major and minor axes
        b and a as it traces
        an ellipse with origin
        set at (x, y) rotated
        by degrot degrees

    Args:
        b, a: major and minor axes
        degrot: rotation in degrees

    Yields:
        [x: int, y: int]
    """
    rotvec = computerotvec(degrot)
    c = (x, y)
    for p in iterellipsepart(b, a):
         for v in mirror1stquad(x, y, p):
             yield roundvect(
                    addvect(
                        rotvec2D(
                            subvect(v, c), rotvec), c))


def itercircle(x: int, y: int,
        r: int) -> list[int, int]:
    """Yields (int, int) 2D vertices
        along a path defined by
        radius r as it traces
        a circle with origin set
        at (x, y)

    Args:
        x, y: int centerpoint
                  coordinates
        r   : int radius

    Yields:
        [x: int, y: int]
    """
    for p in itercirclepart(r):
         for v in mirror1stquad(x, y, p):
             yield v


def bezierblend(i: int, n: int, u: int):
    return comb(n, i) * (u ** i) * ((1 - u) ** (n - i))


def iterbeziercurve(pntlist: list) -> list:
    i = 0
    cnt = len(pntlist)
    w = v = pntlist[0]
    klim = cnt << 2
    while i < cnt:
        if i > cnt - 2:
            last = i - 1
            for k in range(0, klim):
                u = k / klim
                v = [0, 0]
                for j in range(0,i):
                    v = addvect(v,
                         scalarmulvect(
                                pntlist[j],
                          bezierblend(
                                j, last, u)))
                for pnt in iterline(roundvect(v),
                                    roundvect(w)):
                    yield pnt
                w = v
        i += 1


def beziercurvevert(
        pntlist: list,
        isclosed: bool,
        curveback: bool) -> list:
    return [v for v in iterbeziercurve(pntlist)]


def iterbspline(
        pntlist: list,
        isclosed: bool,
        curveback: bool) -> list:
    i = 0
    cnt = len(pntlist)
    v = pntlist[0]
    w = v
    klim = cnt << 2
    ilim = cnt + iif(isclosed, 2, 0)
    mx = cnt-1
    while i < ilim:
        for k in range(0, klim):
            u = k / klim
            v = [0, 0]
            nc = bsplineblend(u)
            for j in range(0, 4):
                k = i + j
                v = addvect(v, scalarmulvect(
                     pntlist[k % cnt if curveback else setmax(k, mx)], nc[j]))
            if i > 1:
                for pnt in iterline(roundvect(v), roundvect(w)):
                    yield pnt
            w = v
        i += 1


def bsplinevert(
    pntlist: list,
    isclosed: bool,
    curveback: bool) -> list:
    return [v for v in iterbspline(pntlist,
                                  isclosed,
                                 curveback)]


#dont edit this square shaped code
def bsplineblend(u: float
          ) -> list[float, float,
                    float, float,]:
    u2,u3= u*u,u*u*u
    d,f = u3/6 , 1/6
    a=-d +u2/2-u/2+f
    b= u3/2 -u2 +2/3
    c=(-u3+u2+u)/2+f
    return (a,b,c,d)


def recvert(x1: int, y1: int,
            x2: int, y2: int
            ) -> list[list[int, int],
                      list[int, int],
                      list[int, int],
                      list[int, int]]:
    return [(x1, y1), (x2, y1),
            (x2, y2), (x1, y2)]


def floatregpolygonvert(
        cx: int, cy: int, r: int,
        sides: int, angle: float
        ) -> list[list[int, int]]:
    v = []
    angle = radians(angle)
    anginc = 360 // sides
    maxang = 360
    for a in range(0, maxang, anginc):
        ang = angle + radians(a)
        v.append([int(cx -r * sin(ang)),
                  int(cy -r * cos(ang))])
    return v


def regpolygonvert(cx: int, cy: int,
        r: int, sides: int,
        angle: float
        ) -> list[list[int, int]]:
    return roundvectlist(
                floatregpolygonvert(
                cx,cy,r,sides,angle))


def horizontalvert(y: int,
        x1: int, x2: int, dx: int
        ) -> list[list[int, int]]:
    return [[x, y]
            for x in range(x1, x2, dx)]


def verticalvert(x: int,
        y1: int, y2: int, dy: int
        ) -> list[list[int, int]]:
    return [[x, y]
            for y in range(y1, y2, dy)]


def circlevert(x: int, y: int, r: int
              ) -> list[list[int, int]]:
    return [v for v in itercircle(x, y, r)]


def arcvert(
        x: int, y: int, r: int,
        startdegangle: float,
        enddegangle: float,
        showoutline: bool):
    v = []
    tol = 0.03
    c = (x, y)
    sa = radians(startdegangle)
    ea = radians(enddegangle)
    for p in itercircle(x, y, r):
        pc = rect2polarcoord2Dwithcenter(c, p)
        a = pc[1]
        if a >= sa and a <= ea:
            v.append(p)
            if abs(a - sa) < tol or \
               abs(a - ea) < tol: #for larger arcs tol may be >0.03
                for np in iterline(c, p):
                    v.append(np)
    return v


def rectboundarycoords(
    vlist: list[Number, Number]
      ) -> list[Number, Number]:
    u = pivotlist(vlist)
    (x, y) = u
    return ((min(x), min(y)),
            (max(x), max(y)))


def itergetneighbors(
        v: list[int, int],
        mx: int,
        my: int,
        includecenter: bool)->list:
    (x, y) = v
    if x > -1 and y > -1:
        lx = x - 1
        ty = y - 1
        rx = x + 1
        by = y + 1
        if ty > 0:
            yield [x, ty]
        if includecenter:
            yield(v)
        if by < my:
            yield [x, by]
        if lx > 0:
            if ty > 0:
                yield [lx, ty]
            yield [lx, y]
            if by < my:
                yield [lx, by]
        if rx < mx:
            if ty > 0:
                yield [rx, ty]
            yield [rx, y]
            if by < my:
                yield [rx, by]


def getneighborlist(
        v: list[int, int],
        mx: int, my: int,
        includecenter: bool):
    return [u for u in itergetneighbors(
                v, mx, my, includecenter)]


def spiralcontrolpointsvert(
        x: int, y: int,
        step: int,
        growthfactor: int,
        turns: int):
    v = [[x, y]]
    inc = step
    while turns > 0:
        x += step
        v.append([x, y])
        step += inc
        y += step
        v.append([x, y])
        step += inc
        x -= step
        v.append([x, y])
        step += inc
        y -= step
        v.append([x, y])
        turns -= 1
        step += inc
        inc *= growthfactor
    return v


def sortrecpoints(
        x1: int, y1: int,
        x2: int, y2: int):
    x1, x2 = swapif(x1, x2, x1 > x2)
    y1, y2 = swapif(y1, y2, y1 > y2)
    return x1, y1, x2, y2


def isinrectbnd(
        x: int, y: int,
        xmin: int, ymin: int,
        xmax: int, ymax: int) -> bool:
    return (x < xmax and y < ymax) and \
           (x > xmin and y > ymin)


def listinrecbnd(
        xylist: list[Number, Number],
        xmin: int, ymin: int,
        xmax: int, ymax: int) -> bool:
    retval = True
    for v in xylist:
        if isinrectbnd(v[0], v[1],
                       xmin, ymin,
                       xmax, ymax) == \
            False:
            break
    return retval


def entirecircleisinboundary(
        x: int, y: int,
        minx: int, maxx: int,
        miny: int, maxy: int,
        r: int):
    return (isinrange(x - r, maxx, minx) and \
            isinrange(x + r, maxx, minx)) and \
           (isinrange(y - r, maxy, miny) and \
            isinrange(y + r, maxy, miny))


def entireellipseisinboundary(
        x: int, y: int,
        minx: int, maxx: int,
        miny: int, maxy: int,
        b: int, a: int):
    return (isinrange(x - b, maxx, minx) and \
            isinrange(x + b, maxx, minx)) and \
           (isinrange(y - a, maxy, miny) and \
            isinrange(y + a, maxy, miny))


def ellipsevert(
    x: int, y: int,
    b: int, a: int) -> list[int, int]:
    return [v for v in iterellipse(
                         x, y, b, a)]
