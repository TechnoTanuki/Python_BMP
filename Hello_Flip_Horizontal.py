notice = """
        Flip Horizontal Demo
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
        fliphorizontal as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        rootdir = path.dirname(__file__)
        imgedt = 'mspaint'  # replace with another editor if Unix
        bmp = loadBMP(f'{rootdir}/assets/tanuki.bmp')
        f(bmp) # call fliphorizonal and return byref
        file = f'Hello{f.__name__}.bmp' # file name
        saveBMP(file, bmp) # save to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


