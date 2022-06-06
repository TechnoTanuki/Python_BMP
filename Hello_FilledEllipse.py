notice = """
      Hello Filled Ellipse Demo
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
        filledellipse as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = newBMP(220, 200, 4) # 16 color 300 x 200 bmp
        (a, b)  = centercoord(bmp) # How to get center of the bitmap
        a >>= 2
        b >>= 2
        d = b >> 1
        e = a >> 1
        for y in range(0, 4):
                c = y << 2
                for x in range(0, 4):
                        f(bmp, b + b * x * 2 + 16,
                               a * y * 2 + 16,
                               d, e, c) # call filledellipse all unsigned ints
                        c += 1

        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


