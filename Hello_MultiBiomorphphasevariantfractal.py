notice = """
Multi Biomorph Phase Variant Fractal
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
        savemultibiomorphphasevariantfractal2file as f,
        fractaldomainparamdict as d,
        getfuncmetastr as meta,
        )
from math import pi
import subprocess as proc
from os import path
import sys


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(path.abspath(sys.argv[0])) #get path of running script
        mx = my = 256 # square canvas
        cf = getX11RGBfactors() #color info
        par = d() # get common parameters
        file = f'hello{f.__name__}.bmp' # random file name
        f(file, mx, my, # file and bitmap size
          1 - 1j, # complex number
          2, # power of z
          [-pi, pi, -pi, pi], # location to plot
          cf['darkseagreen1']) # color
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


