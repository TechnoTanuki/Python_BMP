notice = """
Non Linear Radial Multichannel Gradient
(Make fancy wallpaper with math demo)
 -----------------------------------
| Copyright 2022 by Joel C. Alcarez |
| [joelalcarez1975@gmail.com]       |
|-----------------------------------|
|    We make absolutely no warranty |
| of any kind, expressed or implied |
|-----------------------------------|
|   This graphics library outputs   |
|   to a bitmap file.               |
 -----------------------------------
"""

from Python_BMP.BITMAPlib import(
        newBMP,
        centercoord as c,
        plotRGBxybit as p,
        distance as d,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(d)}\n{meta(c)}\n{meta(p)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx, my = 800, 600 # dimensions of the bmp
        bmp = newBMP(mx, my, 24) # (x,y,bit depth) 24 bit BMP
        cen = c(bmp) # get x,y of center
        f = lambda d: d ** 3 # simple non linear func try different funcs
        for y in range(my): # row sweep
                for x in range(mx): # column sweep
                        g = int(f(d(cen, (x, y)) * (1 / 8))) % 256 # green gradient
                        b = 255 - g # blue gradient
                        r = (abs(b - g)) % 256 # red gradient
                        p(bmp, x, y, (r, g, b)) # make a rainbow
        file = f'Hello{d.__name__}{c.__name__}{p.__name__}1.bmp' # file name
        saveBMP(file, bmp) # dump bytearray to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
