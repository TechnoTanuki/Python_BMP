# Python BMP Public API

**def addvect(u: list[numbers.Number], v: list[numbers.Number]) -> list[numbers.Number]:**
>"""Add vectors u and v by adding their components

    Args:
        u, v: list of ints or floats

    Returns:
        list of ints or floats
    """


**def addvectinlist(vlist: list[list[numbers.Number]]) -> numbers.Number:**
>"""Gets the sum of the vectors in a list of vectors

    Args:
        vlist: list of vectors

    Returns:
        list or vector
    """


**def adjustbrightness2file(ExistingBMPfile: str, NewBMPfile: str, percentadj: float):**
>"""Apply a brightness adjustment to the image in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        percentadj     : can be a
                         positive or
                         negative value
                         (signed float)

    Returns:
        new bitmap file
    """


**def adjustbrightnessinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, percentadj: float):**
>"""Brightness adjustment to rectangular area in a 24-bit BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region
        percentadj     : can be a
                         positive or
                         negative
                         adjustment
                        (signed float)

    Returns:
        new bitmap file
    """


**def adjustcolordicttopal(bmp: array.array, colordict: dict):**
>"""Adjust a color dictionary to match
    as closely as possible a bitmap palette

    Args:
        bmp      : unsigned byte array
                   with bmp format
        colordict: dictionary of colors

    Returns:
        byref modified dictionary of colors
    """


**def adjustthresholdinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, lumrange: list):**
>"""Threshold adjust in a rectangular area in a 24-bit BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region
        lumrange       : (byte:byte)
                         threshold to
                         apply

    Returns:
        new bitmap file
    """


**def adjustxbufsize(bmp: array.array, x1: int, x2: int) -> int:**
>"""Returns a 32 -bit padded
        int buffer size for a
        buffer with the bit depth
        stored in byte number 28
        of the bitmap bmp and an
        int length of x2 - x1 + 1

    Args:
        bmp   : unsigned byte array
                with bmp format
        x1, x2: int params for
                a x coord line
                in the bitmap

    Returns:
        int adjusted buffer size
    """


**def andvect(u: list[int], v: list[int]) -> list[int]:**
>"""Bitwise and operation of between
    the elements of two lists of ints

    Args:
        v      : list[int]
        bitmask: int

    Returns:
        list[int]
    """


**def anglebetween2Dlines(u: list[numbers.Number, numbers.Number], v: list[numbers.Number, numbers.Number]) -> float:**
>"""Compute the angle between two lines of vectors

    Args:
        u, v: list[Number, Number]

    Returns:
        float angle in radians
    """


**def applybrightnessadjtoBGRbuf(buf: array.array, percentadj: float) -> array.array:**
>"""Apply a brightness adjustment
        to a BGR buffer

    Args:
        buf: unsigned byte array
             holding BGR data

        percentadj: float brightness
                    adjust can be
                    positive or
                    negative

    Returns:
        unsigned byte array
        holding brightness adjusted
        BGR data
    """


**def applycolorfiltertoBGRbuf(buf: array.array, rgbfactors: list[float, float, float]):**
>"""Apply a color filter to a
        BGR buffer

    Args:
        buf: unsigned byte array
             holding BGR data

        rgbfactors: color filter as
                      [r: float,
                       g: float,
                       b: float]

    Returns:
        byref unsigned byte array
        holding color BGR data
    """


**def applygammaBGRbuf(buf: array.array, gamma: float):**
>"""Apply a gamma adjustment to a
        BGR buffer

    Args:
        buf: unsigned byte array
             holding BGR data

        gamma: float gamma adjust

    Returns:
        byref unsigned byte array
        holding gamma adjusted
        BGR data
    """


**def applymonochromefiltertoBGRbuf(buf: array.array):**
>"""Apply a monochrome filter to a
        BGR buffer

    Args:
        buf: unsigned byte array
             holding BGR data

        rgbfactors: color filter as
                      [r: float,
                       g: float,
                       b: float]

    Returns:
        byref unsigned byte array
        holding mono BGR data
    """


**def applythresholdadjtoBGRbuf(buf: array.array, lumrange: list) -> array.array:**
>"""Apply a threshold adjustment
        to a BGR buffer

    Args:
        buf: unsigned byte array
             holding BGR data

        lumrange: [min: int, max: int]
                  brightness threshold

    Returns:
        unsigned byte array
        holding threshold adjusted
        BGR data
    """


**def arcvert(x: int, y: int, r: int, startdegangle: float, enddegangle: float):**
>"""Returns a list[(int, int)] of 2D vertices
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


**def autocropimg2file(ExistingBMPfile: str, NewBMPfile: str, similaritythreshold: float):**
>"""Perform an auto crop to the image in a bitmap file

    Args:
        ExistingBMPfile    : Whole path to
                             existing file
        NewBMPfile         : New file to
                             save changes in
        similaritythreshold: used to tune
                             autocrop

    Returns:
        new bitmap file
    """


**def beziercurve(bmp: array.array, pntlist: list[list[numbers.Number, numbers.Number]], penradius: int, color: int):**
>"""Draws a Bezier Curve

    Args:
        bmp      : unsigned byte array
                   with bmp format
        pntlist  : [(x,y)...]
                   the control points
        penradius: radius of pen
        color    : color of the
                   bezier curve

    Returns:
        byref modified unsigned byte array
    """


**def BMPbitBLTget(bmp: array.array, offset: int, bufsize: int) -> array.array:**
>"""Gets [offset: offset + bufsize] to a new array

    Args:
        bmp    : unsigned byte array
                 with bmp format
        offset : unsigned int
                 address in buffer
        bufsize: unsigned int
                 size of buffer

    Returns:
        unsigned byte array
    """


**def BMPbitBLTput(bmp: array.array, offset: int, arraybuf: array.array):**
>"""Sets offset in array to arraybuf

    Args:
        bmp     : unsigned byte array
                  with bmp format
        offset  : unsigned int
                  address in buffer
        arraybuf: unsigned byte array

    Returns:
        byref modified unsigned byte array
    """


**def bottomrightcoord(bmp: array.array) -> tuple:**
>"""Gets the maximum bottom right coordinates of a bmp

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        tuple (x:int,y:int)
    """


**def brightnessadjcircregion(bmp: array.array, x: int, y: int, r: int, percentadj: float):**
>"""Brightness adjustment to a circular area

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y, r   : center (x, y)
                    and radius r
                    of the region
        percentadj: float percent of the
                    brightness adjustment

    Returns:
        byref modified unsigned byte array
    """


**def brightnessadjcircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, percentadj: float):**
>"""Brightness gradient to a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
                         of a circular
                         region
                         in which we
                         apply a
        percentadj     : brightness
                         adjustment
                         that can be
                         positive
                         or negative

    Returns:
        new bitmap file
    """


**def brightnessadjust(rgb: list[int, int, int], percentadj: float) -> list[int, int, int]:**
>"""Apply a brightness adjustment
        to a rgb

    Args:
        rgb: color as [r: byte,
                       g: byte,
                       b: byte]
        percentadj: brightness
                    adjustment
                    in percent
                    can be positive
                    or negative

    Returns:
        a brightness adjusted color as
        [r: byte, g: byte, b: byte]
    """


**def brightnesseadjto24bitimage(bmp: array.array, percentadj: float):**
>"""Brightness adjustment to a whole BMP

    Args:
        bmp       : unsigned byte array
                    with bmp format
        percentadj: float percentage
                    brightness
                    adjustment
                    can be positive
                    or negative

    Returns:
        byref modified unsigned byte array
    """


**def brightnesseadjto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, percentadj: float):**
>"""Brightness adjustment to a rectangular area

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines
                        the rectangle
        percentadj    : float percentage
                        brightness adjust
                        can be positive
                        or negative

    Returns:
        byref modified unsigned byte array
    """


**def bspline(bmp: array.array, pntlist: list, penradius: int, color: int, isclosed: bool, curveback: bool):**
>"""Draws a Bspline

    Args:
        bmp      : unsigned byte array
                   with bmp format
        pntlist  : [(x, y)...]
                   the control points
        penradius: radius of pen
        color    : color of curve
        isclosed : True means the
                   curve is closed
        curveback: True means
                   extra computation
                   for curve to loop
                   back on itself

    Returns:
        byref modified unsigned byte array
    """


**def bsplinevert(pntlist: list[list[int, int]], isclosed: bool, curveback: bool) -> list[list[int, int]]:**
>"""Creates a list of vertices for a bspline curve

    Args:
        pntlist: 2D control points
                 for the bspline curve
                 as list[list[x: int,
                              y: int]]

    Returns:
        list of vertices as
        list[list[x: int, y: int]]
    """


**def buf2int(buf: array.array) -> int:**
>"""Converts an unsigned byte array
        to an integer value

    Args:
        buf: unsigned byte array

    Returns:
        unsigned int value
    """


**def centercoord(bmp: array.array) -> tuple:**
>"""Gets the central coordinates of a BMP

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        tuple (x:int,y:int)
    """


**def centerpoint(x1: int, y1: int, x2: int, y2: int):**
>"""Returns the centerpoint x, y in rectangular area

    Args:
        x1, y1 : defines the
        x2, y2   rectangular area

    Returns:
        x: int, y: int centerpoint
    """


**def char2int(charcodestr: str) -> int:**
>"""Packs a string into an int
        using ascii code

    Args:
        charcodestr: string

    Yields:
        int value
    """


**def checklink(func: Callable):**
>"""Decorator to test if the first
        parameter in a function is
        a valid file

    Args:
        function

    Returns:
        caller function
    """


**def checklinks(func: Callable):**
>"""Decorator to test if the two
        parameters in a function
        are valid files

    Args:
        function

    Returns:
        caller function
    """


**def circle(bmp: array.array, x: int, y: int, r: int, color: int, isfilled: bool = None):**
>"""Draws a Circle

    Args:
        bmp     : unsigned byte array
                  with bmp format
        x, y, r : center (x,y)
                  and radius r
                  of the circle
        color   : color of the circle
        isfilled: toggles if the
                  circle is filled
                  True -> filled circle
                  False -> circle outline

    Returns:
        byref modified unsigned byte array
    """


**def circle2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, color: int):**
>"""Draws a Circle

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r
        color          : color of circle

    Returns:
        new bitmap file
    """


**def circleinvolutevert(x: int, y: int, a: float, delta: float, lim: float):**
>"""Returns (int, int) 2D vertices
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


**def circlevec(bmp: array.array, v: list, r: int, color: int, isfilled: bool = None):**
>"""Draws a circle

    Args:
        bmp     : unsigned byte array
                  with bmp format
        v       : (x, y) center of
                  the circular region
        r       : radius of the
                  circular region
        color   : color of the circle
        isfilled: toggles if the
                  circle is filled

    Returns:
        byref modified unsigned byte array
    """


**def colorfilter(rgb: list[int, int, int], rgbfactors: list[float, float, float]) -> list[int, int, int]:**
>"""Apply a color filter
        rgbfactors to rgb

    Args:
        rgb: color as [r: byte,
                       g: byte,
                       b: byte]

        rgbfactors: color filter as
                      [r: float,
                       g: float,
                       b: float]

    Returns:
        a color filtered
        color as [r: byte,
                  g: byte,
                  b: byte]
    """


**def colorfilter2file(ExistingBMPfile: str, NewBMPfile: str, rgbfactors: list[float, float, float]):**
>"""Applies Color Filter rgbfactors to a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        rgbfactors     : (r,g,b) r, g, b
                         values range
                         from 0.0 to 1.0

    Returns:
        new bitmap file
    """


**def colorfiltercircregion(bmp: array.array, x: int, y: int, r: int, rgbfactors: list[float, float, float]):**
>"""Color Filter to a circular area

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y, r   : center (x, y)
                    and radius r
                    of the region
        rgbfactors: [r, g, b] range of
                    r, g and b are from
                    0.0 min to 1.0 max

    Returns:
        byref modified unsigned byte array
    """


**def colorfiltercircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, rgbfactors: list[float, float, float]):**
>"""Applies a color filter to a circular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
        rgbfactors     : (r, g, b) values
                         range from 0 to 1

    Returns:
        new bitmap file
    """


**def colorfilterinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, rgbfactors: list[float, float, float]):**
>"""Color Filter to a Rectangular Area in a 24-bit BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region
        rgbfactors     : (r,g,b)
                         values range
                         from
                         0.0 to 1.0

    Returns:
        new bitmap file
    """


**def colorfilterto24bitimage(bmp: array.array, rgbfactors: list[float, float, float]):**
>"""Applies a color filter
        to a whole image in
        an in-memory 24 bit bitmap

    Args:
        bmp       : unsigned byte array
                    with bmp format
        rgbfactors: color filter
                    r,g and b values
                    are from 0.0 to 1.0

    Returns:
        byref modified
        unsigned byte array
    """


**def colorfilterto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, rgbfactors: list[float, float, float]):**
>"""Applies a color filter to
        a rectangular area defined
        by (x1, y1) and (x2, y2)
        in a 24-bit bitmap

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangular
                        region
        rgbfactors    : color filter
                        r, g and b
                        range from
                        0.0 to 1.0

    Returns:
        byref modified
        unsigned byte array

    """


**def colorfiltertoBGRbuf(buf: array.array, rgbfactors: list[float, float, float]) -> array.array:**
>"""Apply a color filter to a
        BGR buffer

    Args:
        buf: unsigned byte array
             holding BGR data

        rgbfactors: color filter as
                      [r: float,
                       g: float,
                       b: float]

    Returns:
        unsigned byte array
        holding color BGR data
    """


**def colorhistorgram(bmp: array.array) -> list:**
>"""Creates a color histogram

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        list sorted in descending order of color frequencies
    """


**def colormix(lum: int, RGBfactors: list[float, float, float]) -> int:**
>"""Mix a byte luminosity value to
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


**def conevertandsurface(vcen: list[float, float, float], r: float, zlen: float, deganglestep: float) -> tuple:**
>"""Returns a list of sparse
        vertices and tiled surfaces
        for a cone

    Args:
        vcen       : [x: float, center
                      y: float, of the
                      z: float] sphere
        r           : radius of
                      conical base
        zlen        : height of
                      the cone
        deganglestep: angle step between
        vertices that controls how sparse
        the list will be

    Returns:
        list of vertices and surfaces
        for plot3Dsolid()
        see Hello_Cone.py
    """


**def convertbufto24bit(buf: array.array, bgrpalbuf: array.array, bits: int) -> array.array:**
>"""Converts 1, 4 and 8-bit buffers to a BGR buffer

    Args:
        buf      : unsigned byte array
        bgrpalbuf: BGR palette info
        bits     : color depth
                   (1, 4, 8)

    Returns:
        unsigned byte array
    """


**def convertselection2BMP(buf: array.array):**
>"""Converts custom unsigned byte array to bmp format

    Args:
        buf: unsigned byte array

    Returns:
        unsigned byte array with bmp format
    """


**def copyBMPhdr(bmp: array.array) -> array.array:**
>"""Copies the bitmap header of an in-memory bmp
    to a new unsigned byte array

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        unsigned byte array with bmp format
    """


**def CopyBMPxydim2newBMP(bmp: array.array, newbits: int) -> array.array:**
>"""Creates a new bitmap with the same dimensions as bmp

    Args:
        bmp    : unsigned byte array
                 with bmp format
        newbits: bit depth
                 (1, 4, 8, 24)

    Returns:
        unsigned byte array with bitmap layout
    """


**def copycircregion(bmp: array.array, x: int, y: int, r: int, newxy: list):**
>"""Copy a circular buffer with center at (x, y)
    and a radius r to a new area with centerpoint at
    newxy [x, y]

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of the
                 circular region
        newxy :  center of
                 circular area
                 to paste
                 the buffer into

    Returns:
        byref modified unsigned byte array
    """


**def copycircregion2buf(bmp: array.array, x: int, y: int, r: int) -> list:**
>"""Copies a circular region to a
    buffer which is defined by
    centerpoint at (x, y) and radius r

    Args:
        bmp     : unsigned byte array
                  with bmp format
        x, y, r : center (x, y)
                  and radius r
                  of the circular area

    Returns:
        list with buffer of circular region
    """


**def copycircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, newxycenterpoint: list):**
>"""Copy/Paste of a circular area in a BMP

    Args:
        ExistingBMPfile : Whole path
                          to existing file
        NewBMPfile      : New file to
                          save changes to
        x, y, r         : center (x,y)
                          and radius r
        newxycenterpoint: (x:int,y:int)
                          where to paste

    Returns:
        new bitmap file
    """


**def copyrect(bmp: array.array, x1: int, y1: int, x2: int, y2: int) -> array.array:**
>"""Copy a rectangular region to a custom buffer

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        custom unsigned byte array
    """


**def copyRGBpal(sourceBMP: array.array, destBMP: array.array):**
>"""Copies the RGB palette info from
    a source unsigned byte array to
    a destination unsigned byte array

    Args:
        sourceBMP and destBMP are both
        unsigned byte arrays with bmp format

    Returns:
        byref modified destBMP
        (unsigned byte array)
    """


**def cosaffin(u: list[numbers.Number], v: list[numbers.Number]) -> float:**
>"""Compute Cosine Similarity or Cosine Affinity

    Args:
        u, v : list of ints or floats

    Returns:
        float value
            proportional vectors = 1
            orthogonal vectors = 0
            opposite vectors = -1
            and values in between
    """


**def crop(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Crops the image to a rectangular
        region defined by (x1, y1)
                      and (x2, y2)

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: the rectangular
                        region

    Returns:
        unsigned byte array
        with bitmap layout
    """


**def cropBMPandsave(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Crops and saves a rectangular area to a BMP

    Args:
        ExistingBMPfile: Whole path
                         to an
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x1, y1, x2, y2 : the rectagular
                         region

    Returns:
        new bitmap file
    """


**def cropBMPandsaveusingrectbnd(ExistingBMPfile: str, NewBMPfile: str, rectbnd: list):**
>"""Crops and saves a rectangular area to a BMP

    Args:
        ExistingBMPfile: Whole path
                         to existing file
        NewBMPfile     : New file to
                         save changes in
        rectbnd        : list defining
                         a rectangular
                         region
                         [(x1, y1),
                          (x2, y2),
                          (x3, y3),
                          (x4, y4)]

    Returns:
        new bitmap file
    """


**def cubevert(x: float) -> list[list[float, float, float]]:**
>"""Returns a list of vertices
        for a cube

    Args:
        x: length of a side

    Returns:
        list (x: float,
              y: float,
              z: float)
    """


**def cylindervertandsurface(vcen: list[float, float, float], r: float, zlen: float, deganglestep: float) -> tuple:**
>"""Returns a list of sparse vertices
       and tiled surfaces for a cylinder

    Args:
        vcen       : [x: float, center
                      y: float, of the
                      z: float] sphere
        r           : radius
        zlen        : height of the
                      cylinder
        deganglestep: angle step between
        vertices that controls how sparse
        the list will be

    Returns:
        list of vertices and surfaces
        for plot3Dsolid()
        see Hello_Coin.py
    """


**def decahedvertandsurface(x: float) -> list[list[float, float, float]]:**
>"""Returns a list of vertices
        for a decahedron

    Args:
        x: min radius of sphere
           that can hold
           the decahedron

    Returns:
        list (x: float,
              y: float,
              z: float)
    """


**def dict2descorderlist(d: dict) -> list:**
>"""Creates a sorted list in
        decending order from
        a dictionary with counts

    Args:
        dict: histogram or
              frequency count

    Returns:
        list
    """


**def distance(u: list[float], v: list[float]) -> float:**
>"""Compute the Distance or length of a vector v
    of arbitrary dimension n in a n-dimensional
    Euclidean space where u and v are both vectors
    with n components

    Args:
        u, v: list of ints or floats

    Returns:
        float
    """


**def drawarc(bmp: array.array, x: int, y: int, r: int, startdegangle: float, enddegangle: float, color: int, showoutline: bool, fillcolor: int, isfilled: bool):**
>"""Draws an Arc

    Args:
        bmp        : unsigned
                     byte array
                     with bmp format
        x, y, r    : defines a circle
                     that contains
                     the arc
        color      : color of arc
        showoutline: True -> draw arc
                             outline
        fillcolor  : color of arc
                     filling
        isfilled   : True -> set area
                             inside the
                             arc to
                             fillcolor

    Returns:
        byref modified unsigned byte array
    """


**def drawvec(bmp: array.array, u: list, v: list, headsize: int, color: int, penradius: int = None):**
>"""Draws a vector (line segment with arrow head)

    Args:
        bmp      : unsigned byte array
                   with bmp format
        u        : (x: float, y: float)
                    point 1 origin
        v        : (x: float, y: float)
                   point 2 has arrow
        headsize : size of the arrow
                   0 for default size
        color    : color of the vector
        penradius: optional parameter
                   for thick arrow

    Returns:
        byref modified unsigned byte array
    """


**def ellipse(bmp: array.array, x: int, y: int, b: int, a: int, color: int, isfilled: bool = None):**
>"""Draws an Ellipse

    Args:
        bmp     : unsigned byte array
                  with bmp format
        x, y    : center of ellipse
        b, a    : major amd minor axis
        color   : color of the ellipse
        isfilled: True -> filled
                          ellipse
                  False-> one pixel
                          thick
                          ellipse

    Returns:
        byref modified unsigned byte array
    """


**def ellipsevert(x: int, y: int, b: int, a: int) -> list[int, int]:**
>"""Returns (int, int) 2D vertices
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


**def entirecircleinboundary(func):**
>"""Decorator to ensure that the 2nd,
        3rd, 4th parameters are ints
        whose values when interpreted
        as the centerpoint x, y
        and radius r of a circle
        lay within the RGB bitmap.

    Args:
        function(bmp:array,x:int,y:int,r:int...)

    Returns:
        caller function
    """


**def entirecircleisinboundary(x: int, y: int, minx: int, maxx: int, miny: int, maxy: int, r: int):**
>"""Checks if an entire circle
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


**def entireellipseisinboundary(x: int, y: int, minx: int, maxx: int, miny: int, maxy: int, b: int, a: int):**
>"""Checks if an entire ellipse
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


**def entirerectinboundary(func):**
>"""Decorator to ensure that the
        2nd, 3rd, 4th and 5th
        parameters are ints whose
        values when interpreted as
        x and y coordinates of a
        rectangle lay within the
        bitmap.

    Args:
        function

    Returns:
        caller function
    """


**def enumbits(byteval: int):**
>"""Yields the 8 bits in a byte

    Args:
        byteval: int value
                 from 0 to 255

    Yields:
        Eight bits that is either
        int 0 or int 1
    """


**def enumletters(st: str) -> str:**
>"""Enumerates the characters
        in a string

    Args:
        st: string

    Yields:
        individual characters
    """


**def enumreverseletters(st: str) -> str:**
>"""Enumerates the characters in a
        string in reverse order

    Args:
        st: string

    Yields:
        individual characters
    """


**def epicycloidvert(x: int, y: int, a: float, b: float, delta: float, lim: float):**
>"""Returns (int, int) 2D vertices
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


**def erasealternatehorizontallines(bmp: array.array, int_eraseeverynline: int, int_eraseNthline: int, bytepat: int):**
>"""Erase every nth line

    Args:
        bmp                : unsigned
                             byte array
                             with
                             bmp format
        int_eraseeverynline: erase every
                             nth line
                             in the
                             region
        int_eraseNthline   : control
                             which line
                             every
                             n lines
                             to erase
        bytepat            : byte pattern
                             to overwrite
                             the erased
                             lines

    Returns:
        byref modified unsigned byte array
    """


**def erasealternatehorizontallinesincircregion(bmp: array.array, x: int, y: int, r: int, int_eraseeverynline: int, int_eraseNthline: int, bytepat: int):**
>"""Erase every nth line
        in a circular region

    Args:
        bmp                : unsigned
                             byte array
                             with bmp
                             format
        x, y, r            : (x, y)
                             centerpoint
                             and radius r
                             of the
                             circular area
        int_eraseeverynline: erase every
                             nth line
                             in the
                             circular
                             region
        int_eraseNthline   : control which
                             line every
                             n lines
                             to erase
        bytepat            : pattern to
                             overwrite
                             the erased
                             lines

    Returns:
        byref modified unsigned byte array
    """


**def erasealternatehorizontallinesinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, int_eraseeverynline: int, int_eraseNthline: int, bytepat: int):**
>"""Erase every nth line in a rectangular region

    Args:
        bmp                : unsigned
                             byte array
                             with bmp
                             format
        x1, y1, x2, y2     : ints that
                             defines the
                             rectangular
                             region
        int_eraseeverynline: erase every
                             nth line
                             in the region
        int_eraseNthline   : control which
                             line every
                             n lines
                             to erase
        bytepat            : pattern to
                             overwrite
                             the erased
                             lines

    Returns:
        byref modified unsigned byte array
    """


**def eraseeverynthhoriline2file(ExistingBMPfile: str, NewBMPfile: str, n: int):**
>"""Erase every nth line

    Args:
        ExistingBMPfile: Whole path
                         to existing file
        NewBMPfile     : New file to
                         save changes in
        n              : erase every
                         nth line

    Returns:
        new bitmap file
    """


**def eraseeverynthhorilineinccircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, n: int):**
>"""Erase every nth horzontal line in a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
                         in which we
        n              : omit every
                         nth line

    Returns:
        new bitmap file
    """


**def eraseeverynthhorilineinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, n: int):**
>"""Erase every nth line in a
        rectangular region

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangular
                        region
        n             : erase every
                        nth line in the
                        rectangular area

    Returns:
        byref modified
        unsigned byte array
    """


**def eraseeverynthhorilineinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, n: int):**
>"""Erase every nth line in a rectangular region

    Args:
        ExistingBMPfile: Whole path to
                         an existing
                         file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region
        n              : erase every
                         nth line

    Returns:
        new bitmap file
    """


**def eraseeverynthhorizontalline(bmp: array.array, n: int):**
>"""Erase every nth horizontal line

    Args:
        bmp: unsigned byte array
             with bmp format
        n  : erase every nth line

    Returns:
        byref modified unsigned byte array
    """


**def eraseeverynthhorizontallineinccircregion(bmp: array.array, x: int, y: int, r: int, n: int):**
>"""Erase every nth horizontal line in a circular region

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of the circular area
        n      : erase every nth line

    Returns:
        byref modified unsigned byte array
    """


**def fern(bmp: array.array, x1: int, y1: int, x2: int, y2: int, color: int):**
>"""Draws an IFS fern fractal

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: rectangular
                        area to draw
                        the fern in
        color         : color of the
                        fern fractal

    Returns:
        byref modified unsigned byte array
    """


**def fern2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, color: int):**
>"""Fern Fractal in a bounding rectangle

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular region
        color          : color of the
                         fern fractal

    Returns:
        new bitmap file
    """


**def fillbackgroundwithgrad(bmp: array.array, lumrange: list[int, int], RGBfactors: list[float, float, float], direction: int):**
>"""Fills entire bitmap with a linear gradient

    Args:
        bmp       : unsigned byte array
                    with bmp format
        lumrange  : [byte,byte] that
                    define the range
                    the of gradient
        RGBfactors: [r,g,b] each item
                    in list are unsigned
                    floats from 0 to 1
        direction : 0 - vertical
                    1 - horizontal

    Returns:
        byref modified unsigned byte array
    """


**def fillboundary(bmp: array.array, bndfilldic: dict, color: int):**
>"""Draws lines in a boundary to fill it

    Args:
        bmp       : unsigned byte array
                    with bmp format
        bndfilldic: boundary dictionary
        color     : color of fill

    Returns:
        byref modified unsigned byte array
    """


**def filledcircle(bmp: array.array, x: int, y: int, r: int, color: int):**
>"""Draws a Filled Circle

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of filled circle
        color  : color of the
                 filled circle

    Returns:
        byref modified unsigned byte array
    """


**def filledcircle2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, color: int):**
>"""Draws a Filled Circle

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
        color          : color of the
                         circular region

    Returns:
        new bitmap file
    """


**def filledellipse(bmp: array.array, x: int, y: int, b: int, a: int, color: int):**
>"""Filled Ellipse

    Args:
        bmp  : unsigned byte array
               with bmp format
        x, y : center of ellipse
        b, a : major amd minor axis
        color: color of the ellipse

    Returns:
        byref modified unsigned byte array
    """


**def filledgradrect(bmp: array.array, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int], RGBfactors: list[float, float, float], direction: int):**
>"""Draw a filled rectangle with a linear gradient

    Args:
        bmp            : unsigned
                         byte array
                         with bmp format
        x1, y1, x2, y2 : defines the
                         rectangular
                         region
        lumrange       : [byte, byte]
                         defines
                         the range
                         of the
                         gradient
        RGBfactors     : [r, g, b] items
                         in list are
                         unsigned floats
                         from 0.0 to 1.0
        direction      : 0 - vertical
                         1 - horizontal

    Returns:
        byref modified
        unsigned byte array
    """


**def filledparallelogram(bmp: array.array, p1: list, p2: list, p3: list, color: int):**
>"""Creates a filled parallelogram defined by 3 points

    Args:
        bmp       : unsigned byte array
                    with bmp format
        p1, p2, p3:(x: float, y: float)
                    points that define
                    a parallelogram
        color     : color of the
                    filled parallelgram

    Returns:
        byref unsigned modified byte array
    """


**def filledrect(bmp: array.array, x1: int, y1: int, x2: int, y2: int, color: int):**
>"""Draws a Filled Rectangle

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangular
                        region
        color         : color of the
                        rectangle

    Returns:
        byref modified unsigned byte array
    """


**def fillpolydata(polybnd: list[list[int, int]], xlim: int, ylim: int) -> list:**
>"""Generates a list of x values per
        y values for filling polygon
        boundaries

    Args:
        polybnd : list of 2D vertices
                  list[list[x: int,
                            y: int]]
                  that forms a
                  complete polygon
                  boundary (see
                  def polyboundary)
        xlim    : Screen limit x dim
        ylim    : Screen limit x dim

    Returns:
        A dictionary with y values
        as key and list of x values
        per key (if within bounds)
        or an empty list if out of
        bounds
    """


**def fliphoricircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Flips horizontally a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of circular region

    Returns:
        byref modified
        unsigned byte array
    """


**def fliphoricircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Horizontal Flip of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x,y)
                         and radius r

    Returns:
        new bitmap file
    """


**def fliphorizontal(bmp: array.array):**
>"""Does a horizontal flip of an
        in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def fliphorizontal2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Flips horizontally the image in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def fliphorizontalregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Does a horizontal flip
        of a rectangular area

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangular
                        region

    Returns:
        byref modified
        unsigned byte array
    """


**def fliphorizontalregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Flips horizontally a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region

    Returns:
        new bitmap file
    """


**def fliphorzontalpixelbased(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Flips horizontal
        a rectangular region
        using pixel addressing
        (slightly slow)

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangular
                        region

    Returns:
        byref modified
        unsigned byte array

    """


**def fliphverticalalpixelbased(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Flips vertical
        a rectangular region
        using pixel addressing
        (slightly slow)

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: the rectangular
                        region

    Returns:
        byref modified
        unsigned byte array
    """


**def flipnibbleinbuf(buf: array.array) -> array.array:**
>"""Flips a 4-bit image buffer

    Args:
        buf: unsigned byte array

    Returns:
        unsigned byte array
    """


**def flipvertcircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Vertical Flip of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of a region

    Returns:
        byref modified unsigned byte array
    """


**def flipvertcircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Vertical Flip of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def flipvertical(bmp: array.array):**
>"""Does an vertical flip of a bmp

    Args:
        bmp: unsigned byte array
        with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def flipvertical2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Flips a bitmap file vertically

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def flipverticalregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Flips vertical a rectangular area

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangle

    Returns:
        byref modified
        unsigned byte array
    """


**def flipverticalregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Flips vertically a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region

    Returns:
        new bitmap file
    """


**def flipXY(bmp: array.array):**
>"""Flips the x and y coordinates of
        an in-memory bitmap for a
        90 degree rotation

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def flipXY2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Flips the x and y coordinates to rotate by 90 degrees

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def flipXYcircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Flip the X and Y coordinates of a circular area

    Args:
        bmp     : unsigned byte array
                  with bmp format
        x, y, r : center (x,y) and
                  radius r of region

    Returns:
        byref modified unsigned byte array
    """


**def flipXYcircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Flips the x and y coordinates of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def flowervert(cx: int, cy: int, r: int, petals: int, angrot: float):**
>"""Returns a list of 2D points for a flower

    Args:
        cx, cy, r : center (cx,cy)
                    and radius r
        petals    : number of petals
        angrot    : angle of rotation

    Returns:
        list[(x: int, y: int)]
    """


**def func24bitonly(func):**
>"""Decorator to restrict the
        use of this function to only
        24-bit or RGB bitmaps
        (1st parameter)

    Args:
        function(bmp:array,...)

    Returns:
        caller function
    """


**def func24bitonlyandentirecircleinboundary(func):**
>"""Decorator to restrict the
        use of this function to only
        24-bit bitmaps (1st parameter)
        and ensure that the 2nd, 3rd,
        4th parameters are ints whose
        values when interpreted as
        x, y and radius of a circle
        lay within the RGB bitmap.

    Args:
        function(bmp:array,x:int,y:int,r:int...)

    Returns:
        caller function
    """


**def func24bitonlyandentirerectinboundary(func):**
>"""Decorator to restrict the
        use of this function to only
        24-bit or RGB bitmaps
        (1st parameter) and ensure that
        the 2nd, 3rd, 4th and 5th
        parameters are ints whose
        values when interpreted as
        x and y coordinates lay
        within the RGB bitmap.

    Args:
        function

    Returns:
        caller function
    """


**def func8and24bitonlyandentirecircleinboundary(func):**
>"""Decorator to restrict the
        use of this function to only
        24-bit or 8-bit bitmaps
        (1st parameter) and ensure
        that the 2nd, 3rd, 4th
        parameters are ints whose
        values when interpreted as
        x, y and radius of a circle
        lay within the RGB bitmap.

    Args:
        function(bmp:array,x:int,y:int,r:int...)

    Returns:
        caller function
    """


**def func8and24bitonlyandentirerectinboundary(func):**
>"""Decorator to restrict the
        use of this functiom to only
        24 bit or 8 bit bitmaps
        (1st parameter) and ensure
        that the 2nd, 3rd, 4th and
        5th parameters are ints whose
        values when interpreted as
        x and y coordinates of a
        rectangle lay within
        the RGB bitmap.

    Args:
        function

    Returns:
        caller function
    """


**def functimer(func):**
>"""Function timer Decorator

    Args:
        function

    Returns:
        caller function

    """


**def gammaadj2file(ExistingBMPfile: str, NewBMPfile: str, gamma: float):**
>"""Applies a Gamma Correction

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        gamma          : gamma
                         correction

    Returns:
        new bitmap file
    """


**def gammaadjto24bitimage(bmp: array.array, gamma: float):**
>"""Gamma correction to an in-memory 24-bit BMP

    Args:
        bmp  : unsigned byte array
               with bmp format
        gamma: gamma correction

    Returns:
        byref modified unsigned byte array
    """


**def gammaadjto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, gamma: float):**
>"""Gamma correction to a rectangular area in a 24-bit BMP

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangular
                        region
        gamma         : gamma correction

    Returns:
        byref modified unsigned byte array
    """


**def gammaadjtoregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, gamma: float):**
>"""Gamma Correction to a Rectangular Region

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region
        gamma          : gamma
                         correction

    Returns:
        new bitmap file
    """


**def gammaBGRbuf(buf: array.array, gamma: float) -> array.array:**
>"""Apply a gamma adjustment to a
        BGR buffer

    Args:
        buf: unsigned byte array
             holding BGR data

        gamma: float gamma adjust

    Returns:
        unsigned byte array
        holding gamma adjusted
        BGR data
    """


**def gammacorrect(rgb: list[int, int, int], gamma: float) -> list[int, int, int]:**
>"""Apply a gamma factor to a rgb

    Args:
        rgb: color as [r: byte,
                       g: byte,
                       b: byte]
        gamma  : gamma adjustment

    Returns:
        a gamma adjusted color as
        [r: byte, g: byte, b: byte]
    """


**def gammacorrectcircregion(bmp: array.array, x: int, y: int, r: int, gamma: float):**
>"""Gamma correction to a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of the region
        gamma  : float value of the
                 gamma adjustment

    Returns:
        byref modified unsigned byte array
    """


**def gammacorrectcircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, gamma: float):**
>"""Gamma Adjust to a circular area in a BMP

    Args:
        ExistingBMPfile: Whole path
                         to existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
                         of a circular
                         region
        gamma          : gamma
                         adjustment

    Returns:
        new bitmap file
    """


**def genpiechartdata(dlist: list):**
>"""Preprocess data to make
        it suitable for a pie chart

    Args:
        dlist: [[20, c['red']],
                [30, c['brightyellow']],
                ...]

    Returns:
        list and large value (if any)
    """


**def gensides(pointlists: list[list, list], transvect: list[float, float, float], sides: list[list[float]]) -> tuple:**
>"""Generates a list of polygons
        and normals from 3D polygon
        and side data to a list of
        sides and normals with
        with the hidden surfaces
        removed that is suitable
        for rendering on a 2D surface
        and also applies a
        3D translation vector for
        positioning
    """


**def getallRGBpal(bmp: array.array) -> list[list[int, int, int]]:**
>"""Gets the RGB palette of a bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        [(r: byte, g: byte, b: byte), ...]
    """


**def getBGRpalbuf(bmp: array.array):**
>"""Gets bitmap palette as stored in the bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        unsigned byte array (BGR)
    """


**def getBMPimgbytes(bmp: array.array) -> list:**
>"""Gets the raw image buffer of a bmp without the header

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        list of unsigned bytes
    """


**def getcharfont(charbuf: list, character: str) -> list:**
>"""None"""


**def getcolorname2HSLdict() -> dict:**
>"""None"""


**def getcolorname2RGBdict() -> dict:**
>"""None"""


**def getdatalisttotal(dlist: list[numbers.Number]) -> numbers.Number:**
>"""Returns the total of a
        list of ints or floats

    Args:
        dlist: list of ints or floats

    Returns:
        float or int
    """


**def getdefaultbitpal(bits: int) -> list:**
>"""Gets the standard bitmap palette
        for a  specified bit depth bits

    Args:
        bits: int value (1, 4, 8, 24)

    Returns:
        list of palette entries
    """


**def getdefaultlumrange() -> dict:**
>"""Gets the default luminosity
        ranges lookup

    Returns:
        a dict for default
        luminosity ranges
    """


**def getfuncmetastr(f: Callable):**
>"""None"""


**def getIFSparams() -> dict:**
>"""None"""


**def getimagedgevert(bmp: array.array, similaritythreshold: int):**
>"""Find edges in an image

    Args:
        bmp                : unsigned
                             byte array
                             with bmp
                             format
        similaritythreshold: how close
                             to the color
                             before we
                             yield it

    Yields:
        [(x: int, y: int),...]
    """


**def getimageregionbyRGB(bmp: array.array, rgb: list[int, int, int], similaritythreshold: int):**
>"""Select a region by color

    Args:
        bmp                 :unsigned
                             byte array
                             with bmp
                             format
        rgb                 :(r: byte,
                              g: byte,
                              b: byte)
        similaritythreshold: controls
                             the edge
                             detection
                             sensitivity

    Returns:
        list of vertices
    """


**def getmaxcolors(bmp: array.array) -> int:**
>"""Get the maximum number of colors supported by a BMP

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        int value
    """


**def getmaxx(bmp: array.array) -> int:**
>"""Gets the x value stored in the windows bmp header

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        int value of x bmp dimension
    """


**def getmaxxy(bmp: array.array) -> tuple:**
>"""Gets the max x and y values stored in the bmp header

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        tuple (x:int,y:int)
    """


**def getmaxxyandbits(bmp: array.array) -> tuple:**
>"""Returns bitmap metadata
       (x-dimension, y-dimension, bit depth)

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        (x-dimension, y-dimension, bit depth)
    """


**def getmaxy(bmp: array.array) -> int:**
>"""Gets the y value stored in the windows bmp header

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        int value of y bmp dimension
    """


**def getneighborcolorlist(bmp: array.array, v: list):**
>"""None"""


**def getRGBfactors() -> dict:**
>"""None"""


**def getRGBpal(bmp: array.array, c: int) -> list[int, int, int]:**
>"""Gets the [R, G, B] values
        of color c in a bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
        c  : unsigned int color

    Returns:
        [R: byte, G: byte, B:byte]
    """


**def getRGBxybit(bmp: array.array, x: int, y: int) -> list[int, int, int]:**
>"""Gets [R:byte, G:byte, B:byte]
    of pixel at (x, y) in a bitmap

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int
              locations in x and y

    Returns:
        [R: byte, G: byte, B: byte]
    """


**def getRGBxybitvec(bmp: array.array, v: list) -> list:**
>"""Gets the RGB of a pixel at (x,y) in a BMP

    Args:
        bmp: unsigned byte array
             with bmp format
        v  : pixel location
             (x:int, y:int)

    Returns:
        [R: byte, G: byte, B: byte]
    """


**def getshapesidedict() -> dict:**
>"""Returns a dictionary of side
        or polygon definitions for
        simple solids

    Returns:
        dictionary of side or polygon
        definitions for basic solids
    """


**def getX11colorname2HSLdict() -> dict:**
>"""None"""


**def getX11colorname2RGBdict() -> dict:**
>"""None"""


**def getX11RGBfactors() -> dict:**
>"""None"""


**def getXKCDcolorname2HSLdict() -> dict:**
>"""None"""


**def getXKCDcolorname2RGBdict() -> dict:**
>"""None"""


**def getXKCDRGBfactors() -> dict:**
>"""None"""


**def getxybit(bmp: array.array, x: int, y: int) -> int:**
>"""Gets color of pixel at (x, y) in a BMP

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int
              locations in x and y

    Returns:
        unsigned int color value
    """


**def getxybitvec(bmp: array.array, v: list) -> int:**
>"""Gets color of pixel at (x, y)

    Args:
        bmp: unsigned byte array
             with bmp format
        v  : (x: int, y: int)
             pixel coordinates

    Returns:
        unsigned int color value
    """


**def gradcircle(bmp: array.array, x: int, y: int, r: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):**
>"""Filled Circle with Gradient

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y, r   : center (x, y)
                    and radius r
        lumrange  : [byte,byte] range of
                    the gradient
        rgbfactors: [r, g, b] range are
                    from 0.0 to 1.0

    Returns:
        byref modified unsigned byte array
    """


**def gradellipse(bmp: array.array, x: int, y: int, b: int, a: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):**
>"""Ellipical gradient

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : center of ellipse
        b, a      : major amd minor axis
        lumrange  : [byte:byte] controls
                    the range of the
                    luminosity gradient
        rgbfactors: [r, g, b] range
                    are from 0.0 to 1.0

    Returns:
        byref modified unsigned byte array
    """


**def gradthickcircle(bmp: array.array, x: int, y: int, r: int, penradius: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):**
>"""Thick Circle with a Gradient

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y, r   : center (x, y)
                    and radius r
        penradius : radius of the
                    round pen
        lumrange  : [byte,byte] range
                    of the luminosity
                    gradient
        rgbfactors: [r,g,b] range are
                    from 0.0 to 1.0

    Returns:
        byref modified unsigned byte array
    """


**def gradthickellipserot(bmp: array.array, x: int, y: int, b: int, a: int, degrot: float, penradius: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):**
>"""Thick Ellipse with a Gradient fill

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : center of ellipse
        b, a      : major amd minor axis
        degrot    : rotation of
                    the ellipse in degrees
        penradius : defines the
                    thickness of the pen
        lumrange  : [byte:byte] sets
                    the range of the
                    luminosity gradient
        rgbfactors: [r, g, b] range are
                    from 0.0 min to 1.0 max

    Returns:
        byref modified unsigned byte array
    """


**def gradthickplotpoly(bmp: array.array, vertlist: list, penradius: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):**
>"""Draws a polygon of a given gradient and thickness

    Args:
        bmp       : unsigned byte array
                    with bmp format
        vertlist  : [(x,y)...] the
                    list of vertices
        penradius : radius of pen
        lumrange  : [byte,byte] range
                    of the gradient
        RGBfactors: [r, g, b] value
                    range from
                    0.0 to 1.0

    Returns:
        byref modified unsigned byte array
    """


**def gradthickroundline(bmp: array.array, p1: list, p2: list, penradius: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):**
>"""Draw a Thick Rounded Line with a Gradient

    Args:
        bmp      : unsigned byte array
                   with bmp format
        p1, p2   : (x, y) endpoints
                    of the line
        penradius: radius of pen
        lumrange : list of two
                   byte values
                   [gradstart,gradend]
                   that define the
                   luminosity gradient
        RGBfactors: [r, g, b]
                    each item
                    in list is an
                    unsigned float
                    with a range
                    from 0.0 to 1.0

    Returns:
        byref modified
        unsigned byte array
    """


**def gradvert(bmp: array.array, vertlist: list[list[int, int]], penradius: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):**
>"""List of 2d vertices as spheres of a given color

    Args:
        bmp       : unsigned byte array
                    with bmp format
        vertlist  : [(x, y), ...]
                    list of vertices
        penradius : radius of
                    the spheres
        lumrange  : [byte, byte] sets
                    the luminosity
                    gradient
        RGBfactors: (r, g, b)
                    values range from
                    min 0.0 to 1.0 max

    Returns:
        byref modified
        unsigned byte array
    """


**def hexahedravert(x: float) -> list[list[float, float, float]]:**
>"""Returns a list of vertices
        for a hexahedron

    Args:
        x: length of a side

    Returns:
        list (x: float,
              y: float,
              z: float)
    """


**def horibrightnessgrad2circregion(bmp: array.array, x: int, y: int, r: int, lumrange: list[int, int]):**
>"""Horizontal brightness gradient adjustment to a circular area

    Args:
        bmp     : unsigned byte array
                  with bmp format
        x, y, r : center (x, y)
                  and radius r
                  of a circular area
        lumrange: [byte, byte] the
                  luminosity range

    Returns:
        byref modified unsigned byte array
    """


**def horibrightnessgrad2circregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, lumrange: list[int, int]):**
>"""Horizontal brightness gradient to a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
                         of a circular
                         region in which
                         we apply a
        lumrange       : brightness gradient
                         (byte, byte) adjust

    Returns:
        new bitmap file
    """


**def horiline(bmp: array.array, y: int, x1: int, x2: int, color: int):**
>"""Draw a Horizontal Line

    Args:
        bmp   : unsigned byte array
                with bmp format
        y     : constant y value
                of the line
        x1    : starts at x1
        x2    : ends at x2
        color : color of the line

    Returns:
        byref modified unsigned byte array
    """


**def horilinevert(bmp: array.array, vlist: list[list[int, int]], linelen: int, xadj: int, color: int):**
>"""Horizontal line marks at vertices in vlist

    Args:
        bmp    : unsigned byte array
                 with bmp format
        vlist  : [(x, y), ...]
                 the list of
                 2D vertices
        linelen: length of the
                 vertical lines
        xadj   : sets an adjustment
                 for x coordinates
        color  : color of the line

    Returns:
        byref modified unsigned byte array
    """


**def horitransformincircregion(bmp: array.array, x: int, y: int, r: int, trans: str):**
>"""Horizontal transform to a circular area

    Args:
        bmp  :   unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r of region
        trans:   single letter
                 transform code
                 'L' -> mirror left
                 'R' -> mirror right
                 'F' -> flip

    Returns:
        byref modified
        unsigned byte array
    """


**def horizontalbrightnessgrad2file(ExistingBMPfile: str, NewBMPfile: str, lumrange: list[int, int]):**
>"""Horizontal brightness gradient to a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        lumrange       : (byte:byte)
                         defines the
                         brightness
                         gradient

    Returns:
        new bitmap file
    """


**def horizontalbrightnessgradregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int]):**
>"""Horizontal brightness gradient to a rectangular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2 ,y2 : defines the
                         rectangular
                         region
        lumrange       : (byte:byte)
                         brightness
                         gradient

    Returns:
        new bitmap file
    """


**def horizontalbrightnessgradto24bitimage(bmp: array.array, lumrange: list[int, int]):**
>"""Applies a horizontal brightness
        gradient to a 24-bit bitmap

    Args:
        bmp     : unsigned byte array
                  with bmp format
        lumrange: [byte,byte]
                  the range of the
                  luminosity gradient

    Returns:
        byref modified
        unsigned byte array
    """


**def horizontalbrightnessgradto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int]):**
>"""Apply a horizontal brightness gradient
    to a rectangular area in a 24-bit bitmap

    Args:
        bmp            : unsigned
                         byte array
                         with bmp format
        x1, y1, x2, y2: defines the
                        rectangular
                        region
        lumrange      : (byte: byte)
                        defines
                        the brightness
                        gradient

    Returns:
        byref modified unsigned byte array
    """


**def horizontalbulkswap(bmp: array.array, x1: int, y1: int, x2: int, y2: int, swapfunc: Callable):**
>"""Applies function swapfunc
        to a rectangular area

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: the rectangular
                        region

    Returns:
        byref modified
        unsigned byte array
    """


**def horizontalvert(y: int, x1: int, x2: int, dx: int) -> list[list[int, int]]:**
>"""Creates a list of int vertices along
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


**def hypotrochoidvert(x: int, y: int, a: float, b: float, c: float, delta: float, lim: float):**
>"""Returns (int, int) 2D vertices
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


**def icosahedvertandsurface(x: float) -> list[list[list[float, float, float]], tuple]:**
>"""Returns a list of vertices
        and surfaces for an icosahedron

    Args:
        x: min radius of sphere
           that can hold
           the icosahedron

    Returns:
        list (x: float,
              y: float,
              z: float)
    """


**def IFS(bmp: array.array, IFStransparam: tuple, x1: int, y1: int, x2: int, y2: int, xscale: int, yscale: int, xoffset: int, yoffset: int, color: int, maxiter: int):**
>"""Draw an Interated Function System Fractal

    Args:
        bmp            : unsigned
                         byte array
                         with bmp format
        IFStransparam  : see fractals.py
        x1, y1, x2, y2 : rectangular
                         region
                         to draw in
        xscale,yscale  : scaling factors
        xoffset,yoffset: used to move
                         the fractal
        color          : color of fractal
        maxiter        : when to break
                         color compute

    Returns:
        byref modified unsigned byte array
    """


**def iif(boolcond: bool, trueval: <built-in function any>, falseval: <built-in function any>) -> <built-in function any>:**
>"""Returns trueval if
        boolcond is true
        else return falseval

    Args:
        boolcond: an expression that
                  evaluates as either
                  True or False
        trueval : value to return if
                  boolcond evaluates
                  to True
        falseval: value to return if
                  boolcond evaluates
                  to False

    Returns:
        a value depending on boolcond
    """


**def imagecomp(inputfile1: str, inputfile2: str, diff_file: str, func: Callable):**
>"""Perform a bitwise comparison of two bitmap files
    with the same x and y dimensions and bit depth
    using a user defined bitwise comparator function

    Args:
        Inputfile1: path to bmp file
        Inputfile2: path to bmp file
        diff_file : New file to save
                    comparison in
        func      : User provided
                    bitwise function

    Returns:
        new bitmap file
    """


**def imagediff(inputfile1: str, inputfile2: str, diff_file: str):**
>"""Compares 2 files and saves diff to a bitmap file

    Args:
        inputfile1: Whole paths
        inputfile2 to existing files

        diff_file: New file
                   to store diff

    Returns:
        new bitmap file
    """


**def imgregionbyRGB2file(ExistingBMPfile: str, NewBMPfile: str, edgeradius: int, edgecolor: int, rgb: list[int, int, int], similaritythreshold: float, showedgeonly: bool):**
>"""Gets an image region by rgb in a bitmap file

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        edgeradius     : radius of pen
                         for the edge
        edgecolor      : color of edge
        rgb            : (r: byte,
                          g: byte,
                          b: byte)
                         color to select
        similaritythreshold: how close
                             the color
                             is to rgb
                             before
                             selection
        showedgeonly: True-> only edges
                 False-> edge and image

    Returns:
        new bitmap file
    """


**def int2BGRarr(i: int) -> array.array:**
>"""Returns a bgr array from
        int i color input

    Args:
        i: color value

    Returns:
        unsigned byte BGR array
    """


**def int2buf(cnt: int, value: int) -> array.array:**
>"""Converts an integer value to an
        unsigned byte array

    Args:
        cnt   : uint length of int data
        value : value of uint data

    Returns:
        unsigned byte array
    """


**def int2RGB(i: int):**
>"""Break down int color i to its
        byte valued r, g and b
        components

    Args:
        i: int color value

    Returns:
        r: byte, g: byte, b: byte
    """


**def int2RGBarr(i: int) -> array.array:**
>"""Returns a rgb array from
        int i color input


    Args:
        i: color value

    Returns:
        unsigned byte RGB array
    """


**def int2RGBlist(i: int) -> list[int, int, int]:**
>"""Break down int color i to its
        byte valued r, g and b
        components in a list

    Args:
        i: int color value

    Returns:
        [r: byte, g: byte, b: byte]
    """


**def intcircleparam(func):**
>"""Decorator to test if the
        2nd, 3rd, 4th parameters
        in a function that renders
        circle are ints

    Args:
        function(bmp:array,x,y,r....)

    Returns:
        caller function
    """


**def intcircleparam24bitonly(func):**
>"""Decorator to test if 2nd, 3rd,
        4th parameters in a function
        that renders circle are ints
        and restrict the use of this
        function to only 24-bit or
        RGB bitmaps (1st parameter)

    Args:
        function(bmp:array,x,y,r....)

    Returns:
        caller function
    """


**def intlinevec(bmp: array.array, u: list, v: list, color: int):**
>"""Draw a line in a bitmap

    Args:
        bmp   : unsigned byte array
                with bmp format
        u, v  : (x: int, y: int) points
                that defines the line
        color : color of the line

    Returns:
        byref modified unsigned byte array
    """


**def intplotvecxypoint(bmp: array.array, v: list[int, int], c: int):**
>"""Sets the color of a pixel at (x, y)

    Args:
        bmp: unsigned byte array
             with bmp format
        v  : (x:int, y:int)
             pixel coordinates
        c  : unsigned int
             color value

    Returns:
        byref modified unsigned byte array
    """


**def intscalarmulvect(vec: list[numbers.Number], scalarval: numbers.Number) -> list[int]:**
>"""Scales a vector by multiplying a scalar value (float)
    to all components of the vector or a list of numbers
    then rounds off values in the list to a whole number

    Args:
        v        : the vector or
                   a list of
                   ints or floats
        scalarval: scalar value
                   (float or int)

    Returns:
        list of ints
    """


**def invertbits2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Inverts the bits in a bmp file

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def invertbitsinbuffer(buf: array.array) -> array.array:**
>"""Flips all the bits in an
        unsigned byte array

    Args:
        buf: unsigned byte array

    Returns:
        bit flipped unsigned byte array
    """


**def invertbitsincircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Inverts the bits in a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x,y)
                 and radius r
                 of the region

    Returns:
        byref modified unsigned byte array
    """


**def invertbitsincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Inverts bits in a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def invertimagebits(bmp: array.array):**
>"""Inverts the bits in a bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified unsigned byte array
    """


**def invertregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Inverts the bits in a
        rectangular region defined
        by (x1,y1) and (x2,y2)

    Args:
        bmp          :  unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: the rectangle

    Returns:
        byref modified
        unsigned byte array
    """


**def invertregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Inverts the bits in a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region

    Returns:
        new bitmap file
    """


**def isdefaultpal(bmp: array.array) -> bool:**
>"""Checks if bitmap has a default RGB color palette

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        True if default
        False if not default
    """


**def isinBMPrectbnd(bmp: array.array, x: int, y: int) -> bool:**
>"""Checks if (x,y) coordinates are within the BMP

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int value
              of location
              in x-axis and y-axis

    Returns:
        True if within bounds
        False if out of bounds
    """


**def isinrange(value: numbers.Number, highlimit: numbers.Number, lowlimit: numbers.Number) -> bool:**
>"""Checks is value is within high and low limits

    Args:
        value    : numeric variable
                   to check
        highlimit: upper limit of
                   the variable
        lowlimit : lower limit of
                   the variable

    Returns:
        True if within bounds
    """


**def isinrectbnd(x: int, y: int, xmin: int, ymin: int, xmax: int, ymax: int) -> bool:**
>"""Checks if the x and y values
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


**def isvalidcolorbit(bits: int) -> bool:**
>"""Checks if bits is in the valid
        color bits list (1, 4, 8, 24)

    Args:
        bits: int value

    Returns:
        True if bits in (1, 4, 8, 24)
        False if other values not in
              the list above
    """


**def iterbeziercurve(pntlist: list[list[int, int]]) -> list[int, int]:**
>"""Yields a list of vertices for a bezier curve
    based on 2D control points in pntlist

    Args:
        pntlist: 2D control points
                 for the bezier curve
                 as list[list[x: int,
                              y: int]]

    Yields:
        vertices as list[x: int, y: int]
    """


**def iterbspline(pntlist: list[list[int, int]], isclosed: bool, curveback: bool) -> list[int, int]:**
>"""Yields a list of vertices for a bspline curve
    based on 2D control points in pntlist

    Args:
        pntlist: 2D control points
                 for the bspline curve
                 as list[list[x: int,
                              y: int]]

    Yields:
        vertices as list[x: int, y: int]
    """


**def itercircle(x: int, y: int, r: int) -> list[int, int]:**
>"""Yields (int, int) 2D vertices along
    a path defined by radius r as it traces
    a circle with origin set at (x, y)

    Args:
        x, y: int centerpoint
                  coordinates
        r   : int radius

    Yields:
        [x: int, y: int]
    """


**def itercircleinvolute(x: int, y: int, a: float, delta: float, lim: float):**
>"""Yields (int, int) 2D vertices
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


**def itercirclepart(r: int) -> list[int, int]:**
>"""Yields (int, int) 2D vertices along
    a path defined by radius r as it traces
    one fourth of a circle with origin set
    at (0, 0)

    Args:
        r: int radius

    Yields:
        [x: int, y: int]
    """


**def itercirclepartlineedge(r: int) -> list[int, int]:**
>"""Yields (int, int) 2D vertices along
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


**def itercirclepartvertlineedge(r: int) -> list[int, int]:**
>"""Yields (int, int) 2D vertices along
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


**def itercopyrect(bmp: array.array, x1: int, y1: int, x2: int, y2: int) -> array.array:**
>"""Scan a rectangular area and yield scan lines

    Args:
        bmp            : unsigned
                         byte array
                         with bmp format
        x1, y1, x2, y2 : defines the
                         rectangle

    Yields:
        unsigned byte array
        scanlines of the area
    """


**def iterdrawvec(u: list, v: list, headsize: int):**
>"""Yields a vector (line segment with arrow head)

    Args:
        u       : (x: float, y: float)
                  point 1 origin
        v       : (x: float, y: float)
                  point 2 has arrow
        headsize: size of the arrow
                  0 for default size

    Yields:
        ((x1: int, y1: int), (x2: int, y2: int))
    """


**def iterellipse(x: int, y: int, b: int, a: int):**
>"""Yields (int, int) 2D vertices along
    a path defined by major and minor axes
    b and a as it traces an ellipse with
    origin set at (x, y)

    Args:
        b, a: major and minor axes

    Yields:
        [x: int, y: int]
    """


**def iterellipsepart(b: int, a: int):**
>"""Yields (int, int) 2D vertices along
    a path defined by major and minor axes
    b and a as it traces one fourth of an
    ellipse with origin set at (0, 0)

    Args:
        b, a: major and minor axes

    Yields:
        [x: int, y: int]
    """


**def iterellipserot(x: int, y: int, b: int, a: int, degrot: float):**
>"""Yields (int, int) 2D vertices along
    a path defined by major and minor axes
    b and a as it traces an ellipse with origin
    set at (x, y) rotated by degrot degrees

    Args:
        b, a: major and minor axes
        degrot: rotation in degrees

    Yields:
        [x: int, y: int]
    """


**def iterepicycloid(x: int, y: int, a: float, b: float, delta: float, lim: float):**
>"""Yields (int, int) 2D vertices
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


**def iterflower(cx: int, cy: int, r: int, petals: int, angrot: float):**
>"""Yields 2D points for a flower

    Args:
        cx, cy, r : center (cx,cy)
                    and radius r
        petals    : number of petals
        angrot    : angle of rotation

    Yields:
        (x: int, y: int)
    """


**def itergetcolorfromrectregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Yields color info of
        a rectangular area

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangle

    Yields:
        ((x: int, y: int), color: int)
        for all points in area
    """


**def itergetneighbors(v: list[int, int], mx: int, my: int, includecenter: bool) -> list[int, int]:**
>"""Yields the neighboring pixels of point v

    Args:
        v : (x: int, y: int) point
        mx: maximum x
        my: maximum y
        includecenter: do we yield
                       point v too

    Yields:
        [x: int, y: int]
    """


**def iterhypotrochoid(x: int, y: int, a: float, b: float, c: float, delta: float, lim: float):**
>"""Yields (int, int) 2D vertices
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


**def iterIFS(IFStransparam: tuple, x1: int, y1: int, x2: int, y2: int, xscale: int, yscale: int, xoffset: int, yoffset: int, maxiter: int):**
>"""Yield 2D points for an Interated Function System Fractal

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


**def iterimagecolor(bmp: array.array, waitmsg: str, rowprocind: str, finishmsg: str):**
>"""Yields color information for entire bitmap

    Args:
        bmp       : unsigned byte array
                    with bmp format
        waitmsg   : what to display
                    in the terminal
                    when process starts
        rowprocind: string to print in
                    the terminal as a
                    row is processed as
                    a process indicator
        finishmsg : what to display
                    in the terminal
                    when process ends

    Yields:
        ((x: int, y: int), color: int)
    """


**def iterimagedgevert(bmp: array.array, similaritythreshold: float):**
>"""Find edges in an image

    Args:
        bmp                : unsigned
                             byte array
                             with
                             bmp format
        similaritythreshold: how close
                             to the color
                             before we
                             yield it

    Yields:
        (x: int, y: int)
    """


**def iterimageregionvertbyRGB(bmp: array.array, rgb: list[int, int, int], similaritythreshold: int):**
>"""RGB Color selection by color similarity

    Args:
        bmp                : unsigned
                             byte array
                             with bmp
                             format
        rgb                : (r: byte,
                              g: byte,
                              b: byte)
        similaritythreshold: how close
                             to the color
                             before we
                             yield it

    Yields:
        ((x: int, y: int), (r: byte, g: byte, b: byte))
    """


**def iterimageRGB(bmp: array.array, waitmsg: str, rowprocind: str, finishmsg: str):**
>"""Yields (r, g, b) information for the entire bitmap

    Args:
        bmp       : unsigned byte array
                    with bmp format
        waitmsg   : what to display
                    in terminal at
                    process start
        rowprocind: char to display as
                    a row is processed
        finishmsg : what to display
                    in terminal at
                    process end

    Yields:
        ((x: int, y: int), (r: byte, g: byte, b: byte))
    """


**def iterline(p1: list[int, int], p2: list[int, int]) -> list[int, int]:**
>"""Yields (int, int) 2D vertices
    along a line segment defined
    by endpoints p1 and p2

    Args:
        p1, p2: line endpoints
                both [x:int, y:int]

    Yields:
        [x:int, y:int]
    """


**def iterlissajouscurve(x: int, y: int, a: float, b: float, c: float, d: float, e: float, delta: float, lim: float):**
>"""Yields (int, int) 2D vertices
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


**def itermandelbrot(x1: int, y1: int, x2: int, y2: int, mandelparam: list[float, float, float, float], maxiter: int):**
>"""Yields a Mandelbrot set

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

    Yields:
        (x:int, y: int, c: int)
    """


**def iterparallelogram(p1: list[int, int], p2: list[int, int], p3: list[int, int]) -> list[int, int]:**
>"""None"""


**def iterspirograph(x: int, y: int, r: int, l: float, k: float, delta: float, lim: float):**
>"""Yields (int, int) 2D vertices
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


**def line(bmp: array.array, x1: int, y1: int, x2: int, y2: int, color: int):**
>"""Draw a Line in a bitmap

    Args:
        bmp   : unsigned byte array
                with bmp format
        x1, y1: endpoint 1
        x2, y2: endpoint 2
        color : color of the line

    Returns:
        byref modified
        unsigned byte array
    """


**def linevec(bmp: array.array, u: list, v: list, color: int):**
>"""Draw a line in a bitmap

    Args:
        bmp  : unsigned byte array
               with bmp format
        u, v : (x:float,y:float)
               the endpoints
               of the line
        color: the color of the line

    Returns:
        byref modified unsigned byte array
    """


**def lissajouscurvevert(x: int, y: int, a: float, b: float, c: float, d: float, e: float, delta: float, lim: float):**
>"""Returns (int, int) 2D vertices
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


**def listinBMPrecbnd(bmp: array.array, xylist: list) -> bool:**
>"""Checks if a list of (x, y) coordinates are within the BMP

    Args:
        bmp   : unsigned byte array
                with bmp format
        xylist: list of (x, y)
                coordinates
                to be checked

    Returns:
        True if within bounds
        False if out of bounds
    """


**def listinrecbnd(xylist: list[list[numbers.Number, numbers.Number]], xmin: int, ymin: int, xmax: int, ymax: int) -> bool:**
>"""Checks if all the values in a
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


**def loadBMP(filename: str) -> array.array:**
>"""Load bitmap to a byte array
       (uncompressed bitmap only)

    Args:
        filename: full path to
                  the file to be loaded

    Returns:
        byte array with bmp file contents
    """


**def LSMslope(XYdata: list) -> float:**
>"""Slope of a line obtained by Least Squares Method

    Args:
        XYdata: list of vectors
        first two values in the
        list must be [[x, y, ..,], ...]

    Returns:
        float slope of line
    """


**def LSMYint(XYdata: list) -> float:**
>"""Returns the y-intercept of a line obtained
    by Least Squares Method

    Args:
        XYdata: list of vectors
        first two values in the
        list must be [[x, y, ..,], ...]

    Returns:
        float y-intercept of line
    """


**def magnifyNtimescircregion(bmp: array.array, x: int, y: int, r: int, n: int):**
>"""Magnify a circular region in a bitmap file by int n

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x,y)
                 and radius r
        n      : int magnification
                 factor

    Returns:
        byref modified unsigned byte array
    """


**def magnifyNtimescircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, intmagfactor: int):**
>"""Magnify a circular region by an integer factor n times

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
        intmagfactor   : int magnification
                         factor

    Returns:
        new bitmap file
    """


**def makeBGRbuf(bbuf: array.array, gbuf: array.array, rbuf: array.array) -> array.array:**
>"""Assemble a BGR buffer from
        blue, green and red buffers

    Args:
        bbuf: unsigned byte array
              for blue data
        gbuf: unsigned byte array
              for green data
        rbuf: unsigned byte array
              for red data

    Returns:
        unsigned byte array
        holding BGR data
    """


**def makenewpalfromcolorhist(chist: list, colors: int, similaritythreshold: float) -> list:**
>"""Creates a new palatte based on a color histogram

    Args:
        chist              : list sorted in
                             descending order
                             of color
                             frequencies
        colors             : maximum colors
                             of new palette
        similaritythreshold: controls how
                             close palette
                             entries can be

    Returns:
        unsigned byte array with bmp format
    """


**def mandelbrot(bmp: array.array, x1: int, y1: int, x2: int, y2: int, mandelparam: list[float, float, float, float], RGBfactors: list[float, float, float], maxiter: int):**
>"""Draw a Mandelbrot set

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
        byref modified unsigned byte array
    """


**def mandelparamdict() -> dict:**
>"""None"""


**def matchRGBtopal(RGB: list, pal: list) -> int:**
>"""Color matching from a 24-bit
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


**def mirror(pt: float, delta: float):**
>"""Mirrors a value in a numberline

    Args:
        pt   : real value in numberline
        delta: value to mirror

    Returns:
        pt - delta, pt + delta
    """


**def mirrorbottom(bmp: array.array):**
>"""Mirrors the bottom-half of a bmp

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrorbottom2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Mirrors the bottom half of a BMP

    Args:
        ExistingBMPfile: Whole path
                         to an existing
                         file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def mirrorbottomincircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Mirror the bottom-half of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of region

    Returns:
        byref modified unsigned byte array
    """


**def mirrorbottomincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Mirror the bottom-half of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def mirrorbottominregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Mirror the bottom-half
        of a rectangular region

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangle

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrorbottominregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the bottom-half region in a rectangular area in a bmp

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region

    Returns:
        new bitmap file
    """


**def mirrorbottomleft(bmp: array.array):**
>"""Mirrors the bottom-left part
        of an in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrorbottomleft2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Mirrors the bottom-left of a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def mirrorbottomleftincircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Mirror the bottom-left of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x,y) and
                 radius r of region

    Returns:
        byref modified unsigned byte array
    """


**def mirrorbottomleftincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Mirror the bottom-left of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def mirrorbottomleftinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the bottom-left of a
        rectangular region defined
        by (x1, y1) and (x2, y2)

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangle

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrorbottomleftinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the bottom-left region in a rectangular area in a bmp

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region

    Returns:
        new bitmap file
    """


**def mirrorbottomright(bmp: array.array):**
>"""Mirrors the bottom right part
        of an in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrorbottomright2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Mirrors the bottom-right of a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def mirrorbottomrightincircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Mirror the bottom-right of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x,y) and
                 radius r of region

    Returns:
        byref modified unsigned byte array
    """


**def mirrorbottomrightincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Mirror the bottom-right of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def mirrorbottomrightinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the bottom-right of a
        rectangular region defined by
        (x1, y1) and (x2, y2)

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: the rectangular
                        region

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrorbottomrightinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the bottom-right region in a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2  :the rectangular
                         region

    Returns:
        new bitmap file
    """


**def mirrorleft(bmp: array.array):**
>"""Mirrors the left-half of an
        in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrorleft2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Mirrors the left-half of a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def mirrorleftincircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Mirrors the top-left of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y) and
                 radius r of region

    Returns:
        byref modified unsigned byte array
    """


**def mirrorleftincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Mirror the left-half of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def mirrorleftinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the left-half
        of a rectangular area

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangle

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrorleftinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the left-half region in a rectangular area in a bmp

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region

    Returns:
        new bitmap file
    """


**def mirrorright(bmp: array.array):**
>"""Mirrors the right-half of an
        in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrorright2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Mirrors the right half of a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def mirrorrightincircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Mirrors the right-half of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of a region

    Returns:
        byref modified unsigned byte array
    """


**def mirrorrightincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Mirror the right-half of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def mirrorrightinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the right-half of
        a rectangular area in a bitmap

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangle

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrorrightinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the right-half region in a rectangular area in a bmp

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region

    Returns:
        new bitmap file
    """


**def mirrortop(bmp: array.array):**
>"""Mirrors the top-half of a bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrortop2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Mirrors the top-half of a bitmap

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def mirrortopincircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Mirror the top-half of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r of area

    Returns:
        byref modified unsigned byte array
    """


**def mirrortopincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Mirror the top-half of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def mirrortopinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Mirror the top-half of
        a rectangular region

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangular
                        region

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrortopinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the top-half region in a rectangular area in a bmp

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region

    Returns:
        new bitmap file

    """


**def mirrortopleft(bmp):**
>"""Mirrors the top-left part
        of an in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrortopleft2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Mirrors the top-left of a bitmap

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def mirrortopleftincircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Mirror the top-left of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of region

    Returns:
        byref modified unsigned byte array
    """


**def mirrortopleftincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Mirror the top-left of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def mirrortopleftinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the top-left of a
        rectangular region defined by
        (x1, y1) and (x2, y2)

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangle

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrortopleftinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the top-left region in a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region

    Returns:
        new bitmap file
    """


**def mirrortopright(bmp: array.array):**
>"""Mirrors the top-right part
        of an in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrortopright2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Mirrors the top-right of a
        bitmap file

    Args:
        ExistingBMPfile: Whole path
                         to existing
                         file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def mirrortoprightincircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Mirror the top-right of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y) and
                 radius r of region

    Returns:
        byref modified unsigned byte array
    """


**def mirrortoprightincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Mirror the top-right of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def mirrortoprightinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the top-right of a
        rectangular region defined by
        (x1, y1) and (x2, y2)

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangle

    Returns:
        byref modified
        unsigned byte array
    """


**def mirrortoprightinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Mirrors the top-right region in a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region

    Returns:
        new bitmap file
    """


**def monochrome(rgb: list[int, int, int]) -> list[int, int, int]:**
>"""Returns a monochrome color
        based on a 24-bit RGB value

    Args:
        rgb: color values
            [r: byte, g: byte, b: byte]

    Returns:
        a gray color (r = g = b)
        [r: byte, g: byte, b: byte]
    """


**def monochrome2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Applies a monochrome filter to a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def monochromecircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Monochrome filter to a circular region

    Args:
        ExistingBMPfile: Whole path
                         to an existing
                         file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def monochromefiltertoBGRbuf(buf: array.array) -> array.array:**
>"""Apply a monochrome filter to a
        BGR buffer

    Args:
        buf: unsigned byte array
             holding BGR data

        rgbfactors: color filter as
                      [r: float,
                       g: float,
                       b: float]

    Returns:
        unsigned byte array
        holding mono BGR data
    """


**def monochromepal(bits: int, rgbfactors: list[float, float, float]) -> list[list[int, int, int]]:**
>"""Returns a monochrome palette
        based on bit depth bits and
        rgbfactors

    Args:
        bits      : bit depth
                    (1, 4, 8)
        rgbfactors: color values
                    0.0 to 1.0
                    [r: float,
                     g: float,
                     b: float]

    Returns:
      a palette as
      list[list[r: int, g: int, b int]]
    """


**def monocircle(bmp: array.array, x: int, y: int, r: int):**
>"""Monochrome filter to a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of the region

    Returns:
        byref modified unsigned byte array
    """


**def monofilterinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Monochrome filter to rectangular area in a 24-bit BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region

    Returns:
        new bitmap file
    """


**def monofilterto24bitimage(bmp: array.array):**
>"""Applies a mono filter
        to a 24 bit in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified
        unsigned byte array
    """


**def monofilterto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Applies a monochrome filter
        to a rectangular area
        defined by (x1, y1) and
        (x2, y2) in a 24 bit bitmap

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: the rectangle

    Returns:
        byref modified
        unsigned byte array
    """


**def newBMP(x: int, y: int, colorbits: int) -> array.array:**
>"""Creates a new in-memory bitmap

    Args:
        x, y     : unsigned int values
                   of x and y dims
        colorbits: bit depth
                   (1, 4, 8, 24) bits

    Returns:
        unsigned byte array with bitmap layout
    """


**def numbervert(bmp: array.array, vlist: list[list[int, int]], xadj: int, yadj: int, scale: int, valstart: numbers.Number, valstep: numbers.Number, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list, suppresszero: bool, suppresslastnum: bool, rightjustify: bool):**
>"""None"""


**def octahedravert(x: float) -> list[list[float, float, float]]:**
>"""Returns a list of vertices
        for an octrahedron

    Args:
        x: length of a side

    Returns:
        list (x: float,
              y: float,
              z: float)
    """


**def outline(bmp: array.array):**
>"""Applies an Outline Filter

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified unsigned byte array
    """


**def outline2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Applies an outline filter

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def outlinecircregion(bmp: array.array, x: int, y: int, r: int):**
>"""Outlines a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of the region

    Returns:
        byref modified unsigned byte array
    """


**def outlinecircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):**
>"""Outlines area in a circular region

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r

    Returns:
        new bitmap file
    """


**def outlineregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):**
>"""Outines a rectangular region in a BMP

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines
                        the rectangular
                        region

    Returns:
        byref modified unsigned byte array
    """


**def outlineregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):**
>"""Outline filter to rectangular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x1, y1, x2, y2 : defines the
                         rectangular
                         region

    Returns:
        new bitmap file
    """


**def pastecirularbuf(bmp: array.array, x: int, y: int, circbuf: list):**
>"""Paste a circular buffer with a
    given radius to a centerpoint at (x, y)

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y   : center of circular
                 region
        circbuf: list generated by
                 copycircregion2buf

    Returns:
        byref modified unsigned byte array
    """


**def pasterect(bmp: array.array, buf: array.array, x1: int, y1: int):**
>"""Paste a rectangular area from a buffer to a bmp

    Args:
        bmp   : unsigned byte array
                with bmp format
        buf   : rectangular
                image buffer
        x1, y1: point to paste
                the buffer

    Returns:
        byref modified unsigned byte array
    """


**def perspective(vlist: list[list[numbers.Number, numbers.Number, numbers.Number]], rotvec: list[list[float, float], list[float, float], list[float, float]], dispvec: list[numbers.Number, numbers.Number, numbers.Number], d: float) -> tuple:**
>"""Projects 3D points to 2D and
        apply rotation and translation
        vectors

    Args:
        vlist  : list of 3D vertices
        rotvec : 3D rotation vector
        dispvec: 3D translation vector
        d      : Distance of observer
                 from the screen

    Returns:
        tuple (list, list)
    """


**def piechart(bmp: array.array, x: int, y: int, r: int, dataandcolorlist: list):**
>"""Draw a piechart

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y, r         : center (x, y)
                          and radius r
        dataandcolorlist: stuff to plot
                          + color

    Returns:
        byref modified unsigned byte array

    """


**def pixelizenxn(bmp: array.array, n: int) -> array.array:**
>"""Pixelize a whole image with n by n areas
    in which colors are averaged

    Args:
        bmp: unsigned byte array
             with bmp format
        n  : size of pixel blur

    Returns:
        byref modified unsigned byte array
    """


**def pixelizenxncircregion(bmp: array.array, x: int, y: int, r: int, n: int):**
>"""Pixelize a circular region in a BMP by n

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
        n      : integer pixellation
                 dimension n by n

    Returns:
        byref modified unsigned byte array
    """


**def pixelizenxncircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, intpixsize: int):**
>"""Apply a Pixel Blur in a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
        intpixsize     : n by n
                         pixel blur size

    Returns:
        new bitmap file
    """


**def pixelizenxntofile(ExistingBMPfile: str, NewBMPfile: str, n: int):**
>"""Pixellate a bitmap file with n by n pixel areas

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def plot3d(bmp: array.array, sides: list[list, list], issolid: bool, RGBfactors: list[float, float], showoutline: bool, outlinecolor: int):**
>"""The 3D rendering function

    Args:
        bmp         : unsigned
                      byte array
                      with bmp format
        sides       : list of polygons
                      and normals
        isolid      : toggles solid render
        RGBfactors  : [r,g,b] r, g, b
                      range in value
                      from 0.0 to 1.0
        showoutine  : toggles the
                      polygon outline
        outlinecolor: color of the
                      polygon outline

    Returns:
        byref modified unsigned byte array
    """


**def plot3Dsolid(bmp: array.array, vertandsides: list[list, list], issolid: bool, RGBfactors: list[float, float, float], showoutline: bool, outlinecolor: int, rotvect: list[float, float, float], transvect3D: list[float, float, float], d: int, transvect: list[int, int]):**
>"""3D solid rendering function

    Args:
        bmp         : unsigned
                      byte array
                      with bmp format
        sides       : list of polygons
                      and normals
        isolid      : toggles the
                      solid render
        RGBfactors  : [r,g,b] r, g, b
                      range in value
                      from 0.0 to 1.0
        showoutine  : toggles the
                      polygon outline
        outlinecolor: color of the
                      polygon outline
        rotvect     : rotation vector
        transvect3D : 3D translation
                      vector
        d           : distance of the
                      observer from
                      the screen
        transvect   : 2D translation
                      vector for
                      screen position

    Returns:
        byref modified unsigned byte array
    """


**def plot8bitpattern(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit pattern

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plot8bitpatternasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit pattern as circles

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the
                    pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plot8bitpatternastext(bitpattern: list[int], onechar: str, zerochar: str):**
>"""Outputs the bits of a list
        of bytes to console

    Args:
        bitpattern: list of bytes
        onechar   : char to display
                    if bit is 1
        zeropchar : char to display
                    if bit is 0

    Returns:
        console output
    """


**def plot8bitpatternsideway(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit pattern sideways

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to
                    draw the pattern
        bitpattern: list of bytes that
                    makes the pattern
        scale     : control how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plot8bitpatternsidewaywithdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit pattern sideways with dots

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to
                    draw the pattern
        bitpattern: list of bytes that
                    makes the pattern
        scale     : control how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plot8bitpatternsidewaywithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):**
>"""Draws a 8-bit pattern sideways with a function

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to
                    draw the pattern
        bitpattern: list of bytes that
                    makes the pattern
        scale     : control how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plot8bitpatternupsidedown(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit pattern upsidedown

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to
                    draw the pattern
        bitpattern: list of bytes that
                    makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the
                    pattern

    Returns:
        byref modified unsigned byte array
    """


**def plot8bitpatternupsidedownasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit pattern upsidedown with dots

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to
                    draw the pattern
        bitpattern: list of bytes that
                    makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plot8bitpatternupsidedownwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):**
>"""Draws a 8-bit pattern upsidedown with a function

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to
                    draw the pattern
        bitpattern: list of bytes that
                    makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern
        fn        : function

    Returns:
        byref modified unsigned byte array
    """


**def plot8bitpatternwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):**
>"""8-bit pattern with a function

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the
                    pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotbitsastext(bits: int):**
>"""Outputs the bits of byte to
        console

    Args:
        bits: byte value

    Returns:
        space for 0
        *     for 1
    """


**def plotbmpastext(bmp: array.array):**
>"""Plot a bitmap as text
    (cannot output 24-bit bmp)

    Args:
        bmp : unsigned byte array
              with bmp format

    Returns:
        console text output
        for debug and ascii art

    """


**def plotcircinsqr(bmp, x, y, d, color):**
>"""Draws a circle in an
        invisible square with side
        equal to the circle's diameter
        and positioned by (x, y)
        at  the upper left
        of the bounding square

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        d         : diameter of the
                    circle
     Returns:
        byref modified unsigned byte array
    """


**def plotfilledflower(bmp: array.array, cx: int, cy: int, r: int, petals: float, angrot: float, lumrange: list[int, int], RGBfactors: list[float, float, float]):**
>"""Draw a filled flower

    Args:
        bmp       : unsigned byte array
                    with bmp format
        cx, cy, r : center (cx, cy)
                    and radius r
        petals    : number of petals
        angrot    : angle of rotation
        lumrange  : (byte:byte) range
                    of brightness
        rgbfactors: [r, g, b] values
                    of r, g and b
                    range from
                    0.0 to 1.0

    Returns:
        byref modified unsigned byte array

    """


**def plotflower(bmp: array.array, cx: int, cy: int, r: int, petals: float, angrot: float, lumrange: list[int, int], RGBfactors: list[float, float, float]):**
>"""Draw a flower

    Args:
        bmp       : unsigned byte array
                    with bmp format
        cx, cy, r : center (cx,cy)
                    and radius r
        petals    : number of petals
        angrot    : angle of rotation
        lumrange  : (byte:byte) range
                    of brightness for
                    the gradient
        rgbfactors: [r, g, b] values
                    all range from
                    0.0 to 1.0

    Returns:
        byref modified unsigned byte array
    """


**def plotimgedges(bmp: array.array, similaritythreshold: int, edgeradius: int, edgecolor: int):**
>"""Draw edges

    Args:
        bmp                : unsigned
                             byte array
                             with bmp
                             format
        similaritythreshold: controls
                             the edge
                             detection
                             sensitivity
        edgeradius         : radius and
        edgecolor            color of
                             the pen
                             used to
                             draw the
                             edges

    Returns:
        byref modified unsigned byte array
    """


**def plotitalic8bitpattern(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit italic pattern

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the
                    pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit
        color     : color of pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotitalic8bitpatternasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit italic pattern as dots

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotitalic8bitpatternsideway(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws an italic 8-bit pattern sideways

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to
                    draw the pattern
        bitpattern: list of bytes that
                    makes the pattern
        scale     : control how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotitalic8bitpatternsidewayasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws an italic 8-bit pattern sideways as dots

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to
                    draw the pattern
        bitpattern: list of bytes that
                    makes the pattern
        scale     : control how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotitalic8bitpatternsidewaywithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):**
>"""Draws an Italic 8-bit pattern sideways with a function

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to
                    draw the pattern
        bitpattern: list of bytes that
                    makes the pattern
        scale     : control how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotitalic8bitpatternupdsidedownasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit italic pattern upsidedown as dots

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotitalic8bitpatternupsidedownwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):**
>"""Italic 8-bit pattern upsidedown with a function

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to
                    draw the pattern
        bitpattern: list of bytes that
                    makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern
        fn        : function

    Returns:
        byref modified unsigned byte array
    """


**def plotitalic8bitpatternwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):**
>"""Italic 8-bit pattern with a function

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the
                    pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotitalicstring(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string as Italic

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the
                          string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotitalicstringasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string as Italic dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the
                          string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotitalicstringsideway(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws an Italic String Sideways

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
                          can be an int
                              or a
                          list of ints
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotitalicstringsidewayasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws an italic string sideways as dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotitalicstringvertical(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws an italic string vertically with dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotitalicstringverticalasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws an italic string vertically with dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotlines(bmp: array.array, vertlist: list, color: int):**
>"""Draws connected lines defined by a list of vertices

    Args:
        bmp     : unsigned byte array
                  with bmp format
        vertlist: [(x:uint,y:uint),...]
                  list of vertices
        color   : color of the lines

    Returns:
        byref modified unsigned byte array
    """


**def plotpoly(bmp: array.array, vertlist: list, color: int):**
>"""Draws a polygon defined by a list of vertices

    Args:
        bmp     : unsigned byte array
                  with bmp format
        vertlist: [(x:uint,y:uint),...]
                  list of vertices
        color   : color of the lines

    Returns:
        byref modified unsigned byte array
    """


**def plotpolyfill(bmp: array.array, vertlist: list[list[numbers.Number, numbers.Number]], color: int):**
>"""Draws a filled polygon with a given color

    Args:
        bmp     : unsigned byte array
                  with bmp format
        vertlist: [(x, y), ...]
                  list of vertices
        color   : color of the
                  filled polygon

    Returns:
        byref modified unsigned byte array
    """


**def plotpolyfillist(bmp: array.array, sides: list[list[list[list]], list[list[float, float, float]]], RGBfactors: list[float, float]):**
>"""3D polygon rendering function

    Args:
        bmp       : unsigned byte array
                    with bmp format
        sides     : list of polygons
                    and normals
        RGBfactors: [r, g, b]
                    r, g, b are
                    float values
                    from 0.0 to 1.0

    Returns:
        byref modified unsigned byte array
    """


**def plotpolylist(bmp: array.array, polylist: list, color: int):**
>"""Draws a list of polygons of a given color

    Args:
        bmp      : unsigned byte array
                   with bmp format
        polytlist: [[(x:uint,y:uint),
                    ...],...]
                   list of polygons
        color    : color of the lines

    Returns:
        byref modified unsigned byte array
    """


**def plotreverseditalic8bitpattern(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit reversed italic pattern

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotreverseditalic8bitpatternasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit reversed italic pattern as dots

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotreverseditalicstring(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a reversed string as Italic

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of font
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotreverseditalicstringasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a Reversed String as Italic dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the
                          string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotreversestring(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string reversed

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotreversestringasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string reversed with dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotRGBxybit(bmp: array.array, x: int, y: int, rgb: list):**
>"""Sets pixel at (x, y) in a bitmap to color [R, G, B]

    Args:
        bmp: unsigned byte array
             with bmp format
        x,y: unsigned int locations
             in x and y
        rgb: color defined by
             [R: byte, G: byte, B: byte]

    Returns:
        byref modified unsigned byte array
    """


**def plotRGBxybitvec(bmp: array.array, v: list, rgb: list):**
>"""Sets [R, G, B] of pixel at (x, y)

    Args:
        bmp: unsigned byte array
             with bmp format
        v  : (x: float, y: float)
        rgb: [R: byte,
              G: byte,
              B: byte]

    Returns:
        byref modified unsigned byte array
    """


**def plotrotated8bitpattern(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit pattern with the bits rotated

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : where to draw
                    the pattern
        bitpattern: list of bytes
                    that make a pattern
        scale     : control how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the
                    pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotrotated8bitpatternwithdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit pattern with the bits rotated

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : where to draw
                    the pattern
        bitpattern: list of bytes
                    that make a pattern
        scale     : control how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the
                    pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotrotated8bitpatternwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):**
>"""Draws a 8-bit pattern with
    the bits rotated with a function

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : where to draw
                    the pattern
        bitpattern: list of bytes
                    that make a pattern
        scale     : control how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotrotateditalic8bitpatternwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):**
>"""Bit rotated Italic 8-bit pattern
    with a function

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the
                    pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotstring(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the
                          string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
                          (can be an int
                               or a
                          list of ints)
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotstringasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string as Dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of the font
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotstringfunc(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list, orderfunc: Callable, fontrenderfunc: Callable):**
>"""Draws a string

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
            `             each bit
        spacebetweenchar: space between
                          the characters
        color           : color of the font
        fontbuf         : the font
                          (see fonts.py)
        orderfunc       : function that
                          enumerates
                          each char
                          in the
                          input string
        fontrenderfunc  : function that
                          renders the font

    Returns:
        byref modified unsigned byte array
    """


**def plotstringsideway(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string sideways

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotstringsidewayasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string sideways as dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotstringsidewayfn(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list, fn: Callable):**
>"""Draws a string sideways with a function

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotstringupsidedown(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string upsidedown

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotstringupsidedownasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string upsidedown as dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of the font
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotstringvertical(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string vertically

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotstringverticalasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draws a string vertically with dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotstringverticalwithfn(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list, fn: Callable):**
>"""Draws a string vertically using a function

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                         (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotupsidedownitalic8bitpattern(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit italic pattern upsidedown

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotupsidedownitalic8bitpatternasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):**
>"""Draws a 8-bit italic pattern upsidedown as dots

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : sets where to draw
                    the pattern
        bitpattern: list of bytes
                    that makes the pattern
        scale     : controls how big
                    the pattern is
        pixspace  : space between
                    each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array
    """


**def plotupsidedownitalicstring(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draw an italic string upsidedown

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the
                          string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotupsidedownitalicstringasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):**
>"""Draw an italic string upsidedown as dots

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        x, y            : sets where to
                          draw the
                          string
        str2plot        : string to draw
        scale           : control how big
                          the font is
        pixspace        : space between
                          each bit
        spacebetweenchar: space between
                          the characters
        color           : color of
                          the font
        fontbuf         : the font
                          (see fonts.py)

    Returns:
        byref modified unsigned byte array
    """


**def plotvecxypoint(bmp: array.array, v: list, c: int):**
>"""Sets the color of a pixel
        at (x, y)

    Args:
        bmp: unsigned byte array
             with bmp format
        v  : (x:float, y:float)
                    or
             (x:int, y:int)
        c  : unsigned int
             color value

    Returns:
        byref modified
        unsigned byte array
    """


**def plotxybit(bmp: array.array, x: int, y: int, c: int):**
>"""Sets pixel at (x, y) in a bitmap to color c

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int
              locations in x and y
        c   : unsigned int color

    Returns:
        byref modified unsigned byte array
    """


**def plotxypointlist(bmp: array.array, vlist: list, penradius: int, color: int):**
>"""Draws a circle or a point
    depending on the penradius
    with a given color for
    all points in a point list

    Args:
        bmp      : unsigned byte array
                   with bmp format
        vlist    : [(x: uint, y: uint) ,...]
                   list of points
        penradius: radius of the pen
                   (in pixels)
        color    : color of the pen

    Returns:
        byref modified unsigned byte array
    """


**def polar2rectcoord2D(vpolarcoord: list[float, float]) -> list[float, float]:**
>"""Converts from polar coordinates with
    origin at (0, 0) to 2D rectangular coordinates

    Args:
        vcylindcoord:(r: float,
                  theta: float)

    Returns:
        [x: float,
         y: float]
    """


**def polyboundary(vertlist: list[list[int, int]]) -> list[list[int, int]]:**
>"""Generates a polygon boundary
        from a list of 2D vertices

    Args:
        polybnd : list of 2D vertices
                  list[list[x: int,
                            y: int]]

    Returns:
        list[list[x: int, y: int]]
        A list of vertices that traces
        the boundaries of the polygon
    """


**def probplotRGBto1bit(rgb: list[int, int, int], brightness: int) -> int:**
>"""Use a non deterministic plot
        to convert 24-bit colors to
        1-bit

    Args:
        rgb: color byte values
             [r: byte,
              g: byte,
              b: byte]

    Returns:
        0 or 1
    """


**def range2baseanddelta(lst_range: list[int, int]):**
>"""Gets the base and range values in a list of numbers

    Args:
        lst_range: list[min: int,
                        max: int]

    Returns:
        minimum value and delta of min and max value
        in lst_range
    """


**def readint(offset: int, cnt: int, arr: int) -> int:**
>"""Reads an integer value in an
        unsigned byte array

    Args:
        offset: uint starting offset in
                buffer or array
                to read from
        cnt   : uint length of int data
                to read
        arr   : unsigned byte array
                to read int data from

    Returns:
        unsigned int value
    """


**def rectangle(bmp: array.array, x1: int, y1: int, x2: int, y2: int, color: int):**
>"""Draws a Rectangle

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: the rectangular
                        region
        color         : color of the
                        rectangle

    Returns:
        byref modified unsigned byte array
    """


**def rectangle2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, color: int):**
>"""Draws a Rectangle

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular region
        color          : color of rectangle

    Returns:
        new bitmap file
    """


**def rectboundarycoords(vlist: list) -> list:**
>"""Returns the rectangular bounds of a list of 2D vertices

    Args:
        vlist: list[(x: int, y :int)]

    Yields:
        ((min(x), min(y)),
         (max(x), max(y)))
    """


**def recvert(x1: int, y1: int, x2: int, y2: int) -> list[list[int, int], list[int, int], list[int, int], list[int, int]]:**
>"""Creates a list of vertices for a rectangle

    Args:
        x1, y1, x1, y2: int values

    Returns:
        list of vertices
        [(x1, y1), (x2, y1),
         (x2, y2), (x1, y2)]
    """


**def reduce24bitimagebits(Existing24BMPfile: str, NewBMPfile: str, newbits: int, similaritythreshold: float, usemonopal: bool, RGBfactors: list[float, float, float] = None):**
>"""Reduce bits used to encode color in a 24-bit BMP

    Args:
        ExistingBMPfile    : Whole path
                             to existing file
        NewBMPfile         : New file to
                             save changes in
        newbits            : can be 1, 4
                             or 8 bits
        similaritythreshold: how close can
                             a color be to
                             another color
        usemonopal         : True -> image
                             will be mono
        RGBfactors         : (r: float,
                              b: float,
                              g: float)
                             values range
                             from 0 to 1
                             used only if
                             usemonopal
                             is True
    Returns:
        new bitmap file

    """


**def regpolygonvert(cx: int, cy: int, r: int, sides: int, angle: float) -> list[list[int, int]]:**
>"""Creates a list of int vertices for a regular polygon

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


**def resizebufNtimesbigger(buf: array.array, n: int, bits: int) -> array.array:**
>"""Resize a buffer n times bigger
        given a particular bit depth n

    Args:
        buf : array to resize
        n   : resize factor
        bits: bit depth of
              color info
              (1, 4, 8, 24) bits

    Returns:
        list
    """


**def resizeNtimesbigger(bmp: array.array, n: int):**
>"""Resize an in-memory bmp
        n times bigger

    Args:
        buf : array to resize
        n   : resize factor
        bits: bit depth of
              the color info
              (1, 4, 8, 24)

    Returns:
        unsigned byte array
    """


**def resizeNtimesbigger2file(ExistingBMPfile: str, NewBMPfile: str, n: int):**
>"""Resize a bitmap file n times bigger

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def resizeNtimessmaller(bmp: array.array, n: int) -> array.array:**
>"""Resize a whole image int n times smaller

    Args:
        bmp: unsigned byte array
             with bmp format
        n  : int resize factor

    Returns:
        byref modified unsigned byte array
    """


**def resizeNtimessmaller2file(ExistingBMPfile: str, NewBMPfile: str, n: int):**
>"""Resize a bitmap file n times smaller

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def resizesmaller24bitbuf(buf: array.array) -> array.array:**
>"""Resize a 24-bit buffer
        n times smaller

    Args:
        buf: unsigned byte array
        n  : buffer multiplier

    Returns:
        unsigned byte array
    """


**def RGB2BGRarr(r: int, g: int, b: int) -> array.array:**
>"""Returns a bgr array from
        individual r, g and b color
        component inputs

    Args:
        r, g, b: byte color values

    Returns:
        unsigned byte BGR array
    """


**def RGB2BGRbuf(buf: array.array):**
>"""Convert an RGB buffer
             to a BGR buffer

    Args:
        buf: unsigned byte array
             holding RGB data

    Returns:
        byref unsigned byte array
        holding BGR data
    """


**def RGB2HSL(r: int, g: int, b: int) -> list[int, int, int]:**
>"""Converts an RGB value to HSL

    Args:
        r: unsigned byte red value
        g: unsigned byte green value
        b: unsigned byte blue value

    Returns:
        [hue: int,  ->  in degrees
         sat: int,  ->  percentage
         lum: int]  ->  percentage
    """


**def RGB2int(r: int, g: int, b: int) -> int:**
>"""Pack byte r, g and b color value
        components to an int
        representation for a
        specific color

    Args:
        r, g, b: color byte values

    Returns:
        int color val
    """


**def RGBfactors2RGB(RGBfactors: list[float, float, float], bytelum: int) -> list[int, int, int]:**
>"""Mix a byte luminosity value to
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


**def RGBfactorstoBaseandRange(lumrange: list[int, int], rgbfactors: list[float, float, float]):**
>"""Get base color luminosity and
        luminosity range from color
        expressed as r, g, b  float
        values and min and max byte
        luminosity values

    Args:
        lumrange: [minval: byte
                   maxval: byte]

        rgbfactors: color  as
                    [r: float,
                     g: float,
                     b: float]

    Returns:
        base luminosity as
        [r: byte, g: byte, b: byte]

        luminosity range as
        [r: byte, g: byte, b: byte]
    """


**def RGBpalbrightnessadjust(bmp: array.array, percentadj: float) -> list:**
>"""Copies the RGB palette info from
    a source unsigned byte array to
    a destination unsigned byte array

    Args:
        bmp       : unsigned byte array
                    with bmp format
        percentadj: signed float
                    brightness adj in %

    Returns:
        list of modified RGB values
    """


**def rotatebits(bits: int) -> int:**
>"""Rotates the bits in a byte

    Args:
        bits: the int 8 bits to rotate

    Returns:
        int value of rotated 8 bits
    """


**def rotatebitsinbuf(buf: array.array) -> array.array:**
>"""Does a bit rotate to the bytes
        in an unsigned byte array

    Args:
        buf: unsigned byte array

    Returns:
        unsigned byte array
    """


**def rotvec3D(roll: float, pitch: float, yaw: float) -> tuple:**
>"""Returns a 3D rotation vector

    Args:
        All input arguements are in
        degrees (roll, pitch, yaw)

    Returns:
        tuple ((float, float),
               (float, float),
               (float, float))
    """


**def roundpen(bmp: array.array, point: list, penradius: int, color: int):**
>"""Draws a circle or a point
    depending on the penradius
    with a given color

    Args:
        bmp      : unsigned byte array
                   with bmp format
        point    : (x:uint,y:uint)
                   centerpoint
        penradius: radius of the
                   pen in pixels
        color    : color of the pen

    Returns:
        byref modified unsigned byte array
    """


**def roundvect(v: list[numbers.Number]) -> list[int]:**
>"""Rounds off the components of a vector
       (list of floats -> list of ints)

    Args:
        v: list of floats

    Returns:
        list of ints
    """


**def saveBMP(filename: str, bmp: array.array):**
>"""Saves bitmap to file

    Args:
        filename: full path to
                  the file to be saved
        bmp     : unsigned byte array
                  with the layout of
                  a bitmap file
    Returns:
        A Bitmap File
    """


**def setBMP2monochrome(bmp: array.array, RGBfactors: list[float, float, float]) -> list:**
>"""Sets a bitmap to use a monochrome palette

    Args:
        bmp       : unsigned byte array
                    with bmp format
        RGBfactors: (r, g, b)
                    all values range
                    from 0.0 to 1.0

    Returns:
        list of modified RGB values
        byref modified byte array
    """


**def setBMPimgbytes(bmp: array.array, buf: array.array):**
>"""Sets the raw image buffer of a bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
        buf: array of unsigned bytes

    Returns:
        byref modified  unsigned byte array
    """


**def setbmppal(bmp: array.array, pallist: list):**
>"""Sets the RGB palette of a bitmap

    Args:
        bmp    : unsigned byte array
                 with bmp format
        pallist: [(r: byte,
                   g: byte,
                   b: byte), ...]

    Returns:
        byref modified unsigned byte array
    """


**def setmax(val: numbers.Number, maxval: numbers.Number) -> numbers.Number:**
>"""Set the value of val to maxval if val > maxval

    Args:
        val   : numeric variable
        maxval: upper limit of variable

    Returns:
        Number
    """


**def setmin(val: numbers.Number, minval: numbers.Number) -> numbers.Number:**
>"""Set the value of val to minval if val < minval

    Args:
        val   : numeric variable
        minval: lower limit of variable

    Returns:
        Number
    """


**def setminmax(val: numbers.Number, minval: numbers.Number, maxval: numbers.Number) -> numbers.Number:**
>"""Set the value of val to minval if val < minval
    or the value of val to maxval if val > maxval

    Args:
        val   : numeric variable
        minval: lower limit of variable
        maxval: upper limit of variable

    Returns:
        Number
    """


**def setnewpalfromsourcebmp(sourcebmp: array.array, newbmp: array.array, similaritythreshold: float) -> list:**
>"""Copies the RGB palette info from
    a source unsigned byte array
    to a destination unsigned byte array
    (source and destination
    can have different bit depths)

    Args:
        sourceBMP, newBMP  : unsigned
                             byte arrays
                             with
                             bmp format
        similaritythreshold: how close
                             can a color
                             in a palette
                             entry be to
                             another color

    Returns:
        byRef modified newBMP
        (unsigned byte array) and a
        list of new palette entries
        based on source bitmap
    """


**def setRGBpal(bmp: array.array, c: int, r: int, g: int, b: int):**
>"""Sets the r,g,b values of color c in a bitmap

    Args:
        bmp    : unsigned byte array
                 with bmp format
        r, g, b: unsigned byte values
                 for red, green and
                 blue
        c      : unsigned int color

    Returns:
        byref modified unsigned byte array
    """


**def showsimilarparts(inputfile1: str, inputfile2: str, diff_file: str):**
>"""Compares 2 files and saves the similar parts to a BMP

    Args:
        inputfile1: Whole paths
        inputfile2  to existing files

        diff_file : New file to
                    store similar parts

    Returns:
        new bitmap file
    """


**def sortrecpoints(x1: int, y1: int, x2: int, y2: int):**
>"""Sorts the x and y values that sets a rectangular area

    Args:
        x1, x2: int x coordinates
        y1, y2: int y coordinates

    Returns:
        sorted coordinates
        x1, y1, x2, y2
        such that
        x1 < x2 and y1 < y2
    """


**def sphere(bmp: array.array, x: int, y: int, r: int, rgbfactors: list[float, float, float]):**
>"""Draws a Rendered Sphere

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : center of sphere
                    in the image
        r         : radius of sphere
                    in pixels
        rgbfactors: (r,g,b) r, g and b
                    values range from
                    0.0 to 1.0

    Returns:
        byref modified unsigned byte array
    """


**def sphere2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, rgbfactors: list[float, float, float]):**
>"""Renders a sphere

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r
        rgbfactors     : (r, g, b)
                         values
                         range from
                         0.0 to 1.0

    Returns:
        new bitmap file
    """


**def spherevertandsurface(vcen: list[float, float, float], r: float, deganglestep: float) -> tuple:**
>"""Returns a list of sparse
        vertices and tiled surfaces
        for a sphere

    Args:
        vcen       : [x: float, center
                      y: float, of the
                      z: float] sphere
        r           : spherical radius
        deganglestep: angle step between
        vertices that controls how sparse
        the list will be

    Returns:
        list of vertices and surfaces
        for plot3Dsolid()
        see Hello_DiscoBall.py
        and Hello_Globe.py
    """


**def spiralcontrolpointsvert(x: int, y: int, step: int, growthfactor: float, turns: int):**
>"""Returns a list of 2D vertices of a Square Spiral

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


**def spirographvert(x: int, y: int, r: int, l: float, k: float, delta: float, lim: float):**
>"""Returns a list(int, int) of
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


**def subvect(u: list[numbers.Number], v: list[numbers.Number]) -> list[numbers.Number]:**
>"""Subtracts vectors u and v by subtracting their components

    Args:
        u, v: list of ints or floats

    Returns:
        list of ints or floats
    """


**def surfplot3Dvertandsurface(x1: int, y1: int, x2: int, y2: int, step: int, fnxy: Callable) -> tuple:**
>"""Does a 3D surface plot of a
        function z = fnxy(x, y)

    Args:
        x1, y1, x2, y2: set drawing area
        fnxy          : fnxy(x, y)
                        Callable
                        (lambda or fn)

    Returns:
        list of vertices and surfaces
        for plot3Dsolid()
        see Hello_3D_surfaceplot.py
    """


**def swapcolors(bmp: array.array, p1: list, p2: list):**
>"""Swaps the colors of two points in a BMP

    Args:
        bmp   : unsigned byte array
                with bmp format
        p1, p2: endpoints of the
                line(x: uint, y: uint)

    Returns:
        byref modified unsigned byte array
    """


**def swapif(val1: <built-in function any>, val2: <built-in function any>, boolcond: bool):**
>"""Swaps val1 and val2 if
        boolcond is true

    Args:
        boolcond  : an expression that
                    evaluates as either
                    True or False
        val1, val2: values to swap if
                    boolcond is True

    Returns:
        values depending on boolcond
    """


**def swapxy(v: list) -> list:**
>"""Swaps the first two values in a list

    Args:
        list[x, y]

    Returns:
        list[y, x]
    """


**def tetrahedravert(x: float) -> list[list[float, float, float]]:**
>"""Returns a list of vertices
        for a tetrahedron

    Args:
        x: length of a side

    Returns:
        list (x: float,
              y: float,
              z: float)
    """


**def thickcircle(bmp: array.array, x: int, y: int, r: int, penradius: int, color: int):**
>"""Draws a Thick Circle

    Args:
        bmp      : unsigned byte array
                   with bmp format
        x, y, r  : center (x, y)
                   and radius r
        penradius: radius of round pen
        color    : color of the circle

    Returns:
        byref modified unsigned byte array
    """


**def thickellipserot(bmp: array.array, x: int, y: int, b: int, a: int, degrot: float, penradius: int, color: int):**
>"""Draws a Thick Ellipse

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : center of ellipse
        b, a      : major and minor axis
        degrot    : rotation of
                    the ellipse in degrees
        penradius : thickness of the pen
        color     : color of the ellipse

    Returns:
        byref modified
        unsigned byte array
    """


**def thickencirclearea(bmp: array.array, x: int, y: int, r: int, rgbfactors: list[float, float, float]):**
>"""Encircle area with a gradient

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y      : center of circle
        r         : radius of circle
        rgbfactors: (r,g,b) r, g and b
                    values are 0 to 1
                    unsigned floats

    Returns:
        byref modified unsigned byte array
    """


**def thickencirclearea2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, rgbfactors: list[float, float, float]):**
>""""Encircle area with a gradient and save to a file

    Args:
        bmp       : unsigned byte array
                    with bmp format

        x, y      : center of circle
        r         : radius of circle
        rgbfactors: (r, g, b) values
                    are from 0.0 to 1.0

    Returns:
        new bitmap file
"""


**def thickplotpoly(bmp: array.array, vertlist: list[list[numbers.Number, numbers.Number]], penradius: int, color: int):**
>"""Draws a polygon of a given color and thickness

    Args:
        bmp      : unsigned byte array
                   with bmp format
        vertlist : [(x, y)...]
                   list of vertices
        penradius: radius of pen
        color    : color of the polygon

    Returns:
        byref modified unsigned byte array
    """


**def thickroundline(bmp: array.array, p1: list, p2: list, penradius: int, color: int):**
>"""Draw a Thick Rounded Line

    Args:
        bmp       : unsigned byte array
                    with bmp format
        p1, p2    : (x, y) endpoints
                    of the line
        penradius : radius of pen
                    in pixels
        color     : color of the line

    Returns:
        byref modified unsigned byte array
    """


**def thresholdadjcircregion(bmp: array.array, x: int, y: int, r: int, lumrange: list[int, int]):**
>"""Threshold adjustment to a circular area

    Args:
        bmp      : unsigned byte array
                   with bmp format
        x, y, r  : centerpoint (x, y)
                   and radius r
        lumrange : (byte: byte)
                   threshold adjustment
                   luminosity range

    Returns:
        byref modified unsigned byte array
    """


**def thresholdadjcircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, lumrange: list[int, int]):**
>"""Threshold adjustment to a circular region in a 24-bit BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
        lumrange       : (byte:byte)
                         threshold range

    Returns:
        new bitmap file
    """


**def thresholdadjto24bitimage(bmp: array.array, lumrange: list[int, int]):**
>"""Threshold adjustment to a whole BMP

    Args:
        bmp     : unsigned byte array
                  with bmp format
        lumrange: (byte: byte)
                  threshold adjustment
                  luminosity range

    Returns:
        byref modified unsigned byte array
    """


**def thresholdadjto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int]):**
>"""Threshold adjustment to a rectangular area

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: ints that defines
                        the rectangular
                        region
        lumrange      : (byte:byte)
                        threshold
                        adjustment
                        luminosity range

    Returns:
        byref modified unsigned byte array
    """


**def thresholdadjust(rgb: list[int, int, int], lumrange: list[int, int]) -> list[int, int, int]:**
>"""Apply a threshold adjustment
        to a rgb

    Args:
        rgb: color as [r: byte,
                       g: byte,
                       b: byte]
        lumrange: [min: byte,
                   max: byte]
                  brightness
                  threshold
                  adjustment
                  limits

    Returns:
        a brightness threshold adjusted
        color as [r: byte,
                  g: byte,
                  b: byte]
    """


**def thresholdadjust2file(ExistingBMPfile: str, NewBMPfile: str, lumrange: list[int, int]):**
>"""Apply a threshold adjustment

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        lumrange       : (byte:byte)
                         threshold
                         to apply

    Returns:
        new bitmap file
    """


**def trans(vlist: list[list[numbers.Number]], u: list[numbers.Number]) -> list[list[numbers.Number]]:**
>"""Translates list of vectors by adding vector u
    to all vectors in the list of vectors

    Args:
        vlist: list of vectors
        u    : translation vector

    Returns:
        list of vectors
    """


**def upgradeto24bitimage(bmp: array.array):**
>"""Upgrade an image to 24-bits

    Args:
        bmp: unsigned byte array
             with bmp format

    Returns:
        byref modified unsigned byte array
    """


**def upgradeto24bitimage2file(ExistingBMPfile: str, NewBMPfile: str):**
>"""Upgrades a bitmap file to 24-bits

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in

    Returns:
        new bitmap file
    """


**def userdef2Dcooordsys2screenxy(x: int, y: int, lstcooordinfo: list):**
>"""2D coordinate trans from user to screen

    Args:
        x, y         : user coordinates
        lstcooordinfo: info on how to
                       transform the
                       2D coordinate
                       system
                       [origin,
                        steps,
                        xylimits,
                        xyvalstarts,
                        xysteps]
                        all
                        (x: int,
                         y: int) pairs

    Returns:
        [x: int, y: int] screen coordinates

    """


**def vertBMPbitBLTget(bmp: array.array, x: int, y1: int, y2: int) -> array.array:**
>"""Gets vertical slice to a new array

    Args:
        bmp   : unsigned byte array
                with bmp format
        x     : unsigned int x
        y1, y2  and y coordinates

    Returns:
        unsigned byte array
    """


**def vertbrightnessgrad2circregion(bmp: array.array, x: int, y: int, r: int, lumrange: list[int, int]):**
>"""Vertical brightness gradient adjustment to a circular area

    Args:
        bmp     : unsigned byte array
                  with bmp format
        x, y, r : center (x,y)
                  and radius r
        lumrange: [byte,byte]
                  that define
                  the range of
                  luminosity

    Returns:
        byref modified unsigned byte array
    """


**def vertbrightnessgrad2circregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, lumrange: list[int, int]):**
>"""Vertical brightness gradient to a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
                         of a circular
                         region
        lumrange       : brightness
                         gradient
                         (byte: byte)
                         adjust

    Returns:
        new bitmap file
    """


**def verticalbrightnessgrad2file(ExistingBMPfile: str, NewBMPfile: str, lumrange: list[int, int]):**
>"""Applies a Vertical brightness gradient

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        lumrange       : (byte:byte)
                         defines the
                         brightness
                         gradient

    Returns:
        new bitmap file
    """


**def verticalbrightnessgradregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int]):**
>"""Vertical brightness gradient to a rectangular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region
        lumrange       : (byte:byte)
                         defines the
                         brightness
                         gradient

    Returns:
        new bitmap file
    """


**def verticalbrightnessgradto24bitimage(bmp: array.array, lumrange: list[int, int]):**
>"""Applies a vertical brightness gradient

    Args:
        bmp     : unsigned byte array
                  with bmp format
        lumrange: (byte: byte) the
                  brightness gradient

    Returns:
        byref modified unsigned byte array
    """


**def verticalbrightnessgradto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int]):**
>"""Apply a vertical brightness gradient
    to a rectangular area in a 24-bit bitmap

    Args:
        bmp          :  unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangular
                        region
        lumrange      : (byte:byte)
                        brightness
                        gradient

    Returns:
        byref modified unsigned byte array
    """


**def verticalvert(x: int, y1: int, y2: int, dy: int) -> list[list[int, int]]:**
>"""Creates a list of int vertices
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


**def vertline(bmp: array.array, x: int, y1: int, y2: int, color: int):**
>"""Draw a Vertical Line

    Args:
        bmp  : unsigned byte array
               with bmp format
        x    : constant x value
               of the line
        y1   : starts at y1
        y2   : ends at y2
        color: color of the line

    Returns:
        byref modified unsigned byte array
    """


**def vertlinevert(bmp: array.array, vlist: list[list[int, int]], linelen: int, yadj: int, color: int):**
>"""Vertical line marks at vertices in vlist

    Args:
        bmp    : unsigned byte array
                 with bmp format
        vlist  : [(x,y),...] the
                 list of vertices
        linelen: lenght of the
                 vertical lines
        yadj   : sets an adjustment
                 for y coordinates
        color  : color of the line

    Returns:
        byref modified unsigned byte array
    """


**def verttrans(bmp: array.array, trans: str):**
>"""Do vertical image transforms

    Args:
        bmp : unsigned byte array
              with bmp format
        tran: single letter
              transform code
              'T' - mirror top-half
              'B' - mirror bottom-half
              'F' - flip

    Returns:
        byref modified
        unsigned byte array
    """


**def verttransformincircregion(bmp: array.array, x: int, y: int, r: int, trans: str):**
>"""Applies a vertical transform to
    a circular region with a center
    at (x, y) and radius r

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of region
        trans  :single letter
                transform code
                'T' mirror top
                'B' mirror bottom
                'F' flip

    Returns:
        byref modified unsigned byte array
    """


**def verttransregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, trans: str):**
>"""Do vertical image transforms
        in a rectangular region

    Args:
        bmp            : unsigned
                         byte array
                         with bmp format
        x1, y1, x2, y2 : ints that
                         defines the
                         rectangular
                         region
        trans          : single letter
                         transform code
                'T' - mirror top half
                'B' - mirror bottom half
                'F' - flip

    Returns:
        byref modified
        unsigned byte array
    """


**def vmag(v: list[float]) -> float:**
>"""Compute the Magnitude or length of a vector v
    of arbitrary dimension n equal to len(v)

    Args:
        v: list of ints or floats

    Returns:
        float
    """


**def writeint(offset: int, cnt: int, arr: array.array, value: int):**
>"""Writes an integer value to an
        unsigned byte array

    Args:
        offset: uint starting offset in
                buffer or array
                to write to
        cnt   : uint length of int data
                to write
        arr   : unsigned byte array
                to write int data in
        value : value of uint data to
                write in buffer or
                array

    Returns:
        byref unsigned byte array
    """


**def xorvect(u: list[int], v: list[int]) -> list[int]:**
>"""Applies a xor operation of between the elements of
    two lists of ints

    Args:
        v      : list[int]
        bitmask: int

    Returns:
        list[int]
    """


**def XYaxis(bmp: array.array, origin: list[int, int], steps: list[int, int], xylimits: list[int, int], xyvalstarts: list[numbers.Number, numbers.Number], xysteps: list[numbers.Number, numbers.Number], color: int, textcolor: int, showgrid: bool, gridcolor: int):**
>"""XY axis with tick marks and numbers

    Args:
        bmp      : unsigned byte array
                   with bmp format
        origin   : (x, y) on screen
                    origin point
                    of the axis
        steps    : (x, y) steps between
                   tick marks onscreen
        xylimits : (x, y) sets where the
                   graph ends onscreen
        xyvalstarts: (x, y) sets the
                      start point of
                      x and y number
                      lines
        xysteps   : (x, y) sets the
                    number increment
                    along the x and y
                    numberlines
        color    : color of the lines
        textcolor: color of the
                   numberline text
        showgrid : True -> display
                           gridline
                   False -> no grid
        gridcolor: color of the grid

    Returns:
        byref modified
        unsigned byte array
    """


**def xygrid(bmp: array.array, x1: int, y1: int, x2: int, y2: int, xysteps: list[int, int], color: int):**
>"""Draws a grid

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: sets limits
                        of the grid
        xysteps       : [x, y] sets the
                        increments
        color         : sets the color
                        of the grid

    Returns:
        byref modified unsigned byte array
    """


**def xygridvec(bmp: array.array, u: list[int, int], v: list[int, int], steps: list[int, int], gridcolor: int):**
>"""Grid using (x, y) point pairs u and v

    Args:
        bmp  : unsigned byte array
               with bmp format
        u, v : (x, y) sets limits
                of the  grid
        steps: (x, y) -> sets the
               increments for x and y
        color: sets the color
               of the grid

    Returns:
        byref modified unsigned byte array
    """


**def XYscatterplot(bmp: array.array, XYdata: list, XYcoordinfo: list, showLinearRegLine: bool, reglinecolor: int):**
>"""Create a XY scatterplot

    Args:
        bmp             : unsigned
                          byte array
                          with bmp format
        XYData          : [[x,y,
                          radius
                          (max radius is 5),
                          isfilled],...]
        lstcooordinfo   : info on how to
                          transform the
                          coordinate system
                          [origin,
                           -> origin point
                              on screen
                          steps,
                           -> on screen steps
                          xylimits,
                           -> x and y
                              clipping limit
                          xyvalstarts,
                           -> number line
                              start values
                          xysteps
                           -> increments for
                              the number lines
                            ]
                          * (x:int,y:int) pairs
        howLinearRegLine: True -> display linear
                                  regression line
        reglinecolor    : color of linear
                          regression line

    Returns:
        byref modified unsigned byte array
    """


