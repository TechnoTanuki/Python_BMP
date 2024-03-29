notice = """
        Xor div Fractal Demo
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
        savexordivfractal2file as f,
        fractaldomainparamdict,
        getX11RGBfactors,
        getfuncmetastr as meta,
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 256 # square canvas
        par = fractaldomainparamdict() # get common parameters
        file = f'hello{f.__name__}.bmp' # random file name
        cf = getX11RGBfactors() #color info
        f(file, mx, my,
          13, #
        [-200, 200, -200, 200], # location to plot
          cf['royalblue'])
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


