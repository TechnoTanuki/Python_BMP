notice = """
   Circular monochrome filter Demo
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
        centercoord,
        monocircle,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(f'{rootdir}/assets/earth.bmp')
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = x - 20 # radius set to x - 20
        monocircle(bmp, x, y, r)
        # Python_BMP.BITMAPlib.monocircle(bmp bytearray,x int,y int ,r int)
        file='HelloCircularMonoFilter.bmp' #file name
        saveBMP(file, bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()
