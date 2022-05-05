#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#\--------------------------------------------------------------------------/

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
