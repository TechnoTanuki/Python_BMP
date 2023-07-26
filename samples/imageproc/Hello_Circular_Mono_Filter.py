notice = """
   Circular Monochrome Filter Demo
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
        monochromecircregion2file as f,
        getfuncmetastr as meta,
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        origfile =  f'{rootdir}/../assets/earth.bmp'
        file = f'Hello{f.__name__}.bmp' #file name
        x, y = 87, 83 #  center of the bitmap
        r = x - 20 # radius set to x - 20
        f(origfile, file, x, y, r) # call monocircle to apply the filter
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
