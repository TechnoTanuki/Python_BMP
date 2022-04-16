#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get current script path
        mx=my=200 # bitmap size
        bmp=b.newBMP(mx,my,4) # 2^4=16 color bitmap black background
        x=y=100 # centerpoint
        r=x-20 # radius of a circle that contains all the vertices 
        sides=5 # for a pentagon
        angle=30 # for rotation in degrees
        polygonvertexlist=b.regpolygonvert(x,y,r,sides,angle) # generate vertices
        color=11 # color in 4 bit mode (min 0 - max 15)
        b.plotpoly(bmp,polygonvertexlist,color) # plot the polygon
        file='HelloRegularPolygon.bmp' # file name
        b.saveBMP(file,bmp) # save the bitmap
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()




