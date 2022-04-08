#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.c
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        mx=500
        my=500
        bmp=b.newBMP(mx,my,24)
        cf=b.getRGBfactors() #color info
        mandelpar=b.mandelparamdict()#seems preferable to store common params
        b.mandelbrot(bmp,0,0,500,500,mandelpar['maxeqdim'],cf['brightgreen'],255)
        file='fern.bmp'
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


