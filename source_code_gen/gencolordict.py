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
        return i >> 16, (i >> 8) & 0xff, i & 0xff

def _getcolorname2RGBdict() -> dict:#define colors here
    return {
       'black':0,
       'blue': RGB2int(0, 0, 192),
       'green': RGB2int(0, 192, 0),
       'cyan': RGB2int(64, 192, 192),
       'red': RGB2int(192, 0, 0),
       'magenta': RGB2int(192, 0, 192),
       'brown': RGB2int(128, 128, 0),
       'white': RGB2int(222, 222, 222),
       'silver': RGB2int(192, 192, 192),
       'gray': RGB2int(128, 128, 128),
       'lightblue': RGB2int(128, 128, 192),
       'lightgreen': RGB2int(128, 192, 128),
       'lightcyan': RGB2int(128, 192, 192),
       'lightred': RGB2int(192, 128, 128),
       'yellow': RGB2int(222, 222, 0),
       'orange': RGB2int(192, 128, 0),
       'lightgray':RGB2int(165, 165, 165),
       'brightwhite':RGB2int(255, 255, 255),
       'brightblue':RGB2int(0, 0, 255),
       'brightcyan':RGB2int(128, 255, 255),
       'brightgreen':RGB2int(0, 255, 0),
       'brightred':RGB2int(255, 0, 0),
       'brightmagenta': RGB2int(255, 0, 255),
       'brightyellow': RGB2int(255, 255, 0),
       'brightorange': RGB2int(255, 164, 0),
       'darkgray': RGB2int(92, 92, 92),
       'darkblue': RGB2int(0, 0, 92),
       'darkgreen':RGB2int(0, 92, 0),
       'darkred': RGB2int(92, 0, 0),
       'darkmagenta': RGB2int(92, 0, 92),
       'darkbrown': RGB2int(92, 92, 0),
       'gold': RGB2int(255, 215, 0),
       'orangered': RGB2int(255, 69, 0),
       'flesh': RGB2int(210, 169, 161),
       }


def _getcolorname2HSLdict() -> dict:#define colors here
    return {
       'black':0,
       'blue': RGB2HSL(0, 0, 192),
       'green': RGB2HSL(0, 192, 0),
       'cyan': RGB2HSL(64, 192, 192),
       'red': RGB2HSL(192, 0, 0),
       'magenta': RGB2HSL(192, 0, 192),
       'brown': RGB2HSL(128, 128, 0),
       'white': RGB2HSL(222, 222, 222),
       'silver': RGB2HSL(192, 192, 192),
       'gray': RGB2HSL(128, 128, 128),
       'lightblue': RGB2HSL(128, 128, 192),
       'lightgreen': RGB2HSL(128, 192, 128),
       'lightcyan': RGB2HSL(128, 192, 192),
       'lightred': RGB2HSL(192, 128, 128),
       'yellow': RGB2HSL(222, 222, 0),
       'orange': RGB2HSL(192, 128, 0),
       'lightgray': RGB2HSL(165, 165, 165),
       'brightwhite': RGB2HSL(255, 255, 255),
       'brightblue': RGB2HSL(0, 0, 255),
       'brightcyan': RGB2HSL(128, 255, 255),
       'brightgreen': RGB2HSL(0, 255, 0),
       'brightred': RGB2HSL(255, 0, 0),
       'brightmagenta': RGB2HSL(255, 0, 255),
       'brightyellow': RGB2HSL(255, 255, 0),
       'brightorange': RGB2HSL(255, 164, 0),
       'darkgray': RGB2HSL(92, 92, 92),
       'darkblue': RGB2HSL(0, 0, 92),
       'darkgreen': RGB2HSL(0, 92, 0),
       'darkred': RGB2HSL(92, 0, 0),
       'darkmagenta': RGB2HSL(92, 0, 92),
       'darkbrown': RGB2HSL(92, 92, 0),
       'gold': RGB2HSL(255, 215, 0),
       'orangered': RGB2HSL(255, 69, 0),
       'flesh': RGB2HSL(210, 169, 161),
       }


def _getRGBfactors() -> dict:#used by functions that generate color gradients
    d = {}
    colordict = _getcolorname2RGBdict()
    for color in colordict:
        r, g, b = int2RGB(colordict[color])
        d.setdefault(color, [r / 255,
                             g / 255,
                             b / 255])
    return d


def main():
    #print(_getcolorname2RGBdict())
    #print(_getRGBfactors())
    print(_getcolorname2HSLdict())

if __name__ == "__main__":
        main()
