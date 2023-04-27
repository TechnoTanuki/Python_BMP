notice = """
       Hello Superellipse Demo
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
        superellipsevert as f,
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
        bmp = newBMP(mx, my, 4) # 16 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        file = f'Hello{f.__name__}.bmp' # file name
        r = 200
        for c in range(1, 16):
            e = c / 5 # exponent set to 1/5 of color
            p(bmp, f(x, y, # center of superellipse
                  r, r,  # major and minor axes a = b = r
                  e, e), # exponents m = n = e
                  c) # color
            r -= 8 # decrease size
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()