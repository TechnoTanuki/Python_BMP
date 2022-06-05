notice = """
      Hello Square Spiral Demo
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
        plotlines,
        spiralcontrolpointsvert as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 250 # bitmap size
        bmp = newBMP(mx, my, 4) # 16 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        file = f'Hello{f.__name__}.bmp' # file name
        step = 5 # pixel interval between spiral turn
        growthfactor = 1 # greater than 1 means exponential spiral
        turns = 13 # number of turns of spiral
        vertlist = f(x, y, step, growthfactor, turns) # list of (x,y) control points
        color = 9
        plotlines(bmp, vertlist, color) # connect the dots with lines
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


