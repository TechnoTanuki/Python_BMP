#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])  # get path of running script
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') #load earth to memory
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        r=x-30 # radius set to x - 30
        n=5 # blursize n = 5x5 pix
        b.pixelizenxncircregion(bmp,x,y,r,n)
        # Python_BMP.BITMAPlib.pixelizenxncircregion(bmp bytarray,x int ,y int ,r int ,n int)
        file='HelloCircularPixellate.bmp' #file name
        b.saveBMP(file,bmp) # save the image
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


