#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        mx,my=500,80 #bitmap size
        bmp=b.newBMP(mx,my,24)
        b.plotstring(bmp,50,10,'Hello World!!',4,1,0,b.getcolorname2RGBdict()['lightgray'],b.font8x14)
        file='HelloWorld.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


