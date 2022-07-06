notice = """
 8 bit Sin(z) Julia Set Fractal Demo
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
        savesinjulia2file as f,
        fractaldomainparamdict,
        getfuncmetastr as meta,
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 600 # square canvas
        juliapar = fractaldomainparamdict() # common parameters
        file = f'hello 8 bit{f.__name__}.bmp' # random file name
        f(file, # path to new file
        mx, my, # size of file
        0.984808 + 0.173648j, # complex number
        juliapar['maxeqdim'], # fractal domain
        [], 8) # color
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


