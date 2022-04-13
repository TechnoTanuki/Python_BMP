#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of running script
        mx,my=200,200 # bitmap size
        bmp=b.newBMP(mx,my,4) # 4 bit = 16 color
        p1=(12,12) # 1st point as (x,y) 
        p2=(mx-12,my-12) # 2nd point as (x,y) 
        penradius=10
        color=13
        b.thickroundline(bmp,p1,p2,penradius,color) # all unsigned
        #Python_BMP.BITMAPlib.thickroundline(bmp bytearray,p1 xy-tuple,p2 xy-tuple,penradius int,color int)
        file='HelloThickroundLine.bmp' #file name
        b.saveBMP(file,bmp) # save file 
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


