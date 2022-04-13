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
        r=x-20 # radius set to x - 20
        rf,gf,bf=1,.7,.3 # RGB color factors (0 to 1) float
        cf=(rf,gf,bf) # RGB color factor 0..1
        b.colorfiltercircregion(bmp,x,y,r,cf)
        # Python_BMP.colorfiltercircregion(bmp bytearray,x int ,y int ,r int,cf tuple of RGB 0..1 )
        file='HelloCircularColorFilter.bmp' #file name
        b.saveBMP(file,bmp) #save to file 
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


