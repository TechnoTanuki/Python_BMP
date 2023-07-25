notice = """
          Hello World Demo
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
        plotstring2file as f,
        getX11colorname2RGBdict,
        font8x14,
        getfuncmetastr as meta,
        )

import subprocess as proc
from os import path

def main():
        outstr=f'{notice}\n{meta(f)}'
        print(outstr)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        instr = notice
        c = getX11colorname2RGBdict()
        file = f'Hello{f.__name__}.bmp' #file name
        endmsg ='Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)
        f(file,
          f'{outstr}\n{endmsg}', # random text
           2, # uint font size multiplier
           0, # uint space between pixels
           0, # uint default space between char
           c['white'],
           font8x14,
           c['darkblue']
           )
        print(endmsg) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
