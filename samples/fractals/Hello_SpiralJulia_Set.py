notice = """
    Spiral Julia Set Fractal Demo
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
        getX11RGBfactors,
        savespiraljulia2file as f,
        fractaldomainparamdict,
        getfuncmetastr as meta,
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 300 # square canvas
        cf = getX11RGBfactors() #color info
        juliapar = fractaldomainparamdict() # common parameters
        file = f'hello{f.__name__}.bmp' # random file name
        f(file, # path to new file
        mx, my, # size of file
        2.2 + 0.33j, # complex number
        juliapar['maxeqdim'], # fractal domain
        cf['greenyellow']) # color
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


