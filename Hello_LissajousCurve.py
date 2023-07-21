notice = """
     Hello Lissajous Curve Demo
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

from pythonbmp.BITMAPlib import(
        newBMP,
        pi,
        centercoord,
        plotlines,
        lissajouscurvevert as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 500 # bitmap size
        bmp = newBMP(mx, my, 8) # 256 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        file = f'Hello{f.__name__}.bmp' # file name
        d = 1/120
        lim = pi * 25 + d
        for c in range(10, 200, 15):
                plotlines(bmp, f(x, y, # position the curve
                 c, c, # axis mulitipliers
                 1/3, .25, # frequency multipliers
                 pi / 2, # phase shift
                 d, lim), # angle increment + limit
                 c) # connect the dots with lines
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
