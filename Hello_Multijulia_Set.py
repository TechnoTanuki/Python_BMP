notice = """
      Multijulia Set Fractal Demo
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
        savemultijuliafractal2file as f,
        fractaldomainparamdict as d,
        getfuncmetastr as meta
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 600 # square canvas
        cf = getX11RGBfactors() #color info
        par = d() # get common parameters
        file = f'hello{f.__name__}.bmp' # random file name
        f(file, mx, my, # file and bitmap size
          -0.70176 - 0.3842j, # complex nunber
          5, # power of z
          par['maxeqdim'], # location to plot
          cf['darkseagreen1']) # color
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


