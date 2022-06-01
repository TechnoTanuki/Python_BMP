notice = """
  Vertical text over an image Demo
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
        getcolorname2RGBdict,
        plotstringvertical,
        font8x14,
        font8x8,
        saveBMP
)

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        bmp = loadBMP(f'{rootdir}/assets/earth.bmp')
        c = getcolorname2RGBdict() #friendly color names 2 rgb
        fontsize = 2 # uint font size multiplier
        pixspace = 0 # uint space between bitmap font pixels (0 = default)
        charspace = 0 # unit space bitmap font characters (0 = default)
        x, y = 125, 5 # text anchor x,y uint
        plotstringvertical(bmp, x, y, 'Hello',
                fontsize, pixspace, charspace,
                c['brightwhite'], font8x14)
        pixspace = 1 # uint space between bitmap font pixels (0 = default)
        charspace = 14 # unint space bitmap font characters (0 = default)
        x , y= 150, 10 # text anchor x,y uint
        plotstringvertical(bmp, x,y, 'Earth',
                fontsize, pixspace, charspace,
                c['brightyellow'], font8x8)
        file = 'HelloEarthVertText.bmp' # file name
        saveBMP(file, bmp) # save bitmap  to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
