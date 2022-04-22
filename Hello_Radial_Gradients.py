#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as bm,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        mx,my=1024,768 # x and y dim of bmp
        bmp=bm.newBMP(mx,my,24) # (x,y,bit depth)  24 bit BMP
        end=bm.getmaxxy(bmp) # get max x and y
        cen=bm.centercoord(bmp) # get x,y of center
        ori=(0,0) # define as origin
        for y in range(0,my):
                for x in range(0,mx):
                        pt=(x,y) # pacc x,y to tuple
                        r=int(bm.distance(ori,pt))%256 # red gradient
                        g=int(bm.distance(end,pt))%256 # green gradient
                        b=int(bm.distance(cen,pt))%256 # blue gradient
                        bm.plotRGBxybit(bmp,x,y,(r,g,b)) # make a rainbow
        file='HelloRadialGradients.bmp' #file name
        bm.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()
