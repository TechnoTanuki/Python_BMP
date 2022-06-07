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
    """Yields (int, int) 2D vertices along
    a path defined by radius r as it traces
    one fourth of a circle with origin set
    at (0, 0)

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
    d = _2r_sqr * ((row - 1 ) * (row)) + \
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
    """Yields (int, int) 2D vertices along
    a path defined by radius r as it traces
    one fourth of a circle with origin set
    at (0, 0) tuned for generating
    filled circles with horizontal lines
     and other tasks involving circular areas

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
    """Yields (int, int) 2D vertices along
    a path defined by radius r as it traces
    one fourth of a circle with origin set
    at (0, 0) tuned for generating
    filled circles with vertical lines
    and other tasks involving circular areas

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


def iterline(p1: list[int,int],
             p2: list[int,int]
            ) -> list[int,int]:
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
        for _ in range(ilim):
            y += dyabs
            if y >= dxabs:
                y -= dxabs
                py += sdy
            yield([px, py])
            px += sdx
    else:
        ilim = dyabs + 1
        for _ in range(ilim):
            x += dxabs
            if x >= dyabs:
                x -= dyabs
                px += sdx
            yield([px, py])
            py += sdy
    yield p2


def iterparallelogram(
         p1: list[int, int],
         p2: list[int, int],
         p3: list[int, int]
        ) -> list[int, int]:
    p = lineseg(p1, p3)
    q = lineseg(p2, addvect(p3,
                    subvect(p2, p1)))
    for u, v in zip(p, q):
        yield [u, v]


def lineseg(p1: list[int, int],
            p2: list[int, int]
      ) -> list[list[int, int]]:
    """Generates a list of (int, int)
    2D vertices along a line segment
    defined by endpoints p1 and p2

    Args:
        p1, p2: line endpoints
                both [x:int, y:int]

    Returns:
        [[x:int, y:int],..]
    """
    return list(iterline(p1, p2))


def iterellipsepart(b: int, a: int):
    """Yields (int, int) 2D vertices along
    a path defined by major and minor axes
    b and a as it traces one fourth of an
    ellipse with origin set at (0, 0)

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
    while row > -1:
        yield [col, row]
        if d >= 0:
            col += 1
            d -= _4b_sqr * col
        d += _2a_sqr * (3 + (row << 1))
        row -= 1


def iterellipse(x: int, y: int,
                b: int, a: int):
    """Yields (int, int) 2D vertices along
    a path defined by major and minor axes
    b and a as it traces an ellipse with
    origin set at (x, y)

    Args:
        b, a: major and minor axes

    Yields:
        [x: int, y: int]
    """
    for p in iterellipsepart(b,a):
        yield from mirror1stquad(x,y,p)


def iterellipserot(x: int, y: int,
                   b: int, a: int,
                   degrot: float):
    """Yields (int, int) 2D vertices along
    a path defined by major and minor axes
    b and a as it traces an ellipse with origin
    set at (x, y) rotated by degrot degrees

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
    """Yields (int, int) 2D vertices along
    a path defined by radius r as it traces
    a circle with origin set at (x, y)

    Args:
        x, y: int centerpoint
                  coordinates
        r   : int radius

    Yields:
        [x: int, y: int]
    """
    for p in itercirclepart(r):
        yield from mirror1stquad(x, y, p)


def _bezierblend(i: int, n: int, u: int):
    return comb(n, i) * (u ** i) * \
              ((1 - u) ** (n - i))


def iterbeziercurve(
        pntlist: list[list[int, int]]
                 ) -> list[int, int]:
    """Yields a list of vertices for a bezier curve
    based on 2D control points in pntlist

    Args:
        pntlist: 2D control points
                 for the bezier curve
                 as list[list[x: int,
                              y: int]]

    Yields:
        vertices as list[x: int, y: int]
    """
    cnt = len(pntlist)
    w = v = pntlist[0]
    klim = cnt << 2
    for i in range(cnt):
        if i > cnt - 2:
            last = i - 1
            for k in range(klim):
                u = k / klim
                v = [0, 0]
                for j in range(i):
                    v = addvect(v,
                         scalarmulvect(
                                pntlist[j],
                          _bezierblend(
                                j, last, u)))
                yield from iterline(roundvect(v),
                                    roundvect(w))
                w = v


def beziercurvevert(
        pntlist: list[list[int, int]],
        isclosed: bool,
        curveback: bool) -> list[int, int]:
    """Creates a list of vertices for a bezier curve
    based on 2D control points in pntlist

    Args:
        pntlist: 2D control points
                 for the bezier curve
                 as list[list[x: int,
                              y: int]]

    Returns:
        list of vertices as
        list[list[x: int, y: int]]
    """
    return list(iterbeziercurve(pntlist))


def iterbspline(
        pntlist: list[list[int, int]],
        isclosed: bool,
        curveback: bool) -> list[int, int]:
    """Yields a list of vertices for a bspline curve
    based on 2D control points in pntlist

    Args:
        pntlist: 2D control points
                 for the bspline curve
                 as list[list[x: int,
                              y: int]]

    Yields:
        vertices as list[x: int, y: int]
    """
    i = 0
    cnt = len(pntlist)
    v = pntlist[0]
    w = v
    klim = cnt << 2
    ilim = cnt + iif(isclosed, 2, 0)
    mx = cnt-1
    while i < ilim:
        for k in range(klim):
            u = k / klim
            v = [0, 0]
            nc = _bsplineblend(u)
            for j in range(4):
                k = i + j
                v = addvect(v, scalarmulvect(
                     pntlist[k % cnt if curveback else setmax(k, mx)], nc[j]))
            if i > 1:
                yield from iterline(roundvect(v),
                                    roundvect(w))
            w = v
        i += 1


def bsplinevert(
    pntlist: list[list[int, int]],
    isclosed: bool,
    curveback: bool
    ) -> list[list[int, int]]:
    """Creates a list of vertices for a bspline curve

    Args:
        pntlist: 2D control points
                 for the bspline curve
                 as list[list[x: int,
                              y: int]]

    Returns:
        list of vertices as
        list[list[x: int, y: int]]
    """
    return list(iterbspline(pntlist, isclosed, curveback))


#dont edit this square shaped code
def _bsplineblend(u: float
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
    """Creates a list of vertices for a rectangle

    Args:
        x1, y1, x1, y2: int values

    Returns:
        list of vertices
        [(x1, y1), (x2, y1),
         (x2, y2), (x1, y2)]
    """
    return [(x1, y1), (x2, y1),
            (x2, y2), (x1, y2)]


def floatregpolygonvert(
        cx: int, cy: int, r: int,
        sides: int, angle: float
        ) -> list[list[float, float]]:
    """Creates a list of float vertices for a regular polygon

    Args:
        cx, cy: int center of a circle
        r     : int radius of a circle
                that circumscribes the
                regular polygon
        sides : int sides of the
                regular polygon
        angle:  angle of rotation
                of the polygon in
                degrees

    Returns:
        list of float vertices
        [(x, y), ...]
    """
    v = []
    angle = radians(angle)
    anginc = 360 // sides
    maxang = 360
    for a in range(0, maxang, anginc):
        ang = angle + radians(a)
        v.append([cx - r * sin(ang),
                  cy - r * cos(ang)])
    return v


def regpolygonvert(cx: int, cy: int,
        r: int, sides: int,
        angle: float
        ) -> list[list[int, int]]:
    """Creates a list of int vertices for a regular polygon

    Args:
        cx, cy: int center of a circle
        r     : int radius of a circle
                that circumscribes the
                regular polygon
        sides : int sides of the
                regular polygon
        angle:  angle of rotation
                of the polygon in
                degrees

    Returns:
        list of int vertices
        [(x, y), ...]
    """
    return roundvectlist(
            floatregpolygonvert(
            cx, cy, r, sides, angle))


def horizontalvert(y: int,
        x1: int, x2: int, dx: int
        ) -> list[list[int, int]]:
    """Creates a list of int vertices along
    a horizontal line with int step dx

    Args:
        y : int constant y
        x1: int start point
        x2: int end point
        dx: int x step increment

    Returns:
        list of int vertices
        [(x, y), ...]
    """
    return [[x, y]
            for x in range(x1, x2, dx)]


def verticalvert(x: int,
        y1: int, y2: int, dy: int
        ) -> list[list[int, int]]:
    """Creates a list of int vertices
    along a vertical line with int step dy

    Args:
        x : int constant x
        y1: int start point
        y2: int end point
        dy: int y step increment

    Returns:
        list of int vertices
        [(x, y), ...]
    """
    return [[x, y]
            for y in range(y1, y2, dy)]


def circlevert(x: int, y: int, r: int
              ) -> list[list[int, int]]:
    """Returns a list[(int, int)] of 2D vertices
    along a path defined by radius r as it
    traces a circle with origin set at (x, y)

    Args:
        x, y: int centerpoint
                  coordinates
        r   : int radius

    Yields:
        list of vertices
        to draw a circle
        list[[x: int, y: int]]
    """
    return list(itercircle(x, y, r))


def arcvert(x: int, y: int, r: int,
            startdegangle: float,
            enddegangle: float):
    """Returns a list[(int, int)] of 2D vertices
    along a path defined by radius r as it
    traces an arc with origin set at (x, y)

    Args:
        x, y: int centerpoint
                  coordinates
        r   : int radius

        startangle: degree start of arc
        endangle  : degree end of arc

    Yields:
        list of vertices of the arc
        list[[x: int, y: int]]
    """
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
                v.extend(iter(iterline(c, p)))
    return v


def rectboundarycoords(
        vlist: list) -> list:
    """Returns the rectangular bounds of a list of 2D vertices

    Args:
        vlist: list[(x: int, y :int)]

    Yields:
        ((min(x), min(y)),
         (max(x), max(y)))
    """
    (x, y) = pivotlist(vlist)
    return ((min(x), min(y)),
            (max(x), max(y)))


def itergetneighbors(v: list[int, int],
                      mx: int, my: int,
                   includecenter: bool
                   ) -> list[int, int]:
    """Yields the neighboring pixels of point v

    Args:
        v : (x: int, y: int) point
        mx: maximum x
        my: maximum y
        includecenter: do we yield
                       point v too

    Yields:
        [x: int, y: int]
    """
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
        includecenter: bool) -> list:
    """Returns the neighboring pixels of point v

    Args:
        v : (x: int, y: int) point
        mx: maximum x
        my: maximum y
        includecenter: do we yield
                       point v too

    Returns:
        list of neighboring pixels
        [[x: int, y: int],...]
    """
    return list(itergetneighbors(v, mx, my, includecenter))


def spiralcontrolpointsvert(
        x: int, y: int,
        step: int,
        growthfactor: float,
        turns: int):
    """Returns a list of 2D vertices of a Square Spiral

    Args:
        x, y: int centerpoint
                  coordinates
        step: int step increment
        growthfactor: float multiplier
                      to step increment
                      to make exponential
                      spirals
        turns: number of turns of the
               spiral

    Returns:
        list of vertices of the spiral
        list[[x: int, y: int]]
    """
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


def sortrecpoints(x1: int, y1: int,
                  x2: int, y2: int):
    """Sorts the x and y values that sets a rectangular area

    Args:
        x1, x2: int x coordinates
        y1, y2: int y coordinates

    Returns:
        sorted coordinates
        x1, y1, x2, y2
        such that
        x1 < x2 and y1 < y2
    """
    x1, x2 = swapif(x1, x2, x1 > x2)
    y1, y2 = swapif(y1, y2, y1 > y2)
    return x1, y1, x2, y2


def isinrectbnd(x: int, y: int,
        xmin: int, ymin: int,
        xmax: int, ymax: int) -> bool:
    """Checks if the x and y values
    lie within the rectangular area
    defined by xmin, ymin and xmax, ymax

    Args:
        x, y: (x,y) coordinates to test
        xmin, ymin: min (x, y) bounds
        xmax, ymax: max (x, y) bounds

    Returns:
        boolean value
        True  -> (x, y) is in bounds
        False -> (x, y) is out of bounds
    """
    return (x < xmax and y < ymax) and \
           (x > xmin and y > ymin)


def listinrecbnd(
        xylist: list[list[Number, Number]],
        xmin: int, ymin: int,
        xmax: int, ymax: int) -> bool:
    """Checks if all the values in a
    list of x and y value pairs
    lie within the rectangular area
    defined by xmin, ymin and xmax, ymax

    Args:
        x, y: list[list(x,y)] list of
              x, y pairs to test
        xmin, ymin: min (x, y) bounds
        xmax, ymax: max (x, y) bounds


    Returns:
        boolean value
        True  -> All (x, y)
                 is in bounds
        False -> Not all (x, y)
                 is in bounds
    """
    for v in xylist:
        if isinrectbnd(v[0], v[1],
                       xmin, ymin,
                       xmax, ymax) == \
            False:
            break
    return True


def entirecircleisinboundary(
        x: int, y: int,
        minx: int, maxx: int,
        miny: int, maxy: int,
        r: int):
    """Checks if an entire circle
    is within a rectagular area

    Args:
        x, y: center of the ellipse
        xmin, ymin: min (x, y) bounds
        xmax, ymax: max (x, y) bounds
        r   : radius of the circle

    Returns:
        boolean value
        True  -> All (x, y)
                 is in bounds
        False -> Not all (x, y)
                 is in bounds
    """
    return (isinrange(x - r, maxx, minx) and \
            isinrange(x + r, maxx, minx)) and \
           (isinrange(y - r, maxy, miny) and \
            isinrange(y + r, maxy, miny))


def entireellipseisinboundary(
        x: int, y: int,
        minx: int, maxx: int,
        miny: int, maxy: int,
        b: int, a: int):
    """Checks if an entire ellipse
    is within a rectagular area

    Args:
        x, y: center of the ellipse
        xmin, ymin: min (x, y) bounds
        xmax, ymax: max (x, y) bounds
        b, a: major and minor axes

    Returns:
        boolean value
        True  -> All (x, y)
                 is in bounds
        False -> Not all (x, y)
                 is in bounds
    """
    return (isinrange(x - b, maxx, minx) and \
            isinrange(x + b, maxx, minx)) and \
           (isinrange(y - a, maxy, miny) and \
            isinrange(y + a, maxy, miny))


def ellipsevert(x: int, y: int,
                b: int, a: int
               ) -> list[int, int]:
    """Returns (int, int) 2D vertices
    along a path defined by major and
    minor axes b and a as it traces
    an ellipse with origin set at (x, y)

    Args:
        x, y: center of the ellipse
        b, a: major and minor axes

    Returns:
        The list vertices of an
        ellipse
        [[x: int, y: int], ...]
    """
    return list(iterellipse(x, y, b, a))


def iterspirograph(
        x: int, y:int, r: int,
        l: float, k: float,
        delta: float, lim: float):
    """Yields (int, int) 2D vertices
    along a path defined by spirograph
    scaling factor r and dimensionless
    parameters l and k with an origin
    set at (x, y)

    Args:
        x, y : center of the spirograph
        r    : spirograph scaling factor
        l, k : spirograph shape parameters
        delta: angle increment in radians
        lim  : angle limit in radians

    Yields:
        The vertices of an
        spirograph
        [[x: int, y: int], ...]
    """
    a = 0
    e = l * k
    d = 1 - k
    f = d / k
    while a < lim:
        b = a * f
        dx =  round(r * (d * cos(a) + \
                         e * cos(b)))
        dy =  round(r * (d * sin(a) + \
                         e * sin(b)))
        a += delta
        yield (x + dx, y + dy)


def spirographvert(
        x: int, y: int, r: int,
        l: float, k: float,
        delta: float, lim: float):
    """Returns a list(int, int) of
    2D vertices along a path defined
    by a spirograph with scaling factor r
    and dimensionless parametersl and k
    with an origin set at (x, y)

    Args:
        x, y : center of the spirograph
        r    : spirograph scaling factor
        l, k : spirograph shape parameters
        delta: angle increment in radians
        lim  : angle limit in radians

    Returns:
        The vertices of an
        spirograph in a list
        [[x: int, y: int], ...]
    """
    return list(iterspirograph(x, y, r,
                l, k, delta, lim))


def iterlissajouscurve(
        x: int, y: int,
        a: float, b: float,
        c: float, d: float, e: float,
        delta: float, lim: float):
    """Yields (int, int) 2D vertices
    along a path defined by lissajous
    curve axis scaling factors a and b
    and frequency scaling factors
    parameters c and d and
    radian phase shift angle e
    with an origin set at (x, y)

    Args:
        x, y : center of the curve
        a, b : axis scaling factors
        c, d : frequency scaling factors
        e    : phase shift in radians
        delta: angle increment in radians
        lim  : angle limit in radians

    Yields:
        Vertices of a lissajous curve
        [x: int, y: int]
    """
    t = 0
    while t < lim:
        dx = round(a * cos(c * t + e))
        dy = round(b * sin(d * t))
        t += delta
        yield (x + dx, y + dy)


def lissajouscurvevert(
        x: int, y: int,
        a: float, b: float,
        c: float, d: float,
        e: float,
        delta: float, lim: float):
    """Returns (int, int) 2D vertices
    along a path defined by a lissajous curve
    axis scaling factors a and b and
    frequency scaling factors parameters
    c and d and radian phase shift angle e
    with an origin set at (x, y)

    Args:
        x, y : center of the curve
        a, b : axis scaling factors
        c, d : frequency scaling factors
        e    : phase shift in radians
        delta: angle increment in radians
        lim  : angle limit in radians

    Returns:
        Vertices of a lissajous curve
        in a list [[x: int, y: int], ...]
    """
    return list(iterlissajouscurve(x, y,
                          a, b, c, d, e,
                            delta, lim))


def itercircleinvolute(
        x: int, y: int, a: float,
        delta: float, lim: float):
    """Yields (int, int) 2D vertices
    along a path defined by the involute
    of a circle with scaling factor a
    and an origin set at (x, y)

    The involute of a circle is the path
    traced out by a point on a straight
    line that rolls around a circle.

    It was studied by Huygens when he was
    considering clocks without pendulums
    that might be used on ships at sea.

    Args:
        x, y : center of the curve
        a    : scaling factor
        delta: angle increment in radians
        lim  : angle limit in radians

    Yields:
        The vertices of the
        involute of a circle
        [[x: int, y: int], ...]
    """
    t = 0
    while t < lim:
        dx =  round(a * (cos(t) + t * sin(t)))
        dy =  round(a * (sin(t) - t * cos(t)))
        t += delta
        yield (x + dx, y + dy)


def circleinvolutevert(
        x: int, y: int, a: float,
        delta: float, lim: float):
    """Returns (int, int) 2D vertices
    along a path defined by the involute
    of a circle with scaling factor a
    and an origin set at (x, y)

    The involute of a circle is the path
    traced out by a point on a straight
    line that rolls around a circle.

    It was studied by Huygens when he was
    considering clocks without pendulums
    that might be used on ships at sea.

    Args:
        x, y : center of the curve
        a    : scaling factor
        delta: angle increment in radians
        lim  : angle limit in radians

    Yields:
        The vertices of the
        involute of a circle in a list
        [[x: int, y: int], ...]
    """
    return list(itercircleinvolute(x, y,
                        a, delta, lim))


def iterepicycloid(
        x: int, y: int,
        a: float, b: float,
        delta: float, lim: float):
    """Yields (int, int) 2D vertices
    along a path defined by epicycloid
    traced by a circleof radius b which
    rolls round a circle of radius a
    with an origin set at (x, y)

    Args:
        x, y : center of epicycloid
        a    : radius of fixed circle
        b    : radius of rolling circle
        delta: angle increment in radians
        lim  : angle limit in radians

    Yields:
        The vertices of an
        epicycloid
        [[x: int, y: int], ...]
    """
    ab = a + b
    c = (a / b) + 1
    t = 0
    while t < lim:
        d = c * t
        dx =  round(ab * cos(t) - \
                     b * cos(d))
        dy =  round(ab * sin(t) - \
                     b * sin(d))
        t += delta
        yield (x + dx, y + dy)


def epicycloidvert(
        x: int, y: int,
        a: float, b: float,
        delta: float, lim: float):
    """Returns (int, int) 2D vertices
    along a path defined by epicycloid
    traced by a circle of radius b which
    rolls round a circle of radius a
    with an origin set at (x, y)

    Args:
        x, y : center of epicycloid
        a    : radius of fixed circle
        b    : radius of rolling circle
        delta: angle increment in radians
        lim  : angle limit in radians

    Returns:
        The vertices of an
        epicycloid in a list
        [[x: int, y: int], ...]
    """
    return list(iterepicycloid(x, y,
                  a, b, delta, lim))


def iterhypotrochoid(
        x: int, y: int,
        a: float, b: float, c: float,
        delta: float, lim: float):
    """Yields (int, int) 2D vertices
    along a path defined by a hypotrochoid
    traced by a point from with distance c
    from the center of circle of radius b
    which rolls round a circle of radius a
    with an origin set at (x, y)

    Args:
        x, y : center of epicycloid
        a    : radius of fixed circle
        b    : radius of rolling circle
        c    : distance of pen from the
               center of circle with
               radius b
        delta: angle increment in radians
        lim  : angle limit in radians

    Yields:
        The vertices of an
        epicycloid
        [[x: int, y: int], ...]
    """
    ab = a - b
    d = (a / b) + 1
    t = 0
    while t < lim:
        e = d * t
        dx =  round(ab * cos(t) - \
                     c * cos(e))
        dy =  round(ab * sin(t) - \
                     c * sin(e))
        t += delta
        yield (x + dx, y + dy)


def hypotrochoidvert(
            x: int, y: int,
            a: float, b: float, c: float,
            delta: float, lim: float):
    """Returns (int, int) 2D vertices
    along a path defined by a hypotrochoid
    traced by a point with distance c from
    the center of circle of radius b
    which rolls round a circle of radius a
    with an origin set at (x, y)

    Args:
        x, y : center of hypotrochoid
        a    : radius of fixed circle
        b    : radius of rolling circle
        c    : distance of pen from the
               center of circle with
               radius b
        delta: angle increment in radians
        lim  : angle limit in radians

    Returns:
        The vertices of an
        hypotrochoid in a list
        [[x: int, y: int], ...]
    """
    return list(iterhypotrochoid(x, y,
                  a, b, c, delta, lim))