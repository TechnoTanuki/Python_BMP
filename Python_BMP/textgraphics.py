#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#\--------------------------------------------------------------------------/

def plotbitsastext(bits: int):
    mask = 128
    while mask > 0:
        if (mask & bits) == 0:
            print(' ', end='')
        else:
            print('*', end='')
        mask = mask >> 1


def plot8bitpatternastext(bitpattern, onechar, zerochar):
    s = ""
    for bits in bitpattern:
        mask = 128
        while mask > 0:
            s += onechar if mask & bits > 0 else zerochar
            mask = mask >> 1
        s += '\n'
    return s
