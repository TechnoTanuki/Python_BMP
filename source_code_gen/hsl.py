def rgb2hsl(r: int, g: int, b: int
           ) -> list[int, int, int]:
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
    return [hue, sat, lum]


def main():
    print(rgb2hsl(100, 189, 255))


if __name__ == "__main__":
        main()

