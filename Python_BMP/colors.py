"""
  Color manipulation numerics module
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

from random import randint
from array import array
from .conditionaltools import iif
from .bmppal import(
    bmpstdpal,
    bmpvalidcolorbits
    )

from .mathlib import(
    addvect,
    distance,
    intscalarmulvect,
    intsetminmaxvec,
    mean,
    mulvect,
    roundvect,
    scalarmulvect,
    setminmax,
    setminmaxvec,
    subvect,
    )


def getdefaultlumrange() -> dict:
    return {'maxdesc': [255, 0],
             'maxasc': [0, 255],
            'middesc': [192, 64],
            ' midasc': [64, 192],
          'upperdesc': [255, 128],
           'upperasc': [128, 255],
          'lowerdesc': [128, 0],
           'lowerasc': [0, 128]}


def isvalidcolorbit(bits: int) -> bool:
    """Checks if bits is in the valid
        color bits list (1, 4, 8, 24)

    Args:
        bits: int value

    Returns:
        True if bits in (1, 4, 8, 24)
        False if other values not in
              the list above
    """
    return bits in bmpvalidcolorbits


def getdefaultbitpal(
        bits: int) -> list:
    """Gets the standard bitmap palette
        for a  specified bit depth bits

    Args:
        bits: int value (1, 4, 8, 24)

    Returns:
        list of palette entries
    """
    return bmpstdpal[bits]


def colormix(lum: int,
      RGBfactors: list[float, float, float]
             ) -> int:
    """Mix a byte luminosity value to
        an rgb triplet that express
        a color value in [r, g, b]
        ratios from 0.0 to 1.0 to
        obtain an int value for a
        specific color

    Args:
        lum       : a byte value for
                    luminosity
        RGBfactors: list[r: float,
                         g: float,
                         b: float]
                    float values from
                    0.0 to 1.0

    Returns:
        int color val
    """
    return RGB2int(int(RGBfactors[0] * lum),
                   int(RGBfactors[1] * lum),
                   int(RGBfactors[2] * lum))


def int2RGB(i: int):
    """Break down int color i to its
        byte valued r, g and b
        components

    Args:
        i: int color value

    Returns:
        r: byte, g: byte, b: byte
    """
    return i >> 16, (i >> 8) & 0xff, i & 0xff


def int2RGBlist(i: int
         ) -> list[int, int, int]:
    """Break down int color i to its
        byte valued r, g and b
        components in a list

    Args:
        i: int color value

    Returns:
        [r: byte, g: byte, b: byte]
    """
    return [i >> 16, (i >> 8) & 0xff,
                            i & 0xff]


def int2BGRarr(i: int) -> array:
    """Returns a bgr array from
        int i color input

    Args:
        i: color value

    Returns:
        unsigned byte BGR array
    """
    return array('B', [i & 0xff,
                      (i >> 8) & 0xff,
                       i >> 16])


def int2RGBarr(i: int) -> array:
    """Returns a rgb array from
        int i color input


    Args:
        i: color value

    Returns:
        unsigned byte RGB array
    """
    return array('B', [i >> 16,
                      (i >> 8) & 0xff,
                       i & 0xff])

def RGB2BGRarr(r: int,
               g: int,
               b: int) -> array:
    """Returns a bgr array from
        individual r, g and b color
        component inputs

    Args:
        r, g, b: byte color values

    Returns:
        unsigned byte BGR array
    """
    return array('B', [b, g, r])


def RGBfactors2RGB(
        RGBfactors: list[float,
                         float,
                         float],
        bytelum: int
               ) -> list[int,
                         int,
                         int]:
    """Mix a byte luminosity value to
        an rgb triplet that express
        a color value in [r, g, b]
        ratios from 0.0 to 1.0 to
        obtain byte r, g, b values
        stored in a list [r, g, b]


    Args:
        lum       : a byte value for
                    luminosity
        RGBfactors: list[r: float,
                         g: float,
                         b: float]
                    float values from
                    0.0 to 1.0

    Returns:
        [r: byte, g: byte, b: byte]
    """
    return roundvect(scalarmulvect(
                RGBfactors, bytelum))


def RGB2int(r: int, g: int, b: int
                          ) -> int:
    """Pack byte r, g and b color value
        components to an int
        representation for a
        specific color

    Args:
        r, g, b: color byte values

    Returns:
        int color val
    """
    return b + (g << 8) + (r << 16)


def matchRGBtodefault4bitpal(
        RGB: list[int, int, int]
             ) -> int:
    """Deterministic color matching
        from a 24-bit palette to a
        the default 4-bit palette
        using formulas

    Args:
        RGB: color byte values
             [r: byte,
              g: byte,
              b: byte]

    Returns:
        int color val (4-bit)
    """
    (r, g, b) = RGB
    r >>= 6
    g >>= 6
    b >>= 6
    color = 0
    if r > 1 or g > 1 or b > 1:
        color = 8
    if r >= 1:
        color += 4
    if g >= 1:
        color += 2
    if b >= 1:
        color += 1
    return color


def matchRGBtopal(RGB: list,
                  pal: list) -> int:
    """Color matching from a 24-bit
        palette to any 1, 4 or 8-bit
        palette using Euclidean
        distance minimization
        in an rgb colorspace for
        the closest color match

    Args:
        RGB: color byte values
             [r: byte,
              g: byte,
              b: byte]
        pal: the bmp palette to match

    Returns:
        int color val (4-bit)
    """
    c = i = 0
    d = 442
    if RGB in pal:
        c = pal.index(RGB)
    else:
        for p in pal:
            if p != [0,0,0] and RGB != [0,0,0]:
                newd = distance(RGB, p)
                if newd < d:
                    c = i
                    d = newd
            i += 1
    return c


def RGBtoRGBfactorsandlum(
        rgb: list[int, int, int]
        ) -> list[list[float, float,
                       float], int]:
    """Separates luminosity from
        color and express color
        as ratios of r, g and b
        float values from 0.0 to 1.0


    Args:
        rgb: color byte values
             [r: byte,
              b: byte,
              g: byte]

    Returns:
        list[list[r: float,
                  g: float,
                  b: float], lum: byte]
    """
    lum = max(rgb)
    if lum == 0:
        lum = 1
    return [[rgb[0] / lum,
             rgb[1] / lum,
             rgb[2] / lum], lum]


def probplotRGBto1bit(
        rgb: list[int, int, int],
        brightness: int) -> int:
    """Use a non deterministic plot
        to convert 24-bit colors to
        1-bit

    Args:
        rgb: color byte values
             [r: byte,
              b: byte,
              g: byte]

    Returns:
        0 or 1
    """
    return round(brightness * randint(0, sum(rgb)) / 768)


def probplotRGBto4bitpal(
        rgb: list[int, int, int]
                       ) -> int:
    """Use a non deterministic plot
        to convert 24-bit colors to
        4-bits

    Args:
        rgb: color byte values
             [r: byte,
              b: byte,
              g: byte]

    Returns:
        4 bit int value
    """
    color = 0
    (r, g, b) = rgb
    if round(randint(0, r) / 256) == 1:
        color += 4
    if round(randint(0, g) / 256) == 1:
        color += 2
    if round(randint(0, b) / 256) == 1:
        color += 1
    r >>= 6
    g >>= 6
    b >>= 6
    if r > 1 or g > 1 or b > 1:
        color += 8
    return color


def monochromepal(
        bits: int,
        RGBfactors: list) -> list:
    inc = (256 >> bits) + \
        iif(bits == 4, 1,
        iif(bits == 1, 127, 0))
    return [[round(RGBfactors[0] * c),
             round(RGBfactors[1] * c),
             round(RGBfactors[2] * c)]
             for c in range(0, 256, inc)]


def monochrome(
        rgb: list) -> list:
    return [round(mean(rgb))] * 3


def gammacorrectbyte(
        lumbyte: list,
        gamma: float) -> int:
    return int(((lumbyte / 255) ** gamma) * 255)


def gammacorrect(rgb: list,
               gamma: int) -> list:
    c = RGBtoRGBfactorsandlum(rgb)
    return setminmaxvec(RGBfactors2RGB(c[0],
            gammacorrectbyte(c[1], gamma)),
            0, 255)


def brightnessadjust(
        rgb: list,
        percentadj: float) -> list:
    c = RGBtoRGBfactorsandlum(rgb)
    return setminmaxvec(RGBfactors2RGB(c[0],
     c[1] + c[1] * (percentadj / 100)),
     0, 255)


def thresholdadjust(
        rgb: list,
        lumrange: list) -> list:
    c = RGBtoRGBfactorsandlum(rgb)
    lumrange = intsetminmaxvec(lumrange, 0, 255)
    if  lumrange[0] > lumrange[1]:
        lumrange[1],  lumrange[0] = \
        lumrange[0],  lumrange[1]
    return RGBfactors2RGB(c[0],
                setminmax(c[1],lumrange[0],
                               lumrange[1]))


def colorfilter(
        rgb: list,
        rgbfactors: list) -> list:
    return intsetminmaxvec(mulvect(
            rgb,rgbfactors), 0, 255)


def applymonochromefiltertoBGRbuf(
        buf: array):
       m = len(buf)
       buf[0: m - 2: 3] = \
       buf[1: m - 1: 3] = \
       buf[2: m: 3] = \
       array('B',[int((b + g + r) / 3)
       for b, g, r in zip(buf[0: m - 2: 3],
                          buf[1: m - 1: 3],
                          buf[2: m: 3])])


def monochromefiltertoBGRbuf(
        buf:array) -> array:
       applymonochromefiltertoBGRbuf(buf)
       return buf


def applycolorfiltertoBGRbuf(
        buf: array,
        rgbfactors: list):
    m = len(buf) - 1
    buf[0: m - 2: 3], buf[1: m - 1: 3], buf[2: m: 3] = \
        array('B', intscalarmulvect(buf[0: m - 2: 3], rgbfactors[2])), \
        array('B', intscalarmulvect(buf[1: m - 1: 3], rgbfactors[1])), \
        array('B', intscalarmulvect(buf[2: m: 3], rgbfactors[0]))


def colorfiltertoBGRbuf(
        buf: array,
        rgbfactors: list) -> array:
    applycolorfiltertoBGRbuf(buf,rgbfactors)
    return buf


def applygammaBGRbuf(
        buf: array, gamma: float):
    imax = len(buf)
    i = 0
    while i < imax:
        lum = max(buf[i: i + 3])
        if lum == 0:
            lum = 1
        f = int(((lum / 255) ** gamma) * 255) / \
                  lum
        j = i + 1
        k = i + 2
        buf[i] = int(buf[i] * f) & 0xff
        buf[j] = int(buf[j] * f) & 0xff
        buf[k] = int(buf[k] * f) & 0xff
        i += 3


def gammaBGRbuf(
        buf: array,
        gamma: float) -> array:
    applygammaBGRbuf(buf,gamma)
    return buf


def gammacorrectbyte(
        lumbyte: int,
        gamma: float) -> int:
    return int(((lumbyte / 255) ** gamma) * 255)


def RGBfactorstoBaseandRange(
        lumrange: list,
        RGBfactors: list):
    baselum = scalarmulvect(RGBfactors,lumrange[0])
    lumrange = subvect(scalarmulvect(
                    RGBfactors,lumrange[1]),
                    baselum)
    return baselum, lumrange


def invertbitsinbuffer(buf: array
                       ) -> array:
    return array('B', [b ^ 0xFF
                   for b in buf])


def applybrightnessadjtoBGRbuf(
        buf: array,
        percentadj: float) -> array:
    return array('B',setminmaxvec(addvect(buf,
            intscalarmulvect(buf, percentadj / 100)), 0, 255))


def applythresholdadjtoBGRbuf(
        buf: array,
        lumrange: list) -> array:
    lummin = lumrange[0] & 0xff
    lummax = lumrange[1] & 0xff
    m = len(buf)
    i = 0
    while i < m:
        lum = max(buf[i:i+3])
        f = 1
        if lummin > lummax:
            lummin, lummax = lummax, lummin
        if lum > 0:
            if lum < lummin:
                f = lummin / lum
            if lum > lummax:
                f = lummax / lum
        if f != 1:
            buf[i] = int(f * buf[i])
            buf[i + 1] = int(f * buf[i + 1])
            buf[i + 2] = int(f * buf[i + 2])
        i += 3
    return buf


def RGB2BGRbuf(buf: array):
    m = len(buf)
    buf[0: m - 2: 3], buf[2: m: 3] = \
    buf[2: m: 3], buf[0: m - 2: 3]


def makeBGRbuf(
        bbuf: array,
        gbuf: array,
        rbuf: array) -> array:
    buf = []
    for b, g, r in zip(bbuf, gbuf, rbuf):
        buf += [b, g, r]
    return array('B', buf)
