notice = """
    Hello Regular %i sided Polygon
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
        regpolygonvert,
        plotpoly,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        sides = 5 # for a pentagon
        print(notice % (sides))
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my =200 # bitmap size
        bmp = newBMP(mx, my, 4) # 2^4=16 color bitmap black background
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = x - 20 # radius of a circle that contains all the vertices
        angle = 30 # for rotation in degrees
        polygonvertexlist = \
                regpolygonvert(x, y, r, sides, angle) # generate vertices
        color = 11 # color in 4 bit mode (min 0 - max 15)
        plotpoly(bmp, polygonvertexlist, color) # plot the polygon
        file = 'HelloRegularPolygon.bmp' # file name
        saveBMP(file,bmp) # save the bitmap
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()



