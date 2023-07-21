notice = """
 Hello World Reversed Rainbow Italic
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

from pythonbmp.BITMAPlib import(
        newBMP,
        plotreverseditalicstring as f,
        getcolorname2RGBdict,
        font8x8,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx, my = 1000, 90 # bitmap size
        bmp = newBMP(mx, my, 24) # RGB bitmap
        c = getcolorname2RGBdict()
        f(bmp, 25, 10, # position the text
         'Hello World!!', # random text
          9, # uint font size multiplier
          1, # uint space between pixels
          0, # uint default space between char
          (c['brightred'],
           c['brightorange'],
           c['brightyellow'],
           c['brightgreen'],
           c['cyan'],
           c['brightblue'],
           c['brightmagenta']),
          font8x8)
        file = f'HelloWorld{f.__name__}rainbow.bmp' #file name
        saveBMP(file, bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
