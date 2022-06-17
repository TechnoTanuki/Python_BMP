notice = """
        Hello Egg Curve Demo
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
        centercoord,
        plotpoly as p,
        eggcurvevert as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}\n{meta(p)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 420 # bitmap size
        bmp = newBMP(mx, my, 4)
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        file = f'Hello{f.__name__}.bmp' # file name
        x += 110
        for c in range(16, 0, -1):
            l = f(x, y, # center
                  c * 40, 14)  # radius, egg factor
            p(bmp, l, c) # plot stuff
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()