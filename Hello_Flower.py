#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        x=y=256 # square bitmap
        bmp=b.newBMP(x,y,24) # (x,y,bit depth) -> 24 bit BMP
        (x,y)=b.centercoord(bmp) # helper method to get center of a bitmap
        r=x-10 # radius of flower
        petals=3
        angrot=45 # angle of rotation in degrees
        lumrange=(0,255) # for brightness gradient
        rgbfactors=(1,1,0) # color as rgb of ufloat 0 to 1
        file='HelloFlower.bmp' #file name
        b.plotfilledflower(bmp,x,y,r,petals,angrot,lumrange,rgbfactors)
        b.saveBMP(file,bmp) # dump bytearray to file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()
