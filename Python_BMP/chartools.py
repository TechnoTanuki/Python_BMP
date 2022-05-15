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

def enumletters(st: str) -> str:
    """Enumerates the characters
    in a string

    Args:
        st: string

    Yields:
        individual characters

    """
    c, i = len(st), 0
    while i < c:
        yield st[i: i + 1]
        i += 1


def enumreverseletters(
        st: str) -> str:
    """Enumerates the characters
    in a string in reverse order

    Args:
        st: string

    Yields:
        individual characters

    """

    i = len(st) - 1
    while i > -1:
        yield st[i: i + 1]
        i -= 1


def char2int(
        charcodestr: str) -> int:
    """Packs a string into
    an int using ascii code

    Args:
        charcodestr: string

    Yeilds:
        int value

    """
    place, strhash = 0, 0
    for c in enumletters(charcodestr):
        strhash += \
            ord(c) * (256 ** place)
        place += 1
    return strhash
