#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') # load earth to memory
        rf,gf,bf=1,.7,.3 #RGB factors 0 to 1 float
        # colorfilterto24bitregion(bmp,x1,y1,x2,y2,[rf,gf,bf])
        b.colorfilterto24bitregion(bmp,30,30,138,138,[rf,gf,bf])
        file='HelloRectangularColorFilter.bmp' # file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()
