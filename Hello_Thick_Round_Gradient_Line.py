notice = """
   Thick round gradient line Demo
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
        gradthickroundline as f,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames[0:6]}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 300 # bitmap size
        bmp = newBMP(mx, my, 24) # 24 bit BMP
        mx = my = mx - 1  # max-1 for screen
        p1 = (12, 12) # point1 as (x int,y int) both unsigned
        p2 = (mx - 12, my - 12) # point2 as (x int ,y int) both unsigned
        lumrange = (255, 0) # tuple of bytes for brightness range both unsigned
        rf, gf, bf = .8, .5, .7 # rgb unsigned floats 0 to 1
        penradius = 10 # unsigned int
        f(bmp, p1, p2, penradius,
          lumrange, [rf, gf, bf]) # call gradthickroundline
        file = f'Hello{fname}.bmp' # file name
        saveBMP(file, bmp) # save to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

