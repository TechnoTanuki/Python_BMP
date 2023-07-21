notice = """
      Hello Bezier Curve Demo
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
        centercoord,
        regpolygonvert,
        beziercurve as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = newBMP(250, 250, 4) # 250 x 250  16 color bitmap
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        polyrad = 80 # radius or circle that circumscribes the regular polygon
        sides = 5 # a pentagon
        degrot = 30 # no rotation
        ctrlpntlst = \
                regpolygonvert(x, y, polyrad,
                               sides, degrot)
        penradius = 3 # uint radius of pen in pixels
        color = 12 # unit color
        f(bmp, ctrlpntlst, penradius, color)
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

