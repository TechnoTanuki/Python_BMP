notice = """
    Hello radial gradients Demo
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
        mx, my = 1024, 768 # x and y dim of bmp
        bmp = newBMP(mx,my,24) # (x,y,bit depth)  24 bit BMP
        end = getmaxxy(bmp) # get max x and y
        cen = centercoord(bmp) # get x,y of center
        ori = (0, 0) # define as origin
        for y in range(my):
                for x in range(mx):
                        pt = (x, y) # pacc x,y to tuple
                        r = int(distance(ori, pt)) % 256 # red gradient
                        g = int(distance(end, pt)) % 256 # green gradient
                        b = int(distance(cen, pt)) % 256 # blue gradient
                        plotRGBxybit(bmp, x, y, (r, g, b)) # make a rainbow
        file='HelloRadialGradients.bmp' #file name
        saveBMP(file, bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
