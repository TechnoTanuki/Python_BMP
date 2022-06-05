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
        pixelizenxncircregion as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        bmp = loadBMP(f'{rootdir}/assets/earth.bmp')
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = x - 30 # radius set to x - 30
        n = 5 # blursize n = 5x5 pix
        f(bmp, x, y, r, n) # pixelizenxncircregion(bmp bytarray,x int ,y int ,r int ,n int)
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # save the image
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


