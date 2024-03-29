notice = """
Circular Region Brightness Adjustment
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
        brightnessadjcircregion as f,
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
        r1 = 60 # radius 1 set to 60
        r2 = 40 # radius 2 set to 40
        br1 = -50.8 # brightness adj set to -50.8%
        br2 = 120 # brightness adj set to 120%
        f(bmp, x, y, r1, br1)
        f(bmp, x, y, r2, br2)
        # pythonbmp.BITMAPlib.brightnessadjcircregion(bmp bytearray,x int,y int, r int ,br signed float)
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
