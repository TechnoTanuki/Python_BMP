notice = """
Rectangular Brightness Adjustment Demo
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
        brightnesseadjto24bitregion as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(f'{rootdir}/assets/earth.bmp')
        #brightnesseadjto24bitregion(bmp bytearray,x1,y1,x2,y2,brightnessadjpercent)
        f(bmp, 30, 30, 138, 138, -50) # darken rectangular region
        f(bmp, 50, 50, 118, 118, 100) # lighten rectangular region
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # dump byte array to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
