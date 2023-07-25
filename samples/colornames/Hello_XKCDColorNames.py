notice = """
   Hello XKCD Color Text Name Demo
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
 see https://xkcd.com/color/rgb.txt
"""
from pythonbmp.BITMAPlib import(
        newBMP,
        getXKCDcolorname2RGBdict,
        plotstring,
        font8x14,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = newBMP(4400,700,24) #load earth to memory
        c = getXKCDcolorname2RGBdict() #friendly color names 2 rgb
        y = 2
        x = 2
        for color in c:
            plotstring(bmp,
                x, y, # location of text
                color, # color of text
                1, # font size
                0, # space between bitmap font pixels (0 = default)
                0, # space bitmap font characters (0 = default)
                c[color],
                font8x14)
            y += 16
            if y > 680:
                y = 2
                x += 200

        file = 'HelloXKCDColorNames.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
