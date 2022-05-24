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


from ast import Num
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

from numbers import Number
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


def roundvect(v: list[Number]
            ) -> list[int]:
    """Rounds off the components of a
        vector
       (list of floats -> list of ints)

    Args:
        v: list of floats

    Returns:
        list of ints
    """
    return [round(n) for n in v]


def roundvectlist(
        vlist: list[list[Number]]
          ) -> list[list[int]]:
    """Rounds the components of a vector
        in a list within a list
        lists of (list of floats) ->
        lista of (list of ints)

    Args:
        vlist: list[list[floats]

    Returns:
        list[list[ints]
    """
    return [roundvect(v) for v in vlist]


def addvect(u: list[Number],
            v: list[Number]
          ) -> list[Number]:
    """Add vectors u and v by
        adding their components

    Args:
        u, v: list of ints or floats

    Returns:
        list of ints or floats
    """
    return [i + j for i, j in zip(u, v)]


def trans(vlist: list[Number],
              u: list[Number]
            ) -> list[Number]:
    return [addvect(v, u) for v in vlist]


def subvect(u: list[Number],
            v: list[Number]
          ) -> list[Number]:
    """Subtracts vectors u and v by
        subtracting their components

    Args:
        u, v: list of ints or floats

    Returns:
        list of ints or floats
    """
    return [i - j
            for i, j in zip(u, v)]


def mulvect(u: list[Number],
            v: list[Number]
          ) -> list[Number]:
    """Gets the inner product of
        vector u and vector v

    Args:
        u, v: list of ints or floats

    Returns:
        list of ints or floats
    """
    return [i * j for i, j in zip(u, v)]


def divvect(u: list[Number],
            v: list[Number]
          ) -> list[float]:
    return [i / j for i, j in zip(u, v)]


def scalarmulvect(
            v: list[Number],
         scalarval: Number
          ) -> list[Number]:
    """Scales a vector by multiplying
        a scalar value (float) to all
        components of the vector or a
        list of numbers in pure Python

    Args:
        v        : the vector or
                   a list of
                   ints or floats
        scalarval: scalar value
                   (float or int)

    Returns:
        list of ints or floats
    """
    return [s * scalarval for s in v]


def intscalarmulvect(vec: list[Number],
                    scalarval: Number
                    ) -> list[int]:
    """Scales a vector by multiplying
        a scalar value (float) to all
        components of the vector or a
        list of numbers in pure Python
        then rounds off values in the
        list to a whole number

    Args:
        v        : the vector or
                   a list of
                   ints or floats
        scalarval: scalar value
                   (float or int)

    Returns:
        list of ints
    """
    return [round(s * scalarval)
            for s in vec]


def mean(v: list[Number]) -> float:
    """Gets the average of a list
        of numbers

    Args:
        v: the vector or a list of
           ints or floats

    Returns:
        float
    """
    return sum(v) / len(v)


def meanlist(
      vlist: list[list[float]]
        ) -> list[float]:
    """Gets the averages of a list
        of list of numbers

    Args:
        vlist: the vector or a list
               of ints or floats

    Returns:
        list[float, ...]
    """
    return [mean(v) for v in vlist]


def pivotlist(
        vlist:list[list[any]]
         ) -> list[list[any]]:
    j = len(vlist[0])
    """Does a pivot table with a list
        of list of anything

    Args:
        vlist: a list of lists

    Returns:
        list of lists
    """
    return [[v[i] for v in vlist]
            for i in range(0, j)]


def variance(v: list[Number]
           ) -> list[float]:
    """Computes the variance
        of the elements in
        a list of numbers

    Args:
        vlist: a list of
               ints or floats


    Returns:
        list of floats
    """
    ave = mean(v)
    return [n - ave for n in v]


def isinrange(value: float,
          highlimit: float,
           lowlimit: float) -> bool:
    return (value > lowlimit) and \
           (value < highlimit)


def setmax(val: Number,
        maxval: Number) -> Number:
    """Set the value of val
        to maxval if val > maxval

    Args:
        val   : numeric variable
        maxval: upper limit of variable

    Returns:
        Number
    """
    return maxval if val > maxval else val


def setmin(val: Number,
        minval: Number) -> Number:
    """Set the value of val
        to minval if val < minval

    Args:
        val   : numeric variable
        minval: lower limit of variable

    Returns:
        Number
    """
    return minval if val < minval else val


def setminmax(val: Number,
           minval: Number,
           maxval: Number) -> Number:
    """Set the value of val
        to minval if val < minval
        or the value of val
        to maxval if val > maxval

    Args:
        val   : numeric variable
        minval: lower limit of variable
        maxval: upper limit of variable

    Returns:
        Number
    """
    if val > maxval:
        val = maxval
    if val < minval:
        val = minval
    return val


def intsetminmax(val: Number,
              minval: int,
              maxval: int) -> int:
    """Set the value of val
        to minval if val < minval
        or the value of val
        to maxval if val > maxval
        and return an int

    Args:
        val   : numeric variable
        minval: lower limit of variable
        maxval: upper limit of variable

    Returns:
        int
    """
    val = round(val)
    if val > maxval:
        val = maxval
    if val < minval:
        val = minval
    return val


def sign(intval: int) -> int:
    """Returns an int depending
        on the sign of intval
    Args:
        intval   : an int

    Returns:
        Postive value ->  1
        zero          ->  0
        Negative value-> -1
    """
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
    XY = pivotlist(XYdata)
    N = len(XYdata)
    X = XY[0]
    Y = XY[1]
    EX = sum(X)
    EY = sum(Y)
    EXY = sum(mulvect(X, Y))
    EsqX = sum(mulvect(X, X))
    EsqY = sum(mulvect(Y, Y))
    return ((N * EXY) - (EX * EY)) / \
        sqrt(abs(((N * EsqX) - (EX ** 2))) * \
            abs(((N * EsqY) - (EY ** 2))))


def Rsquare(XYdata: list) -> float:
    return PearsonsR(XYdata) ** 2


def TTest(XYdata: list) -> float:
    r = PearsonsR(XYdata)
    return r * sqrt((len(XYdata) - 2) / (1 - r ** 2))


def StdDev(v: list) -> float:
    vr = variance(v)
    return sqrt(sum(mulvect(vr, vr)) / len(v))


def slope(u: list[float, float],
          v: list[float, float]) -> float:

    return (v[1] - u[1]) / \
           (v[0] - u[0])


def coefvar(v: list[Number]) -> float:
    """Coefficient of variation (CV)
        is a statistical measure of
        the relative dispersion of
        data points in a data series
        around the mean.

        It is also known as (RSD) or
        relative standard deviation
        and is defined as the ratio
        of the standard deviation
        to the mean

    Args:
        v: list of ints or floats

    Returns:
        float

    """
    return StdDev(v) / mean(v)


def vectiszero(v: list[Number]) -> bool:
    """Checks if a vector is all zero

    Args:
        v: list of ints or floats

    Returns:
        True  :if list is all zero
        False :if there is any non zero
               in the list
    """
    return all(u == 0 for u in v)


def isorthogonal(
        u: list[Number],
        v: list[Number]) -> bool:
    """Checks if vector u and vector v
        are orthogonal to each other

    Args:
        u, v: list of ints or floats

    Returns:
        True  : vectors are orthogonal
                since the inner product
                of u and v is a
                zero vector or a
                null vector that
                has a zero magnitude
                and no direction

        False : inner product of
                u and v is a
                non zero vector
                so they are
                nonorthogonal vectors
    """
    return vectiszero(mulvect(u, v))


def crossprod3d(
        u: list[float, float, float],
        v: list[float, float, float]
      ) -> list[float, float, float]:
    """Compute the cross product of
        3D vectors u and v.

        The cross product is
        perpendicular to both
        u and v

    Args:
        u, v: list of ints
              or floats
              [x, y, z]

    Returns:
        [x, y, z] : after u x v
                    where x is
                    crossprod
    """
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


def dotprod(u: list[Number],
            v: list[Number]) -> float:
    """Dot product is an algebraic
        operation that takes two
        equal-length sequences of
        numbers and returns a float.

        It is the sum of the products
        of the corresponding entries
        of the two sequences of numbers

    Args:
        u, v : list of ints or floats

    Returns:
        float
    """
    return sum(mulvect(u, v))


def vmag(v: list[float]) -> float:
    """Compute the Magnitude or length
        of a vector v of arbitrary
        dimension n equal to len(v)

    Args:
        v: list of ints or floats

    Returns:
        float
    """
    s = 0
    for i in v:
        s += i * i
    return sqrt(s)


def distance(u: list[float],
             v: list[float]) -> float:
    """Compute the Distance or length
        of a vector v of arbitrary
        dimension n in a n-dimensional
        Euclidean space where u and v
        are both vectors with
        n components

    Args:
        u, v: list of ints or floats

    Returns:
        float
    """
    return vmag(subvect(u, v))


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


def cosaffin(u: list[Number],
             v: list[Number]) -> float:
    """Compute Cosine Similarity
        or Cosine Affinity

    Args:
        u, v : list of ints or floats

    Returns:
        float value
            proportional vectors = 1
            orthogonal vectors = 0
            opposite vectors = -1
            and values in between
    """
    return dotprod(u, v) / \
         (vmag(u) * vmag(v))


def dircos(v: list[Number]
         ) -> list[float]:
    """Direction cosine of the vector
        computed by dividing the
        corresponding coordinate
        of a vector by the
        vector length.

        The unit vector
        coordinate is equal to the
        direction cosine. One such
        property of the direction
        cosine is that the addition
        of the squares of the
        direction cosines is
        equivalent to one

    Args:
        v : list of ints or floats
            (vector components)

    Returns:
        Direction Cosine list
        list[float,...]

    """
    mag = vmag(v)
    return [i / mag for i in v]


def diracos(dcos: list[float]
              )-> list[float]:
    """Takes the Direction cosine
        of the vector and returns
        a list of angles in radians

    Args:
        v : Direction Cosine
            list[float]

    Returns:
        list of angles in radians
        per vector component
        list[float,...]

    """
    return [acos(d) for d in dcos]


def dirdeg(raddir: list[float]
              ) -> list[float]:
    """Takes the Directional angles
        of the vector in radians
        and returns a list of
        angles in degrees

    Args:
        v : list of angles
            per vector component
            in radians

    Returns:
        list of angles in degrees
        per vector component
        list[float,...]

    """
    return [degrees(d) for d in raddir]


def rect2sphericalcoord3D(
        v: list[Number]
      ) -> list[float, float, float]:
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
            atan(v[1] / v[0]),
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
        v: list[int, int]) -> list[list[int, int]]:

    xmin, xmax = mirror(x, v[0])
    ymin, ymax = mirror(y, v[1])
    return [[xmin, ymax], [xmax, ymax],
            [xmin, ymin], [xmax, ymin]]


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


def bitmaskvect(v: list[int],
        bitmask: int) -> list[int]:
    """Applies a bitmask to a list
        of ints

    Args:
        v      : list[int]
        bitmask: int

    Returns:
        list[int]

    """
    return [b & bitmask for b in v ]


def orvect(u: list[int],
           v: list[int]) -> list[int]:
    """Applies a bitwise or operation
        of between the elements of
        two lists of ints

    Args:
        v      : list[int]
        bitmask: int

    Returns:
        list[int]

    """
    return [i | j for i, j in zip(u, v)]


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
    sa = 0
    tot = getdatalisttotal(dlist)
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


