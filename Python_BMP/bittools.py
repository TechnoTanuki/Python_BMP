#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#\--------------------------------------------------------------------------/

from array import array
from .mathlib import enumbits

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
