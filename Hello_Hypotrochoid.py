notice = """
        Hello Hypotrochoid Demo
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
        pi,
        centercoord,
        plotlines,
        hypotrochoidvert as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 500 # bitmap size
        bmp = newBMP(mx, my, 4) # 16 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        file = f'Hello{f.__name__}.bmp' # file name
        d = 1/120 # angle increment
        lim = pi * 10 + d # angle limit
        color = 10
        for c in range(1, 16):
                plotlines(bmp, f(x, y, # position the epicycloid
                 300, # radius of fixed circle
                 200, # radius of rolling circle
                 100 - c * 8, # distance from center of rolling circle
                 d, lim),# angle step and limit
                c) # connect the dots with lines
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()