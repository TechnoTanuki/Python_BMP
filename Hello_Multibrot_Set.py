notice = """
      Multibrot Set Fractal Demo
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
        getX11RGBfactors,
        savemultibrotfractal2file as f,
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
        mx = my = 600 # square canvas
        cf = getX11RGBfactors() #color info
        par = fractaldomainparamdict() # get common parameters
        file = f'hello{f.__name__}.bmp' # random file name
        f(file, mx, my,
          5, # power of z
          par['maxeqdim'], # location to plot
          cf['cornflowerblue'])
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


