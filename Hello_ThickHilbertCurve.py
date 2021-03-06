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
        savehilbertcurve2file as f,
        getfuncmetastr as meta,
        newBMP,
        saveBMP
        )

import subprocess as proc
from os import path
import sys


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(path.abspath(sys.argv[0])) # get path of this script
        mx = my = 512 # bitmap size
        file = f'Hello{f.__name__}.bmp' # file name
        bmp = newBMP(600, 600, 24)
        saveBMP(file, bmp)
        f(file, mx, my, 4, 4, 15, 2, 5, 1)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()