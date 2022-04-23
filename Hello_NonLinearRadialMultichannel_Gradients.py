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
        f=lambda d:d*d # simple non linear func
        for y in range(0,my):
                for x in range(0,mx):
                        b=int(f(bm.distance(cen,(x,y))*(1/8)))%256 # blue gradient
                        g=255-b # green gradient 
                        r=(abs(g-b))%256 # red gradient 
                        bm.plotRGBxybit(bmp,x,y,(r,g,b)) # make a rainbow
        file='HelloNonLinearRadialMultichannelGradients.bmp' # file name
        bm.saveBMP(file,bmp) # dump bytearray to file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()