notice = """
Multi tan(z) Biomorph dichromic demo
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
        getX11colorname2RGBdict,
        savemultitanbiomorphfractal2file as f,
        fractaldomainparamdict as d,
        getfuncmetastr as meta,
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 256 # square canvas
        c = getX11colorname2RGBdict() #color info
        par = d() # get common parameters
        file = f'hello{f.__name__}.bmp' # random file name
        f(file, mx, my, # file and bitmap size
          .3 + .9j, # complex number
          3, # power of z
          [-2.5, 2.5, -2.5, 2.5], # location to plot
          [c['darkblue'], c['darkseagreen']]) # color
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


