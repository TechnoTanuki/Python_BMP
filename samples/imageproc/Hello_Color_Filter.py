notice = """
          Color Filter Demo
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
        getX11RGBfactors as c,
        colorfilter2file as f,
        getfuncmetastr as meta,
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        origfile = f'{rootdir}/../assets/tanuki.bmp'
        file = f'Hello{f.__name__}.bmp' #file name
        f(origfile, file, c()['greenyellow'])
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


