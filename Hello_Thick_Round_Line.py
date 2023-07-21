notice = """
    Hello Thick Round Line Demo
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
        thickroundline as f,
        addvect as addv,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames[0:5]}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 400 # bitmap size
        bmp = newBMP(mx, my, 4) # 4 bit = 16 color
        r = 10
        my -= 1
        p1 = (20 + r, r) # 1st point as (x,y)
        p2 = (20 + r, my - r) # 2nd point as (x,y)
        d =  (2 * r + 4, 0) # delta vector
        for c in range(1, 16):
                f(bmp, p1, p2, r, c) # all unsigned
                p1 = addv(p1, d) # do vector add
                p2 = addv(p2, d) # to move line
        #pythonbmp.BITMAPlib.thickroundline(bmp bytearray,p1 xy-tuple,p2 xy-tuple,penradius int,color int)
        file = f'Hello{fname}.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


