#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # obtain the path of this script
        x,y=200,100 # bitmap size
        bmp=b.newBMP(x,y,4) # 2^4 = 16 colors -> black background by default
        j=19 # border
        color=10 # change this 0 to 15 -> if 4 bits... 0 black thou lmao
        x1=y1=j # define top left (x,y) 
        x2,y2=x-j,y-j # define bottom right (x,y) 
        b.filledrect(bmp,x1,y1,x2,y2,color)        
        file='HelloFilledRectangle.bmp' #file name
        b.saveBMP(file,bmp) # bmp <byte array> to file 
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()
