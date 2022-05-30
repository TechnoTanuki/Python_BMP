from os import path

def RGB2HSL(r: int, g: int, b: int
           ) -> list[int, int, int]:
    """Converts an RGB value to HSL

    Args:
        r: unsigned byte red value
        g: unsigned byte green value
        b: unsigned byte blue value

    Returns:
        [hue: int,  ->  in degrees
         sat: int,  ->  percentage
         lum: int]  ->  percentage
    """
    r /= 255
    g /= 255
    b /= 255
    hi = max(r, g, b)
    lo = min(r, g, b)
    lum = (hi + lo) / 2
    hue = sat = 0
    if (hi != lo):
        c = hi - lo
        sat = c / (1 - abs(2 * lum - 1))
        if hi == r:
            hue =  (g - b) / c
            if g < b:
                hue += 6
        elif hi == g:
            hue = (b - r) / c + 2
        elif hi == b:
            hue = (r - g) / c + 4
    hue = round(hue * 60)
    sat = round(sat * 100)
    lum = round(lum * 100)
    return (hue, sat, lum)


def RGB2int(r: int,
            g: int,
            b: int) -> int:
    return b + (g << 8) + (r << 16)

def int2RGB(i: int):
        return  i >> 16, (i >> 8) & 0xff, i & 0xff

def load(filename, delimiter):
    m = []
    with open(filename) as f:
        m.extend(line.replace('\n', '').split(delimiter) for line in f)
        f.close()
    return m

def main():
    code ="{\n"
    code1 ="{\n"
    code2 ="{\n"
    rootdir = path.dirname(__file__)
    m = load(f"{rootdir}/XKCDrgb.txt", '\t')
    for n in m:
        o = int2RGB(int(n[1],16))
        code += "'%s': %s,\n" % (n[0], RGB2int(o[0], o[1], o[2]))
        code1 += "'%s': [%f, %f, %f],\n" % (n[0], o[0] / 255, o[1] / 255 , o[2] / 255)
        code2 += "'%s': %s,\n" % (n[0], RGB2HSL(o[0], o[1], o[2]))
    code +="}\n"
    code1 +="}\n"
    code2 +="}\n"
    #print(code)
    #print(code1)
    print(code2)
if __name__ == "__main__":
        main()
