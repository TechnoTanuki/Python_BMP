#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as bm,subprocess as proc
from os import path,sys

def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        mx,my=640,480 # x and y dim of bmp
        bmp=bm.newBMP(mx,my,24) # (x,y,bit depth) 24 bit BMP
        cen=bm.centercoord(bmp) # get x,y of center
        ori=(0,0) # define as origin
        f=lambda d:d*d # simple non linear func
        r=b=0 # turn off red and blue
        for y in range(0,my):
                for x in range(0,mx):
                        g=int(f(bm.distance(cen,(x,y))))%256 # green gradient
                        bm.plotRGBxybit(bmp,x,y,(r,g,b)) # make a rainbow
        file='HelloNonLinearRadialGradients.bmp' # file name
        bm.saveBMP(file,bmp) # dump bytearray to file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()
