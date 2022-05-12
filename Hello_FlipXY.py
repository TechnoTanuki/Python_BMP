notice = """
     Flip XY or 90 degree demo
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
import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path

def main():
        print(notice)
        rootdir = path.dirname(__file__) # get path of this script
        bmp = b.loadBMP(rootdir + '/assets/somebody.bmp') # load bitmap to byte array-> bmp
        bmp = b.flipXY(bmp) # need to return new XY flipped image
        file = 'HelloFlipXY.bmp' # file name
        b.saveBMP(file, bmp) # save XY flipped image
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint ' + file) # replace with another editor if Unix

if __name__=="__main__":
        main()


