notice = """
    Hello Regular %i sided Polygon
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
        regpolygonvert as f,
        plotpoly,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        sides = 5 # for a pentagon
        print(f'{notice % (sides) }\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 200 # bitmap size
        bmp = newBMP(mx, my, 4) # 2^4=16 color bitmap black background
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = x - 20 # radius of a circle that contains all the vertices
        angle = 30 # for rotation in degrees
        for c in range(1, 16):
                plotpoly(bmp,  f(x, y, r, sides, angle), c) # plot the polygon
                r -= 5
        file = f'Hello{f.__name__}.bmp' # file name
        saveBMP(file,bmp) # save the bitmap
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()



