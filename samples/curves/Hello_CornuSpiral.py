notice = """
      Hello Cornu Spiral Demo
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
        newBMP,
        plotlines,
        cornuspiralvert as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 512 # bitmap size
        bmp = newBMP(mx, my, 4) # 16 color
        file = f'Hello{f.__name__}.bmp' # file name
        for c in range (1, 3):
                s = c << 1 + 2
                l = f(s, s, 500 / c ) # cornuspiralvert(x, y, radius)
                plotlines(bmp, l, 8 + c, 2 if c == 1 else 1) # plot the Cornu Spiral
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()