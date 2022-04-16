#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        mx,my=500,80 # bitmap size
        bmp=b.newBMP(mx,my,24) # RGB bitmap
        fontsize=4 # font size multiplier
        pixspace=1 # space between pixels
        charspace=0 # default space between char
        b.plotstring(bmp,50,10,'Hello World!!',fontsize,pixspace,charspace,b.getcolorname2RGBdict()['yellow'],b.font8x14)
        file='HelloWorld.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()
