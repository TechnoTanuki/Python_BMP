notice = """
    Hello Circular Gradient Demo
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
        centercoord,
        dist,
        gradcircle as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 320 # bitmap size x
        bmp = newBMP(mx, my, 24) # RGB bitmap
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = int(dist((x, y), (0, 0)))  # max radius of gradient
        lumrange = (0, 255) # increase in color brightness farther from (x,y)
        rgbfactors = (.25, .75, .5) # rgb triplet as ufloat 0 to 1
        f(bmp, x, y, r, lumrange, rgbfactors) # compute gradient
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
