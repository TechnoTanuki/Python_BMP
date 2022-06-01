notice = """
     Hello Color Text Name Demo
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
        getcolorname2RGBdict,
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
        bmp = newBMP(600,600,24) #load earth to memory
        c = getcolorname2RGBdict() #friendly color names 2 rgb
        y = 2
        x = 70
        for color in c:
            plotstring(bmp,
                x, y, # location of text
                color, # color of text
                2, # font size
                0, # space between bitmap font pixels (0 = default)
                0, # space bitmap font characters (0 = default)
                c[color],
                font8x14)
            y += 32
            if y > 570:
                y = 2
                x = 300

        file = 'HelloColorNames.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
