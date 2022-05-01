#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        bmp=b.newBMP(250,500,4) # 250 x 500 x 16 color
        b.fern(bmp,0,0,249,499,10) #b.fern(bmp,x1,y1,x2,y2,color)
        file='fern.bmp' #random filenme here
        b.saveBMP(file,bmp) #save the fern
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()
