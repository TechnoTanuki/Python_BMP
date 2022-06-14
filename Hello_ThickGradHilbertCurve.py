notice = """
    Hello Thick Hilbert Curve Demo
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
        gradplotlines as g,
        hilbertvert as f,
        getX11RGBfactors as c,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}\n{meta(g)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 512 # bitmap size
        bmp = newBMP(mx, my, 24) #  monochrome
        file = f'Hello{f.__name__}{g.__name__}.bmp' # file name
        l = [] # empty list to pass to func
        f(l, # list is returned byref by hilbertvert
        (0, 0), # origin point
        (511, 0, 0, 511), # set extents and orientation
        4) # number of recursions
        g(bmp, # pass bmp array return it byref
          l, # pass the vertex list
          8, # pass the pen radius
          [255, 0], # pass luminosity range
          c()['orange'] # pass rgb color factors
          ) # plot the Hilbert curve
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()