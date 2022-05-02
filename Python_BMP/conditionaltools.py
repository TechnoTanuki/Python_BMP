#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#\--------------------------------------------------------------------------/

def iif(boolcond: bool, trueval: any, falseval: any) -> any:
    return trueval if boolcond else falseval


def swapif(val1: any, val2: any, boolcond: bool):
    if boolcond:
        val1, val2 = val2, val1
    return val1, val2
