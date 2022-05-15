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

from array import array


def writeint(offset: int,
                cnt: int,
                arr: array,
              value: int):
    j = cnt - 1
    for i in range(0, j):
        b = value & 0xff
        arr[offset + i] = b
        value = value >> 8


def readint(offset: int,
               cnt: int,
               arr: int) -> int:
    v, j = 0, cnt-1
    for i in range(0, j):
        v += arr[offset + i] << (i << 3)
    return v


def int2buf(cnt: int,
          value: int) -> array:
    return array('B', [(value >> (i * 8)) & 0xff
                        for i in range(0, cnt)])


def buf2int(buf: array):
    v, j = 0, len(buf) - 1
    for i in range(0, j):
        v += buf[i] << (i << 3)
    return v
