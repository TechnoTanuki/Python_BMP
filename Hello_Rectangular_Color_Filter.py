notice = """
     Hello apply a Color filter
     to rectangular region Demo
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
        loadBMP,
        colorfilterto24bitregion,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(f'{rootdir}/assets/earth.bmp')
        rf, gf, bf = 1, .7, .3 #RGB factors 0 to 1 float
        # colorfilterto24bitregion(bmp,x1,y1,x2,y2,[rf,gf,bf])
        colorfilterto24bitregion(bmp, 30, 30, 138, 138,[rf, gf, bf])
        file = 'HelloRectangularColorFilter.bmp' # file name
        saveBMP(file,bmp) # dump bytearray bmp to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()
