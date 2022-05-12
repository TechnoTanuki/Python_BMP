notice = """
        Linear Gradient Demo
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
        fillbackgroundwithgrad,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 500 # bitmap size
        bmp = newBMP(mx, my, 24)
        file = 'HelloLinearGradient.bmp' # file name
        rf, gf, bf = 0, .5, 1 # floats for r,g,b 0 to 1
        minval, maxval = 0, 255 #=gradient range int 0 to 255
        fillbackgroundwithgrad(bmp, [minval, maxval], [rf, gf, bf], 0) #last param alters orientation 0 or 1 
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call(imgedt + ' ' + file) # load the image

if __name__=="__main__":
        main()


