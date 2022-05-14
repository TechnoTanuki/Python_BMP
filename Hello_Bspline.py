notice = """
         Hello Bspline Demo
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
        bspline,
        spiralcontrolpointsvert,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 250 # bitmap size
        bmp = newBMP(mx, my, 4) # 4 bit = 2^4 = 16 bits
        file = 'HelloBspline.bmp' # file name
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        step = 5 # pixel interval between spiral turn
        growthfactor = 1 # greater than 1 means exponential spiral
        turns = 13 # number of turns of spiral
        vertlist = spiralcontrolpointsvert(
                        x, y, step,# list of (x,y) control points
                        growthfactor, turns)

        penradius = 2 # radius of pen
        color = 11
        isclosed = True # closed curve
        curveback = True # do extra computation to curve back to origin
        bspline(bmp, vertlist, penradius,
                color, isclosed, curveback)
        saveBMP(file, bmp) # save bitmap
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()

