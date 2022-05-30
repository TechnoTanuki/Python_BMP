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
    if hi != lo:
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
    return [hue, sat, lum]


def HSL2RGB(h: int, s: int, l: int
           ) -> list[int, int, int]:
    """Converts an RGB value to HSL

    Args:
        h: uint hue
        s: uint saturation
        l: uint luminosity

    Returns:
        [r: byte, g: byte, b: byte]
    """
    h /= 60
    s /= 100
    l /= 100



    def hue2rgb(p, q, t):
        t += 1 if t < 0 else 0
        t -= 1 if t > 1 else 0
        if t < 1/6: return p + (q - p) * 6 * t
        if t < 1/2: return q
        if t < 2/3: p + (q - p) * (2/3 - t) * 6
        return p

    if s == 0:
        r = g = b = l * 255
    else:
        if l < 0.5:
            q = l * (l + s)
        else:
            q =  l + s - l * s
        p = 2 * l - q
        r = round(hue2rgb(p, q, h - 1/3) * 255)
        g = round(hue2rgb(p, q, h + 1/3) * 255)
        b = round(hue2rgb(p, q, h + 2/3) * 255)

    return [r, g, b]


def main():
    rgb  = [255, 255, 100]
    hsl = RGB2HSL(*rgb)
    print(rgb, hsl)

    print(HSL2RGB(*hsl))


if __name__ == "__main__":
        main()

