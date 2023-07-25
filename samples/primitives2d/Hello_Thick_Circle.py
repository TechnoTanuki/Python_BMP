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

from pythonbmp.BITMAPlib import(
        newBMP,
        centercoord,
        thickcircle as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 512 # bitmap size y = x square bitmap
        bmp = newBMP(mx, my, 4) # 4 bit = 16 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        penradius = 7 # control the thickness
        r = x - penradius  # set radius = x - 12
        dr = 2 * penradius + 3
        for c in range(1, 16):
                f(bmp, x, y, r, penradius, c) # all unsigned
                r -= dr
        #pythonbmp.BITMAPlib.thickcircle(bmp bytyearray,x int,y int ,r int,penradius int,color int)
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) #dump the bytearray to disk
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


