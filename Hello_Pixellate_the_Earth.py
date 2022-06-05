notice = """
   Hello Pixellate the World Demo
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
        pixelizenxn as f,
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
        bmp = f(bmp, 4) # 4x4 pix unit to blend for blur effect
        file = f'Hello{f.__name__}.bmp' # file name
        saveBMP(file, bmp) # save in-memory bitmap to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

