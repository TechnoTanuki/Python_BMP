#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get directory of this script
        mx,my=250,250 #bitmap size
        bmp=b.newBMP(mx,my,24) # 24 bit BMP
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        r=80 # radius of circle that circumscribes the regular polygon
        sides=6 # we want a hexagon
        lumrange=(255,0) # lum intensity decrease from center (byte,byte) unsigned
        rgbfactors=(.4,.7,.3) # color as unsigned tuple of (r,g,b) -> min 0 max 1
        angle=0 # angle of rotation of regular polygon in degrees 
        polyvertlist=b.regpolygonvert(x,y,r,sides,angle) # generate polygon vertices
        atomrad=55 # make radius of carbon atoms 55 pixels
        b.gradvert(bmp,polyvertlist,atomrad,lumrange,rgbfactors)
        file='HelloBenzene.bmp' #file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


