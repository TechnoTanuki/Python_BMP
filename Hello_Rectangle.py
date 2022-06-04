notice = """
        Hello Rectangle Demo
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
        rectangle as f,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        x, y = 220, 200 # bitmap size
        bmp = newBMP(x, y, 4) # 2^4 = 16 colors -> black background by default
        j = 19 # border
        x1 = y1 = j # define top left (x,y)
        x2, y2 = x - j, y - j # define bottom right (x,y)
        for c in range(1, 16):
                d = c * 5
                f(bmp, x1 + d, y1 + d,
                       x2 - d, y2 - d, c) # draw a rectangle
        file = f'Hello{fname}.bmp' #file name
        saveBMP(file, bmp) # we dump the byte array bmp -> file (so simple)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

