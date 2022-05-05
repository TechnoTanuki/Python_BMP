#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#\--------------------------------------------------------------------------/
from array import array

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