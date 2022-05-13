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
        circle,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 512 # bitmap size y = x square bitmap
        bmp = newBMP(mx, my, 8) #8 bit = 256 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        for r in range(0,x): # increase the radius of the circle from 0 to x
                c = r # set color equal to radius
                circle(bmp,x,y,r,c,False) # all ints are unsigned
                # Python_BMP.BITMAPlib.circle(bmp bytearray,x int ,y int, r int, c int,isfilled bool)
        file='HelloCircles.bmp' # file name
        saveBMP(file,bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()


