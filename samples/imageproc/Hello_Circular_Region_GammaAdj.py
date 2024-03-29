notice = """
  Circular Region Gamma Adjust Demo
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
        loadBMP,
        centercoord,
        gammacorrectcircregion as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        bmp = loadBMP(f'{rootdir}/../assets/earth.bmp')
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = 60 # radius
        gc = .1 # gamma correction
        f(bmp, x, y, r, gc)
        #pythonbmp.BITMAPlib.gammacorrectcircregion(bmp bytearray,x int,y int,r int,gc signed float)
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


