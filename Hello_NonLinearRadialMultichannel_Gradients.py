notice = """
Non Linear Radial Multichannel Gradient
(Make fancy wallpaper with math demo)
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
        plotRGBxybit,
        distance,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx, my = 1024, 768 # dimensions of the bmp
        bmp = newBMP(mx, my, 24) # (x,y,bit depth) 24 bit BMP
        cen = centercoord(bmp) # get x,y of center
        f = lambda d: d ** 1.8 # simple non linear func try different funcs
        for y in range(0, my): # row sweep
                for x in range(0, mx): # column sweep
                        g = int(f(distance(cen, (x, y)) * (1 / 8))) % 256 # green gradient
                        b = 255 - g # blue gradient
                        r = (abs(b - g)) % 256 # red gradient
                        plotRGBxybit(bmp, x, y, (r, g, b)) # make a rainbow
        file = 'HelloNonLinearRadialMultichannelGradients.bmp' # file name
        saveBMP(file, bmp) # dump bytearray to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call(imgedt + ' ' + file) # load the image

if __name__=="__main__":
        main()
