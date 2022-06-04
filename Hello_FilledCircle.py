notice = """
         Filled Circle Demo
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
        filledcircle as f,
        saveBMP
)

import subprocess as proc
from os import path


def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames[0:5]}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        my = mx = 256 # bitmap size y = x square bitmap
        bmp = newBMP(mx, my, 4) # 4 bit = 16 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = x - 12 # radius
        c = 11 # color
        f(bmp, x, y, r, c) # draw filled circle
        # Python_BMP.BITMAPlib.filledcircle(bmp bytearray,x int ,y int, r int, c int)
        file = f'Hello{fname}.bmp' # some random file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()



