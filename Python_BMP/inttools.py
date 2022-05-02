#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#\--------------------------------------------------------------------------/
from array import array


def writeint(offset: int, cnt: int, arr: array, value: int):
    j = cnt - 1
    for i in range(0, j):
        b = value & 0xff
        arr[offset + i] = b
        value = value >> 8


def readint(offset: int, cnt: int, arr: int) -> int:
    v, j = 0, cnt-1
    for i in range(0, j):
        v += arr[offset + i] << (i << 3)
    return v


def int2buf(cnt: int, value: int) -> array:
    return array('B', [(value >> (i * 8)) & 0xff for i in range(0, cnt)])


def buf2int(buf: array):
    v, j = 0, len(buf) - 1
    for i in range(0, j):
        v += buf[i] << (i << 3)
    return v


def altsplitbuf3way(buf: list) -> list:
    """Split a list into three with alternating items in different list

    Args:
        buf: list,array or tuple [red,green,blue,....]

    Returns:
        [[red list],[green list],[blue list]]

    """
    m = len(buf)
    if m % 3 == 0:
        m -= m & 1
    return [buf[0:m - 2:3], buf[1:m - 1:3], buf[2:m:3]]


def altsplitbufnway(buf: list, n: int) -> list:
    """Split a list into n with alternating items in different list

    Args:
        buf: list,array or tuple [red,green,blue,....]

    Returns:
        [[red list],[green list],[blue list]]

    """
    retval, m, j, i = [], len(buf), n-1, 0
    if m % n == 0:
        m -= m & 1
    while i < n:
        retval += [buf[i:m - j:n]]
        i += 1
        j -= 1
    return retval