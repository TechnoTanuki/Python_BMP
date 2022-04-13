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
        bmp=b.newBMP(mx,my,8) #8 bit = 256 color
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        for r in range(0,x): # increase the radius of the circle from 0 to x
                c=r # set color equal to radius
                b.circle(bmp,x,y,r,c,False) 
                # Python_BMP.BITMAPlib.circle(bmp bytearray,x int ,y int, r int, c int,isfilled bool)
        file='HelloCircles.bmp' # file name 
        b.saveBMP(file,bmp) # save file 
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


