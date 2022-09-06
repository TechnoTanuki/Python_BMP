notice = """
     Circular Color Filter Demo
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
        colorfiltercircregion2file as f,
        getfuncmetastr as meta,
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        origfile =f'{rootdir}/assets/earth.bmp'
        file = f'Hello{f.__name__}.bmp' #file name
        x, y = 87, 83 # How to get center of the bitmap
        r = x - 20 # radius set to x - 20
        rf, gf, bf = 1, .7, .3 # RGB color factors (0 to 1) float
        f(origfile, file, x, y, r, (rf, gf, bf)) # apply the color filter
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


