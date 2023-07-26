notice = """
           Text Logo Demo
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
        plotitalicstringasdots as f,
        getcolorname2RGBdict,
        font8x8sanserif,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        logostr = 'TetraPlex' #change text as needed
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx, my = 540, 70 # bitmap size
        bmp = newBMP(mx, my, 24) # RGB bitmap
        c = getcolorname2RGBdict()
        f(bmp, 0, 10, # position the text
           logostr, # random text
           7, # uint font size multiplier
           0, # uint space between pixels
           0, # uint default space between char
           (c['yellow'],
            c['brightyellow']),
           font8x8sanserif)
        file = f'{logostr}.bmp' #file name
        saveBMP(file, bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
