notice = """
        Newtons Fractal Demo
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
        newBMP,
        getX11RGBfactors,
        newtonsfractal as f,
        funcparamdict,
        fractaldomainparamdict as d,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 600 # square canvas
        bmp = newBMP(mx, my, 24) # RGB bitmap 600 x 600
        cf = getX11RGBfactors() #color info
        par = d() # get common parameters
        roots = f(bmp, 0, 0, mx, my,
          funcparamdict()[5.3],
          par['maxeqdim'],
          (cf['red'], cf['yellow'],
          cf['green'], cf['blue'],
          cf['violet'])
          , 255)
        print('Roots:')
        for root in roots:
                print(root)
        file = f'hello{f.__name__}.bmp' # random file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


