notice = """
          Hello World Demo
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
        plotstring as f,
        getX11colorname2RGBdict,
        font8x14,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx, my = 600, 80 # bitmap size
        bmp = newBMP(mx, my, 24) # RGB bitmap
        c = getX11colorname2RGBdict()
        f(bmp, 35, 10, # position the text
          'Hello World!!', # random text
           5, # uint font size multiplier
           1, # uint space between pixels
           0, # uint default space between char
           [c['orangered'], c['orange']],
           font8x14)
        file = f'Hello{fname}.bmp' #file name
        saveBMP(file,bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
