notice = """
      Elliptical Gradient Demo
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
        gradellipse as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        bmp = newBMP(350, 300, 24) # 24 bit 300 x 200 bmp
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        b = y # b axis = y
        a = x # a axis = x
        lumrange = (255, 0) # decreasing gradient from center uint bytes
        rgbfactors = (.3, .9, .5) # rgb triplet as values 0 to 1 unsigned float
        f(bmp, a, b, b, a, lumrange, rgbfactors)  # call gradellipse
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
