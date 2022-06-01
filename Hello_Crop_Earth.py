notice = """
   Hello Crop image and save Demo
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
        cropBMPandsave
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        existingfile = f'{rootdir}/assets/earth.bmp'
        file = 'HelloCropEarth.bmp' #file name
        # crop a rectangular region (x1,y1,x2,y2) to a file
        cropBMPandsave(
                existingfile,
                file, # new file to save in
                20, 20, 100, 100 # area to crop
                )
        print(f'All done close {imgedt} to finish')
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


