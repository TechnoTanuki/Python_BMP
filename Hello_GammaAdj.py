notice = """
        Gamma Adjustment Demo
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
        gammaadjto24bitimage,
        saveBMP
)

import subprocess as proc
from os import path,sys

def main():
        print(notice)
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(rootdir + '/assets/tanuki.bmp') # load to memory
        gammaadjto24bitimage(bmp, .5)  # 2nd param for gamma adj unsigned float
        file='HelloGammaAdj.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s' % (file,rootdir) )
        print('\nAll done close mspaint to finish')
        ret = proc.call('mspaint ' + file) # replace with another editor if Unix

if __name__=="__main__":
        main()


