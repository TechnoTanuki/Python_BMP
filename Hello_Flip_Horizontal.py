notice = """
        Flip Horizontal Demo
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
        loadBMP,
        fliphorizontal,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        bmp = loadBMP(path.dirname(__file__) + \
                '/assets/tanuki.bmp') #load to memory
        fliphorizontal(bmp)
        file = 'HelloFliphorzontal.bmp' #file name
        saveBMP(file, bmp) # save to file
        print('\nAll done close mspaint to finish')
        ret = proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__":
        main()


