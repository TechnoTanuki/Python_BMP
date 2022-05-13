notice = """
  Non linear radial gradients Demo
    (make a wallpaper with math)
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
        distance,
        centercoord,
        plotRGBxybit,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx, my = 640, 480 # x and y dim of bmp
        bmp = newBMP(mx, my, 24) # (x,y,bit depth) 24 bit BMP
        cen = centercoord(bmp) # get x,y of center
        f = lambda d: d * d # simple non linear func
        r = b = 0 # turn off red and blue
        for y in range(0, my):
                for x in range(0, mx):
                        g = int(f(distance(cen, (x, y)))) % 256 # green gradient
                        plotRGBxybit(bmp, x, y, (r, g, b)) # make a rainbow
        file='HelloNonLinearRadialGradients.bmp' # file name
        saveBMP(file, bmp) #dump the bytearray to disk
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()

