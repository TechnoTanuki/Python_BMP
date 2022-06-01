notice = """
  Circular region gamma adjust demo
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
        gammacorrectcircregion,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        bmp = loadBMP(f'{rootdir}/assets/earth.bmp')
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = 60 # radius
        gc = .1 # gamma correction
        gammacorrectcircregion(bmp, x, y, r, gc)
        #Python_BMP.BITMAPlib.gammacorrectcircregion(bmp bytearray,x int,y int,r int,gc signed float)
        file='HelloCircularRegionGammaAdj.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


