notice = """
       BMP Palette Shift Demo
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
        colorcycle2dir as f,
        getfuncmetastr as meta,
        )

import subprocess as proc
from os import path, chdir


def main():
        print(f'{notice}\n{meta(f)}')
        rootdir = path.dirname(__file__) # get path of this script
        file = f'Hello{f.__name__}.bmp' # file name
        chdir(rootdir)
        chdir("../assets/")
        f('biomorph.bmp', "colorcycle", True)



if __name__=="__main__":
        main()


