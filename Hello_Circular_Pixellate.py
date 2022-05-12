notice = """
   Circular region pixel blur demo
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
        pixelizenxncircregion,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        bmp = loadBMP(rootdir + '/assets/earth.bmp') #load earth to memory
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = x - 30 # radius set to x - 30
        n = 5 # blursize n = 5x5 pix
        pixelizenxncircregion(bmp, x, y, r, n)
        # Python_BMP.BITMAPlib.pixelizenxncircregion(bmp bytarray,x int ,y int ,r int ,n int)
        file='HelloCircularPixellate.bmp' #file name
        saveBMP(file, bmp) # save the image
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call(imgedt + ' ' + file) # load the image

if __name__=="__main__":
        main()


