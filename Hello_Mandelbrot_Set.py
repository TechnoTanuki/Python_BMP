#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get current script path
        mx=my=500 # square canvas
        bmp=b.newBMP(mx,my,24) # RGB bitmap 500 x 500
        cf=b.getRGBfactors() #color info
        mandelpar=b.mandelparamdict() # common parameters 
        #mandelbrot(bmp,x1,y1,x2,y2,mandelpar[],RGBfactors,maxiter)
        b.mandelbrot(bmp,0,0,mx,my,mandelpar['maxeqdim'],cf['brightgreen'],255)
        file='mandelbrot.bmp'
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()

