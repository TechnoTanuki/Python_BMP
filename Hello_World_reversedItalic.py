notice = """
   Hello World Reversed Italic Font
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
        plotreverseditalicstring2file as f,
        getcolorname2RGBdict,
        font8x14,
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
        file = f'HelloWorld{f.__name__}.bmp' #file name
        bmp = newBMP(600, 600, 24)
        saveBMP(file, bmp)
        f(file, 'Hello World!!', # random text
           7, # uint font size multiplier
           1, # uint space between pixels
           0, # uint default space between char
           getcolorname2RGBdict()['yellow'],
           font8x14)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
