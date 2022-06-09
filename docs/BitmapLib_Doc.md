# Python BMP Public API

### [`_1bmof`](#Python_BMP.BITMAPlib._1bmof)

```py
def _1bmof(bmp: array.array, x: int, y: int) -> int:
```

Get the offset in a byte array
with 1 bit color data given x and y data

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int value
              of location in
              x-axis and y-axis
    
    Returns:
        int value of offset to that data in byte array


### [`_1bmofhd`](#Python_BMP.BITMAPlib._1bmofhd)

```py
def _1bmofhd(bmp: array.array, x: int, y: int) -> int:
```

Get the offset in a byte array
    with 1 bit color data given
    x and y with adjustments
    made for a bmp header

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int value
              of location in
              x-axis and y-axis
    
    Returns:
        int value of offset to that data in byte array


### [`_24bmof`](#Python_BMP.BITMAPlib._24bmof)

```py
def _24bmof(bmp: array.array, x: int, y: int) -> int:
```

Get the offset in a byte array with RGB data given x and y

    Args:
        bmp: unsigned byte array
             with bmp format
        x,y: unsigned int value
             of location in
             x-axis and y-axis
    
    Returns:
        int value of offset to that data in byte array


### [`_24bmofhd`](#Python_BMP.BITMAPlib._24bmofhd)

```py
def _24bmofhd(bmp: array.array, x: int, y: int) -> int:
```

Get the offset in a byte array
with RGB data given x and y with bmp header

    Args:
        bmp:  unsigned byte array
              with bmp format
        x, y: unsigned int value
              of location in
              x-axis and y-axis
    
    Returns:
        int value of offset to that data in byte array


### [`_4bmof`](#Python_BMP.BITMAPlib._4bmof)

```py
def _4bmof(bmp: array.array, x: int, y: int) -> int:
```

Get the offset in a byte array
with 4 bit color data given x and y data

    Args:
        bmp:  unsigned byte array
              with bmp format
        x, y: unsigned int value
              of location in
              x-axis and y-axis
    
    Returns:
        int value of offset to that data in byte array


### [`_4bmofhd`](#Python_BMP.BITMAPlib._4bmofhd)

```py
def _4bmofhd(bmp: array.array, x: int, y: int) -> int:
```

Get the offset in a byte array
with 4 bit color data given
x and y with adjustments
made due to a header

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int value
              of location in
              x-axis and y-axis
    
    Returns:
        int value of offset to that data in byte array


### [`_8bmof`](#Python_BMP.BITMAPlib._8bmof)

```py
def _8bmof(bmp: array.array, x: int, y: int) -> int:
```

Get the offset in a byte array
with 8 bit color data given x and y data

    Args:
        bmp:  unsigned byte array
              with bmp format
        x, y: unsigned int value
              of location in
              x-axis and y-axis
    
    Returns:
        int value of offset to
        that data in byte array


### [`_8bmofhd`](#Python_BMP.BITMAPlib._8bmofhd)

```py
def _8bmofhd(bmp: array.array, x: int, y: int) -> int:
```

Get the offset in a byte array
with 8 bit color data given
x and y with adjustments
made for a bmp header

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int value
              of location in
              x-axis and y-axis
    
    Returns:
        int value of offset to
        that data in byte array


### [`_bmmeta`](#Python_BMP.BITMAPlib._bmmeta)

```py
def _bmmeta(x: int, y: int, bits: int) -> tuple:
```

Computes bitmap meta data

    Args:
        x, y : unsigned int
               values of the
               x and y dimension
        bits : bit depth (1, 4, 8, 24)
    
    Returns:
        unsigned int values for
        (filesize, headersize,
        xdim, ydim, bitdepth)


### [`_BMoffset`](#Python_BMP.BITMAPlib._BMoffset)

```py
def _BMoffset(bmp: array.array, x: int, y: int) -> int:
```

Returns the offset given a bmp and (x, y) coordinates

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int location
              in x-axis and y-axis
    
    Returns:
        unsigned int offset to data in buffer


### [`_BMoffsethd`](#Python_BMP.BITMAPlib._BMoffsethd)

```py
def _BMoffsethd(bmp: array.array, x: int, y: int) -> int:
```

Returns the offset given a bmp
and (x, y) coordinates with header considered

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int location
              in x-axis and y-axis
    
    Returns:
        unsigned int offset to data in buffer


### [`_cmpimglines`](#Python_BMP.BITMAPlib._cmpimglines)

```py
def _cmpimglines(bmp: array.array, x1: int, y1: int, x2: int, y2: int, func: Callable):
```



    


### [`_flsz`](#Python_BMP.BITMAPlib._flsz)

```py
def _flsz(bmp: array.array) -> int:
```

Get the file size of a win bmp
    from its bmp header

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        unsigned int value of size
        of the bmp header


### [`_fnwithpar2vertslice`](#Python_BMP.BITMAPlib._fnwithpar2vertslice)

```py
def _fnwithpar2vertslice(bmp: array.array, x: int, y1: int, y2: int, func: Callable, funcparam):
```

Apply a user defined function to vertical slices

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y1, y2 : unsigned int
                    x and y coordinates
        func      : user defined function
        funcparam : parameters of
                    the user defined
                    function
    
    Returns:
        byref modified unsigned byte array


### [`_getbmflsz`](#Python_BMP.BITMAPlib._getbmflsz)

```py
def _getbmflsz(x: int, y: int, bits: int) -> int:
```

Computes bitmap file size

    Args:
        x, y: unsigned int value
              of x and y dimensions
        bits: bit depth (1, 4, 8, 24)
    
    Returns:
        int value of file size


### [`_getBMofffunc`](#Python_BMP.BITMAPlib._getBMofffunc)

```py
def _getBMofffunc(bmp: array.array):
```

Returns the correct function
to use in computing the offset
in a given bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        function to compute offsets


### [`_getBMoffhdfunc`](#Python_BMP.BITMAPlib._getBMoffhdfunc)

```py
def _getBMoffhdfunc(bmp: array.array):
```

Returns the correct function
to use in computing offsets
with headers in a given bmp

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        function to compute offsets with headers


### [`_getclrbits`](#Python_BMP.BITMAPlib._getclrbits)

```py
def _getclrbits(bmp: array.array) -> int:
```

Get the bit depth of BMP

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        int value of bit depth
        (1, 4, 8, 24) bits


### [`_hdsz`](#Python_BMP.BITMAPlib._hdsz)

```py
def _hdsz(bmp: array.array) -> int:
```

Get the header size of a BMP

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        int value of header size


### [`_pdbytes`](#Python_BMP.BITMAPlib._pdbytes)

```py
def _pdbytes(x: int, bits: int) -> int:
```

Get the number of bytes used to pad for
32-bit alignment given x dimension and bit depth

    Args:
        x   : unsigned int value of
              x-dimension
        bits: unsigned int value of
              bit depth (1, 4, 8, 24)
    
    Returns:
        int value of number of pad bytes


### [`_setflsz`](#Python_BMP.BITMAPlib._setflsz)

```py
def _setflsz(bmp: array.array, size: int):
```

Set the file size of a BMP

    Args:
        bmp  : unsigned byte array
               with bmp format
        size : unsigned int value
               of size of
               the bmp file
    
    Returns:
        byref modified unsigned byte array
        with new file size


### [`_sethdsz`](#Python_BMP.BITMAPlib._sethdsz)

```py
def _sethdsz(bmp: array.array, hdsize: int):
```

Set the header size of a win bmp

    Args:
        bmp   : unsigned byte array
                with bmp format
        hdsize: unsigned int value
                of size of the
                bmp header
    
    Returns:
        byref modified byte array
        with new header size


### [`_setmeta`](#Python_BMP.BITMAPlib._setmeta)

```py
def _setmeta(bmpmeta: list) -> array.array:
```

Creates a new bitmap
    with the properties set
    by bmpmeta to
    a new unsigned byte array

    Args:
        bmpmeta: [filesize, hdrsize,
                  x, y, bits]
    
    Returns:
        unsigned byte array with bmp format


### [`_setx`](#Python_BMP.BITMAPlib._setx)

```py
def _setx(bmp: array.array, xmax: int):
```

Sets the x value stored in the windows bmp header

    Args:
        bmp: unsigned byte array
             with bmp format
        int: value of x dimension
    
    Returns:
        byref modified unsigned byte array


### [`_sety`](#Python_BMP.BITMAPlib._sety)

```py
def _sety(bmp: array.array, ymax: int):
```

Sets the y value stored in the windows bmp header

    Args:
        bmp: unsigned byte array
             with bmp format
        int: value of y dimension
    
    Returns:
        byref modified unsigned byte array


### [`_use24bitfn2reg`](#Python_BMP.BITMAPlib._use24bitfn2reg)

```py
def _use24bitfn2reg(bmp: array.array, x1: int, y1: int, x2: int, y2: int, func: Callable, funcparam):
```

Apply func(funcparam) to a rectangular area
in a 24-bit bitmap

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangular area
        func          : user defined
                        function
        funcparam     : parameters of
                        the function
    
    Returns:
        byref modified unsigned byte array


### [`_use24btbyrefclrfn2regnsv`](#Python_BMP.BITMAPlib._use24btbyrefclrfn2regnsv)

```py
def _use24btbyrefclrfn2regnsv(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, func: Callable, funcparam):
```

Apply a 24-bit byref
color modification function
to a rectangular area and save

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2:  the rectangular
                         area
        func           : user defined
                         function
        funcparam      : function
                         parameters
    
    Returns:
        new bitmap file


### [`_use24btclrfn`](#Python_BMP.BITMAPlib._use24btclrfn)

```py
def _use24btclrfn(ExistingBMPfile: str, NewBMPfile: str, func: Callable, funcparam):
```

Apply a user provided color adjustment function
to a 24-bit bitmap

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save the
                         changes in
        func           : user defined
                         function
        funcparam      : parameters of
                         the function
    
    Returns:
        new bitmap file


### [`_use24btclrfntocircregion`](#Python_BMP.BITMAPlib._use24btclrfntocircregion)

```py
def _use24btclrfntocircregion(ExistingBMPfile: str, NewBMPfile: str, func: Callable, x: int, y: int, r: int):
```

Apply a no parameter color adjustment function
to a circular area (24-bit only)

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r
        func           : user defined
                         function
    
    Returns:
        new bitmap file


### [`_use24btclrfnwithpar2circreg`](#Python_BMP.BITMAPlib._use24btclrfnwithpar2circreg)

```py
def _use24btclrfnwithpar2circreg(ExistingBMPfile: str, NewBMPfile: str, func: Callable, x: int, y: int, r: int, funcparam):
```

Apply a user provided color adjustment function
to a circular area (24-bit only)

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x,y)
                         and radius r
        func           : user defined
                         function
        funcparam      : parameters of
                         the function
    
    Returns:
        new bitmap file


### [`_use24btfn2circreg`](#Python_BMP.BITMAPlib._use24btfn2circreg)

```py
def _use24btfn2circreg(bmp: array.array, x: int, y: int, r: int, func: Callable, funcparam):
```

Apply function func to a
circular region with center at
(x, y) and a radius r that is
within a 24-bit bitmap

    Args:
        bmp       : unsigned byte array
                    with bmp format
        x, y, r   : center (x, y)
                    and radius r
                    of the circular area
        func      : function to apply
        funcparam : parameters of the
                    function
    
    Returns:
        byref modified
        unsigned byte array


### [`_use24btfnwithparnsv`](#Python_BMP.BITMAPlib._use24btfnwithparnsv)

```py
def _use24btfnwithparnsv(ExistingBMPfile: str, NewBMPfile: str, func: Callable, funcparam):
```

Apply a 24-bit only function with parameters and save

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        func           : user defined
                         function
        funcparam      : parameters of
                         the function
    
    Returns:
        new bitmap file


### [`_usebyref24btfn2reg`](#Python_BMP.BITMAPlib._usebyref24btfn2reg)

```py
def _usebyref24btfn2reg(bmp: array.array, x1: int, y1: int, x2: int, y2: int, func: Callable, funcparam):
```

Apply byref func(funcparam) to a rectangular area
in a 24-bit bitmap

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangular area
        func          : user defined
                        function
        funcparam     : parameters of
                        the function
    
    Returns:
        byref modified unsigned byte array


### [`_usebyref24btfn2regnsv`](#Python_BMP.BITMAPlib._usebyref24btfn2regnsv)

```py
def _usebyref24btfn2regnsv(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, func: Callable):
```

Apply a 24-bit byref function
with no parameters to a
rectangular area and save

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region
        func           : user defined
                         function
    
    Returns:
        new bitmap file


### [`_usebyreffn2regnsv`](#Python_BMP.BITMAPlib._usebyreffn2regnsv)

```py
def _usebyreffn2regnsv(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, func: Callable):
```

Apply a byref function
with no parameters to a
rectangular region and save

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region
        func           : user defined
                         function
    
    Returns:
        new bitmap file


### [`_usebyreffnsv`](#Python_BMP.BITMAPlib._usebyreffnsv)

```py
def _usebyreffnsv(ExistingBMPfile: str, NewBMPfile: str, func: Callable):
```

Apply a by-ref function with no parameters and save

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        func           : user defined
                         function
    
    Returns:
        new bitmap file


### [`_usebyreffnwithpar2regnsv`](#Python_BMP.BITMAPlib._usebyreffnwithpar2regnsv)

```py
def _usebyreffnwithpar2regnsv(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, func: Callable, funcparam):
```

Apply a 24-bit byref function
to a rectangular area and save

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         area
        func           : user defined
                         function
        funcparam      : function
                         parameters
    
    Returns:
        new bitmap file


### [`_usebyreffnwithparnsv`](#Python_BMP.BITMAPlib._usebyreffnwithparnsv)

```py
def _usebyreffnwithparnsv(ExistingBMPfile: str, NewBMPfile: str, func: Callable, funcparam):
```



    


### [`_usebyrefnopar24bitfn2reg`](#Python_BMP.BITMAPlib._usebyrefnopar24bitfn2reg)

```py
def _usebyrefnopar24bitfn2reg(bmp: array.array, x1: int, y1: int, x2: int, y2: int, func: Callable):
```

Apply a func to a rectangular area in a 24-bit bitmap

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: the rectangular
                        area
        func          : user defined
                        function
    
    Returns:
        byref modified unsigned byte array


### [`_useclradjfn`](#Python_BMP.BITMAPlib._useclradjfn)

```py
def _useclradjfn(ExistingBMPfile: str, NewBMPfile: str, func: Callable, funcparam):
```

Apply a user provided color adjustmen function
to an existing bitmap

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        func           : user defined
                         function
        funcparam      : parameters of
                         the function
    
    Returns:
        new bitmap file


### [`_usefn2circreg`](#Python_BMP.BITMAPlib._usefn2circreg)

```py
def _usefn2circreg(ExistingBMPfile: str, NewBMPfile: str, func: Callable, x: int, y: int, r: int):
```

Apply a user provided function (no parameters)
to a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r
        func           : user defined
                         function
    
    Returns:
        new bitmap file


### [`_usefn2regsv`](#Python_BMP.BITMAPlib._usefn2regsv)

```py
def _usefn2regsv(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, func: Callable):
```

Apply a function withno parameters to a
rectangular area and save

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : defines the
                         rectangular
                         region
        func           : user defined
                         function
    
    Returns:
        new bitmap file


### [`_usefnsv`](#Python_BMP.BITMAPlib._usefnsv)

```py
def _usefnsv(ExistingBMPfile: str, NewBMPfile: str, func: Callable):
```

Apply a function with no parameters and save

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        func           : user defined
                         function
    
    Returns:
        new bitmap file


### [`_usefnwithpar2circreg`](#Python_BMP.BITMAPlib._usefnwithpar2circreg)

```py
def _usefnwithpar2circreg(ExistingBMPfile: str, NewBMPfile: str, func: Callable, x: int, y: int, r: int, funcparam):
```

Apply a user provided function with parameters
to a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x,y)
                         and radius r
        func           : user defined
                         function
        funcparam      : parameters of
                         the function
    
    Returns:
        new bitmap file


### [`_usenopar24btfn2circreg`](#Python_BMP.BITMAPlib._usenopar24btfn2circreg)

```py
def _usenopar24btfn2circreg(bmp: array.array, x: int, y: int, r: int, func: Callable):
```

Apply a no parameter function
to a circular region with
center at (x, y) and a radius r
in a 24-bit bitmap

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of the circular area
        func   : function to apply
    
    Returns:
        byref modified unsigned byte array


### [`_usenoparclradjfn`](#Python_BMP.BITMAPlib._usenoparclradjfn)

```py
def _usenoparclradjfn(ExistingBMPfile: str, NewBMPfile: str, func: Callable):
```

Apply a user provided no parameter color
    adjustment function to an existing bitmap

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        func           : user defined
                         function
    
    Returns:
        new bitmap file


### [`_usenoparfn2circreg`](#Python_BMP.BITMAPlib._usenoparfn2circreg)

```py
def _usenoparfn2circreg(bmp: array.array, x: int, y: int, r: int, func: Callable):
```

Apply a no parameter function
to a circular region with a
center at (x,y) and a radius r

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x,y)
                 and radius r
                 of the
                 circular area
        func   : function
                 to apply
                 to the area
    
    Returns:
        byref modified unsigned byte array


### [`_xbytes`](#Python_BMP.BITMAPlib._xbytes)

```py
def _xbytes(x: int, bits: int) -> int:
```

Get the number of bytes in
a bmp row given x dimension and bit depth

    Args:
        x   : unsigned int value of
              x-dimension
        bits: unsigned int value of
              bit depth (1, 4, 8, 24)
    
    Returns:
        int value of number of bytes in a row


### [`_xchrcnt`](#Python_BMP.BITMAPlib._xchrcnt)

```py
def _xchrcnt(bmp: array.array) -> int:
```

Get the chars or bytes in row of a BMP

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        count of bytes or
        chars in a row (x dim)


### [`addvect`](#Python_BMP.mathlib.addvect)

```py
def addvect(u: list[numbers.Number], v: list[numbers.Number]) -> list[numbers.Number]:
```

Add vectors u and v by adding their components

    Args:
        u, v: list of ints or floats
    
    Returns:
        list of ints or floats


### [`addvectinlist`](#Python_BMP.mathlib.addvectinlist)

```py
def addvectinlist(vlist: list[list[numbers.Number]]) -> numbers.Number:
```

Gets the sum of the vectors in a list of vectors

    Args:
        vlist: list of vectors
    
    Returns:
        list or vector


### [`adjustbrightness2file`](#Python_BMP.BITMAPlib.adjustbrightness2file)

```py
def adjustbrightness2file(ExistingBMPfile: str, NewBMPfile: str, percentadj: float):
```

Apply a brightness adjustment to the image in a BMP

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


### [`adjustbrightnessinregion2file`](#Python_BMP.BITMAPlib.adjustbrightnessinregion2file)

```py
def adjustbrightnessinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, percentadj: float):
```

Brightness adjustment to rectangular area in a 24-bit BMP

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


### [`adjustcolordicttopal`](#Python_BMP.BITMAPlib.adjustcolordicttopal)

```py
def adjustcolordicttopal(bmp: array.array, colordict: dict):
```

Adjust a color dictionary to match
as closely as possible a bitmap palette

    Args:
        bmp      : unsigned byte array
                   with bmp format
        colordict: dictionary of colors
    
    Returns:
        byref modified dictionary of colors


### [`adjustthresholdinregion2file`](#Python_BMP.BITMAPlib.adjustthresholdinregion2file)

```py
def adjustthresholdinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, lumrange: list):
```

Threshold adjust in a rectangular area in a 24-bit BMP

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


### [`adjustxbufsize`](#Python_BMP.bufresize.adjustxbufsize)

```py
def adjustxbufsize(bmp: array.array, x1: int, x2: int) -> int:
```

Returns a 32 -bit padded
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


### [`andvect`](#Python_BMP.mathlib.andvect)

```py
def andvect(u: list[int], v: list[int]) -> list[int]:
```

Bitwise and operation of between
the elements of two lists of ints

    Args:
        v      : list[int]
        bitmask: int
    
    Returns:
        list[int]


### [`anglebetween2Dlines`](#Python_BMP.mathlib.anglebetween2Dlines)

```py
def anglebetween2Dlines(u: list[numbers.Number, numbers.Number], v: list[numbers.Number, numbers.Number]) -> float:
```

Compute the angle between two lines of vectors

    Args:
        u, v: list[Number, Number]
    
    Returns:
        float angle in radians


### [`applybrightnessadjtoBGRbuf`](#Python_BMP.colors.applybrightnessadjtoBGRbuf)

```py
def applybrightnessadjtoBGRbuf(buf: array.array, percentadj: float) -> array.array:
```

Apply a brightness adjustment
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


### [`applycolorfiltertoBGRbuf`](#Python_BMP.colors.applycolorfiltertoBGRbuf)

```py
def applycolorfiltertoBGRbuf(buf: array.array, rgbfactors: list[float, float, float]):
```

Apply a color filter to a
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


### [`applygammaBGRbuf`](#Python_BMP.colors.applygammaBGRbuf)

```py
def applygammaBGRbuf(buf: array.array, gamma: float):
```

Apply a gamma adjustment to a
    BGR buffer

    Args:
        buf: unsigned byte array
             holding BGR data
    
        gamma: float gamma adjust
    
    Returns:
        byref unsigned byte array
        holding gamma adjusted
        BGR data


### [`applymonochromefiltertoBGRbuf`](#Python_BMP.colors.applymonochromefiltertoBGRbuf)

```py
def applymonochromefiltertoBGRbuf(buf: array.array):
```

Apply a monochrome filter to a
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


### [`applythresholdadjtoBGRbuf`](#Python_BMP.colors.applythresholdadjtoBGRbuf)

```py
def applythresholdadjtoBGRbuf(buf: array.array, lumrange: list) -> array.array:
```

Apply a threshold adjustment
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


### [`arcvert`](#Python_BMP.primitives2D.arcvert)

```py
def arcvert(x: int, y: int, r: int, startdegangle: float, enddegangle: float):
```

Returns a list[(int, int)] of 2D vertices
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


### [`autocropimg2file`](#Python_BMP.BITMAPlib.autocropimg2file)

```py
def autocropimg2file(ExistingBMPfile: str, NewBMPfile: str, similaritythreshold: float):
```

Perform an auto crop to the image in a bitmap file

    Args:
        ExistingBMPfile    : Whole path to
                             existing file
        NewBMPfile         : New file to
                             save changes in
        similaritythreshold: used to tune
                             autocrop
    
    Returns:
        new bitmap file


### [`beziercurve`](#Python_BMP.BITMAPlib.beziercurve)

```py
def beziercurve(bmp: array.array, pntlist: list[list[numbers.Number, numbers.Number]], penradius: int, color: int):
```

Draws a Bezier Curve

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


### [`BMPbitBLTget`](#Python_BMP.BITMAPlib.BMPbitBLTget)

```py
def BMPbitBLTget(bmp: array.array, offset: int, bufsize: int) -> array.array:
```

Gets [offset: offset + bufsize] to a new array

    Args:
        bmp    : unsigned byte array
                 with bmp format
        offset : unsigned int
                 address in buffer
        bufsize: unsigned int
                 size of buffer
    
    Returns:
        unsigned byte array


### [`BMPbitBLTput`](#Python_BMP.BITMAPlib.BMPbitBLTput)

```py
def BMPbitBLTput(bmp: array.array, offset: int, arraybuf: array.array):
```

Sets offset in array to arraybuf

    Args:
        bmp     : unsigned byte array
                  with bmp format
        offset  : unsigned int
                  address in buffer
        arraybuf: unsigned byte array
    
    Returns:
        byref modified unsigned byte array


### [`bottomrightcoord`](#Python_BMP.BITMAPlib.bottomrightcoord)

```py
def bottomrightcoord(bmp: array.array) -> tuple:
```

Gets the maximum bottom right coordinates of a bmp

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        tuple (x:int,y:int)


### [`brightnessadjcircregion2file`](#Python_BMP.BITMAPlib.brightnessadjcircregion2file)

```py
def brightnessadjcircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, percentadj: float):
```

Brightness gradient to a circular area

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


### [`brightnessadjcircregion`](#Python_BMP.BITMAPlib.brightnessadjcircregion)

```py
def brightnessadjcircregion(bmp: array.array, x: int, y: int, r: int, percentadj: float):
```

Brightness adjustment to a circular area

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


### [`brightnessadjust`](#Python_BMP.colors.brightnessadjust)

```py
def brightnessadjust(rgb: list[int, int, int], percentadj: float) -> list[int, int, int]:
```

Apply a brightness adjustment
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


### [`brightnesseadjto24bitimage`](#Python_BMP.BITMAPlib.brightnesseadjto24bitimage)

```py
def brightnesseadjto24bitimage(bmp: array.array, percentadj: float):
```

Brightness adjustment to a whole BMP

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


### [`brightnesseadjto24bitregion`](#Python_BMP.BITMAPlib.brightnesseadjto24bitregion)

```py
def brightnesseadjto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, percentadj: float):
```

Brightness adjustment to a rectangular area

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


### [`bspline`](#Python_BMP.BITMAPlib.bspline)

```py
def bspline(bmp: array.array, pntlist: list, penradius: int, color: int, isclosed: bool, curveback: bool):
```

Draws a Bspline

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


### [`bsplinevert`](#Python_BMP.primitives2D.bsplinevert)

```py
def bsplinevert(pntlist: list[list[int, int]], isclosed: bool, curveback: bool) -> list[list[int, int]]:
```

Creates a list of vertices for a bspline curve

    Args:
        pntlist: 2D control points
                 for the bspline curve
                 as list[list[x: int,
                              y: int]]
    
    Returns:
        list of vertices as
        list[list[x: int, y: int]]


### [`buf2int`](#Python_BMP.inttools.buf2int)

```py
def buf2int(buf: array.array) -> int:
```

Converts an unsigned byte array
    to an integer value

    Args:
        buf: unsigned byte array
    
    Returns:
        unsigned int value


### [`centercoord`](#Python_BMP.BITMAPlib.centercoord)

```py
def centercoord(bmp: array.array) -> tuple:
```

Gets the central coordinates of a BMP

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        tuple (x:int,y:int)


### [`centerpoint`](#Python_BMP.mathlib.centerpoint)

```py
def centerpoint(x1: int, y1: int, x2: int, y2: int):
```

Returns the centerpoint x, y in rectangular area

    Args:
        x1, y1 : defines the
        x2, y2   rectangular area
    
    Returns:
        x: int, y: int centerpoint


### [`char2int`](#Python_BMP.chartools.char2int)

```py
def char2int(charcodestr: str) -> int:
```

Packs a string into an int
    using ascii code

    Args:
        charcodestr: string
    
    Yields:
        int value


### [`checklink`](#Python_BMP.fileutils.checklink)

```py
def checklink(func: Callable):
```

Decorator to test if the first
    parameter in a function is
    a valid file

    Args:
        function
    
    Returns:
        caller function


### [`checklinks`](#Python_BMP.fileutils.checklinks)

```py
def checklinks(func: Callable):
```

Decorator to test if the two
    parameters in a function
    are valid files

    Args:
        function
    
    Returns:
        caller function


### [`circle2file`](#Python_BMP.BITMAPlib.circle2file)

```py
def circle2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, color: int):
```

Draws a Circle

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


### [`circle`](#Python_BMP.BITMAPlib.circle)

```py
def circle(bmp: array.array, x: int, y: int, r: int, color: int, isfilled: bool = None):
```

Draws a Circle

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


### [`circleinvolutevert`](#Python_BMP.primitives2D.circleinvolutevert)

```py
def circleinvolutevert(x: int, y: int, a: float, delta: float, lim: float):
```

Returns (int, int) 2D vertices
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


### [`circlevec`](#Python_BMP.BITMAPlib.circlevec)

```py
def circlevec(bmp: array.array, v: list, r: int, color: int, isfilled: bool = None):
```

Draws a circle

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


### [`colorfilter2file`](#Python_BMP.BITMAPlib.colorfilter2file)

```py
def colorfilter2file(ExistingBMPfile: str, NewBMPfile: str, rgbfactors: list[float, float, float]):
```

Applies Color Filter rgbfactors to a BMP

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


### [`colorfilter`](#Python_BMP.colors.colorfilter)

```py
def colorfilter(rgb: list[int, int, int], rgbfactors: list[float, float, float]) -> list[int, int, int]:
```

Apply a color filter
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


### [`colorfiltercircregion2file`](#Python_BMP.BITMAPlib.colorfiltercircregion2file)

```py
def colorfiltercircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, rgbfactors: list[float, float, float]):
```

Applies a color filter to a circular area in a BMP

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


### [`colorfiltercircregion`](#Python_BMP.BITMAPlib.colorfiltercircregion)

```py
def colorfiltercircregion(bmp: array.array, x: int, y: int, r: int, rgbfactors: list[float, float, float]):
```

Color Filter to a circular area

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


### [`colorfilterinregion2file`](#Python_BMP.BITMAPlib.colorfilterinregion2file)

```py
def colorfilterinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, rgbfactors: list[float, float, float]):
```

Color Filter to a Rectangular Area in a 24-bit BMP

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


### [`colorfilterto24bitimage`](#Python_BMP.BITMAPlib.colorfilterto24bitimage)

```py
def colorfilterto24bitimage(bmp: array.array, rgbfactors: list[float, float, float]):
```

Applies a color filter
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


### [`colorfilterto24bitregion`](#Python_BMP.BITMAPlib.colorfilterto24bitregion)

```py
def colorfilterto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, rgbfactors: list[float, float, float]):
```

Applies a color filter to
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


### [`colorfiltertoBGRbuf`](#Python_BMP.colors.colorfiltertoBGRbuf)

```py
def colorfiltertoBGRbuf(buf: array.array, rgbfactors: list[float, float, float]) -> array.array:
```

Apply a color filter to a
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


### [`colorhistorgram`](#Python_BMP.BITMAPlib.colorhistorgram)

```py
def colorhistorgram(bmp: array.array) -> list:
```

Creates a color histogram

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        list sorted in descending order of color frequencies


### [`colormix`](#Python_BMP.colors.colormix)

```py
def colormix(lum: int, RGBfactors: list[float, float, float]) -> int:
```

Mix a byte luminosity value to
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


### [`conevertandsurface`](#Python_BMP.solids3D.conevertandsurface)

```py
def conevertandsurface(vcen: list[float, float, float], r: float, zlen: float, deganglestep: float) -> tuple:
```

Returns a list of sparse
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


### [`convertbufto24bit`](#Python_BMP.BITMAPlib.convertbufto24bit)

```py
def convertbufto24bit(buf: array.array, bgrpalbuf: array.array, bits: int) -> array.array:
```

Converts 1, 4 and 8-bit buffers to a BGR buffer

    Args:
        buf      : unsigned byte array
        bgrpalbuf: BGR palette info
        bits     : color depth
                   (1, 4, 8)
    
    Returns:
        unsigned byte array


### [`convertselection2BMP`](#Python_BMP.BITMAPlib.convertselection2BMP)

```py
def convertselection2BMP(buf: array.array):
```

Converts custom unsigned byte array to bmp format

    Args:
        buf: unsigned byte array
    
    Returns:
        unsigned byte array with bmp format


### [`copyBMPhdr`](#Python_BMP.BITMAPlib.copyBMPhdr)

```py
def copyBMPhdr(bmp: array.array) -> array.array:
```

Copies the bitmap header of an in-memory bmp
to a new unsigned byte array

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        unsigned byte array with bmp format


### [`CopyBMPxydim2newBMP`](#Python_BMP.BITMAPlib.CopyBMPxydim2newBMP)

```py
def CopyBMPxydim2newBMP(bmp: array.array, newbits: int) -> array.array:
```

Creates a new bitmap with the same dimensions as bmp

    Args:
        bmp    : unsigned byte array
                 with bmp format
        newbits: bit depth
                 (1, 4, 8, 24)
    
    Returns:
        unsigned byte array with bitmap layout


### [`copycircregion2buf`](#Python_BMP.BITMAPlib.copycircregion2buf)

```py
def copycircregion2buf(bmp: array.array, x: int, y: int, r: int) -> list:
```

Copies a circular region to a
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


### [`copycircregion2file`](#Python_BMP.BITMAPlib.copycircregion2file)

```py
def copycircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, newxycenterpoint: list):
```

Copy/Paste of a circular area in a BMP

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


### [`copycircregion`](#Python_BMP.BITMAPlib.copycircregion)

```py
def copycircregion(bmp: array.array, x: int, y: int, r: int, newxy: list):
```

Copy a circular buffer with center at (x, y)
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


### [`copyrect`](#Python_BMP.BITMAPlib.copyrect)

```py
def copyrect(bmp: array.array, x1: int, y1: int, x2: int, y2: int) -> array.array:
```

Copy a rectangular region to a custom buffer

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        custom unsigned byte array


### [`copyRGBpal`](#Python_BMP.BITMAPlib.copyRGBpal)

```py
def copyRGBpal(sourceBMP: array.array, destBMP: array.array):
```

Copies the RGB palette info from
a source unsigned byte array to
a destination unsigned byte array

    Args:
        sourceBMP and destBMP are both
        unsigned byte arrays with bmp format
    
    Returns:
        byref modified destBMP
        (unsigned byte array)


### [`cosaffin`](#Python_BMP.mathlib.cosaffin)

```py
def cosaffin(u: list[numbers.Number], v: list[numbers.Number]) -> float:
```

Compute Cosine Similarity or Cosine Affinity

    Args:
        u, v : list of ints or floats
    
    Returns:
        float value
            proportional vectors = 1
            orthogonal vectors = 0
            opposite vectors = -1
            and values in between


### [`crop`](#Python_BMP.BITMAPlib.crop)

```py
def crop(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Crops the image to a rectangular
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


### [`cropBMPandsave`](#Python_BMP.BITMAPlib.cropBMPandsave)

```py
def cropBMPandsave(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Crops and saves a rectangular area to a BMP

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


### [`cropBMPandsaveusingrectbnd`](#Python_BMP.BITMAPlib.cropBMPandsaveusingrectbnd)

```py
def cropBMPandsaveusingrectbnd(ExistingBMPfile: str, NewBMPfile: str, rectbnd: list):
```

Crops and saves a rectangular area to a BMP

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


### [`cubevert`](#Python_BMP.solids3D.cubevert)

```py
def cubevert(x: float) -> list[list[float, float, float]]:
```

Returns a list of vertices
    for a cube

    Args:
        x: length of a side
    
    Returns:
        list (x: float,
              y: float,
              z: float)


### [`cylindervertandsurface`](#Python_BMP.solids3D.cylindervertandsurface)

```py
def cylindervertandsurface(vcen: list[float, float, float], r: float, zlen: float, deganglestep: float) -> tuple:
```

Returns a list of sparse vertices
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


### [`decahedvertandsurface`](#Python_BMP.solids3D.decahedvertandsurface)

```py
def decahedvertandsurface(x: float) -> list[list[float, float, float]]:
```

Returns a list of vertices
    for a decahedron

    Args:
        x: min radius of sphere
           that can hold
           the decahedron
    
    Returns:
        list (x: float,
              y: float,
              z: float)


### [`dict2descorderlist`](#Python_BMP.dicttools.dict2descorderlist)

```py
def dict2descorderlist(d: dict) -> list:
```

Creates a sorted list in
    decending order from
    a dictionary with counts

    Args:
        dict: histogram or
              frequency count
    
    Returns:
        list


### [`distance`](#Python_BMP.mathlib.distance)

```py
def distance(u: list[float], v: list[float]) -> float:
```

Compute the Distance or length of a vector v
of arbitrary dimension n in a n-dimensional
Euclidean space where u and v are both vectors
with n components

    Args:
        u, v: list of ints or floats
    
    Returns:
        float


### [`drawarc`](#Python_BMP.BITMAPlib.drawarc)

```py
def drawarc(bmp: array.array, x: int, y: int, r: int, startdegangle: float, enddegangle: float, color: int, showoutline: bool, fillcolor: int, isfilled: bool):
```

Draws an Arc

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


### [`drawvec`](#Python_BMP.BITMAPlib.drawvec)

```py
def drawvec(bmp: array.array, u: list, v: list, headsize: int, color: int, penradius: int = None):
```

Draws a vector (line segment with arrow head)

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


### [`ellipse`](#Python_BMP.BITMAPlib.ellipse)

```py
def ellipse(bmp: array.array, x: int, y: int, b: int, a: int, color: int, isfilled: bool = None):
```

Draws an Ellipse

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


### [`ellipsevert`](#Python_BMP.primitives2D.ellipsevert)

```py
def ellipsevert(x: int, y: int, b: int, a: int) -> list[int, int]:
```

Returns (int, int) 2D vertices
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


### [`entirecircleinboundary`](#Python_BMP.paramchecks.entirecircleinboundary)

```py
def entirecircleinboundary(func):
```

Decorator to ensure that the 2nd,
    3rd, 4th parameters are ints
    whose values when interpreted
    as the centerpoint x, y
    and radius r of a circle
    lay within the RGB bitmap.

    Args:
        function(bmp:array,x:int,y:int,r:int...)
    
    Returns:
        caller function


### [`entirecircleisinboundary`](#Python_BMP.primitives2D.entirecircleisinboundary)

```py
def entirecircleisinboundary(x: int, y: int, minx: int, maxx: int, miny: int, maxy: int, r: int):
```

Checks if an entire circle
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


### [`entireellipseisinboundary`](#Python_BMP.primitives2D.entireellipseisinboundary)

```py
def entireellipseisinboundary(x: int, y: int, minx: int, maxx: int, miny: int, maxy: int, b: int, a: int):
```

Checks if an entire ellipse
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


### [`entirerectinboundary`](#Python_BMP.paramchecks.entirerectinboundary)

```py
def entirerectinboundary(func):
```

Decorator to ensure that the
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


### [`enumbits`](#Python_BMP.mathlib.enumbits)

```py
def enumbits(byteval: int):
```

Yields the 8 bits in a byte

    Args:
        byteval: int value
                 from 0 to 255
    
    Yields:
        Eight bits that is either
        int 0 or int 1


### [`enumletters`](#Python_BMP.chartools.enumletters)

```py
def enumletters(st: str) -> str:
```

Enumerates the characters
    in a string

    Args:
        st: string
    
    Yields:
        individual characters


### [`enumreverseletters`](#Python_BMP.chartools.enumreverseletters)

```py
def enumreverseletters(st: str) -> str:
```

Enumerates the characters in a
    string in reverse order

    Args:
        st: string
    
    Yields:
        individual characters


### [`epicycloidvert`](#Python_BMP.primitives2D.epicycloidvert)

```py
def epicycloidvert(x: int, y: int, a: float, b: float, delta: float, lim: float):
```

Returns (int, int) 2D vertices
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


### [`erasealternatehorizontallines`](#Python_BMP.BITMAPlib.erasealternatehorizontallines)

```py
def erasealternatehorizontallines(bmp: array.array, int_eraseeverynline: int, int_eraseNthline: int, bytepat: int):
```

Erase every nth line

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


### [`erasealternatehorizontallinesincircregion`](#Python_BMP.BITMAPlib.erasealternatehorizontallinesincircregion)

```py
def erasealternatehorizontallinesincircregion(bmp: array.array, x: int, y: int, r: int, int_eraseeverynline: int, int_eraseNthline: int, bytepat: int):
```

Erase every nth line
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


### [`erasealternatehorizontallinesinregion`](#Python_BMP.BITMAPlib.erasealternatehorizontallinesinregion)

```py
def erasealternatehorizontallinesinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, int_eraseeverynline: int, int_eraseNthline: int, bytepat: int):
```

Erase every nth line in a rectangular region

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


### [`eraseeverynthhoriline2file`](#Python_BMP.BITMAPlib.eraseeverynthhoriline2file)

```py
def eraseeverynthhoriline2file(ExistingBMPfile: str, NewBMPfile: str, n: int):
```

Erase every nth line

    Args:
        ExistingBMPfile: Whole path
                         to existing file
        NewBMPfile     : New file to
                         save changes in
        n              : erase every
                         nth line
    
    Returns:
        new bitmap file


### [`eraseeverynthhorilineinccircregion2file`](#Python_BMP.BITMAPlib.eraseeverynthhorilineinccircregion2file)

```py
def eraseeverynthhorilineinccircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, n: int):
```

Erase every nth horzontal line in a circular area

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


### [`eraseeverynthhorilineinregion2file`](#Python_BMP.BITMAPlib.eraseeverynthhorilineinregion2file)

```py
def eraseeverynthhorilineinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, n: int):
```

Erase every nth line in a rectangular region

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


### [`eraseeverynthhorilineinregion`](#Python_BMP.BITMAPlib.eraseeverynthhorilineinregion)

```py
def eraseeverynthhorilineinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, n: int):
```

Erase every nth line in a
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


### [`eraseeverynthhorizontalline`](#Python_BMP.BITMAPlib.eraseeverynthhorizontalline)

```py
def eraseeverynthhorizontalline(bmp: array.array, n: int):
```

Erase every nth horizontal line

    Args:
        bmp: unsigned byte array
             with bmp format
        n  : erase every nth line
    
    Returns:
        byref modified unsigned byte array


### [`eraseeverynthhorizontallineinccircregion`](#Python_BMP.BITMAPlib.eraseeverynthhorizontallineinccircregion)

```py
def eraseeverynthhorizontallineinccircregion(bmp: array.array, x: int, y: int, r: int, n: int):
```

Erase every nth horizontal line in a circular region

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of the circular area
        n      : erase every nth line
    
    Returns:
        byref modified unsigned byte array


### [`fern2file`](#Python_BMP.BITMAPlib.fern2file)

```py
def fern2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, color: int):
```

Fern Fractal in a bounding rectangle

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


### [`fern`](#Python_BMP.BITMAPlib.fern)

```py
def fern(bmp: array.array, x1: int, y1: int, x2: int, y2: int, color: int):
```

Draws an IFS fern fractal

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


### [`fillbackgroundwithgrad`](#Python_BMP.BITMAPlib.fillbackgroundwithgrad)

```py
def fillbackgroundwithgrad(bmp: array.array, lumrange: list[int, int], RGBfactors: list[float, float, float], direction: int):
```

Fills entire bitmap with a linear gradient

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


### [`fillboundary`](#Python_BMP.BITMAPlib.fillboundary)

```py
def fillboundary(bmp: array.array, bndfilldic: dict, color: int):
```

Draws lines in a boundary to fill it

    Args:
        bmp       : unsigned byte array
                    with bmp format
        bndfilldic: boundary dictionary
        color     : color of fill
    
    Returns:
        byref modified unsigned byte array


### [`filledcircle2file`](#Python_BMP.BITMAPlib.filledcircle2file)

```py
def filledcircle2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, color: int):
```

Draws a Filled Circle

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


### [`filledcircle`](#Python_BMP.BITMAPlib.filledcircle)

```py
def filledcircle(bmp: array.array, x: int, y: int, r: int, color: int):
```

Draws a Filled Circle

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


### [`filledellipse`](#Python_BMP.BITMAPlib.filledellipse)

```py
def filledellipse(bmp: array.array, x: int, y: int, b: int, a: int, color: int):
```

Filled Ellipse

    Args:
        bmp  : unsigned byte array
               with bmp format
        x, y : center of ellipse
        b, a : major amd minor axis
        color: color of the ellipse
    
    Returns:
        byref modified unsigned byte array


### [`filledgradrect`](#Python_BMP.BITMAPlib.filledgradrect)

```py
def filledgradrect(bmp: array.array, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int], RGBfactors: list[float, float, float], direction: int):
```

Draw a filled rectangle with a linear gradient

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


### [`filledparallelogram`](#Python_BMP.BITMAPlib.filledparallelogram)

```py
def filledparallelogram(bmp: array.array, p1: list, p2: list, p3: list, color: int):
```

Creates a filled parallelogram defined by 3 points

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


### [`filledrect`](#Python_BMP.BITMAPlib.filledrect)

```py
def filledrect(bmp: array.array, x1: int, y1: int, x2: int, y2: int, color: int):
```

Draws a Filled Rectangle

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


### [`fillpolydata`](#Python_BMP.solids3D.fillpolydata)

```py
def fillpolydata(polybnd: list[list[int, int]], xlim: int, ylim: int) -> list:
```

Generates a list of x values per
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


### [`fliphoricircregion2file`](#Python_BMP.BITMAPlib.fliphoricircregion2file)

```py
def fliphoricircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Horizontal Flip of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x,y)
                         and radius r
    
    Returns:
        new bitmap file


### [`fliphoricircregion`](#Python_BMP.BITMAPlib.fliphoricircregion)

```py
def fliphoricircregion(bmp: array.array, x: int, y: int, r: int):
```

Flips horizontally a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of circular region
    
    Returns:
        byref modified
        unsigned byte array


### [`fliphorizontal2file`](#Python_BMP.BITMAPlib.fliphorizontal2file)

```py
def fliphorizontal2file(ExistingBMPfile: str, NewBMPfile: str):
```

Flips horizontally the image in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`fliphorizontal`](#Python_BMP.BITMAPlib.fliphorizontal)

```py
def fliphorizontal(bmp: array.array):
```

Does a horizontal flip of an
    in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`fliphorizontalregion2file`](#Python_BMP.BITMAPlib.fliphorizontalregion2file)

```py
def fliphorizontalregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Flips horizontally a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region
    
    Returns:
        new bitmap file


### [`fliphorizontalregion`](#Python_BMP.BITMAPlib.fliphorizontalregion)

```py
def fliphorizontalregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Does a horizontal flip
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


### [`fliphorzontalpixelbased`](#Python_BMP.BITMAPlib.fliphorzontalpixelbased)

```py
def fliphorzontalpixelbased(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Flips horizontal
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


### [`fliphverticalalpixelbased`](#Python_BMP.BITMAPlib.fliphverticalalpixelbased)

```py
def fliphverticalalpixelbased(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Flips vertical
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


### [`flipnibbleinbuf`](#Python_BMP.bufferflip.flipnibbleinbuf)

```py
def flipnibbleinbuf(buf: array.array) -> array.array:
```

Flips a 4-bit image buffer

    Args:
        buf: unsigned byte array
    
    Returns:
        unsigned byte array


### [`flipvertcircregion2file`](#Python_BMP.BITMAPlib.flipvertcircregion2file)

```py
def flipvertcircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Vertical Flip of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`flipvertcircregion`](#Python_BMP.BITMAPlib.flipvertcircregion)

```py
def flipvertcircregion(bmp: array.array, x: int, y: int, r: int):
```

Vertical Flip of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of a region
    
    Returns:
        byref modified unsigned byte array


### [`flipvertical2file`](#Python_BMP.BITMAPlib.flipvertical2file)

```py
def flipvertical2file(ExistingBMPfile: str, NewBMPfile: str):
```

Flips a bitmap file vertically

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`flipvertical`](#Python_BMP.BITMAPlib.flipvertical)

```py
def flipvertical(bmp: array.array):
```

Does an vertical flip of a bmp

    Args:
        bmp: unsigned byte array
        with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`flipverticalregion2file`](#Python_BMP.BITMAPlib.flipverticalregion2file)

```py
def flipverticalregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Flips vertically a rectangular area in a BMP

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


### [`flipverticalregion`](#Python_BMP.BITMAPlib.flipverticalregion)

```py
def flipverticalregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Flips vertical a rectangular area

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines the
                        rectangle
    
    Returns:
        byref modified
        unsigned byte array


### [`flipXY2file`](#Python_BMP.BITMAPlib.flipXY2file)

```py
def flipXY2file(ExistingBMPfile: str, NewBMPfile: str):
```

Flips the x and y coordinates to rotate by 90 degrees

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`flipXY`](#Python_BMP.BITMAPlib.flipXY)

```py
def flipXY(bmp: array.array):
```

Flips the x and y coordinates of
    an in-memory bitmap for a
    90 degree rotation

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`flipXYcircregion2file`](#Python_BMP.BITMAPlib.flipXYcircregion2file)

```py
def flipXYcircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Flips the x and y coordinates of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`flipXYcircregion`](#Python_BMP.BITMAPlib.flipXYcircregion)

```py
def flipXYcircregion(bmp: array.array, x: int, y: int, r: int):
```

Flip the X and Y coordinates of a circular area

    Args:
        bmp     : unsigned byte array
                  with bmp format
        x, y, r : center (x,y) and
                  radius r of region
    
    Returns:
        byref modified unsigned byte array


### [`flowervert`](#Python_BMP.primitives2D.flowervert)

```py
def flowervert(cx: int, cy: int, r: int, petals: int, angrot: float):
```

Returns a list of 2D points for a flower

    Args:
        cx, cy, r : center (cx,cy)
                    and radius r
        petals    : number of petals
        angrot    : angle of rotation
    
    Returns:
        list[(x: int, y: int)]


### [`func24bitonly`](#Python_BMP.paramchecks.func24bitonly)

```py
def func24bitonly(func):
```

Decorator to restrict the
    use of this function to only
    24-bit or RGB bitmaps
    (1st parameter)

    Args:
        function(bmp:array,...)
    
    Returns:
        caller function


### [`func24bitonlyandentirecircleinboundary`](#Python_BMP.paramchecks.func24bitonlyandentirecircleinboundary)

```py
def func24bitonlyandentirecircleinboundary(func):
```

Decorator to restrict the
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


### [`func24bitonlyandentirerectinboundary`](#Python_BMP.paramchecks.func24bitonlyandentirerectinboundary)

```py
def func24bitonlyandentirerectinboundary(func):
```

Decorator to restrict the
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


### [`func8and24bitonlyandentirecircleinboundary`](#Python_BMP.paramchecks.func8and24bitonlyandentirecircleinboundary)

```py
def func8and24bitonlyandentirecircleinboundary(func):
```

Decorator to restrict the
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


### [`func8and24bitonlyandentirerectinboundary`](#Python_BMP.paramchecks.func8and24bitonlyandentirerectinboundary)

```py
def func8and24bitonlyandentirerectinboundary(func):
```

Decorator to restrict the
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


### [`functimer`](#Python_BMP.proctimer.functimer)

```py
def functimer(func):
```

Function timer Decorator

    Args:
        function
    
    Returns:
        caller function


### [`gammaadj2file`](#Python_BMP.BITMAPlib.gammaadj2file)

```py
def gammaadj2file(ExistingBMPfile: str, NewBMPfile: str, gamma: float):
```

Applies a Gamma Correction

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        gamma          : gamma
                         correction
    
    Returns:
        new bitmap file


### [`gammaadjto24bitimage`](#Python_BMP.BITMAPlib.gammaadjto24bitimage)

```py
def gammaadjto24bitimage(bmp: array.array, gamma: float):
```

Gamma correction to an in-memory 24-bit BMP

    Args:
        bmp  : unsigned byte array
               with bmp format
        gamma: gamma correction
    
    Returns:
        byref modified unsigned byte array


### [`gammaadjto24bitregion`](#Python_BMP.BITMAPlib.gammaadjto24bitregion)

```py
def gammaadjto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, gamma: float):
```

Gamma correction to a rectangular area in a 24-bit BMP

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


### [`gammaadjtoregion2file`](#Python_BMP.BITMAPlib.gammaadjtoregion2file)

```py
def gammaadjtoregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, gamma: float):
```

Gamma Correction to a Rectangular Region

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


### [`gammaBGRbuf`](#Python_BMP.colors.gammaBGRbuf)

```py
def gammaBGRbuf(buf: array.array, gamma: float) -> array.array:
```

Apply a gamma adjustment to a
    BGR buffer

    Args:
        buf: unsigned byte array
             holding BGR data
    
        gamma: float gamma adjust
    
    Returns:
        unsigned byte array
        holding gamma adjusted
        BGR data


### [`gammacorrect`](#Python_BMP.colors.gammacorrect)

```py
def gammacorrect(rgb: list[int, int, int], gamma: float) -> list[int, int, int]:
```

Apply a gamma factor to a rgb

    Args:
        rgb: color as [r: byte,
                       g: byte,
                       b: byte]
        gamma  : gamma adjustment
    
    Returns:
        a gamma adjusted color as
        [r: byte, g: byte, b: byte]


### [`gammacorrectcircregion2file`](#Python_BMP.BITMAPlib.gammacorrectcircregion2file)

```py
def gammacorrectcircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, gamma: float):
```

Gamma Adjust to a circular area in a BMP

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


### [`gammacorrectcircregion`](#Python_BMP.BITMAPlib.gammacorrectcircregion)

```py
def gammacorrectcircregion(bmp: array.array, x: int, y: int, r: int, gamma: float):
```

Gamma correction to a circular area

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


### [`genpiechartdata`](#Python_BMP.charts.genpiechartdata)

```py
def genpiechartdata(dlist: list):
```

Preprocess data to make
    it suitable for a pie chart

    Args:
        dlist: [[20, c['red']],
                [30, c['brightyellow']],
                ...]
    
    Returns:
        list and large value (if any)


### [`gensides`](#Python_BMP.solids3D.gensides)

```py
def gensides(pointlists: list[list, list], transvect: list[float, float, float], sides: list[list[float]]) -> tuple:
```

Generates a list of polygons
and normals from 3D polygon
and side data to a list of
sides and normals with
with the hidden surfaces
removed that is suitable
for rendering on a 2D surface
and also applies a
3D translation vector for
positioning

    


### [`getallRGBpal`](#Python_BMP.BITMAPlib.getallRGBpal)

```py
def getallRGBpal(bmp: array.array) -> list[list[int, int, int]]:
```

Gets the RGB palette of a bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        [(r: byte, g: byte, b: byte), ...]


### [`getBGRpalbuf`](#Python_BMP.BITMAPlib.getBGRpalbuf)

```py
def getBGRpalbuf(bmp: array.array):
```

Gets bitmap palette as stored in the bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        unsigned byte array (BGR)


### [`getBMPimgbytes`](#Python_BMP.BITMAPlib.getBMPimgbytes)

```py
def getBMPimgbytes(bmp: array.array) -> list:
```

Gets the raw image buffer of a bmp without the header

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        list of unsigned bytes


### [`getcharfont`](#Python_BMP.fonts.getcharfont)

```py
def getcharfont(charbuf: list, character: str) -> list:
```



    


### [`getcolorname2HSLdict`](#Python_BMP.colordict.getcolorname2HSLdict)

```py
def getcolorname2HSLdict() -> dict:
```



    


### [`getcolorname2RGBdict`](#Python_BMP.colordict.getcolorname2RGBdict)

```py
def getcolorname2RGBdict() -> dict:
```



    


### [`getdatalisttotal`](#Python_BMP.charts.getdatalisttotal)

```py
def getdatalisttotal(dlist: list[numbers.Number]) -> numbers.Number:
```

Returns the total of a
    list of ints or floats

    Args:
        dlist: list of ints or floats
    
    Returns:
        float or int


### [`getdefaultbitpal`](#Python_BMP.colors.getdefaultbitpal)

```py
def getdefaultbitpal(bits: int) -> list:
```

Gets the standard bitmap palette
    for a  specified bit depth bits

    Args:
        bits: int value (1, 4, 8, 24)
    
    Returns:
        list of palette entries


### [`getdefaultlumrange`](#Python_BMP.colors.getdefaultlumrange)

```py
def getdefaultlumrange() -> dict:
```

Gets the default luminosity
    ranges lookup

    Returns:
        a dict for default
        luminosity ranges


### [`getfuncmetastr`](#Python_BMP.funcmeta.getfuncmetastr)

```py
def getfuncmetastr(f: Callable):
```



    


### [`getIFSparams`](#Python_BMP.fractals.getIFSparams)

```py
def getIFSparams() -> dict:
```



    


### [`getimagedgevert`](#Python_BMP.BITMAPlib.getimagedgevert)

```py
def getimagedgevert(bmp: array.array, similaritythreshold: int):
```

Find edges in an image

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


### [`getimageregionbyRGB`](#Python_BMP.BITMAPlib.getimageregionbyRGB)

```py
def getimageregionbyRGB(bmp: array.array, rgb: list[int, int, int], similaritythreshold: int):
```

Select a region by color

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


### [`getmaxcolors`](#Python_BMP.BITMAPlib.getmaxcolors)

```py
def getmaxcolors(bmp: array.array) -> int:
```

Get the maximum number of colors supported by a BMP

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        int value


### [`getmaxx`](#Python_BMP.BITMAPlib.getmaxx)

```py
def getmaxx(bmp: array.array) -> int:
```

Gets the x value stored in the windows bmp header

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        int value of x bmp dimension


### [`getmaxxy`](#Python_BMP.BITMAPlib.getmaxxy)

```py
def getmaxxy(bmp: array.array) -> tuple:
```

Gets the max x and y values stored in the bmp header

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        tuple (x:int,y:int)


### [`getmaxxyandbits`](#Python_BMP.BITMAPlib.getmaxxyandbits)

```py
def getmaxxyandbits(bmp: array.array) -> tuple:
```

Returns bitmap metadata
   (x-dimension, y-dimension, bit depth)

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        (x-dimension, y-dimension, bit depth)


### [`getmaxy`](#Python_BMP.BITMAPlib.getmaxy)

```py
def getmaxy(bmp: array.array) -> int:
```

Gets the y value stored in the windows bmp header

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        int value of y bmp dimension


### [`getneighborcolorlist`](#Python_BMP.BITMAPlib.getneighborcolorlist)

```py
def getneighborcolorlist(bmp: array.array, v: list):
```



    


### [`getRGBfactors`](#Python_BMP.colordict.getRGBfactors)

```py
def getRGBfactors() -> dict:
```



    


### [`getRGBpal`](#Python_BMP.BITMAPlib.getRGBpal)

```py
def getRGBpal(bmp: array.array, c: int) -> list[int, int, int]:
```

Gets the [R, G, B] values
    of color c in a bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
        c  : unsigned int color
    
    Returns:
        [R: byte, G: byte, B:byte]


### [`getRGBxybit`](#Python_BMP.BITMAPlib.getRGBxybit)

```py
def getRGBxybit(bmp: array.array, x: int, y: int) -> list[int, int, int]:
```

Gets [R:byte, G:byte, B:byte]
of pixel at (x, y) in a bitmap

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int
              locations in x and y
    
    Returns:
        [R: byte, G: byte, B: byte]


### [`getRGBxybitvec`](#Python_BMP.BITMAPlib.getRGBxybitvec)

```py
def getRGBxybitvec(bmp: array.array, v: list) -> list:
```

Gets the RGB of a pixel at (x,y) in a BMP

    Args:
        bmp: unsigned byte array
             with bmp format
        v  : pixel location
             (x:int, y:int)
    
    Returns:
        [R: byte, G: byte, B: byte]


### [`getshapesidedict`](#Python_BMP.solids3D.getshapesidedict)

```py
def getshapesidedict() -> dict:
```

Returns a dictionary of side
    or polygon definitions for
    simple solids

    Returns:
        dictionary of side or polygon
        definitions for basic solids


### [`getX11colorname2HSLdict`](#Python_BMP.X11colordict.getX11colorname2HSLdict)

```py
def getX11colorname2HSLdict() -> dict:
```



    


### [`getX11colorname2RGBdict`](#Python_BMP.X11colordict.getX11colorname2RGBdict)

```py
def getX11colorname2RGBdict() -> dict:
```



    


### [`getX11RGBfactors`](#Python_BMP.X11colordict.getX11RGBfactors)

```py
def getX11RGBfactors() -> dict:
```



    


### [`getXKCDcolorname2HSLdict`](#Python_BMP.XKCDcolordict.getXKCDcolorname2HSLdict)

```py
def getXKCDcolorname2HSLdict() -> dict:
```



    


### [`getXKCDcolorname2RGBdict`](#Python_BMP.XKCDcolordict.getXKCDcolorname2RGBdict)

```py
def getXKCDcolorname2RGBdict() -> dict:
```



    


### [`getXKCDRGBfactors`](#Python_BMP.XKCDcolordict.getXKCDRGBfactors)

```py
def getXKCDRGBfactors() -> dict:
```



    


### [`getxybit`](#Python_BMP.BITMAPlib.getxybit)

```py
def getxybit(bmp: array.array, x: int, y: int) -> int:
```

Gets color of pixel at (x, y) in a BMP

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int
              locations in x and y
    
    Returns:
        unsigned int color value


### [`getxybitvec`](#Python_BMP.BITMAPlib.getxybitvec)

```py
def getxybitvec(bmp: array.array, v: list) -> int:
```

Gets color of pixel at (x, y)

    Args:
        bmp: unsigned byte array
             with bmp format
        v  : (x: int, y: int)
             pixel coordinates
    
    Returns:
        unsigned int color value


### [`gradcircle`](#Python_BMP.BITMAPlib.gradcircle)

```py
def gradcircle(bmp: array.array, x: int, y: int, r: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):
```

Filled Circle with Gradient

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


### [`gradellipse`](#Python_BMP.BITMAPlib.gradellipse)

```py
def gradellipse(bmp: array.array, x: int, y: int, b: int, a: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):
```

Ellipical gradient

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


### [`gradthickcircle`](#Python_BMP.BITMAPlib.gradthickcircle)

```py
def gradthickcircle(bmp: array.array, x: int, y: int, r: int, penradius: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):
```

Thick Circle with a Gradient

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


### [`gradthickellipserot`](#Python_BMP.BITMAPlib.gradthickellipserot)

```py
def gradthickellipserot(bmp: array.array, x: int, y: int, b: int, a: int, degrot: float, penradius: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):
```

Thick Ellipse with a Gradient fill

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


### [`gradthickplotpoly`](#Python_BMP.BITMAPlib.gradthickplotpoly)

```py
def gradthickplotpoly(bmp: array.array, vertlist: list, penradius: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):
```

Draws a polygon of a given gradient and thickness

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


### [`gradthickroundline`](#Python_BMP.BITMAPlib.gradthickroundline)

```py
def gradthickroundline(bmp: array.array, p1: list, p2: list, penradius: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):
```

Draw a Thick Rounded Line with a Gradient

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


### [`gradvert`](#Python_BMP.BITMAPlib.gradvert)

```py
def gradvert(bmp: array.array, vertlist: list[list[int, int]], penradius: int, lumrange: list[int, int], RGBfactors: list[float, float, float]):
```

List of 2d vertices as spheres of a given color

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


### [`hexahedravert`](#Python_BMP.solids3D.hexahedravert)

```py
def hexahedravert(x: float) -> list[list[float, float, float]]:
```

Returns a list of vertices
    for a hexahedron

    Args:
        x: length of a side
    
    Returns:
        list (x: float,
              y: float,
              z: float)


### [`horibrightnessgrad2circregion2file`](#Python_BMP.BITMAPlib.horibrightnessgrad2circregion2file)

```py
def horibrightnessgrad2circregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, lumrange: list[int, int]):
```

Horizontal brightness gradient to a circular area

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


### [`horibrightnessgrad2circregion`](#Python_BMP.BITMAPlib.horibrightnessgrad2circregion)

```py
def horibrightnessgrad2circregion(bmp: array.array, x: int, y: int, r: int, lumrange: list[int, int]):
```

Horizontal brightness gradient adjustment to a circular area

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


### [`horiline`](#Python_BMP.BITMAPlib.horiline)

```py
def horiline(bmp: array.array, y: int, x1: int, x2: int, color: int):
```

Draw a Horizontal Line

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


### [`horilinevert`](#Python_BMP.BITMAPlib.horilinevert)

```py
def horilinevert(bmp: array.array, vlist: list[list[int, int]], linelen: int, xadj: int, color: int):
```

Horizontal line marks at vertices in vlist

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


### [`horitransformincircregion`](#Python_BMP.BITMAPlib.horitransformincircregion)

```py
def horitransformincircregion(bmp: array.array, x: int, y: int, r: int, trans: str):
```

Horizontal transform to a circular area

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


### [`horizontalbrightnessgrad2file`](#Python_BMP.BITMAPlib.horizontalbrightnessgrad2file)

```py
def horizontalbrightnessgrad2file(ExistingBMPfile: str, NewBMPfile: str, lumrange: list[int, int]):
```

Horizontal brightness gradient to a BMP

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


### [`horizontalbrightnessgradregion2file`](#Python_BMP.BITMAPlib.horizontalbrightnessgradregion2file)

```py
def horizontalbrightnessgradregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int]):
```

Horizontal brightness gradient to a rectangular area

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


### [`horizontalbrightnessgradto24bitimage`](#Python_BMP.BITMAPlib.horizontalbrightnessgradto24bitimage)

```py
def horizontalbrightnessgradto24bitimage(bmp: array.array, lumrange: list[int, int]):
```

Applies a horizontal brightness
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


### [`horizontalbrightnessgradto24bitregion`](#Python_BMP.BITMAPlib.horizontalbrightnessgradto24bitregion)

```py
def horizontalbrightnessgradto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int]):
```

Apply a horizontal brightness gradient
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


### [`horizontalbulkswap`](#Python_BMP.BITMAPlib.horizontalbulkswap)

```py
def horizontalbulkswap(bmp: array.array, x1: int, y1: int, x2: int, y2: int, swapfunc: Callable):
```

Applies function swapfunc
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


### [`horizontalvert`](#Python_BMP.primitives2D.horizontalvert)

```py
def horizontalvert(y: int, x1: int, x2: int, dx: int) -> list[list[int, int]]:
```

Creates a list of int vertices along
a horizontal line with int step dx

    Args:
        y : int constant y
        x1: int start point
        x2: int end point
        dx: int x step increment
    
    Returns:
        list of int vertices
        [(x, y), ...]


### [`hypotrochoidvert`](#Python_BMP.primitives2D.hypotrochoidvert)

```py
def hypotrochoidvert(x: int, y: int, a: float, b: float, c: float, delta: float, lim: float):
```

Returns (int, int) 2D vertices
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


### [`icosahedvertandsurface`](#Python_BMP.solids3D.icosahedvertandsurface)

```py
def icosahedvertandsurface(x: float) -> list[list[list[float, float, float]], tuple]:
```

Returns a list of vertices
    and surfaces for an icosahedron

    Args:
        x: min radius of sphere
           that can hold
           the icosahedron
    
    Returns:
        list (x: float,
              y: float,
              z: float)


### [`IFS`](#Python_BMP.BITMAPlib.IFS)

```py
def IFS(bmp: array.array, IFStransparam: tuple, x1: int, y1: int, x2: int, y2: int, xscale: int, yscale: int, xoffset: int, yoffset: int, color: int, maxiter: int):
```

Draw an Interated Function System Fractal

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


### [`iif`](#Python_BMP.conditionaltools.iif)

```py
def iif(boolcond: bool, trueval: <built-in function any>, falseval: <built-in function any>) -> <built-in function any>:
```

Returns trueval if
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


### [`imagecomp`](#Python_BMP.BITMAPlib.imagecomp)

```py
def imagecomp(inputfile1: str, inputfile2: str, diff_file: str, func: Callable):
```

Perform a bitwise comparison of two bitmap files
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


### [`imagediff`](#Python_BMP.BITMAPlib.imagediff)

```py
def imagediff(inputfile1: str, inputfile2: str, diff_file: str):
```

Compares 2 files and saves diff to a bitmap file

    Args:
        inputfile1: Whole paths
        inputfile2 to existing files
    
        diff_file: New file
                   to store diff
    
    Returns:
        new bitmap file


### [`imgregionbyRGB2file`](#Python_BMP.BITMAPlib.imgregionbyRGB2file)

```py
def imgregionbyRGB2file(ExistingBMPfile: str, NewBMPfile: str, edgeradius: int, edgecolor: int, rgb: list[int, int, int], similaritythreshold: float, showedgeonly: bool):
```

Gets an image region by rgb in a bitmap file

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


### [`int2BGRarr`](#Python_BMP.colors.int2BGRarr)

```py
def int2BGRarr(i: int) -> array.array:
```

Returns a bgr array from
    int i color input

    Args:
        i: color value
    
    Returns:
        unsigned byte BGR array


### [`int2buf`](#Python_BMP.inttools.int2buf)

```py
def int2buf(cnt: int, value: int) -> array.array:
```

Converts an integer value to an
    unsigned byte array

    Args:
        cnt   : uint length of int data
        value : value of uint data
    
    Returns:
        unsigned byte array


### [`int2RGB`](#Python_BMP.colors.int2RGB)

```py
def int2RGB(i: int):
```

Break down int color i to its
    byte valued r, g and b
    components

    Args:
        i: int color value
    
    Returns:
        r: byte, g: byte, b: byte


### [`int2RGBarr`](#Python_BMP.colors.int2RGBarr)

```py
def int2RGBarr(i: int) -> array.array:
```

Returns a rgb array from
    int i color input

    
    Args:
        i: color value
    
    Returns:
        unsigned byte RGB array


### [`int2RGBlist`](#Python_BMP.colors.int2RGBlist)

```py
def int2RGBlist(i: int) -> list[int, int, int]:
```

Break down int color i to its
    byte valued r, g and b
    components in a list

    Args:
        i: int color value
    
    Returns:
        [r: byte, g: byte, b: byte]


### [`intcircleparam24bitonly`](#Python_BMP.paramchecks.intcircleparam24bitonly)

```py
def intcircleparam24bitonly(func):
```

Decorator to test if 2nd, 3rd,
    4th parameters in a function
    that renders circle are ints
    and restrict the use of this
    function to only 24-bit or
    RGB bitmaps (1st parameter)

    Args:
        function(bmp:array,x,y,r....)
    
    Returns:
        caller function


### [`intcircleparam`](#Python_BMP.paramchecks.intcircleparam)

```py
def intcircleparam(func):
```

Decorator to test if the
    2nd, 3rd, 4th parameters
    in a function that renders
    circle are ints

    Args:
        function(bmp:array,x,y,r....)
    
    Returns:
        caller function


### [`intlinevec`](#Python_BMP.BITMAPlib.intlinevec)

```py
def intlinevec(bmp: array.array, u: list, v: list, color: int):
```

Draw a line in a bitmap

    Args:
        bmp   : unsigned byte array
                with bmp format
        u, v  : (x: int, y: int) points
                that defines the line
        color : color of the line
    
    Returns:
        byref modified unsigned byte array


### [`intplotvecxypoint`](#Python_BMP.BITMAPlib.intplotvecxypoint)

```py
def intplotvecxypoint(bmp: array.array, v: list[int, int], c: int):
```

Sets the color of a pixel at (x, y)

    Args:
        bmp: unsigned byte array
             with bmp format
        v  : (x:int, y:int)
             pixel coordinates
        c  : unsigned int
             color value
    
    Returns:
        byref modified unsigned byte array


### [`intscalarmulvect`](#Python_BMP.mathlib.intscalarmulvect)

```py
def intscalarmulvect(vec: list[numbers.Number], scalarval: numbers.Number) -> list[int]:
```

Scales a vector by multiplying a scalar value (float)
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


### [`invertbits2file`](#Python_BMP.BITMAPlib.invertbits2file)

```py
def invertbits2file(ExistingBMPfile: str, NewBMPfile: str):
```

Inverts the bits in a bmp file

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`invertbitsinbuffer`](#Python_BMP.colors.invertbitsinbuffer)

```py
def invertbitsinbuffer(buf: array.array) -> array.array:
```

Flips all the bits in an
    unsigned byte array

    Args:
        buf: unsigned byte array
    
    Returns:
        bit flipped unsigned byte array


### [`invertbitsincircregion2file`](#Python_BMP.BITMAPlib.invertbitsincircregion2file)

```py
def invertbitsincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Inverts bits in a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`invertbitsincircregion`](#Python_BMP.BITMAPlib.invertbitsincircregion)

```py
def invertbitsincircregion(bmp: array.array, x: int, y: int, r: int):
```

Inverts the bits in a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x,y)
                 and radius r
                 of the region
    
    Returns:
        byref modified unsigned byte array


### [`invertimagebits`](#Python_BMP.BITMAPlib.invertimagebits)

```py
def invertimagebits(bmp: array.array):
```

Inverts the bits in a bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified unsigned byte array


### [`invertregion2file`](#Python_BMP.BITMAPlib.invertregion2file)

```py
def invertregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Inverts the bits in a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region
    
    Returns:
        new bitmap file


### [`invertregion`](#Python_BMP.BITMAPlib.invertregion)

```py
def invertregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Inverts the bits in a
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


### [`isdefaultpal`](#Python_BMP.BITMAPlib.isdefaultpal)

```py
def isdefaultpal(bmp: array.array) -> bool:
```

Checks if bitmap has a default RGB color palette

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        True if default
        False if not default


### [`isinBMPrectbnd`](#Python_BMP.BITMAPlib.isinBMPrectbnd)

```py
def isinBMPrectbnd(bmp: array.array, x: int, y: int) -> bool:
```

Checks if (x,y) coordinates are within the BMP

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int value
              of location
              in x-axis and y-axis
    
    Returns:
        True if within bounds
        False if out of bounds


### [`isinrange`](#Python_BMP.mathlib.isinrange)

```py
def isinrange(value: numbers.Number, highlimit: numbers.Number, lowlimit: numbers.Number) -> bool:
```

Checks is value is within high and low limits

    Args:
        value    : numeric variable
                   to check
        highlimit: upper limit of
                   the variable
        lowlimit : lower limit of
                   the variable
    
    Returns:
        True if within bounds


### [`isinrectbnd`](#Python_BMP.primitives2D.isinrectbnd)

```py
def isinrectbnd(x: int, y: int, xmin: int, ymin: int, xmax: int, ymax: int) -> bool:
```

Checks if the x and y values
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


### [`isvalidcolorbit`](#Python_BMP.colors.isvalidcolorbit)

```py
def isvalidcolorbit(bits: int) -> bool:
```

Checks if bits is in the valid
    color bits list (1, 4, 8, 24)

    Args:
        bits: int value
    
    Returns:
        True if bits in (1, 4, 8, 24)
        False if other values not in
              the list above


### [`iterbeziercurve`](#Python_BMP.primitives2D.iterbeziercurve)

```py
def iterbeziercurve(pntlist: list[list[int, int]]) -> list[int, int]:
```

Yields a list of vertices for a bezier curve
based on 2D control points in pntlist

    Args:
        pntlist: 2D control points
                 for the bezier curve
                 as list[list[x: int,
                              y: int]]
    
    Yields:
        vertices as list[x: int, y: int]


### [`iterbspline`](#Python_BMP.primitives2D.iterbspline)

```py
def iterbspline(pntlist: list[list[int, int]], isclosed: bool, curveback: bool) -> list[int, int]:
```

Yields a list of vertices for a bspline curve
based on 2D control points in pntlist

    Args:
        pntlist: 2D control points
                 for the bspline curve
                 as list[list[x: int,
                              y: int]]
    
    Yields:
        vertices as list[x: int, y: int]


### [`itercircle`](#Python_BMP.primitives2D.itercircle)

```py
def itercircle(x: int, y: int, r: int) -> list[int, int]:
```

Yields (int, int) 2D vertices along
a path defined by radius r as it traces
a circle with origin set at (x, y)

    Args:
        x, y: int centerpoint
                  coordinates
        r   : int radius
    
    Yields:
        [x: int, y: int]


### [`itercircleinvolute`](#Python_BMP.primitives2D.itercircleinvolute)

```py
def itercircleinvolute(x: int, y: int, a: float, delta: float, lim: float):
```

Yields (int, int) 2D vertices
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


### [`itercirclepart`](#Python_BMP.primitives2D.itercirclepart)

```py
def itercirclepart(r: int) -> list[int, int]:
```

Yields (int, int) 2D vertices along
a path defined by radius r as it traces
one fourth of a circle with origin set
at (0, 0)

    Args:
        r: int radius
    
    Yields:
        [x: int, y: int]


### [`itercirclepartlineedge`](#Python_BMP.primitives2D.itercirclepartlineedge)

```py
def itercirclepartlineedge(r: int) -> list[int, int]:
```

Yields (int, int) 2D vertices along
a path defined by radius r as it traces
one fourth of a circle with origin set
at (0, 0) tuned for generating
filled circles with horizontal lines
 and other tasks involving circular areas

    Args:
        r: int radius
    
    Yields:
        [x: int, y: int]


### [`itercirclepartvertlineedge`](#Python_BMP.primitives2D.itercirclepartvertlineedge)

```py
def itercirclepartvertlineedge(r: int) -> list[int, int]:
```

Yields (int, int) 2D vertices along
a path defined by radius r as it traces
one fourth of a circle with origin set
at (0, 0) tuned for generating
filled circles with vertical lines
and other tasks involving circular areas

    Args:
        r: int radius
    
    Yields:
        [x: int, y: int]


### [`itercopyrect`](#Python_BMP.BITMAPlib.itercopyrect)

```py
def itercopyrect(bmp: array.array, x1: int, y1: int, x2: int, y2: int) -> array.array:
```

Scan a rectangular area and yield scan lines

    Args:
        bmp            : unsigned
                         byte array
                         with bmp format
        x1, y1, x2, y2 : defines the
                         rectangle
    
    Yields:
        unsigned byte array
        scanlines of the area


### [`iterdrawvec`](#Python_BMP.primitives2D.iterdrawvec)

```py
def iterdrawvec(u: list, v: list, headsize: int):
```

Yields a vector (line segment with arrow head)

    Args:
        u       : (x: float, y: float)
                  point 1 origin
        v       : (x: float, y: float)
                  point 2 has arrow
        headsize: size of the arrow
                  0 for default size
    
    Yields:
        ((x1: int, y1: int), (x2: int, y2: int))


### [`iterellipse`](#Python_BMP.primitives2D.iterellipse)

```py
def iterellipse(x: int, y: int, b: int, a: int):
```

Yields (int, int) 2D vertices along
a path defined by major and minor axes
b and a as it traces an ellipse with
origin set at (x, y)

    Args:
        b, a: major and minor axes
    
    Yields:
        [x: int, y: int]


### [`iterellipsepart`](#Python_BMP.primitives2D.iterellipsepart)

```py
def iterellipsepart(b: int, a: int):
```

Yields (int, int) 2D vertices along
a path defined by major and minor axes
b and a as it traces one fourth of an
ellipse with origin set at (0, 0)

    Args:
        b, a: major and minor axes
    
    Yields:
        [x: int, y: int]


### [`iterellipserot`](#Python_BMP.primitives2D.iterellipserot)

```py
def iterellipserot(x: int, y: int, b: int, a: int, degrot: float):
```

Yields (int, int) 2D vertices along
a path defined by major and minor axes
b and a as it traces an ellipse with origin
set at (x, y) rotated by degrot degrees

    Args:
        b, a: major and minor axes
        degrot: rotation in degrees
    
    Yields:
        [x: int, y: int]


### [`iterepicycloid`](#Python_BMP.primitives2D.iterepicycloid)

```py
def iterepicycloid(x: int, y: int, a: float, b: float, delta: float, lim: float):
```

Yields (int, int) 2D vertices
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


### [`iterflower`](#Python_BMP.primitives2D.iterflower)

```py
def iterflower(cx: int, cy: int, r: int, petals: int, angrot: float):
```

Yields 2D points for a flower

    Args:
        cx, cy, r : center (cx,cy)
                    and radius r
        petals    : number of petals
        angrot    : angle of rotation
    
    Yields:
        (x: int, y: int)


### [`itergetcolorfromrectregion`](#Python_BMP.BITMAPlib.itergetcolorfromrectregion)

```py
def itergetcolorfromrectregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Yields color info of
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


### [`itergetneighbors`](#Python_BMP.primitives2D.itergetneighbors)

```py
def itergetneighbors(v: list[int, int], mx: int, my: int, includecenter: bool) -> list[int, int]:
```

Yields the neighboring pixels of point v

    Args:
        v : (x: int, y: int) point
        mx: maximum x
        my: maximum y
        includecenter: do we yield
                       point v too
    
    Yields:
        [x: int, y: int]


### [`iterhypotrochoid`](#Python_BMP.primitives2D.iterhypotrochoid)

```py
def iterhypotrochoid(x: int, y: int, a: float, b: float, c: float, delta: float, lim: float):
```

Yields (int, int) 2D vertices
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


### [`iterIFS`](#Python_BMP.fractals.iterIFS)

```py
def iterIFS(IFStransparam: tuple, x1: int, y1: int, x2: int, y2: int, xscale: int, yscale: int, xoffset: int, yoffset: int, maxiter: int):
```

Yield 2D points for an Interated Function System Fractal

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


### [`iterimagecolor`](#Python_BMP.BITMAPlib.iterimagecolor)

```py
def iterimagecolor(bmp: array.array, waitmsg: str, rowprocind: str, finishmsg: str):
```

Yields color information for entire bitmap

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


### [`iterimagedgevert`](#Python_BMP.BITMAPlib.iterimagedgevert)

```py
def iterimagedgevert(bmp: array.array, similaritythreshold: float):
```

Find edges in an image

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


### [`iterimageregionvertbyRGB`](#Python_BMP.BITMAPlib.iterimageregionvertbyRGB)

```py
def iterimageregionvertbyRGB(bmp: array.array, rgb: list[int, int, int], similaritythreshold: int):
```

RGB Color selection by color similarity

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


### [`iterimageRGB`](#Python_BMP.BITMAPlib.iterimageRGB)

```py
def iterimageRGB(bmp: array.array, waitmsg: str, rowprocind: str, finishmsg: str):
```

Yields (r, g, b) information for the entire bitmap

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


### [`iterline`](#Python_BMP.primitives2D.iterline)

```py
def iterline(p1: list[int, int], p2: list[int, int]) -> list[int, int]:
```

Yields (int, int) 2D vertices
along a line segment defined
by endpoints p1 and p2

    Args:
        p1, p2: line endpoints
                both [x:int, y:int]
    
    Yields:
        [x:int, y:int]


### [`iterlissajouscurve`](#Python_BMP.primitives2D.iterlissajouscurve)

```py
def iterlissajouscurve(x: int, y: int, a: float, b: float, c: float, d: float, e: float, delta: float, lim: float):
```

Yields (int, int) 2D vertices
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


### [`itermandelbrot`](#Python_BMP.fractals.itermandelbrot)

```py
def itermandelbrot(x1: int, y1: int, x2: int, y2: int, mandelparam: list[float, float, float, float], maxiter: int):
```

Yields a Mandelbrot set

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


### [`iterparallelogram`](#Python_BMP.primitives2D.iterparallelogram)

```py
def iterparallelogram(p1: list[int, int], p2: list[int, int], p3: list[int, int]) -> list[int, int]:
```



    


### [`iterspirograph`](#Python_BMP.primitives2D.iterspirograph)

```py
def iterspirograph(x: int, y: int, r: int, l: float, k: float, delta: float, lim: float):
```

Yields (int, int) 2D vertices
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


### [`line`](#Python_BMP.BITMAPlib.line)

```py
def line(bmp: array.array, x1: int, y1: int, x2: int, y2: int, color: int):
```

Draw a Line in a bitmap

    Args:
        bmp   : unsigned byte array
                with bmp format
        x1, y1: endpoint 1
        x2, y2: endpoint 2
        color : color of the line
    
    Returns:
        byref modified
        unsigned byte array


### [`linevec`](#Python_BMP.BITMAPlib.linevec)

```py
def linevec(bmp: array.array, u: list, v: list, color: int):
```

Draw a line in a bitmap

    Args:
        bmp  : unsigned byte array
               with bmp format
        u, v : (x:float,y:float)
               the endpoints
               of the line
        color: the color of the line
    
    Returns:
        byref modified unsigned byte array


### [`lissajouscurvevert`](#Python_BMP.primitives2D.lissajouscurvevert)

```py
def lissajouscurvevert(x: int, y: int, a: float, b: float, c: float, d: float, e: float, delta: float, lim: float):
```

Returns (int, int) 2D vertices
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


### [`listinBMPrecbnd`](#Python_BMP.BITMAPlib.listinBMPrecbnd)

```py
def listinBMPrecbnd(bmp: array.array, xylist: list) -> bool:
```

Checks if a list of (x, y) coordinates are within the BMP

    Args:
        bmp   : unsigned byte array
                with bmp format
        xylist: list of (x, y)
                coordinates
                to be checked
    
    Returns:
        True if within bounds
        False if out of bounds


### [`listinrecbnd`](#Python_BMP.primitives2D.listinrecbnd)

```py
def listinrecbnd(xylist: list[list[numbers.Number, numbers.Number]], xmin: int, ymin: int, xmax: int, ymax: int) -> bool:
```

Checks if all the values in a
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


### [`loadBMP`](#Python_BMP.BITMAPlib.loadBMP)

```py
def loadBMP(filename: str) -> array.array:
```

Load bitmap to a byte array
   (uncompressed bitmap only)

    Args:
        filename: full path to
                  the file to be loaded
    
    Returns:
        byte array with bmp file contents


### [`LSMslope`](#Python_BMP.mathlib.LSMslope)

```py
def LSMslope(XYdata: list) -> float:
```

Slope of a line obtained by Least Squares Method

    Args:
        XYdata: list of vectors
        first two values in the
        list must be [[x, y, ..,], ...]
    
    Returns:
        float slope of line


### [`LSMYint`](#Python_BMP.mathlib.LSMYint)

```py
def LSMYint(XYdata: list) -> float:
```

Returns the y-intercept of a line obtained
by Least Squares Method

    Args:
        XYdata: list of vectors
        first two values in the
        list must be [[x, y, ..,], ...]
    
    Returns:
        float y-intercept of line


### [`magnifyNtimescircregion2file`](#Python_BMP.BITMAPlib.magnifyNtimescircregion2file)

```py
def magnifyNtimescircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, intmagfactor: int):
```

Magnify a circular region by an integer factor n times

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


### [`magnifyNtimescircregion`](#Python_BMP.BITMAPlib.magnifyNtimescircregion)

```py
def magnifyNtimescircregion(bmp: array.array, x: int, y: int, r: int, n: int):
```

Magnify a circular region in a bitmap file by int n

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x,y)
                 and radius r
        n      : int magnification
                 factor
    
    Returns:
        byref modified unsigned byte array


### [`makeBGRbuf`](#Python_BMP.colors.makeBGRbuf)

```py
def makeBGRbuf(bbuf: array.array, gbuf: array.array, rbuf: array.array) -> array.array:
```

Assemble a BGR buffer from
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


### [`makenewpalfromcolorhist`](#Python_BMP.BITMAPlib.makenewpalfromcolorhist)

```py
def makenewpalfromcolorhist(chist: list, colors: int, similaritythreshold: float) -> list:
```

Creates a new palatte based on a color histogram

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


### [`mandelbrot`](#Python_BMP.BITMAPlib.mandelbrot)

```py
def mandelbrot(bmp: array.array, x1: int, y1: int, x2: int, y2: int, mandelparam: list[float, float, float, float], RGBfactors: list[float, float, float], maxiter: int):
```

Draw a Mandelbrot set

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


### [`mandelparamdict`](#Python_BMP.fractals.mandelparamdict)

```py
def mandelparamdict() -> dict:
```



    


### [`matchRGBtopal`](#Python_BMP.colors.matchRGBtopal)

```py
def matchRGBtopal(RGB: list, pal: list) -> int:
```

Color matching from a 24-bit
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


### [`mirror`](#Python_BMP.mathlib.mirror)

```py
def mirror(pt: float, delta: float):
```

Mirrors a value in a numberline

    Args:
        pt   : real value in numberline
        delta: value to mirror
    
    Returns:
        pt - delta, pt + delta


### [`mirrorbottom2file`](#Python_BMP.BITMAPlib.mirrorbottom2file)

```py
def mirrorbottom2file(ExistingBMPfile: str, NewBMPfile: str):
```

Mirrors the bottom half of a BMP

    Args:
        ExistingBMPfile: Whole path
                         to an existing
                         file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`mirrorbottom`](#Python_BMP.BITMAPlib.mirrorbottom)

```py
def mirrorbottom(bmp: array.array):
```

Mirrors the bottom-half of a bmp

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`mirrorbottomincircregion2file`](#Python_BMP.BITMAPlib.mirrorbottomincircregion2file)

```py
def mirrorbottomincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Mirror the bottom-half of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`mirrorbottomincircregion`](#Python_BMP.BITMAPlib.mirrorbottomincircregion)

```py
def mirrorbottomincircregion(bmp: array.array, x: int, y: int, r: int):
```

Mirror the bottom-half of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of region
    
    Returns:
        byref modified unsigned byte array


### [`mirrorbottominregion2file`](#Python_BMP.BITMAPlib.mirrorbottominregion2file)

```py
def mirrorbottominregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the bottom-half region in a rectangular area in a bmp

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region
    
    Returns:
        new bitmap file


### [`mirrorbottominregion`](#Python_BMP.BITMAPlib.mirrorbottominregion)

```py
def mirrorbottominregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Mirror the bottom-half
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


### [`mirrorbottomleft2file`](#Python_BMP.BITMAPlib.mirrorbottomleft2file)

```py
def mirrorbottomleft2file(ExistingBMPfile: str, NewBMPfile: str):
```

Mirrors the bottom-left of a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`mirrorbottomleft`](#Python_BMP.BITMAPlib.mirrorbottomleft)

```py
def mirrorbottomleft(bmp: array.array):
```

Mirrors the bottom-left part
    of an in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`mirrorbottomleftincircregion2file`](#Python_BMP.BITMAPlib.mirrorbottomleftincircregion2file)

```py
def mirrorbottomleftincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Mirror the bottom-left of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`mirrorbottomleftincircregion`](#Python_BMP.BITMAPlib.mirrorbottomleftincircregion)

```py
def mirrorbottomleftincircregion(bmp: array.array, x: int, y: int, r: int):
```

Mirror the bottom-left of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x,y) and
                 radius r of region
    
    Returns:
        byref modified unsigned byte array


### [`mirrorbottomleftinregion2file`](#Python_BMP.BITMAPlib.mirrorbottomleftinregion2file)

```py
def mirrorbottomleftinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the bottom-left region in a rectangular area in a bmp

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region
    
    Returns:
        new bitmap file


### [`mirrorbottomleftinregion`](#Python_BMP.BITMAPlib.mirrorbottomleftinregion)

```py
def mirrorbottomleftinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the bottom-left of a
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


### [`mirrorbottomright2file`](#Python_BMP.BITMAPlib.mirrorbottomright2file)

```py
def mirrorbottomright2file(ExistingBMPfile: str, NewBMPfile: str):
```

Mirrors the bottom-right of a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`mirrorbottomright`](#Python_BMP.BITMAPlib.mirrorbottomright)

```py
def mirrorbottomright(bmp: array.array):
```

Mirrors the bottom right part
    of an in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`mirrorbottomrightincircregion2file`](#Python_BMP.BITMAPlib.mirrorbottomrightincircregion2file)

```py
def mirrorbottomrightincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Mirror the bottom-right of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`mirrorbottomrightincircregion`](#Python_BMP.BITMAPlib.mirrorbottomrightincircregion)

```py
def mirrorbottomrightincircregion(bmp: array.array, x: int, y: int, r: int):
```

Mirror the bottom-right of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x,y) and
                 radius r of region
    
    Returns:
        byref modified unsigned byte array


### [`mirrorbottomrightinregion2file`](#Python_BMP.BITMAPlib.mirrorbottomrightinregion2file)

```py
def mirrorbottomrightinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the bottom-right region in a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2  :the rectangular
                         region
    
    Returns:
        new bitmap file


### [`mirrorbottomrightinregion`](#Python_BMP.BITMAPlib.mirrorbottomrightinregion)

```py
def mirrorbottomrightinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the bottom-right of a
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


### [`mirrorleft2file`](#Python_BMP.BITMAPlib.mirrorleft2file)

```py
def mirrorleft2file(ExistingBMPfile: str, NewBMPfile: str):
```

Mirrors the left-half of a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`mirrorleft`](#Python_BMP.BITMAPlib.mirrorleft)

```py
def mirrorleft(bmp: array.array):
```

Mirrors the left-half of an
    in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`mirrorleftincircregion2file`](#Python_BMP.BITMAPlib.mirrorleftincircregion2file)

```py
def mirrorleftincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Mirror the left-half of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`mirrorleftincircregion`](#Python_BMP.BITMAPlib.mirrorleftincircregion)

```py
def mirrorleftincircregion(bmp: array.array, x: int, y: int, r: int):
```

Mirrors the top-left of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y) and
                 radius r of region
    
    Returns:
        byref modified unsigned byte array


### [`mirrorleftinregion2file`](#Python_BMP.BITMAPlib.mirrorleftinregion2file)

```py
def mirrorleftinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the left-half region in a rectangular area in a bmp

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


### [`mirrorleftinregion`](#Python_BMP.BITMAPlib.mirrorleftinregion)

```py
def mirrorleftinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the left-half
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


### [`mirrorright2file`](#Python_BMP.BITMAPlib.mirrorright2file)

```py
def mirrorright2file(ExistingBMPfile: str, NewBMPfile: str):
```

Mirrors the right half of a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`mirrorright`](#Python_BMP.BITMAPlib.mirrorright)

```py
def mirrorright(bmp: array.array):
```

Mirrors the right-half of an
    in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`mirrorrightincircregion2file`](#Python_BMP.BITMAPlib.mirrorrightincircregion2file)

```py
def mirrorrightincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Mirror the right-half of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`mirrorrightincircregion`](#Python_BMP.BITMAPlib.mirrorrightincircregion)

```py
def mirrorrightincircregion(bmp: array.array, x: int, y: int, r: int):
```

Mirrors the right-half of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of a region
    
    Returns:
        byref modified unsigned byte array


### [`mirrorrightinregion2file`](#Python_BMP.BITMAPlib.mirrorrightinregion2file)

```py
def mirrorrightinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the right-half region in a rectangular area in a bmp

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region
    
    Returns:
        new bitmap file


### [`mirrorrightinregion`](#Python_BMP.BITMAPlib.mirrorrightinregion)

```py
def mirrorrightinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the right-half of
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


### [`mirrortop2file`](#Python_BMP.BITMAPlib.mirrortop2file)

```py
def mirrortop2file(ExistingBMPfile: str, NewBMPfile: str):
```

Mirrors the top-half of a bitmap

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`mirrortop`](#Python_BMP.BITMAPlib.mirrortop)

```py
def mirrortop(bmp: array.array):
```

Mirrors the top-half of a bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`mirrortopincircregion2file`](#Python_BMP.BITMAPlib.mirrortopincircregion2file)

```py
def mirrortopincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Mirror the top-half of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`mirrortopincircregion`](#Python_BMP.BITMAPlib.mirrortopincircregion)

```py
def mirrortopincircregion(bmp: array.array, x: int, y: int, r: int):
```

Mirror the top-half of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r of area
    
    Returns:
        byref modified unsigned byte array


### [`mirrortopinregion2file`](#Python_BMP.BITMAPlib.mirrortopinregion2file)

```py
def mirrortopinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the top-half region in a rectangular area in a bmp

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region
    
    Returns:
        new bitmap file


### [`mirrortopinregion`](#Python_BMP.BITMAPlib.mirrortopinregion)

```py
def mirrortopinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Mirror the top-half of
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


### [`mirrortopleft2file`](#Python_BMP.BITMAPlib.mirrortopleft2file)

```py
def mirrortopleft2file(ExistingBMPfile: str, NewBMPfile: str):
```

Mirrors the top-left of a bitmap

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`mirrortopleft`](#Python_BMP.BITMAPlib.mirrortopleft)

```py
def mirrortopleft(bmp):
```

Mirrors the top-left part
    of an in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`mirrortopleftincircregion2file`](#Python_BMP.BITMAPlib.mirrortopleftincircregion2file)

```py
def mirrortopleftincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Mirror the top-left of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes to
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`mirrortopleftincircregion`](#Python_BMP.BITMAPlib.mirrortopleftincircregion)

```py
def mirrortopleftincircregion(bmp: array.array, x: int, y: int, r: int):
```

Mirror the top-left of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of region
    
    Returns:
        byref modified unsigned byte array


### [`mirrortopleftinregion2file`](#Python_BMP.BITMAPlib.mirrortopleftinregion2file)

```py
def mirrortopleftinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the top-left region in a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region
    
    Returns:
        new bitmap file


### [`mirrortopleftinregion`](#Python_BMP.BITMAPlib.mirrortopleftinregion)

```py
def mirrortopleftinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the top-left of a
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


### [`mirrortopright2file`](#Python_BMP.BITMAPlib.mirrortopright2file)

```py
def mirrortopright2file(ExistingBMPfile: str, NewBMPfile: str):
```

Mirrors the top-right of a
    bitmap file

    Args:
        ExistingBMPfile: Whole path
                         to existing
                         file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`mirrortopright`](#Python_BMP.BITMAPlib.mirrortopright)

```py
def mirrortopright(bmp: array.array):
```

Mirrors the top-right part
    of an in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`mirrortoprightincircregion2file`](#Python_BMP.BITMAPlib.mirrortoprightincircregion2file)

```py
def mirrortoprightincircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Mirror the top-right of a circular area

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`mirrortoprightincircregion`](#Python_BMP.BITMAPlib.mirrortoprightincircregion)

```py
def mirrortoprightincircregion(bmp: array.array, x: int, y: int, r: int):
```

Mirror the top-right of a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y) and
                 radius r of region
    
    Returns:
        byref modified unsigned byte array


### [`mirrortoprightinregion2file`](#Python_BMP.BITMAPlib.mirrortoprightinregion2file)

```py
def mirrortoprightinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the top-right region in a rectangular area in a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x1, y1, x2, y2 : the rectangular
                         region
    
    Returns:
        new bitmap file


### [`mirrortoprightinregion`](#Python_BMP.BITMAPlib.mirrortoprightinregion)

```py
def mirrortoprightinregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Mirrors the top-right of a
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


### [`monochrome2file`](#Python_BMP.BITMAPlib.monochrome2file)

```py
def monochrome2file(ExistingBMPfile: str, NewBMPfile: str):
```

Applies a monochrome filter to a BMP

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`monochrome`](#Python_BMP.colors.monochrome)

```py
def monochrome(rgb: list[int, int, int]) -> list[int, int, int]:
```

Returns a monochrome color
    based on a 24-bit RGB value

    Args:
        rgb: color values
            [r: byte, g: byte, b: byte]
    
    Returns:
        a gray color (r = g = b)
        [r: byte, g: byte, b: byte]


### [`monochromecircregion2file`](#Python_BMP.BITMAPlib.monochromecircregion2file)

```py
def monochromecircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Monochrome filter to a circular region

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


### [`monochromefiltertoBGRbuf`](#Python_BMP.colors.monochromefiltertoBGRbuf)

```py
def monochromefiltertoBGRbuf(buf: array.array) -> array.array:
```

Apply a monochrome filter to a
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


### [`monochromepal`](#Python_BMP.colors.monochromepal)

```py
def monochromepal(bits: int, rgbfactors: list[float, float, float]) -> list[list[int, int, int]]:
```

Returns a monochrome palette
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


### [`monocircle`](#Python_BMP.BITMAPlib.monocircle)

```py
def monocircle(bmp: array.array, x: int, y: int, r: int):
```

Monochrome filter to a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of the region
    
    Returns:
        byref modified unsigned byte array


### [`monofilterinregion2file`](#Python_BMP.BITMAPlib.monofilterinregion2file)

```py
def monofilterinregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Monochrome filter to rectangular area in a 24-bit BMP

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


### [`monofilterto24bitimage`](#Python_BMP.BITMAPlib.monofilterto24bitimage)

```py
def monofilterto24bitimage(bmp: array.array):
```

Applies a mono filter
    to a 24 bit in-memory bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified
        unsigned byte array


### [`monofilterto24bitregion`](#Python_BMP.BITMAPlib.monofilterto24bitregion)

```py
def monofilterto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Applies a monochrome filter
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


### [`newBMP`](#Python_BMP.BITMAPlib.newBMP)

```py
def newBMP(x: int, y: int, colorbits: int) -> array.array:
```

Creates a new in-memory bitmap

    Args:
        x, y     : unsigned int values
                   of x and y dims
        colorbits: bit depth
                   (1, 4, 8, 24) bits
    
    Returns:
        unsigned byte array with bitmap layout


### [`numbervert`](#Python_BMP.BITMAPlib.numbervert)

```py
def numbervert(bmp: array.array, vlist: list[list[int, int]], xadj: int, yadj: int, scale: int, valstart: numbers.Number, valstep: numbers.Number, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list, suppresszero: bool, suppresslastnum: bool, rightjustify: bool):
```



    


### [`octahedravert`](#Python_BMP.solids3D.octahedravert)

```py
def octahedravert(x: float) -> list[list[float, float, float]]:
```

Returns a list of vertices
    for an octrahedron

    Args:
        x: length of a side
    
    Returns:
        list (x: float,
              y: float,
              z: float)


### [`outline2file`](#Python_BMP.BITMAPlib.outline2file)

```py
def outline2file(ExistingBMPfile: str, NewBMPfile: str):
```

Applies an outline filter

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`outline`](#Python_BMP.BITMAPlib.outline)

```py
def outline(bmp: array.array):
```

Applies an Outline Filter

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified unsigned byte array


### [`outlinecircregion2file`](#Python_BMP.BITMAPlib.outlinecircregion2file)

```py
def outlinecircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int):
```

Outlines area in a circular region

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        x, y, r        : center (x, y)
                         and radius r
    
    Returns:
        new bitmap file


### [`outlinecircregion`](#Python_BMP.BITMAPlib.outlinecircregion)

```py
def outlinecircregion(bmp: array.array, x: int, y: int, r: int):
```

Outlines a circular area

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
                 of the region
    
    Returns:
        byref modified unsigned byte array


### [`outlineregion2file`](#Python_BMP.BITMAPlib.outlineregion2file)

```py
def outlineregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int):
```

Outline filter to rectangular area

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


### [`outlineregion`](#Python_BMP.BITMAPlib.outlineregion)

```py
def outlineregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int):
```

Outines a rectangular region in a BMP

    Args:
        bmp           : unsigned
                        byte array
                        with bmp format
        x1, y1, x2, y2: defines
                        the rectangular
                        region
    
    Returns:
        byref modified unsigned byte array


### [`pastecirularbuf`](#Python_BMP.BITMAPlib.pastecirularbuf)

```py
def pastecirularbuf(bmp: array.array, x: int, y: int, circbuf: list):
```

Paste a circular buffer with a
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


### [`pasterect`](#Python_BMP.BITMAPlib.pasterect)

```py
def pasterect(bmp: array.array, buf: array.array, x1: int, y1: int):
```

Paste a rectangular area from a buffer to a bmp

    Args:
        bmp   : unsigned byte array
                with bmp format
        buf   : rectangular
                image buffer
        x1, y1: point to paste
                the buffer
    
    Returns:
        byref modified unsigned byte array


### [`perspective`](#Python_BMP.solids3D.perspective)

```py
def perspective(vlist: list[list[numbers.Number, numbers.Number, numbers.Number]], rotvec: list[list[float, float], list[float, float], list[float, float]], dispvec: list[numbers.Number, numbers.Number, numbers.Number], d: float) -> tuple:
```

Projects 3D points to 2D and
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


### [`piechart`](#Python_BMP.BITMAPlib.piechart)

```py
def piechart(bmp: array.array, x: int, y: int, r: int, dataandcolorlist: list):
```

Draw a piechart

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


### [`pixelizenxn`](#Python_BMP.BITMAPlib.pixelizenxn)

```py
def pixelizenxn(bmp: array.array, n: int) -> array.array:
```

Pixelize a whole image with n by n areas
in which colors are averaged

    Args:
        bmp: unsigned byte array
             with bmp format
        n  : size of pixel blur
    
    Returns:
        byref modified unsigned byte array


### [`pixelizenxncircregion2file`](#Python_BMP.BITMAPlib.pixelizenxncircregion2file)

```py
def pixelizenxncircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, intpixsize: int):
```

Apply a Pixel Blur in a circular area

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


### [`pixelizenxncircregion`](#Python_BMP.BITMAPlib.pixelizenxncircregion)

```py
def pixelizenxncircregion(bmp: array.array, x: int, y: int, r: int, n: int):
```

Pixelize a circular region in a BMP by n

    Args:
        bmp    : unsigned byte array
                 with bmp format
        x, y, r: center (x, y)
                 and radius r
        n      : integer pixellation
                 dimension n by n
    
    Returns:
        byref modified unsigned byte array


### [`pixelizenxntofile`](#Python_BMP.BITMAPlib.pixelizenxntofile)

```py
def pixelizenxntofile(ExistingBMPfile: str, NewBMPfile: str, n: int):
```

Pixellate a bitmap file with n by n pixel areas

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`plot3d`](#Python_BMP.BITMAPlib.plot3d)

```py
def plot3d(bmp: array.array, sides: list[list, list], issolid: bool, RGBfactors: list[float, float], showoutline: bool, outlinecolor: int):
```

The 3D rendering function

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


### [`plot3Dsolid`](#Python_BMP.BITMAPlib.plot3Dsolid)

```py
def plot3Dsolid(bmp: array.array, vertandsides: list[list, list], issolid: bool, RGBfactors: list[float, float, float], showoutline: bool, outlinecolor: int, rotvect: list[float, float, float], transvect3D: list[float, float, float], d: int, transvect: list[int, int]):
```

3D solid rendering function

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


### [`plot8bitpattern`](#Python_BMP.BITMAPlib.plot8bitpattern)

```py
def plot8bitpattern(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit pattern

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


### [`plot8bitpatternasdots`](#Python_BMP.BITMAPlib.plot8bitpatternasdots)

```py
def plot8bitpatternasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit pattern as circles

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


### [`plot8bitpatternastext`](#Python_BMP.textgraphics.plot8bitpatternastext)

```py
def plot8bitpatternastext(bitpattern: list[int], onechar: str, zerochar: str):
```

Outputs the bits of a list
    of bytes to console

    Args:
        bitpattern: list of bytes
        onechar   : char to display
                    if bit is 1
        zeropchar : char to display
                    if bit is 0
    
    Returns:
        console output


### [`plot8bitpatternsideway`](#Python_BMP.BITMAPlib.plot8bitpatternsideway)

```py
def plot8bitpatternsideway(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit pattern sideways

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


### [`plot8bitpatternsidewaywithdots`](#Python_BMP.BITMAPlib.plot8bitpatternsidewaywithdots)

```py
def plot8bitpatternsidewaywithdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit pattern sideways with dots

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


### [`plot8bitpatternsidewaywithfn`](#Python_BMP.BITMAPlib.plot8bitpatternsidewaywithfn)

```py
def plot8bitpatternsidewaywithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):
```

Draws a 8-bit pattern sideways with a function

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


### [`plot8bitpatternupsidedown`](#Python_BMP.BITMAPlib.plot8bitpatternupsidedown)

```py
def plot8bitpatternupsidedown(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit pattern upsidedown

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


### [`plot8bitpatternupsidedownasdots`](#Python_BMP.BITMAPlib.plot8bitpatternupsidedownasdots)

```py
def plot8bitpatternupsidedownasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit pattern upsidedown with dots

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


### [`plot8bitpatternupsidedownwithfn`](#Python_BMP.BITMAPlib.plot8bitpatternupsidedownwithfn)

```py
def plot8bitpatternupsidedownwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):
```

Draws a 8-bit pattern upsidedown with a function

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


### [`plot8bitpatternwithfn`](#Python_BMP.BITMAPlib.plot8bitpatternwithfn)

```py
def plot8bitpatternwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):
```

8-bit pattern with a function

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


### [`plotbitsastext`](#Python_BMP.textgraphics.plotbitsastext)

```py
def plotbitsastext(bits: int):
```

Outputs the bits of byte to
    console

    Args:
        bits: byte value
    
    Returns:
        space for 0
        *     for 1


### [`plotbmpastext`](#Python_BMP.BITMAPlib.plotbmpastext)

```py
def plotbmpastext(bmp: array.array):
```

Plot a bitmap as text
(cannot output 24-bit bmp)

    Args:
        bmp : unsigned byte array
              with bmp format
    
    Returns:
        console text output
        for debug and ascii art


### [`plotcircinsqr`](#Python_BMP.BITMAPlib.plotcircinsqr)

```py
def plotcircinsqr(bmp, x, y, d, color):
```

Draws a circle in an
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


### [`plotfilledflower`](#Python_BMP.BITMAPlib.plotfilledflower)

```py
def plotfilledflower(bmp: array.array, cx: int, cy: int, r: int, petals: float, angrot: float, lumrange: list[int, int], RGBfactors: list[float, float, float]):
```

Draw a filled flower

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


### [`plotflower`](#Python_BMP.BITMAPlib.plotflower)

```py
def plotflower(bmp: array.array, cx: int, cy: int, r: int, petals: float, angrot: float, lumrange: list[int, int], RGBfactors: list[float, float, float]):
```

Draw a flower

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


### [`plotimgedges`](#Python_BMP.BITMAPlib.plotimgedges)

```py
def plotimgedges(bmp: array.array, similaritythreshold: int, edgeradius: int, edgecolor: int):
```

Draw edges

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


### [`plotitalic8bitpattern`](#Python_BMP.BITMAPlib.plotitalic8bitpattern)

```py
def plotitalic8bitpattern(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit italic pattern

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


### [`plotitalic8bitpatternasdots`](#Python_BMP.BITMAPlib.plotitalic8bitpatternasdots)

```py
def plotitalic8bitpatternasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit italic pattern as dots

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


### [`plotitalic8bitpatternsideway`](#Python_BMP.BITMAPlib.plotitalic8bitpatternsideway)

```py
def plotitalic8bitpatternsideway(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws an italic 8-bit pattern sideways

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


### [`plotitalic8bitpatternsidewayasdots`](#Python_BMP.BITMAPlib.plotitalic8bitpatternsidewayasdots)

```py
def plotitalic8bitpatternsidewayasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws an italic 8-bit pattern sideways as dots

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


### [`plotitalic8bitpatternsidewaywithfn`](#Python_BMP.BITMAPlib.plotitalic8bitpatternsidewaywithfn)

```py
def plotitalic8bitpatternsidewaywithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):
```

Draws an Italic 8-bit pattern sideways with a function

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


### [`plotitalic8bitpatternupdsidedownasdots`](#Python_BMP.BITMAPlib.plotitalic8bitpatternupdsidedownasdots)

```py
def plotitalic8bitpatternupdsidedownasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit italic pattern upsidedown as dots

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


### [`plotitalic8bitpatternupsidedownwithfn`](#Python_BMP.BITMAPlib.plotitalic8bitpatternupsidedownwithfn)

```py
def plotitalic8bitpatternupsidedownwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):
```

Italic 8-bit pattern upsidedown with a function

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


### [`plotitalic8bitpatternwithfn`](#Python_BMP.BITMAPlib.plotitalic8bitpatternwithfn)

```py
def plotitalic8bitpatternwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):
```

Italic 8-bit pattern with a function

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


### [`plotitalicstring`](#Python_BMP.BITMAPlib.plotitalicstring)

```py
def plotitalicstring(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string as Italic

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


### [`plotitalicstringasdots`](#Python_BMP.BITMAPlib.plotitalicstringasdots)

```py
def plotitalicstringasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string as Italic dots

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


### [`plotitalicstringsideway`](#Python_BMP.BITMAPlib.plotitalicstringsideway)

```py
def plotitalicstringsideway(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws an Italic String Sideways

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


### [`plotitalicstringsidewayasdots`](#Python_BMP.BITMAPlib.plotitalicstringsidewayasdots)

```py
def plotitalicstringsidewayasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws an italic string sideways as dots

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


### [`plotitalicstringvertical`](#Python_BMP.BITMAPlib.plotitalicstringvertical)

```py
def plotitalicstringvertical(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws an italic string vertically with dots

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


### [`plotitalicstringverticalasdots`](#Python_BMP.BITMAPlib.plotitalicstringverticalasdots)

```py
def plotitalicstringverticalasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws an italic string vertically with dots

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


### [`plotlines`](#Python_BMP.BITMAPlib.plotlines)

```py
def plotlines(bmp: array.array, vertlist: list, color: int):
```

Draws connected lines defined by a list of vertices

    Args:
        bmp     : unsigned byte array
                  with bmp format
        vertlist: [(x:uint,y:uint),...]
                  list of vertices
        color   : color of the lines
    
    Returns:
        byref modified unsigned byte array


### [`plotpoly`](#Python_BMP.BITMAPlib.plotpoly)

```py
def plotpoly(bmp: array.array, vertlist: list, color: int):
```

Draws a polygon defined by a list of vertices

    Args:
        bmp     : unsigned byte array
                  with bmp format
        vertlist: [(x:uint,y:uint),...]
                  list of vertices
        color   : color of the lines
    
    Returns:
        byref modified unsigned byte array


### [`plotpolyfill`](#Python_BMP.BITMAPlib.plotpolyfill)

```py
def plotpolyfill(bmp: array.array, vertlist: list[list[numbers.Number, numbers.Number]], color: int):
```

Draws a filled polygon with a given color

    Args:
        bmp     : unsigned byte array
                  with bmp format
        vertlist: [(x, y), ...]
                  list of vertices
        color   : color of the
                  filled polygon
    
    Returns:
        byref modified unsigned byte array


### [`plotpolyfillist`](#Python_BMP.BITMAPlib.plotpolyfillist)

```py
def plotpolyfillist(bmp: array.array, sides: list[list[list[list]], list[list[float, float, float]]], RGBfactors: list[float, float]):
```

3D polygon rendering function

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


### [`plotpolylist`](#Python_BMP.BITMAPlib.plotpolylist)

```py
def plotpolylist(bmp: array.array, polylist: list, color: int):
```

Draws a list of polygons of a given color

    Args:
        bmp      : unsigned byte array
                   with bmp format
        polytlist: [[(x:uint,y:uint),
                    ...],...]
                   list of polygons
        color    : color of the lines
    
    Returns:
        byref modified unsigned byte array


### [`plotreverseditalic8bitpattern`](#Python_BMP.BITMAPlib.plotreverseditalic8bitpattern)

```py
def plotreverseditalic8bitpattern(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit reversed italic pattern

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


### [`plotreverseditalic8bitpatternasdots`](#Python_BMP.BITMAPlib.plotreverseditalic8bitpatternasdots)

```py
def plotreverseditalic8bitpatternasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit reversed italic pattern as dots

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


### [`plotreverseditalicstring`](#Python_BMP.BITMAPlib.plotreverseditalicstring)

```py
def plotreverseditalicstring(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a reversed string as Italic

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


### [`plotreverseditalicstringasdots`](#Python_BMP.BITMAPlib.plotreverseditalicstringasdots)

```py
def plotreverseditalicstringasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a Reversed String as Italic dots

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


### [`plotreversestring`](#Python_BMP.BITMAPlib.plotreversestring)

```py
def plotreversestring(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string reversed

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


### [`plotreversestringasdots`](#Python_BMP.BITMAPlib.plotreversestringasdots)

```py
def plotreversestringasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string reversed with dots

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


### [`plotRGBxybit`](#Python_BMP.BITMAPlib.plotRGBxybit)

```py
def plotRGBxybit(bmp: array.array, x: int, y: int, rgb: list):
```

Sets pixel at (x, y) in a bitmap to color [R, G, B]

    Args:
        bmp: unsigned byte array
             with bmp format
        x,y: unsigned int locations
             in x and y
        rgb: color defined by
             [R: byte, G: byte, B: byte]
    
    Returns:
        byref modified unsigned byte array


### [`plotRGBxybitvec`](#Python_BMP.BITMAPlib.plotRGBxybitvec)

```py
def plotRGBxybitvec(bmp: array.array, v: list, rgb: list):
```

Sets [R, G, B] of pixel at (x, y)

    Args:
        bmp: unsigned byte array
             with bmp format
        v  : (x: float, y: float)
        rgb: [R: byte,
              G: byte,
              B: byte]
    
    Returns:
        byref modified unsigned byte array


### [`plotrotated8bitpattern`](#Python_BMP.BITMAPlib.plotrotated8bitpattern)

```py
def plotrotated8bitpattern(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit pattern with the bits rotated

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


### [`plotrotated8bitpatternwithdots`](#Python_BMP.BITMAPlib.plotrotated8bitpatternwithdots)

```py
def plotrotated8bitpatternwithdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit pattern with the bits rotated

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


### [`plotrotated8bitpatternwithfn`](#Python_BMP.BITMAPlib.plotrotated8bitpatternwithfn)

```py
def plotrotated8bitpatternwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):
```

Draws a 8-bit pattern with
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


### [`plotrotateditalic8bitpatternwithfn`](#Python_BMP.BITMAPlib.plotrotateditalic8bitpatternwithfn)

```py
def plotrotateditalic8bitpatternwithfn(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int, fn: Callable):
```

Bit rotated Italic 8-bit pattern
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


### [`plotstring`](#Python_BMP.BITMAPlib.plotstring)

```py
def plotstring(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string

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


### [`plotstringasdots`](#Python_BMP.BITMAPlib.plotstringasdots)

```py
def plotstringasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string as Dots

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


### [`plotstringfunc`](#Python_BMP.BITMAPlib.plotstringfunc)

```py
def plotstringfunc(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list, orderfunc: Callable, fontrenderfunc: Callable):
```

Draws a string

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


### [`plotstringsideway`](#Python_BMP.BITMAPlib.plotstringsideway)

```py
def plotstringsideway(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string sideways

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


### [`plotstringsidewayasdots`](#Python_BMP.BITMAPlib.plotstringsidewayasdots)

```py
def plotstringsidewayasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string sideways as dots

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


### [`plotstringsidewayfn`](#Python_BMP.BITMAPlib.plotstringsidewayfn)

```py
def plotstringsidewayfn(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list, fn: Callable):
```

Draws a string sideways with a function

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


### [`plotstringupsidedown`](#Python_BMP.BITMAPlib.plotstringupsidedown)

```py
def plotstringupsidedown(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string upsidedown

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


### [`plotstringupsidedownasdots`](#Python_BMP.BITMAPlib.plotstringupsidedownasdots)

```py
def plotstringupsidedownasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string upsidedown as dots

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


### [`plotstringvertical`](#Python_BMP.BITMAPlib.plotstringvertical)

```py
def plotstringvertical(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string vertically

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


### [`plotstringverticalasdots`](#Python_BMP.BITMAPlib.plotstringverticalasdots)

```py
def plotstringverticalasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draws a string vertically with dots

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


### [`plotstringverticalwithfn`](#Python_BMP.BITMAPlib.plotstringverticalwithfn)

```py
def plotstringverticalwithfn(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list, fn: Callable):
```

Draws a string vertically using a function

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


### [`plotupsidedownitalic8bitpattern`](#Python_BMP.BITMAPlib.plotupsidedownitalic8bitpattern)

```py
def plotupsidedownitalic8bitpattern(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit italic pattern upsidedown

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


### [`plotupsidedownitalic8bitpatternasdots`](#Python_BMP.BITMAPlib.plotupsidedownitalic8bitpatternasdots)

```py
def plotupsidedownitalic8bitpatternasdots(bmp: array.array, x: int, y: int, bitpattern: list, scale: int, pixspace: int, color: int):
```

Draws a 8-bit italic pattern upsidedown as dots

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


### [`plotupsidedownitalicstring`](#Python_BMP.BITMAPlib.plotupsidedownitalicstring)

```py
def plotupsidedownitalicstring(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draw an italic string upsidedown

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


### [`plotupsidedownitalicstringasdots`](#Python_BMP.BITMAPlib.plotupsidedownitalicstringasdots)

```py
def plotupsidedownitalicstringasdots(bmp: array.array, x: int, y: int, str2plot: str, scale: int, pixspace: int, spacebetweenchar: int, color: int, fontbuf: list):
```

Draw an italic string upsidedown as dots

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


### [`plotvecxypoint`](#Python_BMP.BITMAPlib.plotvecxypoint)

```py
def plotvecxypoint(bmp: array.array, v: list, c: int):
```

Sets the color of a pixel
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


### [`plotxybit`](#Python_BMP.BITMAPlib.plotxybit)

```py
def plotxybit(bmp: array.array, x: int, y: int, c: int):
```

Sets pixel at (x, y) in a bitmap to color c

    Args:
        bmp : unsigned byte array
              with bmp format
        x, y: unsigned int
              locations in x and y
        c   : unsigned int color
    
    Returns:
        byref modified unsigned byte array


### [`plotxypointlist`](#Python_BMP.BITMAPlib.plotxypointlist)

```py
def plotxypointlist(bmp: array.array, vlist: list, penradius: int, color: int):
```

Draws a circle or a point
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


### [`polar2rectcoord2D`](#Python_BMP.mathlib.polar2rectcoord2D)

```py
def polar2rectcoord2D(vpolarcoord: list[float, float]) -> list[float, float]:
```

Converts from polar coordinates with
origin at (0, 0) to 2D rectangular coordinates

    Args:
        vcylindcoord:(r: float,
                  theta: float)
    
    Returns:
        [x: float,
         y: float]


### [`polyboundary`](#Python_BMP.solids3D.polyboundary)

```py
def polyboundary(vertlist: list[list[int, int]]) -> list[list[int, int]]:
```

Generates a polygon boundary
    from a list of 2D vertices

    Args:
        polybnd : list of 2D vertices
                  list[list[x: int,
                            y: int]]
    
    Returns:
        list[list[x: int, y: int]]
        A list of vertices that traces
        the boundaries of the polygon


### [`probplotRGBto1bit`](#Python_BMP.colors.probplotRGBto1bit)

```py
def probplotRGBto1bit(rgb: list[int, int, int], brightness: int) -> int:
```

Use a non deterministic plot
    to convert 24-bit colors to
    1-bit

    Args:
        rgb: color byte values
             [r: byte,
              g: byte,
              b: byte]
    
    Returns:
        0 or 1


### [`range2baseanddelta`](#Python_BMP.mathlib.range2baseanddelta)

```py
def range2baseanddelta(lst_range: list[int, int]):
```

Gets the base and range values in a list of numbers

    Args:
        lst_range: list[min: int,
                        max: int]
    
    Returns:
        minimum value and delta of min and max value
        in lst_range


### [`readint`](#Python_BMP.inttools.readint)

```py
def readint(offset: int, cnt: int, arr: int) -> int:
```

Reads an integer value in an
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


### [`rectangle2file`](#Python_BMP.BITMAPlib.rectangle2file)

```py
def rectangle2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, color: int):
```

Draws a Rectangle

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


### [`rectangle`](#Python_BMP.BITMAPlib.rectangle)

```py
def rectangle(bmp: array.array, x1: int, y1: int, x2: int, y2: int, color: int):
```

Draws a Rectangle

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


### [`rectboundarycoords`](#Python_BMP.primitives2D.rectboundarycoords)

```py
def rectboundarycoords(vlist: list) -> list:
```

Returns the rectangular bounds of a list of 2D vertices

    Args:
        vlist: list[(x: int, y :int)]
    
    Yields:
        ((min(x), min(y)),
         (max(x), max(y)))


### [`recvert`](#Python_BMP.primitives2D.recvert)

```py
def recvert(x1: int, y1: int, x2: int, y2: int) -> list[list[int, int], list[int, int], list[int, int], list[int, int]]:
```

Creates a list of vertices for a rectangle

    Args:
        x1, y1, x1, y2: int values
    
    Returns:
        list of vertices
        [(x1, y1), (x2, y1),
         (x2, y2), (x1, y2)]


### [`reduce24bitimagebits`](#Python_BMP.BITMAPlib.reduce24bitimagebits)

```py
def reduce24bitimagebits(Existing24BMPfile: str, NewBMPfile: str, newbits: int, similaritythreshold: float, usemonopal: bool, RGBfactors: list[float, float, float] = None):
```

Reduce bits used to encode color in a 24-bit BMP

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


### [`regpolygonvert`](#Python_BMP.primitives2D.regpolygonvert)

```py
def regpolygonvert(cx: int, cy: int, r: int, sides: int, angle: float) -> list[list[int, int]]:
```

Creates a list of int vertices for a regular polygon

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


### [`resizebufNtimesbigger`](#Python_BMP.bufresize.resizebufNtimesbigger)

```py
def resizebufNtimesbigger(buf: array.array, n: int, bits: int) -> array.array:
```

Resize a buffer n times bigger
    given a particular bit depth n

    Args:
        buf : array to resize
        n   : resize factor
        bits: bit depth of
              color info
              (1, 4, 8, 24) bits
    
    Returns:
        list


### [`resizeNtimesbigger2file`](#Python_BMP.BITMAPlib.resizeNtimesbigger2file)

```py
def resizeNtimesbigger2file(ExistingBMPfile: str, NewBMPfile: str, n: int):
```

Resize a bitmap file n times bigger

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`resizeNtimesbigger`](#Python_BMP.BITMAPlib.resizeNtimesbigger)

```py
def resizeNtimesbigger(bmp: array.array, n: int):
```

Resize an in-memory bmp
    n times bigger

    Args:
        buf : array to resize
        n   : resize factor
        bits: bit depth of
              the color info
              (1, 4, 8, 24)
    
    Returns:
        unsigned byte array


### [`resizeNtimessmaller2file`](#Python_BMP.BITMAPlib.resizeNtimessmaller2file)

```py
def resizeNtimessmaller2file(ExistingBMPfile: str, NewBMPfile: str, n: int):
```

Resize a bitmap file n times smaller

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`resizeNtimessmaller`](#Python_BMP.BITMAPlib.resizeNtimessmaller)

```py
def resizeNtimessmaller(bmp: array.array, n: int) -> array.array:
```

Resize a whole image int n times smaller

    Args:
        bmp: unsigned byte array
             with bmp format
        n  : int resize factor
    
    Returns:
        byref modified unsigned byte array


### [`resizesmaller24bitbuf`](#Python_BMP.bufresize.resizesmaller24bitbuf)

```py
def resizesmaller24bitbuf(buf: array.array) -> array.array:
```

Resize a 24-bit buffer
    n times smaller

    Args:
        buf: unsigned byte array
        n  : buffer multiplier
    
    Returns:
        unsigned byte array


### [`RGB2BGRarr`](#Python_BMP.colors.RGB2BGRarr)

```py
def RGB2BGRarr(r: int, g: int, b: int) -> array.array:
```

Returns a bgr array from
    individual r, g and b color
    component inputs

    Args:
        r, g, b: byte color values
    
    Returns:
        unsigned byte BGR array


### [`RGB2BGRbuf`](#Python_BMP.colors.RGB2BGRbuf)

```py
def RGB2BGRbuf(buf: array.array):
```

Convert an RGB buffer
         to a BGR buffer

    Args:
        buf: unsigned byte array
             holding RGB data
    
    Returns:
        byref unsigned byte array
        holding BGR data


### [`RGB2HSL`](#Python_BMP.colors.RGB2HSL)

```py
def RGB2HSL(r: int, g: int, b: int) -> list[int, int, int]:
```

Converts an RGB value to HSL

    Args:
        r: unsigned byte red value
        g: unsigned byte green value
        b: unsigned byte blue value
    
    Returns:
        [hue: int,  ->  in degrees
         sat: int,  ->  percentage
         lum: int]  ->  percentage


### [`RGB2int`](#Python_BMP.colors.RGB2int)

```py
def RGB2int(r: int, g: int, b: int) -> int:
```

Pack byte r, g and b color value
    components to an int
    representation for a
    specific color

    Args:
        r, g, b: color byte values
    
    Returns:
        int color val


### [`RGBfactors2RGB`](#Python_BMP.colors.RGBfactors2RGB)

```py
def RGBfactors2RGB(RGBfactors: list[float, float, float], bytelum: int) -> list[int, int, int]:
```

Mix a byte luminosity value to
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


### [`RGBfactorstoBaseandRange`](#Python_BMP.colors.RGBfactorstoBaseandRange)

```py
def RGBfactorstoBaseandRange(lumrange: list[int, int], rgbfactors: list[float, float, float]):
```

Get base color luminosity and
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


### [`RGBpalbrightnessadjust`](#Python_BMP.BITMAPlib.RGBpalbrightnessadjust)

```py
def RGBpalbrightnessadjust(bmp: array.array, percentadj: float) -> list:
```

Copies the RGB palette info from
a source unsigned byte array to
a destination unsigned byte array

    Args:
        bmp       : unsigned byte array
                    with bmp format
        percentadj: signed float
                    brightness adj in %
    
    Returns:
        list of modified RGB values


### [`rotatebits`](#Python_BMP.mathlib.rotatebits)

```py
def rotatebits(bits: int) -> int:
```

Rotates the bits in a byte

    Args:
        bits: the int 8 bits to rotate
    
    Returns:
        int value of rotated 8 bits


### [`rotatebitsinbuf`](#Python_BMP.bufferflip.rotatebitsinbuf)

```py
def rotatebitsinbuf(buf: array.array) -> array.array:
```

Does a bit rotate to the bytes
    in an unsigned byte array

    Args:
        buf: unsigned byte array
    
    Returns:
        unsigned byte array


### [`rotvec3D`](#Python_BMP.solids3D.rotvec3D)

```py
def rotvec3D(roll: float, pitch: float, yaw: float) -> tuple:
```

Returns a 3D rotation vector

    Args:
        All input arguements are in
        degrees (roll, pitch, yaw)
    
    Returns:
        tuple ((float, float),
               (float, float),
               (float, float))


### [`roundpen`](#Python_BMP.BITMAPlib.roundpen)

```py
def roundpen(bmp: array.array, point: list, penradius: int, color: int):
```

Draws a circle or a point
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


### [`roundvect`](#Python_BMP.mathlib.roundvect)

```py
def roundvect(v: list[numbers.Number]) -> list[int]:
```

Rounds off the components of a vector
   (list of floats -> list of ints)

    Args:
        v: list of floats
    
    Returns:
        list of ints


### [`saveBMP`](#Python_BMP.BITMAPlib.saveBMP)

```py
def saveBMP(filename: str, bmp: array.array):
```

Saves bitmap to file

    Args:
        filename: full path to
                  the file to be saved
        bmp     : unsigned byte array
                  with the layout of
                  a bitmap file
    Returns:
        A Bitmap File


### [`setBMP2monochrome`](#Python_BMP.BITMAPlib.setBMP2monochrome)

```py
def setBMP2monochrome(bmp: array.array, RGBfactors: list[float, float, float]) -> list:
```

Sets a bitmap to use a monochrome palette

    Args:
        bmp       : unsigned byte array
                    with bmp format
        RGBfactors: (r, g, b)
                    all values range
                    from 0.0 to 1.0
    
    Returns:
        list of modified RGB values
        byref modified byte array


### [`setBMPimgbytes`](#Python_BMP.BITMAPlib.setBMPimgbytes)

```py
def setBMPimgbytes(bmp: array.array, buf: array.array):
```

Sets the raw image buffer of a bitmap

    Args:
        bmp: unsigned byte array
             with bmp format
        buf: array of unsigned bytes
    
    Returns:
        byref modified  unsigned byte array


### [`setbmppal`](#Python_BMP.BITMAPlib.setbmppal)

```py
def setbmppal(bmp: array.array, pallist: list):
```

Sets the RGB palette of a bitmap

    Args:
        bmp    : unsigned byte array
                 with bmp format
        pallist: [(r: byte,
                   g: byte,
                   b: byte), ...]
    
    Returns:
        byref modified unsigned byte array


### [`setmax`](#Python_BMP.mathlib.setmax)

```py
def setmax(val: numbers.Number, maxval: numbers.Number) -> numbers.Number:
```

Set the value of val to maxval if val > maxval

    Args:
        val   : numeric variable
        maxval: upper limit of variable
    
    Returns:
        Number


### [`setmin`](#Python_BMP.mathlib.setmin)

```py
def setmin(val: numbers.Number, minval: numbers.Number) -> numbers.Number:
```

Set the value of val to minval if val < minval

    Args:
        val   : numeric variable
        minval: lower limit of variable
    
    Returns:
        Number


### [`setminmax`](#Python_BMP.mathlib.setminmax)

```py
def setminmax(val: numbers.Number, minval: numbers.Number, maxval: numbers.Number) -> numbers.Number:
```

Set the value of val to minval if val < minval
or the value of val to maxval if val > maxval

    Args:
        val   : numeric variable
        minval: lower limit of variable
        maxval: upper limit of variable
    
    Returns:
        Number


### [`setnewpalfromsourcebmp`](#Python_BMP.BITMAPlib.setnewpalfromsourcebmp)

```py
def setnewpalfromsourcebmp(sourcebmp: array.array, newbmp: array.array, similaritythreshold: float) -> list:
```

Copies the RGB palette info from
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


### [`setRGBpal`](#Python_BMP.BITMAPlib.setRGBpal)

```py
def setRGBpal(bmp: array.array, c: int, r: int, g: int, b: int):
```

Sets the r,g,b values of color c in a bitmap

    Args:
        bmp    : unsigned byte array
                 with bmp format
        r, g, b: unsigned byte values
                 for red, green and
                 blue
        c      : unsigned int color
    
    Returns:
        byref modified unsigned byte array


### [`showsimilarparts`](#Python_BMP.BITMAPlib.showsimilarparts)

```py
def showsimilarparts(inputfile1: str, inputfile2: str, diff_file: str):
```

Compares 2 files and saves the similar parts to a BMP

    Args:
        inputfile1: Whole paths
        inputfile2  to existing files
    
        diff_file : New file to
                    store similar parts
    
    Returns:
        new bitmap file


### [`sortrecpoints`](#Python_BMP.primitives2D.sortrecpoints)

```py
def sortrecpoints(x1: int, y1: int, x2: int, y2: int):
```

Sorts the x and y values that sets a rectangular area

    Args:
        x1, x2: int x coordinates
        y1, y2: int y coordinates
    
    Returns:
        sorted coordinates
        x1, y1, x2, y2
        such that
        x1 < x2 and y1 < y2


### [`sphere2file`](#Python_BMP.BITMAPlib.sphere2file)

```py
def sphere2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, rgbfactors: list[float, float, float]):
```

Renders a sphere

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


### [`sphere`](#Python_BMP.BITMAPlib.sphere)

```py
def sphere(bmp: array.array, x: int, y: int, r: int, rgbfactors: list[float, float, float]):
```

Draws a Rendered Sphere

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


### [`spherevertandsurface`](#Python_BMP.solids3D.spherevertandsurface)

```py
def spherevertandsurface(vcen: list[float, float, float], r: float, deganglestep: float) -> tuple:
```

Returns a list of sparse
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


### [`spiralcontrolpointsvert`](#Python_BMP.primitives2D.spiralcontrolpointsvert)

```py
def spiralcontrolpointsvert(x: int, y: int, step: int, growthfactor: float, turns: int):
```

Returns a list of 2D vertices of a Square Spiral

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


### [`spirographvert`](#Python_BMP.primitives2D.spirographvert)

```py
def spirographvert(x: int, y: int, r: int, l: float, k: float, delta: float, lim: float):
```

Returns a list(int, int) of
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


### [`subvect`](#Python_BMP.mathlib.subvect)

```py
def subvect(u: list[numbers.Number], v: list[numbers.Number]) -> list[numbers.Number]:
```

Subtracts vectors u and v by subtracting their components

    Args:
        u, v: list of ints or floats
    
    Returns:
        list of ints or floats


### [`surfplot3Dvertandsurface`](#Python_BMP.solids3D.surfplot3Dvertandsurface)

```py
def surfplot3Dvertandsurface(x1: int, y1: int, x2: int, y2: int, step: int, fnxy: Callable) -> tuple:
```

Does a 3D surface plot of a
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


### [`swapcolors`](#Python_BMP.BITMAPlib.swapcolors)

```py
def swapcolors(bmp: array.array, p1: list, p2: list):
```

Swaps the colors of two points in a BMP

    Args:
        bmp   : unsigned byte array
                with bmp format
        p1, p2: endpoints of the
                line(x: uint, y: uint)
    
    Returns:
        byref modified unsigned byte array


### [`swapif`](#Python_BMP.conditionaltools.swapif)

```py
def swapif(val1: <built-in function any>, val2: <built-in function any>, boolcond: bool):
```

Swaps val1 and val2 if
    boolcond is true

    Args:
        boolcond  : an expression that
                    evaluates as either
                    True or False
        val1, val2: values to swap if
                    boolcond is True
    
    Returns:
        values depending on boolcond


### [`swapxy`](#Python_BMP.mathlib.swapxy)

```py
def swapxy(v: list) -> list:
```

Swaps the first two values in a list

    Args:
        list[x, y]
    
    Returns:
        list[y, x]


### [`tetrahedravert`](#Python_BMP.solids3D.tetrahedravert)

```py
def tetrahedravert(x: float) -> list[list[float, float, float]]:
```

Returns a list of vertices
    for a tetrahedron

    Args:
        x: length of a side
    
    Returns:
        list (x: float,
              y: float,
              z: float)


### [`thickcircle`](#Python_BMP.BITMAPlib.thickcircle)

```py
def thickcircle(bmp: array.array, x: int, y: int, r: int, penradius: int, color: int):
```

Draws a Thick Circle

    Args:
        bmp      : unsigned byte array
                   with bmp format
        x, y, r  : center (x, y)
                   and radius r
        penradius: radius of round pen
        color    : color of the circle
    
    Returns:
        byref modified unsigned byte array


### [`thickellipserot`](#Python_BMP.BITMAPlib.thickellipserot)

```py
def thickellipserot(bmp: array.array, x: int, y: int, b: int, a: int, degrot: float, penradius: int, color: int):
```

Draws a Thick Ellipse

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


### [`thickencirclearea2file`](#Python_BMP.BITMAPlib.thickencirclearea2file)

```py
def thickencirclearea2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, rgbfactors: list[float, float, float]):
```

"Encircle area with a gradient and save to a file

    Args:
        bmp       : unsigned byte array
                    with bmp format
    
        x, y      : center of circle
        r         : radius of circle
        rgbfactors: (r, g, b) values
                    are from 0.0 to 1.0
    
    Returns:
        new bitmap file


### [`thickencirclearea`](#Python_BMP.BITMAPlib.thickencirclearea)

```py
def thickencirclearea(bmp: array.array, x: int, y: int, r: int, rgbfactors: list[float, float, float]):
```

Encircle area with a gradient

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


### [`thickplotpoly`](#Python_BMP.BITMAPlib.thickplotpoly)

```py
def thickplotpoly(bmp: array.array, vertlist: list[list[numbers.Number, numbers.Number]], penradius: int, color: int):
```

Draws a polygon of a given color and thickness

    Args:
        bmp      : unsigned byte array
                   with bmp format
        vertlist : [(x, y)...]
                   list of vertices
        penradius: radius of pen
        color    : color of the polygon
    
    Returns:
        byref modified unsigned byte array


### [`thickroundline`](#Python_BMP.BITMAPlib.thickroundline)

```py
def thickroundline(bmp: array.array, p1: list, p2: list, penradius: int, color: int):
```

Draw a Thick Rounded Line

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


### [`thresholdadjcircregion2file`](#Python_BMP.BITMAPlib.thresholdadjcircregion2file)

```py
def thresholdadjcircregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, lumrange: list[int, int]):
```

Threshold adjustment to a circular region in a 24-bit BMP

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


### [`thresholdadjcircregion`](#Python_BMP.BITMAPlib.thresholdadjcircregion)

```py
def thresholdadjcircregion(bmp: array.array, x: int, y: int, r: int, lumrange: list[int, int]):
```

Threshold adjustment to a circular area

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


### [`thresholdadjto24bitimage`](#Python_BMP.BITMAPlib.thresholdadjto24bitimage)

```py
def thresholdadjto24bitimage(bmp: array.array, lumrange: list[int, int]):
```

Threshold adjustment to a whole BMP

    Args:
        bmp     : unsigned byte array
                  with bmp format
        lumrange: (byte: byte)
                  threshold adjustment
                  luminosity range
    
    Returns:
        byref modified unsigned byte array


### [`thresholdadjto24bitregion`](#Python_BMP.BITMAPlib.thresholdadjto24bitregion)

```py
def thresholdadjto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int]):
```

Threshold adjustment to a rectangular area

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


### [`thresholdadjust2file`](#Python_BMP.BITMAPlib.thresholdadjust2file)

```py
def thresholdadjust2file(ExistingBMPfile: str, NewBMPfile: str, lumrange: list[int, int]):
```

Apply a threshold adjustment

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


### [`thresholdadjust`](#Python_BMP.colors.thresholdadjust)

```py
def thresholdadjust(rgb: list[int, int, int], lumrange: list[int, int]) -> list[int, int, int]:
```

Apply a threshold adjustment
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


### [`trans`](#Python_BMP.mathlib.trans)

```py
def trans(vlist: list[list[numbers.Number]], u: list[numbers.Number]) -> list[list[numbers.Number]]:
```

Translates list of vectors by adding vector u
to all vectors in the list of vectors

    Args:
        vlist: list of vectors
        u    : translation vector
    
    Returns:
        list of vectors


### [`upgradeto24bitimage2file`](#Python_BMP.BITMAPlib.upgradeto24bitimage2file)

```py
def upgradeto24bitimage2file(ExistingBMPfile: str, NewBMPfile: str):
```

Upgrades a bitmap file to 24-bits

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
    
    Returns:
        new bitmap file


### [`upgradeto24bitimage`](#Python_BMP.BITMAPlib.upgradeto24bitimage)

```py
def upgradeto24bitimage(bmp: array.array):
```

Upgrade an image to 24-bits

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        byref modified unsigned byte array


### [`userdef2Dcooordsys2screenxy`](#Python_BMP.BITMAPlib.userdef2Dcooordsys2screenxy)

```py
def userdef2Dcooordsys2screenxy(x: int, y: int, lstcooordinfo: list):
```

2D coordinate trans from user to screen

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


### [`vertBMPbitBLTget`](#Python_BMP.BITMAPlib.vertBMPbitBLTget)

```py
def vertBMPbitBLTget(bmp: array.array, x: int, y1: int, y2: int) -> array.array:
```

Gets vertical slice to a new array

    Args:
        bmp   : unsigned byte array
                with bmp format
        x     : unsigned int x
        y1, y2  and y coordinates
    
    Returns:
        unsigned byte array


### [`vertbrightnessgrad2circregion2file`](#Python_BMP.BITMAPlib.vertbrightnessgrad2circregion2file)

```py
def vertbrightnessgrad2circregion2file(ExistingBMPfile: str, NewBMPfile: str, x: int, y: int, r: int, lumrange: list[int, int]):
```

Vertical brightness gradient to a circular area

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


### [`vertbrightnessgrad2circregion`](#Python_BMP.BITMAPlib.vertbrightnessgrad2circregion)

```py
def vertbrightnessgrad2circregion(bmp: array.array, x: int, y: int, r: int, lumrange: list[int, int]):
```

Vertical brightness gradient adjustment to a circular area

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


### [`verticalbrightnessgrad2file`](#Python_BMP.BITMAPlib.verticalbrightnessgrad2file)

```py
def verticalbrightnessgrad2file(ExistingBMPfile: str, NewBMPfile: str, lumrange: list[int, int]):
```

Applies a Vertical brightness gradient

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


### [`verticalbrightnessgradregion2file`](#Python_BMP.BITMAPlib.verticalbrightnessgradregion2file)

```py
def verticalbrightnessgradregion2file(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int]):
```

Vertical brightness gradient to a rectangular area

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


### [`verticalbrightnessgradto24bitimage`](#Python_BMP.BITMAPlib.verticalbrightnessgradto24bitimage)

```py
def verticalbrightnessgradto24bitimage(bmp: array.array, lumrange: list[int, int]):
```

Applies a vertical brightness gradient

    Args:
        bmp     : unsigned byte array
                  with bmp format
        lumrange: (byte: byte) the
                  brightness gradient
    
    Returns:
        byref modified unsigned byte array


### [`verticalbrightnessgradto24bitregion`](#Python_BMP.BITMAPlib.verticalbrightnessgradto24bitregion)

```py
def verticalbrightnessgradto24bitregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, lumrange: list[int, int]):
```

Apply a vertical brightness gradient
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


### [`verticalvert`](#Python_BMP.primitives2D.verticalvert)

```py
def verticalvert(x: int, y1: int, y2: int, dy: int) -> list[list[int, int]]:
```

Creates a list of int vertices
along a vertical line with int step dy

    Args:
        x : int constant x
        y1: int start point
        y2: int end point
        dy: int y step increment
    
    Returns:
        list of int vertices
        [(x, y), ...]


### [`vertline`](#Python_BMP.BITMAPlib.vertline)

```py
def vertline(bmp: array.array, x: int, y1: int, y2: int, color: int):
```

Draw a Vertical Line

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


### [`vertlinevert`](#Python_BMP.BITMAPlib.vertlinevert)

```py
def vertlinevert(bmp: array.array, vlist: list[list[int, int]], linelen: int, yadj: int, color: int):
```

Vertical line marks at vertices in vlist

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


### [`verttrans`](#Python_BMP.BITMAPlib.verttrans)

```py
def verttrans(bmp: array.array, trans: str):
```

Do vertical image transforms

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


### [`verttransformincircregion`](#Python_BMP.BITMAPlib.verttransformincircregion)

```py
def verttransformincircregion(bmp: array.array, x: int, y: int, r: int, trans: str):
```

Applies a vertical transform to
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


### [`verttransregion`](#Python_BMP.BITMAPlib.verttransregion)

```py
def verttransregion(bmp: array.array, x1: int, y1: int, x2: int, y2: int, trans: str):
```

Do vertical image transforms
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


### [`vmag`](#Python_BMP.mathlib.vmag)

```py
def vmag(v: list[float]) -> float:
```

Compute the Magnitude or length of a vector v
of arbitrary dimension n equal to len(v)

    Args:
        v: list of ints or floats
    
    Returns:
        float


### [`writeint`](#Python_BMP.inttools.writeint)

```py
def writeint(offset: int, cnt: int, arr: array.array, value: int):
```

Writes an integer value to an
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


### [`xorvect`](#Python_BMP.mathlib.xorvect)

```py
def xorvect(u: list[int], v: list[int]) -> list[int]:
```

Applies a xor operation of between the elements of
two lists of ints

    Args:
        v      : list[int]
        bitmask: int
    
    Returns:
        list[int]


### [`XYaxis`](#Python_BMP.BITMAPlib.XYaxis)

```py
def XYaxis(bmp: array.array, origin: list[int, int], steps: list[int, int], xylimits: list[int, int], xyvalstarts: list[numbers.Number, numbers.Number], xysteps: list[numbers.Number, numbers.Number], color: int, textcolor: int, showgrid: bool, gridcolor: int):
```

XY axis with tick marks and numbers

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


### [`xygrid`](#Python_BMP.BITMAPlib.xygrid)

```py
def xygrid(bmp: array.array, x1: int, y1: int, x2: int, y2: int, xysteps: list[int, int], color: int):
```

Draws a grid

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


### [`xygridvec`](#Python_BMP.BITMAPlib.xygridvec)

```py
def xygridvec(bmp: array.array, u: list[int, int], v: list[int, int], steps: list[int, int], gridcolor: int):
```

Grid using (x, y) point pairs u and v

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


### [`XYscatterplot`](#Python_BMP.BITMAPlib.XYscatterplot)

```py
def XYscatterplot(bmp: array.array, XYdata: list, XYcoordinfo: list, showLinearRegLine: bool, reglinecolor: int):
```

Create a XY scatterplot

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


