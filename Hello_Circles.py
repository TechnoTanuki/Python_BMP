notice = """
             Circle Demo
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
        circle as f,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames[0:6]}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 512 # bitmap size y = x square bitmap
        bmp = newBMP(mx, my, 8) #8 bit = 256 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        for r in range(x): # increase the radius of the circle from 0 to x
                c = r # set color equal to radius
                f(bmp, x, y, c, c, False) # draw circles
                        # Python_BMP.BITMAPlib.circle(bmp bytearray,x int ,y int, r int, c int,isfilled bool)
        file = f'Hello{fname}.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


