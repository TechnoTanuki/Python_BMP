notice = """
   Hello Gradient Spirograph Demo
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
        gradplotlines as g,
        spirographvert as f,
        getX11RGBfactors as c,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}\n{meta(g)}\n')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 500 # bitmap size
        bmp = newBMP(mx, my, 24) # RGB
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        file = f'Hello{f.__name__}{g.__name__}.bmp' # file name
        d = 1/120 # angle increment
        lim = pi * 10 + d # angle limit
        color = 10
        g(bmp, f(x, y, # control spirograph location
                  200, # control spirograph size
                  1, .3, # controls spirograph shape
                  d, lim), # angle step and limit
                  7, # pen radius
                  [255, 0], # luminosity range
                  c()['teal']) # connect the dots with lines
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
