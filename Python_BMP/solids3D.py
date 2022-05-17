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
    sqrt,
    radians
    )

from .mathlib import(
    adddimz,
    addvect,
    computerotvec,
    cylindrical2rectcoord3D,
    distance,
    getnormvec,
    roundvect,
    spherical2rectcoord3D,
    subvect,
    trans
    )

from .primitives2D import(
    floatregpolygonvert,
    iterline,
    rectboundarycoords,
    regpolygonvert
    )

from .messages import sysmsg


def getshapesidedict() -> dict:
    return {"tetrahedra":((2, 1, 0),
                          (2, 3, 1),
                          (0, 3, 2),
                          (3, 0, 1)),
                  "cube":((1, 2, 3, 0),
                          (5, 6, 7, 4),
                          (0, 3, 6, 5),
                          (4, 7, 2, 1),
                          (4, 1, 0, 5),
                          (2, 7, 6, 3)),
             "hexahedra":((2, 3, 1),
                          (0, 3, 2),
                          (3, 0, 1),
                          (1, 4, 2),
                          (2, 4, 0),
                          (1, 0, 4)),
             "octahedra":((1, 2, 0),
                          (4, 1, 0),
                          (3, 4, 0),
                          (2, 3, 0),
                          (2, 1, 5),
                          (1, 4, 5),
                          (4, 3, 5),
                          (3, 2, 5))}


def tetrahedravert(x: float) -> list:
    """Returns a list
        of vertices
        for a tetraheron

    Args:
        x: lenght of a side

    Returns:
        list (x: float,
              y: float,
              z: float)

    """
    x_sqr = x * x
    halfx= x / 2
    return [[0, 0, 0],
            [halfx, sqrt(x_sqr / 2), 0],
            [x, 0, 0],
            [halfx, halfx, sqrt(3 / 8 * x_sqr)]]


def cubevert(x: float) -> list:
    """Returns a list
        of vertices
        for a cube

    Args:
        x: length of a side

    Returns:
        list (x: float,
              y: float,
              z: float)

    """
    return [[0, 0, 0],
            [0, x, 0],
            [x, x, 0],
            [x, 0, 0],
            [0, x, x],
            [0, 0, x],
            [x, 0, x],
            [x, x, x]]


def hexahedravert(x: float) -> list:
    """Returns a list
        of vertices
        for a hexahedron

    Args:
        x: length of a side

    Returns:
        list (x: float,
              y: float,
              z: float)

    """
    x_sqr = x * x
    halfx= x / 2
    z = sqrt(3 / 8 * x_sqr)
    return [[0, 0, 0],
            [halfx, sqrt(x_sqr / 2), 0],
            [x, 0, 0],
            [halfx, halfx, z],
            [halfx, halfx, -z]]


def octahedravert(x:float) -> list:
    """Returns a list
        of vertices
        for an octrahedron

    Args:
        x: length of a side

    Returns:
        list (x: float,
              y: float,
              z: float)

    """
    halfx = x / 2
    return [[halfx, halfx, halfx],
            [0, 0, 0],
            [x, 0, 0],
            [x, x, 0],
            [0, x, 0],
            [halfx, halfx, -halfx]]


def decahedvertandsurface(
        x: float) -> list:
    """Returns a list
        of vertices
        for a icosahedron

    Args:
        x: min radius of sphere
           that can hold
           the decahedron

    Returns:
        list (x: float,
              y: float,
              z: float)

    """
    pts = regpolygonvert(
            0, 0, x, 5, 0)
    z = sqrt(distance(pts[0],
             pts[1]) ** 2 - x * x)
    return [[[0, 0, -z]] + \
            adddimz(pts, 0) + \
            [[0, 0, z]],
            ((1, 2, 0),
             (5, 1, 0),
             (3, 4, 0),
             (2, 3, 0),
             (4, 5, 0),
             (2, 1, 6),
             (1, 5, 6),
             (4, 3, 6),
             (3, 2, 6),
             (5, 4, 6))]


#don't edit this it took much
# computation to make
def icosahedvertandsurface(
        x: float) -> list:
    """Returns a list
        of vertices
        for an icosahedron

    Args:
        x: min radius of sphere
           that can hold
           the icosahedron

    Returns:
        list (x: float,
              y: float,
              z: float)

    """
    pts = floatregpolygonvert(
                0, 0, x, 5, 0)
    pts1 = floatregpolygonvert(
                0, 0, x, 5, 36)
    z = sqrt(distance(pts[0],
               pts[1]) ** 2 - x * x)
    z1 = 2 * x - z
    return [[[0, 0, -z]] + \
             adddimz(pts, 0) + \
             adddimz(pts1, z1 - z) + \
            [[0, 0, z1]],
           ((1, 2, 0),
            (5, 1, 0),
            (3, 4, 0),
            (2, 3, 0),
            (4, 5, 0),
            (2, 1, 6),
            (1, 5, 10),
            (4, 3, 8),
            (3, 2, 7),
            (5, 4, 9),
            (6, 7, 2),
            (7, 8, 3),
            (8, 9, 4),
            (9, 10, 5),
            (10, 6, 1),
            (7, 6, 11),
            (9, 8, 11),
            (8, 7, 11),
            (10, 9, 11),
            (6, 10, 11))]


def rotvec3D(
        roll: float,
        pitch: float,
        yaw: float) -> tuple:
    """Returns a tuple
        of rotation vector

    Args:
        All input arguements
        are in degrees
        roll, pitch, yaw

    Returns:
        tuple ((float,float),
               (float,float),
               (float,float))

    """
    return (computerotvec(roll),
            computerotvec(pitch),
            computerotvec(yaw))


#translated from C code by Roger Stevens
def perspective(
        vlist: list,
        rotvec: list,
        dispvec: list,
        d: float) -> tuple:
    rotvlist = []
    projvlist = []
    [sroll, croll] = rotvec[0]
    [spitch, cpitch] = rotvec[1]
    [syaw, cyaw] = rotvec[2]
    for p in vlist:
        [px, py, pz] = p
        x1 = -cyaw * px - syaw * pz
        y1 = croll * py - sroll * x1
        z1 = -syaw * px + cyaw * pz
        x = croll * x1 + sroll * py
        y = spitch * z1 + cpitch * y1
        z= cpitch * z1 - spitch * y1
        x += dispvec[0]
        y += dispvec[1]
        z += dispvec[2]
        rotvlist.append([x, y, z])
        projvlist.append([-d * x / z,
                          -d * y / z])
    return (rotvlist, projvlist)


#may be slow if polygon goes offscreen
def fillpolydata(
        polybnd: list,
        xlim: int,
        ylim: int) -> list:
    filld = {}
    bnd= rectboundarycoords(polybnd)
    [minx, miny] = bnd[0]
    [maxx, maxy] = bnd[1]
    maxx += 1
    maxy += 1
    if (minx >= 0 and miny >= 0) and \
       (maxx <= xlim and maxy <= ylim):
        for y in range(miny, maxy):
            filld.setdefault(y, [])
            for x in range(minx, maxx):
                if [x, y] in polybnd:
                    filld[y] += [x]
    else:
        print(bnd)
        print(sysmsg['regionoutofbounds'])
        filld = []
    return filld


def polyboundary(
        vertlist: list) -> list:
    px = []
    vertcount = len(vertlist)
    for i in range(0, vertcount):
        if i>0:
            v1 = roundvect(
                    vertlist[i - 1])
            v2 = roundvect(vertlist[i])
            for p in iterline(v1, v2):
                if p not in px:
                    px.append(p)
    v2 = roundvect(vertlist[0])
    v1 = roundvect(
            vertlist[vertcount - 1])
    for p in iterline(v1, v2):
        if p not in px:
            px.append(p)
    return px


def gensides(
        pointlists: list,
        transvect: list,
        sides: list) -> tuple:
    [plist, slist] = pointlists
    polylist = []
    normlist = []
    for sidepts in sides:
        u = plist[sidepts[0]]
        v = plist[sidepts[1]]
        w = plist[sidepts[2]]
        if surfacetest(u, v, w) <= 0:
            polylist.append(
                trans(
                    [slist[i]
                     for i in sidepts], transvect))
            normlist.append(getnormvec(u, v, w))
    return (polylist, normlist)


def spherevert(
        vcen: list,
        r: float,
        deganglestep: float) -> list:
    """Returns a list
        of sparse vertices
        for a sphere

    Args:
        vcen       : [x: float, center
                      y: float, of the
                      z: float] sphere
        r           : spherical radius
        deganglestep: angle step between
                      vertices that
                      controls how sparse
                      the list will be
        
    Returns:
        list (x: float,
              y: float,
              z: float)

    """

    plist = []
    for theta in range(0, 360, deganglestep):
        for phi in range(0, 180, deganglestep):
            p = addvect(vcen,
                   spherical2rectcoord3D(
                       [r, radians(theta),
                           radians(phi)]))
            if p not in plist:
                plist.append(p)
    p = [0, 0, -r]
    if p not in plist:
        plist.append(p)
    return plist


#we have a 3D object and we take z slices
def zlevelcoords(verlist: list) -> tuple:
    zlist = []
    zord = {}
    for p in verlist:
        pind = [verlist.index(p)]
        z = p[2]
        if z not in zord:
            zord.setdefault(z, pind)
            zlist.append(z)
        else:
            zord[z] += pind
    return (zlist, zord)


def genspheresurfaces(
        zlevelcoord:list) -> list:
    [zl, vl] = zlevelcoord
    surf = []
    levels = len(zl) - 1
    northpole = vl[zl[0]][0]
    southpole = vl[zl[levels]][0]
    npts = vl[zl[1]]
    spts = vl[zl[levels - 1]]
    lpts = len(npts)
    maxp = lpts-1
    i = 0
    for i in range(0, lpts):
        j = 0 if i == maxp else i + 1
        surf += [[northpole, npts[j], npts[i]],
                 [southpole, spts[i], spts[j]]]
    if levels > 2:
        mxlv = levels - 1
        for k in range(1, mxlv):
            pts = vl[zl[k]]
            adjpts = vl[zl[k + 1]]
            lpts = len(pts)
            maxadjpts = len(adjpts)
            maxp = lpts - 1
            i = 0
            for i in range(0, lpts):
                j = 0 if i == maxp else i + 1
                surf += [[adjpts[j % maxadjpts],
                          adjpts[i % maxadjpts],
                          pts[i],
                          pts[j]]]
    return surf


def spherevertandsurface(
        vcen: list,
        r: float,
        deganglestep: float)-> tuple:
    s = spherevert(vcen, r, deganglestep)
    return (s, genspheresurfaces(zlevelcoords(s)))


def cylindervertandsurface(
        vcen: list,
        r: float,
        zlen: float,
        deganglestep: float) -> tuple:
    z = zlen / 2
    i =0
    plist = []
    top = []
    bottom = []
    side = []
    maxang = 360 + (deganglestep << 1)
    for theta in range(0, maxang, deganglestep):
        plist.append(addvect(vcen,
            cylindrical2rectcoord3D([r,
                        radians(theta), -z])))
        plist.append(addvect(vcen,
            cylindrical2rectcoord3D([r,
                        radians(theta), z])))
        top.append(i)
        bottom.append(i + 1)
        if i > 2:
            j = i - 2
            side.append([i, i + 1, j + 1, j])
        i += 2
    top.reverse()
    return (plist, [top] + side + [bottom])

def conevertandsurface(
        vcen: list,
        r: float,
        zlen: float,
        deganglestep: float) -> tuple:
    z = zlen / 2
    i = 1
    bottom = []
    side = []
    maxang = 360 + (deganglestep << 1)
    plist = [subvect(vcen, [0, 0, z])]
    for theta in range(0, maxang, deganglestep):
        plist.append(addvect(vcen,
                cylindrical2rectcoord3D(
                    [r, radians(theta), z])))
        bottom.append(i)
        if i > 2:
            side.append([0, i, i - 1])
        i += 1
    return (plist, side + [bottom])

def surfplot3Dvertandsurface(
        x1: int,
        y1: int,
        x2: int,
        y2: int,
        zscale: float,
        step: int) -> tuple:
    vlist = []
    surf = []
    for y in range(y1, y2, step):
        for x in range(x1, x2, step):
            z = x & y
            vlist.append([x, y ,z])
    dx = abs(x2 - x1) // step
    dx1 = dx - 1
    vl = len(vlist)
    for v in vlist:
        i=vlist.index(v)
        idx = i + dx
        idx1 = idx + 1
        if (vl - idx1) >= 0 and (i % dx) < dx1:
             surf.append([idx, idx1, i + 1, i])
    return (vlist, surf)


def surfacetest(
        p1: list,
        p2: list,
        p3: list) -> float:
    return p1[0] * (p3[1] * p2[2] - p2[1] * p3[2]) - \
           p2[0] * (p3[1] * p1[2] - p1[1] * p3[2]) - \
           p3[0] * (p1[1] * p2[2] - p2[1] * p1[2])
