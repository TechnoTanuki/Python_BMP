#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) #get path of running script
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') #load earth to memory
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        r1=60 # radius 1 set to 60
        r2=40 # radius 2 set to 40
        br1=-50.8 # brightness adj set to -50.8%
        br2=120 # brightness adj set to 120%
        b.brightnessadjcircregion(bmp,x,y,r1,br1)
        b.brightnessadjcircregion(bmp,x,y,r2,br2)
        # Python_BMP.BITMAPlib.brightnessadjcircregion(bmp bytearray,x int,y int, r int ,br signed float)
        file='HelloCircularRegionBrightnessAdj.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()
