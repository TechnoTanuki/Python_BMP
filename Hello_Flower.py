notice = """
  Hello Filled Trifolium Curve Demo
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
        plotfilledflower as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        x = y = 256 # square bitmap
        bmp = newBMP(x, y, 24) # (x,y,bit depth) -> 24 bit BMP
        (x, y) = centercoord(bmp) # helper method to get center of a bitmap
        r = x - 10 # radius of flower
        petals = 3 # trifolium curve
        angrot = 45 # angle of rotation in degrees
        lumrange = (0, 255) # for brightness gradient
        rgbfactors = (1, 1, 0) # color as rgb of ufloat 0 to 1
        file = f'Hello{f.__name__}.bmp' #file name
        f(bmp, x, y, r, petals, angrot,
          lumrange, rgbfactors)
        saveBMP(file, bmp) # dump bytearray to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

