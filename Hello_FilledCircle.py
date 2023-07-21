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
from pythonbmp.BITMAPlib import(
        newBMP,
        centercoord,
        filledcircle as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        my = mx = 200 # bitmap size y = x square bitmap
        bmp = newBMP(mx, my, 4) # 4 bit = 16 color
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        d = 40
        r = d >> 1
        for y in range(0, 4):
                c = 4 * y
                y1 = y * d
                for x in range(0, 4):
                        c += 1
                        f(bmp, d + x * d, d + y1, r, c) # draw filled circle
        # pythonbmp.BITMAPlib.filledcircle(bmp bytearray,x int ,y int, r int, c int)
        file = f'Hello{f.__name__}.bmp' # some random file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()



