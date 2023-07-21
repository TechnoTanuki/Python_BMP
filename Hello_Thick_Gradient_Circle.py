notice = """
  Hello Thick Gradient Circle Demo
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
        gradthickcircle as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 256 # bitmap size y = x square bitmap
        bmp = newBMP(mx, my, 24)
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        penradius = 12 # Thickness
        r = x - penradius  # set radius
        lumrange = (255, 0) # byte tuple luminosity range
        rgbfactors = (0, .5, 1) # unsigned float tuple RGB 0 to 1 values
        f(bmp, x, y, r, penradius, lumrange, rgbfactors) # all unsigned
        # gradthickcircle(bmp bytearray,x int, y int, r int, penradius int, lumrange,rgbfactors)
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # save bitmap
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


