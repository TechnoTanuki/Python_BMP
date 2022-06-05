notice = """
        Filled Rectangle Demo
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
        filledrect,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        x, y = 320, 320 # bitmap size
        bmp = newBMP(x, y, 4) # 2^4 = 16 colors -> black background by default
        c = 0
        d = 32
        f = 25
        xf = x >> 2
        yf = y >> 2
        for y in range(0, 4):
                c = y * 4
                for x in range(0, 4):
                        c += x
                        a = f + x * xf
                        b = f + y * yf
                        filledrect(bmp, a, b,
                             a + d, b + d, c) # draw filled rectangle
        file = 'HelloFilledRectangle.bmp' #file name
        saveBMP(file, bmp) # bmp <byte array> to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
