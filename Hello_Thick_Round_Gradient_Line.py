#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get directory of this script
        mx,my=200,200 # bitmap size
        bmp=b.newBMP(mx,my,24) # 24 bit BMP
        mx,my=mx-1,my-1 # max-1 for screen
        p1=(12,12) # point1 as (x int,y int) both unsigned
        p2=(mx-12,my-12) # point2 as (x int ,y int) both unsigned
        lumrange=(255,0) # tuple of bytes for brightness range both unsigned
        rf,gf,bf=.8,.5,.7 # rgb unsigned floats 0 to 1 
        penradius=10 # unsigned int
        b.gradthickroundline(bmp,p1,p2,penradius,lumrange,[rf,gf,bf])
        file='HelloThickRoundGradientLine.bmp' # file name
        b.saveBMP(file,bmp) # save to file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


