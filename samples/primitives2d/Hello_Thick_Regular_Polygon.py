notice = """
  Hello Thick Regular Polygon Demo
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
        regpolygonvert,
        thickplotpoly as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 360 # bitmap size
        bmp =  newBMP(mx, my, 4) # 2^4=16 color bitmap black background
        x = y = mx >> 1 # centerpoint
        r = x - 20
        for c in range(1, 16):# plot the polygons
                f(bmp, regpolygonvert(
                x, y, r, 5, 30), 3, c)
                r -= 10

        file = f'Hello{f.__name__}.bmp' # file name
        saveBMP(file, bmp) # save the bitmap
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()




