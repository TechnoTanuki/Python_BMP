notice = """
Hello Filled Gradient Rectangle Demo
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
        newBMP,
        getRGBfactors,
        filledgradrect as f,
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
        bmp = newBMP(mx, my, 24) # 24 bit or (R,G,B) triplet of 8 bits each
        cf = getRGBfactors() # get color info friendly names
        j = 10 # border in pixel
        #filledgradrect(bmp,x1,y1,x2,y2,lumrange,colorfactorlist,gradientdirection) 
        f(bmp, j, j, mx - j, my - j,
         [0, 255], cf['brightblue'], 1) # vertical gradient
        file = f'Hello{f.__name__}.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


