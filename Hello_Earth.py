#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') #load earth to memory
        b.plotstring(bmp,5,25,'Hello',4,0,0,b.getcolorname2RGBdict()['brightred'],b.font8x14)
        b.plotstring(bmp,5,85,'World',4,0,0,b.getcolorname2RGBdict()['brightyellow'],b.font8x8)
        file='HelloEarth.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


