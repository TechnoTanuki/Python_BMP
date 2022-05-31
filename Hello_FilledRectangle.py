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
        x, y = 320, 200 # bitmap size
        bmp= newBMP(x, y, 4) # 2^4 = 16 colors -> black background by default
        j = 19 # border
        color = 10 # change this 0 to 15 -> if 4 bits... 0 black thou lmao
        x1 = y1 = j # define top left (x,y)
        x2, y2 = x - j, y - j # define bottom right (x,y)
        filledrect(bmp, x1, y1, x2, y2, color) # draw filled rectangle
        file = 'HelloFilledRectangle.bmp' #file name
        saveBMP(file, bmp) # bmp <byte array> to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()
