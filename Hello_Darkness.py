notice = """
  Hello Darkness Code Template Demo
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
        newBMP as f, #insert other func
        saveBMP #here
)

import subprocess as proc
from os import path

def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        bmp = f(640, 480, 24) # (x,y,bit depth) -> 500 x 80 x 24 bit BMP
        file = f'Hello{fname}.bmp' #file name
        #insert something here
        saveBMP(file, bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
