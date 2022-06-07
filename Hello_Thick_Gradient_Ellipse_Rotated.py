notice = """
Hello Thick Rotated Gradient Ellipse
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
        gradthickellipserot as f,
        centercoord,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = newBMP(300, 200, 24) # 300 x 200 24 bit bitmap
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        b = y - 40 # b axis = y-40
        a = x - 40 # a axis = x-40
        lumrange = (255, 0) # decreasing gradient from center uint bytes
        rgbfactors = (.8, .4, 1)  # rgb triplet as values 0 to 1 unsigned float
        penradius = 20 # radius of pen in pixels
        degrot = 30 # rotation of ellipse in degrees
        f(bmp, x, y, b, a, degrot,
          penradius, lumrange, rgbfactors)
        file = f'Hello{f.__name__}.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()





