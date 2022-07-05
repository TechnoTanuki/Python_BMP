notice = """
        Tetration Fractal Demo
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
        savetetrationfractal2file as f,
        fractaldomainparamdict,
        getfuncmetastr as meta,
        )

import subprocess as proc
from os import path
import sys


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(path.abspath(sys.argv[0])) #get path of running script
        par = fractaldomainparamdict() # get common parameters
        file = f'hello{f.__name__}.bmp' # random file name
        lim = 2 << 30
        f(file, 300, 300, lim,
          [1, 2.5, -.75, .75], # location to plot
          [], 4)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


