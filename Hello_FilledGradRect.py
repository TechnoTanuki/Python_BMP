#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get the path of this script
        mx,my=256,256 # bitmap size
        bmp=b.newBMP(mx,my,24) # 24 bit or (R,G,B) triplet of 8 bits each
        cf=b.getRGBfactors() # get color info friendly names
        j=10 # border in pixel
        #filledgradrect(bmp,x1,y1,x2,y2,lumrange,colorfactorlist,gradientdirection) 
        b.filledgradrect(bmp,j,j,mx-j,my-j,[0,255],cf['brightblue'],1) # vertical gradient
        file='HelloFilledGradRec.bmp' # file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



