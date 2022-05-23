# -----------------------------------
#| Copyright 2022 by Joel C. Alcarez |
#| [joelalcarez1975@gmail.com]       |
#|-----------------------------------|
#|    We make absolutely no warranty |
#| of any kind, expressed or implied |
#|-----------------------------------|
#|   Contact primary author          |
#|   if you plan to use this         |
#|   in a commercial product at      |
#|   joelalcarez1975@gmail.com       |
# -----------------------------------


from math import(
    acos,
    atan,
    cos,
    degrees,
    pi,
    radians,
    sin,
    sqrt
    )

from random import randint
from functools import reduce
from typing import Callable
from .conditionaltools import iif


def setmaxvec(
        vlist: list,
        maxval: float) -> list:
    return [setmax(v, maxval)
                for v in vlist]


def setminmaxvec(
        vlist: list,
        minval: float,
        maxval: float) -> list:
    return [setminmax(v, minval, maxval)
                for v in vlist]


def intsetminmaxvec(
        vlist: list,
        minval: int,
        maxval: int) -> list:
    return [intsetminmax(v, minval, maxval)
                for v in vlist]


def range2baseanddelta(lst_range: list):
    return lst_range[0], lst_range[1] - lst_range[0]


def roundvect(v: list) -> list:
    return [round(n) for n in v]


def roundvectlist(
        vlist: list) -> list:
    return [roundvect(v)
            for v in vlist]


def addvect(u: list,
            v: list) -> list:
    return [i + j
            for i, j in zip(u, v)]


def trans(vlist: list,
              u: list) -> list:
    return [addvect(v, u)
            for v in vlist]


def subvect(u: list,
            v: list) -> list:
    return [i - j
            for i, j in zip(u, v)]


def mulvect(u: list,
            v: list) -> list:
    return [i * j
            for i, j in zip(u,v)]


def divvect(u: list,
            v: list) -> list:
    return [i / j
            for i, j in zip(u, v)]


def scalarmulvect(vec: list,
            scalarval: float) -> list:
    return [s*scalarval for s in vec]


def intscalarmulvect(vec: list,
               scalarval: float) -> list:
    return [round(s * scalarval)
            for s in vec]


def mean(v: list) -> float:
    return sum(v) / len(v)


def meanlist(vlist: list) -> list:
    return [mean(v)
            for v in vlist]


def pivotlist(vlist:list) -> list:
    j = len(vlist[0])
    return [[v[i] for v in vlist]
            for i in range(0,j)]


def variance(v: list) -> list:
    ave = mean(v)
    return [n - ave for n in v]


def isinrange(value: float,
          highlimit: float,
           lowlimit: float) -> bool:
    return (value > lowlimit) and \
           (value < highlimit)


def setmax(val: float,
        maxval: float) -> float:
    return maxval if val>maxval else val


def setmin(val: float,
        minval: float) -> float:
    return minval if val<minval else val


def setminmax(val: float,
           minval: float,
           maxval: float) -> float:
    if val > maxval: val = maxval
    if val < minval: val = minval
    return val


def intsetminmax(val: float,
              minval: int,
              maxval: int) -> int:
    val = round(val)
    if val > maxval:
        val = maxval
    if val < minval:
        val = minval
    return val


def sign(intval: int) -> int:
    retval = 0
    if intval > 0:
        retval = 1
    elif intval == 0:
        retval = 0
    else:
        retval = -1
    return retval


def LSMslope(XYdata: list) -> float:#first two values inlist must be [[x and y...]...]
    XY , N = pivotlist(XYdata), len(XYdata)
    X =  XY[0]
    Y =  XY[1]
    EX = sum(X)
    EY = sum(Y)
    EXY = sum(mulvect(X,Y))
    EsqX = sum(mulvect(X,X))
    return ((N * EXY) - (EX * EY)) / \
           ((N * EsqX) - (EX ** 2))


def LSMYint(XYdata:list) -> float:
    XY = pivotlist(XYdata)
    meanX = mean(XY[0])
    meanY = mean(XY[1])
    return meanY - LSMslope(XYdata) * meanX


def PearsonsR(XYdata: list) -> float:#first two values inlist must be [[x and y...]...]
    XY, N = pivotlist(XYdata), len(XYdata)
    X = XY[0]
    Y = XY[1]
    EX = sum(X)
    EY = sum(Y)
    EXY = sum(mulvect(X,Y))
    EsqX = sum(mulvect(X,X))
    EsqY = sum(mulvect(Y,Y))
    return ((N * EXY) - (EX * EY)) / \
        sqrt(abs(((N * EsqX) - (EX ** 2))) * \
            abs(((N * EsqY) - (EY ** 2))))


def Rsquare(XYdata: list) -> float:
    return PearsonsR(XYdata) ** 2


def TTest(XYdata: list) -> float:
    r = PearsonsR(XYdata)
    return r * sqrt((len(XYdata) - 2) / (1 - r ** 2))


def StdDev(v:list) -> float:
    vr=variance(v)
    return sqrt(sum(mulvect(vr, vr)) / len(v))


def slope(u:list,v:list) -> float:
    return (v[1] - u[1]) / \
           (v[0] - u[0])


def coefvar(v: list) -> float:
    return StdDev(v) /mean(v)


def vectiszero(v: list) -> bool:
    b = True
    for i in v:
        if i > 0:
            b = False
            break
    return b


def isorthogonal(u: list,
                 v: list) -> bool:
    return vectiszero(mulvect(u,v))


def crossprod3d(u: list,
                v: list) -> list:
    x = y = z= 0
    if len(u) == 3 and len(v) == 3:
        x = u[1] * v[2] - u[2] * v[1]
        y = u[2] * v[0] - u[0] * v[2]
        z = u[0] * v[1] - u[1] * v[0]
    return [x, y, z]


def getnormvec(
        p1: list[float, float, float],
        p2: list[float, float, float],
        p3: list[float, float, float]) -> list:
    """Gets the normal to a plane
        given 3 vertices (x, y, z) that
        define the surface in 3D space
        using a cross product between
        two vectors a and b:
        The normal vector is orthogonal
        to vectors a and b. (see below)

        a = (p2 - p1)
        b = (p3 - p1)
        n = (a x b) where x is crossprod
        n = ((p2 - p1) x (p3 - p1))
    """
    return crossprod3d(subvect(p2, p1),
                       subvect(p3, p1))


def dotprod(u: list, v: list) -> float:
    """Dot product is an algebraic
        operation that takes two
        equal-length sequences
        of numbers and returns
        a float it is the
        sum of the products
        of the corresponding
        entries of the two
        sequences of numbers

    Args:
        u, v : list of ints or floats

    Returns:
        float
    """
    return sum(mulvect(u, v))


def vmag(v: list) -> float:
    s = 0
    for i in v:
        s += i*i
    return sqrt(s)


def distance(u: list,
             v: list) -> float:
    return vmag(subvect(u,v))


def distancetable(vertlist: list) -> list:
    dlist=[]
    for v in vertlist:
        for u in vertlist:
            if u != v:
                dlist.append([vertlist.index(v),
                              vertlist.index(u),
                              distance(u,v)])
    return dlist


def countdist(distlist: list) -> dict:
    d = {}
    for i in distlist:
        dist = i[2]
        if dist not in d:
            d.setdefault(dist,1)
        else:
            d[dist] += 1
    return d


def det3D(a1: list,
          a2: list,
          a3: list) -> float:
    """Compute the Determinant
        of a 3D matrix

    Args:
        a1, a2, a3 : list of ints
                     or floats
                     [x, y, z]

    Returns:
        float
    """
    return a1[0] * a2[1] * a3[2] + \
           a1[1] * a2[2] * a3[0] + \
           a1[2] * a2[0] * a3[1] - \
           a1[0] * a2[2] * a3[1] - \
           a1[1] * a2[0] * a3[2] - \
           a1[2] * a2[1] * a2[0]


def cosaffin(u: list, v: list) -> float:
    """Compute Cosine Similarity
        or Cosine Affinity

    Args:
        u, v : list of ints or floats

    Returns:
        float
        proportional vectors = 1
        orthogonal vectors = 0
        opposite vectors = -1
        and values in between
    """

    return dotprod(u, v) / \
         (vmag(u) * vmag(v))


def dircos(v: list) -> list:
    mag = vmag(v)
    return [i / mag for i in v]


def diracos(dcos: list) -> list:
    return [acos(d) for d in dcos]


def dirdeg(raddir: list) -> list:
    return [degrees(d) for d in raddir]


def rect2sphericalcoord3D(
        v: list) -> list:
    p = vmag(v)
    azimuth = atan(v[1] / v[0])
    colatitude = acos(v[2] / p)
    return [p, azimuth, colatitude]


def spherical2rectcoord3D(
        vspherecoord3D: list) -> list:
    [p, theta, phi] = vspherecoord3D
    sinphi = sin(phi)
    return [p * sinphi * cos(theta),
            p * sinphi * sin(theta),
            p * cos(phi)]


def rect2cylindricalcoord3D(
        v: list) -> list:
    return [vmag(v),
            atan(v[1]/v[0]),
            v[2]]


def cylindrical2rectcoord3D(
        vcylindcoord3D: list) -> list:
    r = vcylindcoord3D[0]
    theta = vcylindcoord3D[1]
    return [r * cos(theta),
            r * sin(theta),
            vcylindcoord3D[2]]


def polar2rectcoord2D(
        vpolarcoord2D: list) -> list:
    r = vpolarcoord2D[0]
    theta = vpolarcoord2D[1]
    return [r * cos(theta),
            r * sin(theta)]


def rect2polarcoord2D(
        v: list) -> list:
    return [vmag(v),
            atan(v[1] / v[0])]


def polarcoordangle2D(
        v:list) -> float:
    a = acos(cosaffin(v, [0, -1]))
    if v[0] < 0:
        a = 2 * pi - a
    return a


def rect2polarcoord2Dwithcenter(
        vcen: list,
        vpnt: list) -> list:
    v=subvect(vpnt, vcen)
    return [vmag(v),
            polarcoordangle2D(v)]


def computerotvec(degrot:float) -> list:
    a = radians(degrot)
    return (sin(a), cos(a))


def rotvec2D(v: list,
        rotvec: list) -> list:
    return [v[0] * rotvec[1] - v[1] * rotvec[0],
            v[0] * rotvec[0] + v[1] * rotvec[1]]


def mirrorx(p: list, x: float) -> list:
    return [p[0] - x, p[1]], [p[0] + x, p[1]]


def mirrory(p:list, y:float) -> list:
    return [p[0], p[1] - y], [p[0], p[1] + y]


def mirrorvec(vcen: list,
                 v: list) -> list:
    return [subvect(vcen, v),
            addvect(vcen, v)]


def mirror(pt: float, delta: float):
    """Mirrors a value in a nunberline

    Args:
        pt   : real value in numberline
        delta: value to mirror

    Returns:
        pt - delta, pt + delta

    """
    return pt - delta, pt + delta


def randomvect(minrnd: int,
               maxrnd: int) -> list:
    return [randint(minrnd, maxrnd),
            randint(minrnd, maxrnd),
            randint(minrnd, maxrnd)]


def addrndtovert(vertlist: list,
                   minrnd: int,
                   maxrnd: int) -> list:
    return [addvect(pt, randomvect(minrnd, maxrnd))
                for pt in vertlist]


def adddimz(vlist2D: list,
              value: float) -> list:
    """Adds a third value for the
        z dimensiion in a list
        of (x, y) vertices

    Args:
        vlist2D: list of 2D vertices
                 [(x, y), ....]
        value  : constant z value

    Returns:
        list of 3D vertices
        [(x, y, z), ....]

    """
    return [[v[0], v[1], value]
              for v in vlist2D]


def anglebetween2Dlines(
        u: list, v: list) -> float:
    if u[0] != v[0]:
        a = atan(slope(u, v))
    else:
        a = iif(u[0] < v[0],
                    1.5707963267948966,
                    4.71238898038469)
    return a


def rotatebits(bits: int) -> int:
    """Rotates the bits in a byte

    Args:
        bits: the int 8 bits to rotate

    Returns:
        int value of rotated 8 bits

    """
    bit = 7
    retval = 0
    while bit>0:
        retval += \
            ((bits & (1 << bit)) >> bit) << (7 - bit)
        bit -= 1
    return retval


def mirror1stquad(x: int, y: int,
        v: list) -> list:

    xmin, xmax = mirror(x, v[0])
    ymin, ymax = mirror(y, v[1])
    return [[xmin, ymax],[xmax, ymax],
            [xmin, ymin],[xmax, ymin]]


def xorvect(u: list[int],
            v: list[int]) -> list[int]:
    """Applies a xor operation
        of between the elements of
        two lists of ints

    Args:
        v      : list[int]
        bitmask: int

    Returns:
        list[int]

    """
    return [i ^ j for i, j in zip(u, v)]


def andvect(u: list[int],
            v: list[int]) -> list[int]:
    """Applies a bitwise and operation
        of between the elements of
        two lists of ints

    Args:
        v      : list[int]
        bitmask: int

    Returns:
        list[int]

    """
    return [i & j for i, j in zip(u, v)]


def bitmaskvect(v: list,
        bitmask: int) -> list:
    """Applies a bitmask to a list
        of ints

    Args:
        v      : list[int]
        bitmask: int

    Returns:
        list[int]

    """
    return [b & bitmask for b in v ]


def orvect(u: list,
           v: list) -> list:
    return [i | j
            for i, j in zip(u, v)]

def gammacorrectbyte(
        lumbyte: list,
        gamma: float) -> int:
    return int(((lumbyte / 255) ** gamma) * 255)


def addvectinlist(vlist: list):
    return reduce(addvect,vlist)


def addvectpairlist(vpair: list):
    return addvect(vpair[0], vpair[1])


def addvecttripletlist(vtriplet: list):
    return addvect(
           addvect(vtriplet[0],
                   vtriplet[1]),
                   vtriplet[2])


def addvectlist(vlist1: list,
                vlist2: list) -> list:
    return [addvect(u, v)
            for u, v in zip(vlist1, vlist2)]


def mapfunctolist(
        func: Callable,
        vlist: list) -> list:
    return [func(v)
            for v in vlist]


def swapxy(v:list) -> list:
    """Swaps the first two values
        in a list

    Args:
        list[x, y]

    Returns:
        list[y, x]

    """
    return [v[1], v[0]]


def centerpoint(x1: int, y1: int,
                x2: int, y2: int):
    """Returns the centerpoint x, y
        in rectangular area
        defined by (x1, y1)
               and (x2, y2)

    Args:
        x1, y1 : defines the
        x2, y2   rectangular area

    Returns:
        x: int, y: int centerpoint

    """
    return ((x2 - x1) >> 1) + x1, ((y2 - y1) >> 1) + y1


def getdatalisttotal(dlist: list) -> float:
    """Returns the total of a
        list of ints or floats

    Args:
        dlist: list of ints or floats

    Returns:
        float or int

    """
    total = 0
    for d in dlist:
        total += d[0]
    return total


def genpiechartdata(dlist:list): #[[20,c['red']],[30,c['brightyellow']]...]
    sa,tot=0,getdatalisttotal(dlist)
    alist = []
    big = -1
    for d in dlist:
        p = d[0] / tot
        ea = sa + p * 360
        p *= 100
        alist.append([sa, ea, d[1], d[0], p])
        if p >= 50:
            big = dlist.index(d)
        sa = ea
    return alist, big


def enumbits(byteval: int):
    """Yields the 8 bits in a byte

    Args:
        byteval: int value
                 from 0 to 255

    Yields:
        Eight bits that is either
        int 0 or int 1

    """
    bit = 7
    while bit > -1:
        yield  ((byteval & (1<<bit))>>bit)
        bit -= 1


def delta(v: list):
    return (v[1] - v[0])


