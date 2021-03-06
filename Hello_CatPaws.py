notice = """
      Cat Paws Demo
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
        multijulia as f,
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
        mx = my = 1200 # square canvas
        bmp = newBMP(mx, my, 24) # RGB bitmap 500 x 500
        cf = getX11RGBfactors() #color info
        par = d() # get common parameters
        f(bmp, 0, 0, mx, my,
          -0.744 +  0.148j,
          3, # power of z
          par['maxeqdim'], # location to plot
          cf['royalblue2'], 655)
        file = f'hello{f.__name__}.bmp' # random file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

