#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

notice = """
         Hello radial multi
    color channel gradients Demo
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
        getmaxxy,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx, my = 800, 600 # x and y dim of bmp
        bmp = newBMP(mx, my, 24) # (x,y,bit depth) 24 bit BMP
        cen = centercoord(bmp) # get x,y of center
        f = lambda d: d * 4 # simple linear func
        for y in range(0, my):
                for x in range(0, mx):
                        b = int(f(distance(cen, (x, y)))) % 256 # blue gradient
                        r = 255 - b # red gradient get inverse value of b
                        g = (abs(r - b)) % 256 # green gradient func of r and b
                        plotRGBxybit(bmp, x, y, (r, g, b)) # make a rainbow
        file = 'HelloRadialMultichannelGradients.bmp' # file name
        saveBMP(file, bmp) # dump bytearray to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()
