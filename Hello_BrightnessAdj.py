notice = """
 Adjust the brightness of an image
 by %i percent brighter Demo
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
        adjustbrightness2file as f,
        getfuncmetastr as meta
        )

import subprocess as proc
from os import path


def main():
        peradj = 75
        print(f'{notice % (peradj)}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        file = f'Hello{f.__name__}.bmp' # file name <string>
        f(f'{rootdir}/assets/test_images/earth.bmp',
        file, peradj) # 3rd param brightness adj percent + or -
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
