#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') #load earth to memory
        cx,cy= b.getmaxx(bmp)<<1, b.getmaxy(bmp)<<1# center 
        rf,gf,bf=1,.7,.3 #RGB factors 0 to 1 float
        b.colorfilterto24bitregion(bmp,30,30,138,138,[rf,gf,bf])
        file='HelloRectangularColorFilter.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


