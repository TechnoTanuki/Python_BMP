#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # Get script directory
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') # load earth to memory
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        r=60 # radius
        gc=.1 # gamma correction
        b.gammacorrectcircregion(bmp,x,y,r,gc)
        #Python_BMP.BITMAPlib.gammacorrectcircregion(bmp bytearray,x int,y int,r int,gc signed float)
        file='HelloCircularRegionGammaAdj.bmp' #file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


