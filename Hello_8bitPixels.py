notice = """
     Plot 256 Color Pixels Demo
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
        plotxybit as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace w
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 512 #bitmap size
        bmp = newBMP(mx, my, 8) #256 colors
        for x in range(mx):
                for y in range(my):
                        f(bmp, x, y, x & y)
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) #dump the bytearray to disk
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
