from array import array
from .mathlib import(
    addvectinlist,
    intscalarmulvect,
    enumbits
    )

from .buffersplit import(
    altsplitbuf3way,
    altsplitbufnway
    )

from .colors import makeBGRbuf


def packbitlisttobuf(blist: list[int]) -> list[int] :
    """Packs literal list of ones and zeros 
            to a list of bytes
    
    Args:
        blist: literal list of ones and zeros
        
    Returns:
        list 

    """
    retval = []
    j = len(blist)+1
    i = 1
    b = 0
    while i < j:
        m = i % 8
        b += blist[i - 1] << (7 - m)
        if m == 0 and i > 1:
            retval += [b]
            b = 0
        i += 1
    return retval


def resizebitpattenNtimesbigger(
        byteval: int, n: int):
    """Resize byte n times bigger
        bit wise
    
    Args:
        buf: unsigned byte
        n  : buffer multiplier 
        
    Returns:
        list of ones and zeroes

    """
    retval=[]
    for bit in enumbits(byteval):
        retval += [bit] * n
    return retval


def resize1bitbufNtimesbigger(
        buf: array ,n: int):
    """Resize a 1-bit buffer
        n times bigger
    
    Args:
        buf: unsigned byte array
        n  : buffer multiplier 
        
    Returns:
        unsigned byte array

    """
    retval=[]
    for b in buf:
        retval += packbitlisttobuf(
                    resizebitpattenNtimesbigger(b, n))
    return array('B', retval)


def unpack4bitbuf(buf):
    """Unpacks a 4-bit buffer into a list
    
    Args:
        buf: unsigned byte array
        
    Returns:
        list 

    """
    retval=[]
    for b in buf:
        retval+=[b//16, b&0xf]
    return retval


def unpack4bitbufresizeNtimesbigger(buf:array,n:int):
    """unpacks a 4-bit buffer into a list and repeats 4-bit units to resize
    
    Args:
        buf: An unsigned byte array
        n  : unsigned int multiplier to resize buffer
        
    Returns:
        list 

    """
    retval=[]
    for b in buf:
        retval+=[b>>4]*n
        retval+=[b&0xf]*n
    return retval

def pack4bitbuf(unpackedbuf:list) -> list:
    """Packs an unpacked 4-bit buffer into a list
    
    Args:
        buf: An unsigned byte array or list
        
    Returns:
        list 

    """
    retval=[]
    j,i=len(unpackedbuf)-1,0
    while i<j:
        retval+=[(unpackedbuf[i]<<4)+unpackedbuf[i+1]]
        i+=2
    return retval


def resize4bitbufNtimesbigger(buf: array, n: int) -> array:
    """Resize a 4-bit buffer n times bigger
    
    Args:
        buf: An unsigned byte array
        n  : buffer multiplier 
        
    Returns:
        unsigned byte array

    """
    return array('B', pack4bitbuf(unpack4bitbufresizeNtimesbigger(buf, n)))


def resize8bitbufNtimesbigger(
        buf: array, n: int):
    """Resize a 8-bit buffer
        n times bigger
    
    Args:
        buf: unsigned byte array
        n  : buffer multiplier 
        
    Returns:
        unsigned byte array

    """
    retval=[]
    for b in buf:
        retval += [b] * n
    return array('B', retval)

def resizesmaller24bitbuf(buflist: array):
    n,a,m,s=len(buflist),addvectinlist,intscalarmulvect,altsplitbufnway
    c,f=altsplitbuf3way(a(buflist)),1/(n*n)
    return  makeBGRbuf(m(a(s(c[0],n)),f),m(a(s(c[1],n)),f),m(a(s(c[2],n)),f))


def resize24bitbufNtimesbigger(
        buf: array,
        n: int):
    """Resize a 24-bit buffer
        n times bigger
    
    Args:
        buf: unsigned byte array
        n  : buffer multiplier 
        
    Returns:
        unsigned byte array

    """
    c, r = altsplitbuf3way(buf), resize8bitbufNtimesbigger
    return makeBGRbuf(r(c[0], n),
                      r(c[1], n),
                      r(c[2], n))
