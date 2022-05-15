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


def getcolorname2RGBdict() -> dict:#define colors here
    return {
       'black':0,
       'blue': RGB2int(0, 0, 192),
       'green': RGB2int(0, 192, 0),
       'cyan': RGB2int(64, 192, 192),
       'red': RGB2int(192, 0, 0),
       'magenta': RGB2int(192, 0, 192),
       'brown': RGB2int(128, 128, 0),
       'white': RGB2int(222, 222, 222),
       'silver': RGB2int(192, 192, 192),
       'gray': RGB2int(128, 128, 128),
       'lightblue': RGB2int(128, 128, 192),
       'lightgreen': RGB2int(128, 192, 128),
       'lightcyan': RGB2int(128, 192, 192),
       'lightred': RGB2int(192, 128, 128),
       'yellow': RGB2int(222, 222, 0),
       'orange': RGB2int(192, 128, 0),
       'lightgray':RGB2int(165, 165, 165),
       'brightwhite':RGB2int(255, 255, 255),
       'brightblue':RGB2int(0, 0, 255),
       'brightcyan':RGB2int(128, 255, 255),
       'brightgreen':RGB2int(0, 255, 0),
       'brightred':RGB2int(255, 0, 0),
       'brightmagenta': RGB2int(255, 0, 255),
       'brightyellow': RGB2int(255, 255, 0),
       'brightorange': RGB2int(255, 164, 0),
       'darkgray': RGB2int(92, 92, 92),
       'darkblue': RGB2int(0, 0, 92),
       'darkgreen':RGB2int(0, 92, 0),
       'darkred': RGB2int(92, 0, 0),
       'darkmagenta': RGB2int(92, 0, 92),
       'darkbrown': RGB2int(92, 92, 0),
       'gold': RGB2int(255, 215, 0),
       'orangered': RGB2int(255, 69, 0),
       'flesh': RGB2int(210, 169, 161),
       }


def getdefaultlumrange() -> dict:
    return {'maxdesc': [255, 0],
             'maxasc': [0, 255],
            'middesc': [192, 64],
            ' midasc': [64, 192],
          'upperdesc': [255, 128],
           'upperasc': [128, 255],
          'lowerdesc': [128, 0],
           'lowerasc': [0, 128]}


def isvalidcolorbit(bits:int) -> bool:
    return bits in bmpvalidcolorbits

def getdefaultbitpal(
        bits:int) -> list:
    return bmpstdpal[bits]

def colormix(lum: list,
      RGBfactors: list) -> int:
    return RGB2int(int(RGBfactors[0] * lum),
                   int(RGBfactors[1] * lum),
                   int(RGBfactors[2] * lum))

def int2RGB(i: int):
        return i >> 16, (i >> 8) & 0xff, i & 0xff

def int2RGBlist(i: int) -> list:
    return [i >> 16,
           (i >> 8) & 0xff,
            i & 0xff]

def RGBtoBGRarr(r: int,
                g: int,
                b: int) -> array:
    return array('B', [b, g, r])

def int2BGRarr(i: int) -> array:
    return array('B', [i & 0xff,
                      (i >> 8) & 0xff,
                       i >> 16])

def int2RGBarr(i: int) -> array:
    return array('B', [i >> 16,
                      (i >> 8) & 0xff,
                       i & 0xff])

def RGB2BGRarr(r: int,
               g: int,
               b: int) -> array:
    return array('B', [b, g, r])

def RGBfactors2RGB(
        RGBfactors: list,
        bytelum: list) -> list:
    return roundvect(scalarmulvect(
                RGBfactors,bytelum))

def RGB2int(r: int,
            g: int,
            b: int) -> int:
    return b + (g << 8) + (r << 16)


def getRGBfactors() -> dict:#used by functions that generate color gradients
    d={}
    colordict = getcolorname2RGBdict()
    for color in colordict:
        r, g, b = int2RGB(colordict[color])
        d.setdefault(color, [r / 255,
                             g / 255,
                             b / 255])
    return d


def matchRGBtodefault4bitpal(
        RGB:list) -> int:
       r = RGB[0] >> 6
       g = RGB[1] >> 6
       b = RGB[2] >> 6
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


def matchRGBtopal(
        RGB: list,
        pal: list) -> int:
       c = 0
       i = 0
       d = 442
       if RGB in pal:
           c = pal.index(RGB)
       else:
           for p in pal:
               if p != [0,0,0] and RGB != [0,0,0]:
                   newd = distance(RGB,p)
                   if newd < d:
                       c = i
                       d = newd
               i+=1
       return c


def RGBtoRGBfactorsandlum(
        RGB: list) -> list:
    lum = max(RGB)
    if lum == 0:
        lum = 1
    return [[RGB[0] / lum,
             RGB[1] / lum,
             RGB[2] / lum], lum]


def probplotRGBto1bit(
        rgb: list,
        brightness: int) -> int:
    return round(brightness * randint(0, sum(rgb)) / 768)


def probplotRGBto4bitpal(
        rgb: list) -> int:
    color = 0
    [r, g, b] = rgb
    if round(randint(0, r) / 256) == 1:
        color += 4
    if round(randint(0, g) / 256) == 1:
        color += 2
    if round(randint(0, b) / 256) == 1:
        color += 1
    r, g, b = r >> 6, g >> 6, b >> 6
    if r>1 or g>1 or b>1:
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


def gammacorrect(rgb: list,
               gamma: int) -> list:
    c = RGBtoRGBfactorsandlum(rgb)
    return setminmaxvec(RGBfactors2RGB(c[0],
            gammacorrectbyte(c[1], gamma)),
            0, 255)

def brightnessadjust(
        rgb: list,
        percentadj: float) -> list:
    c=RGBtoRGBfactorsandlum(rgb)
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
            rgb,rgbfactors),0,255)


def applymonochromefiltertoBGRbuf(
        buf: array):
       m = len(buf)
       buf[0: m - 2: 3]= \
       buf[1: m - 1: 3]= \
       buf[2: m: 3] = \
       array('B',[int((b + g + r)/3)
       for b,g,r in zip(buf[0: m - 2: 3],
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
        buf: array,
        gamma: float):
    j = len(buf)
    i = 0
    while i < j:
        b = buf[i: i + 3]
        lum = max(b)
        if lum == 0:
            lum = 1
        f = int(((lum / 255) ** gamma) * 255) / lum
        i1 = i + 1
        i2 = i + 2
        buf[i] = int(buf[i] * f) & 0xff
        buf[i1] = int(buf[i1] * f) & 0xff
        buf[i2] = int(buf[i2 ]* f) & 0xff
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


def invertbitsinbuffer(buf:array) -> array:
    return array('B', [b ^ 0xFF for b in buf])


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
        if f!=1:
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
    buf=[]
    for b, g, r in zip(bbuf, gbuf, rbuf):
        buf += [b, g, r]
    return array('B', buf)
