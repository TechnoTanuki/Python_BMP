#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of running script
        mx=512 # bitmap size x
        my=mx # bitmap size y = x square bitmap        
        bmp=b.newBMP(mx,my,24)
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap        
        r=x-12  # set radius = x -12
        lumrange=(255,0) # byte tuple luminosity range
        rgbfactors=(0,.5,1) # unsigned float tuple RGB 0 to 1 values
        thickness=12 # Thickness
        b.gradthickcircle(bmp,x,y,r,thickness,lumrange,rgbfactors)
        # Python_BMP.BITMAPlib.gradthickcircle(bmp bytearray,x int,y int,r int,thickness int,lumrange see line 16,rgbfactors see line 17)
        file='HelloThickGradientCirle.bmp' #file name
        b.saveBMP(file,bmp) # save bitmap
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


