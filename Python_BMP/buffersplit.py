#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#\--------------------------------------------------------------------------/

def altsplitbuf(buf: list) -> list:
    """Split a list into two with alternating items in different list

    Args:
        buf: list,array or tuple

    Returns:
        [[odd list],[even list]]

    """
    m = len(buf)
    if m % 2 == 0:
        m -= m & 1
    return [buf[0:m-1:2], buf[1:m:2]]


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
    return [buf[0:m-2:3], buf[1:m-1:3], buf[2:m:3]]


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
        retval += [buf[i:m-j:n]]
        i += 1
        j -= 1
    return retval