# Python BMP Internal API

### [`_1bmof`](#_1bmof)

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


### [`_1bmofhd`](#_1bmofhd)

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


### [`_24bmof`](#_24bmof)

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


### [`_24bmofhd`](#_24bmofhd)

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


### [`_4bmof`](#_4bmof)

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


### [`_4bmofhd`](#_4bmofhd)

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


### [`_8bmof`](#_8bmof)

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


### [`_8bmofhd`](#_8bmofhd)

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


### [`_bmmeta`](#_bmmeta)

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


### [`_BMoffset`](#_BMoffset)

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


### [`_BMoffsethd`](#_BMoffsethd)

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


### [`_cmpimglines`](#_cmpimglines)

```py
def _cmpimglines(bmp: array.array, x1: int, y1: int, x2: int, y2: int, func: Callable):
```



    


### [`_flsz`](#_flsz)

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


### [`_fnwithpar2vertslice`](#_fnwithpar2vertslice)

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


### [`_getbmflsz`](#_getbmflsz)

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


### [`_getBMofffunc`](#_getBMofffunc)

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


### [`_getBMoffhdfunc`](#_getBMoffhdfunc)

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


### [`_getclrbits`](#_getclrbits)

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


### [`_hdsz`](#_hdsz)

```py
def _hdsz(bmp: array.array) -> int:
```

Get the header size of a BMP

    Args:
        bmp: unsigned byte array
             with bmp format
    
    Returns:
        int value of header size


### [`_pdbytes`](#_pdbytes)

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


### [`_setflsz`](#_setflsz)

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


### [`_sethdsz`](#_sethdsz)

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


### [`_setmeta`](#_setmeta)

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


### [`_setx`](#_setx)

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


### [`_sety`](#_sety)

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


### [`_use24bitfn2reg`](#_use24bitfn2reg)

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


### [`_use24btbyrefclrfn2regnsv`](#_use24btbyrefclrfn2regnsv)

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


### [`_use24btclrfn`](#_use24btclrfn)

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


### [`_use24btclrfntocircregion`](#_use24btclrfntocircregion)

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


### [`_use24btclrfnwithpar2circreg`](#_use24btclrfnwithpar2circreg)

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


### [`_use24btfn2circreg`](#_use24btfn2circreg)

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


### [`_use24btfnwithparnsv`](#_use24btfnwithparnsv)

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


### [`_usebyref24btfn2reg`](#_usebyref24btfn2reg)

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


### [`_usebyref24btfn2regnsv`](#_usebyref24btfn2regnsv)

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


### [`_usebyreffn2regnsv`](#_usebyreffn2regnsv)

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


### [`_usebyreffnsv`](#_usebyreffnsv)

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


### [`_usebyreffnwithpar2regnsv`](#_usebyreffnwithpar2regnsv)

```py
def _usebyreffnwithpar2regnsv(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, func: Callable, funcparam):
```

Apply a byref function
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


### [`_usebyreffnwithparnsv`](#_usebyreffnwithparnsv)

```py
def _usebyreffnwithparnsv(ExistingBMPfile: str, NewBMPfile: str, func: Callable, funcparam: <built-in function any>):
```

Apply a by-ref function with parameter and save

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        func           : user defined
                         function
        funcparam      : function parameter
    
    Returns:
        new bitmap file


### [`_usebyrefnopar24bitfn2reg`](#_usebyrefnopar24bitfn2reg)

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


### [`_useclradjfn`](#_useclradjfn)

```py
def _useclradjfn(ExistingBMPfile: str, NewBMPfile: str, func: Callable, funcparam):
```

Apply a user provided color adjustment function
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


### [`_usefn2circreg`](#_usefn2circreg)

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


### [`_usefn2regsv`](#_usefn2regsv)

```py
def _usefn2regsv(ExistingBMPfile: str, NewBMPfile: str, x1: int, y1: int, x2: int, y2: int, func: Callable):
```

Apply a function with no parameters to a
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


### [`_usefndirsv`](#_usefndirsv)

```py
def _usefndirsv(ExistingBMPfile: str, NewDir: str, func: Callable, overwritedir: bool = False):
```

Apply a function with no parameters and save
images to a directory

    Args:
        ExistingBMPfile: Whole path to
                         existing file
        NewBMPfile     : New file to
                         save changes in
        func           : user defined
                         function
    
    Returns:
        new bitmap files in a new directory


### [`_usefnsv`](#_usefnsv)

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


### [`_usefnwithpar2circreg`](#_usefnwithpar2circreg)

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


### [`_usenopar24btfn2circreg`](#_usenopar24btfn2circreg)

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


### [`_usenoparclradjfn`](#_usenoparclradjfn)

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


### [`_usenoparfn2circreg`](#_usenoparfn2circreg)

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


### [`_xbytes`](#_xbytes)

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


### [`_xchrcnt`](#_xchrcnt)

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


