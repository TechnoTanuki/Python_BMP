notice = """
   Hello Earth Copy and Paste Demo
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
        copyrect,
        pasterect,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp= loadBMP(rootdir + '/assets/earth.bmp') #load earth to memory
        buf = copyrect(bmp, 3, 3, 60, 60) # copy a rectangular region (x1,y1,x2,y2) to a buffer
        pasterect(bmp,buf,40,40) # paste buffer to a rectangular region at (x1,y1)
        file = 'HelloEarthCopyPaste.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call(imgedt + ' ' + file) # load the image

if __name__=="__main__":
        main()


