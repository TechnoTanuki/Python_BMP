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

def getcharbmp(filename: str, ch: str):
    a = ""
    with open(filename, 'rb') as f:
        f.seek(1626 + 8 * ord(ch))
        a = f.read(8)
    return a

def getcharset(filename: str):
    a = ""
    with open(filename, 'rb') as f:
        f.seek(1626)
        a = f.read(2048)
    return a



def  main():
    scriptdir = path.dirname(__file__)
    filename = scriptdir + "/Bm437_IBM_CGA.FON"
    ch = ">"
    a = getcharbmp(filename, ch)
    print(a)
    print(plot8bitpatternastext(a,"*"," "))
    s = getcharset(filename)
    b = '[8,\n'
    for i in range(2048):
        b += "0x{:02x}".format(s[i])
        b += ", " if i< 2047 else "] "
        if (i + 1) % 8 == 0:
            b += "#0x{:02x}\n".format(i // 8)
    print(b)



if __name__ == "__main__":
    main()
