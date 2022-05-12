notice = """
     Circular color filter Demo
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
        colorfiltercircregion,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(rootdir + '/assets/earth.bmp') #load earth to memory
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = x - 20 # radius set to x - 20
        rf, gf, bf = 1, .7, .3 # RGB color factors (0 to 1) float
        cf = (rf, gf, bf) # RGB color factor tuple
        colorfiltercircregion(bmp, x, y, r, cf)
        # Python_BMP.BITMAPlib.colorfiltercircregion(bmp bytearray,x int ,y int ,r int,cf <tuple of RGB 0..1> )
        file='HelloCircularColorFilter.bmp' #file name
        saveBMP(file,bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call(imgedt + ' ' + file)

if __name__=="__main__":
        main()


