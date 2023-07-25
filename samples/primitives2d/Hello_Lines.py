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
from pythonbmp.BITMAPlib import(
        newBMP,
        bottomrightcoord,
        line as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 512 # bitmap size
        bmp = newBMP(mx, my, 8) # 8 bit = 256 color
        (mx, my) = bottomrightcoord(bmp)
        my >>= 1
        for y in range(0, my, 5):
                l = y << 1
                f(bmp, 0, l, mx, l, y) # line(bmp bytearray,x1 int,y1 int,x2 int, y2 int,color int) all unsigned
        file = f'Hello{f.__name__}.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

