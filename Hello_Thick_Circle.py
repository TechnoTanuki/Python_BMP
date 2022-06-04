notice = """
       Hello Thick Circle Demo
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
        thickcircle as f,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames[0:5]}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 256 # bitmap size y = x square bitmap
        bmp = newBMP(mx, my, 4) # 4 bit = 16 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = x - 20  # set radius = x - 12
        color = 6 # set the color
        penradius = 20 # control the thickness
        f(bmp, x, y, r, penradius, color) # all unsigned
        #Python_BMP.BITMAPlib.thickcircle(bmp bytyearray,x int,y int ,r int,penradius int,color int)
        file = f'Hello{fname}.bmp' #file name
        saveBMP(file, bmp) #dump the bytearray to disk
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


