#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        bmp=b.newBMP(250,250,4) # 250 x 250  16 color bitmap
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        polyrad=80 # radius o ciclethat circumscribes the regular polygon
        sides=5 # a pentagon
        degrot=0 # no rotation
        controlpointlist=b.regpolygonvert(x,y,polyrad,sides,degrot) #list of (x,y) uint
        penradius=3 # uint radius of pen in pixels
        color=12 # unit color
        b.beziercurve(bmp,controlpointlist,penradius,color)
        file='HelloBezierCurve.bmp' #file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()
