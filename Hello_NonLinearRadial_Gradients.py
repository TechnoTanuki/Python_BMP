notice = """
  Non linear radial gradients Demo
    (make a wallpaper with math)
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
        dist as d,
        centercoord as c,
        plotRGBxybit as p,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(d)}\n{meta(c)}\n{meta(p)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx, my = 640, 480 # x and y dim of bmp
        bmp = newBMP(mx, my, 24) # (x,y,bit depth) 24 bit BMP
        cen = c(bmp) # get x, y of center call centercoord
        f = lambda d: d * d # simple non linear func
        r = b = 0 # turn off red and blue
        for y in range(my):
                for x in range(mx):
                        g = int(f(d(cen, (x, y)))) % 256 # green gradient
                        p(bmp, x, y, (r, g, b)) # make a rainbow
        file = f'Hello{d.__name__}{c.__name__}{p.__name__}.bmp' # file name
        saveBMP(file, bmp) #dump the bytearray to disk
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

