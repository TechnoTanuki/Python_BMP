notice = """
   Marek Dragon 4 bit Fractal Demo
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
        savemarekdragon2file as f,
        fractaldomainparamdict as d,
        getfuncmetastr as meta,
        getX11RGBfactors,
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 256 # square canvas
        par = d() # get common parameters
        cf = getX11RGBfactors() #color info
        file = f'hello{f.__name__}.bmp' # random file name
        f(file, mx, my,
          0.040884634, # irrational number
          [-1.5, .5, -1.25, 1], # location to plot
           cf['yellowgreen'], 4)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


