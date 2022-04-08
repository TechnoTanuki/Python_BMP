#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.c
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        mx=250
        my=500
        bmp=b.newBMP(mx,my,24)
        c=b.getcolorname2RGBdict() #color info
        b.IFS(bmp,b.getIFSparams()['fern'],0,0,250,500,40,55,125,80,c['lightgreen'],80000)
        file='fern.bmp'
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


