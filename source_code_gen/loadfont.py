from os import path
def plot8bitpatternastext(
        bitpattern: list[int],
        onechar: str,
        zerochar: str):
    """Outputs the bits of a list
        of bytes to console

    Args:
        bitpattern: list of bytes
        onechar   : char to display
                    if bit is 1
        zerochar : char to display
                    if bit is 0

    Returns:
        console output
    """
    s = ""
    for bits in bitpattern:
        mask = 128
        while mask > 0:
            s += onechar if mask & bits > 0 else zerochar
            mask >>= 1
        s += '\n'
    return s

def getcharbmp(filename: str, ch: str, bytecnt: int = 8, dataptr: int = 1626):
    a = ""
    with open(filename, 'rb') as f:
        f.seek(dataptr + bytecnt * ord(ch))
        a = f.read(bytecnt)
    return a

def getcharset(filename: str, dataptr: int = 1626, databytes: int = 8):
    a = ""
    datasz = databytes * 256
    with open(filename, 'rb') as f:
        f.seek(dataptr)
        a = f.read(datasz)
    return a


def  main():
    scriptdir = path.dirname(__file__)
    filename = scriptdir + "/Bm437_ToshibaSat_8x8.FON" #"/Bm437_IBM_CGA.FON"
    ch = "\x01"
    c = 8
    dataptr = 1626
    a = getcharbmp(filename, ch, c, dataptr)
    print(a)
    print(plot8bitpatternastext(a,"*"," "))
    sz = 256 * c
    s = getcharset(filename, dataptr, c)
    b = '[{:01d},\n'.format(c)
    for i in range(sz):
        b += "0x{:02x}".format(s[i])
        b += ", "
        if (i + 1) % c == 0:
            b += "#0x{:02x}\n".format(i // c)
    print(b)



if __name__ == "__main__":
    main()
