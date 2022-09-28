notice = """
   Hello Smootherstep Sphere Demo
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
        sphere as f,
        smoothersteplerp,
        getX11RGBfactors as c,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 300 # bitmap size y = x square bitmap
        bmp = newBMP(mx, my, 24) # 24 bit BMP
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = x - 12 # radius = x - 12
        f(bmp, x, y, r, c()['cadetblue'], smoothersteplerp) # bmp is unsigned byte array
        file = f'Hello{f.__name__}.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


