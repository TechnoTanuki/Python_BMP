notice = """
          Hello Lines Demo
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
        bottomrightcoord,
        centercoord,
        line as f,
        saveBMP
)

import subprocess as proc
from os import path

def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames[0:6]}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my= 300 # bitmap size
        bmp = newBMP(mx,my,4) # 4 bit = 16 color
        (mx, my) = bottomrightcoord(bmp) #max-1 for screen
        (cx, cy) = centercoord(bmp) # How to get center of the bitmap
        #Python_BMP.BITMAPlib.line(bmp bytearray,x1 int,y1 int,x2 int, y2 int,color int) all unsigned
        f(bmp, 0, 0, mx, my, 15)
        f(bmp, mx, 0, 0, my, 14)
        f(bmp, 0, 0, mx, 0, 13)
        f(bmp, 0, 0, 0, my, 11)
        f(bmp, mx, my, mx, 0, 10)
        f(bmp, mx, my, 0, my, 9)
        f(bmp, cx, cy, cx, 0, 8)
        f(bmp, cx, cy, mx, cy, 7)
        f(bmp, cx, cy, cx, my, 6)
        f(bmp, cx, cy, 0, cy, 5)
        file = f'Hello{fname}.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

