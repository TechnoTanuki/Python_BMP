notice = """
     Mandelbrot Set Fractal Demo
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
        newBMP, #insert other func
        getRGBfactors,
        mandelbrot,
        mandelparamdict,
        saveBMP #here
)

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 600 # square canvas
        bmp = newBMP(mx, my, 24) # RGB bitmap 500 x 500
        cf= getRGBfactors() #color info
        mandelpar = mandelparamdict() # common parameters
        #mandelbrot(bmp,x1,y1,x2,y2,mandelpar[],RGBfactors,maxiter)
        mandelbrot(bmp, 0, 0, mx, my,
                mandelpar['maxeqdim'],
                cf['brightgreen'], 255)
        file = 'mandelbrot.bmp' # random file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()


