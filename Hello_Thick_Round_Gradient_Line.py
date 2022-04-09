#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        mx,my=200,200 #bitmap size
        bmp=b.newBMP(mx,my,24) # 16 color
        mx,my=mx-1,my-1 #max-1 for screen
        cx,cy=mx>>1,my>>1 #div by 2
        b.gradthickroundline(bmp,[12,12],[mx-12,my-12],10,[255,0],[1,.3,.5])
        file='HelloThickRoundGradientLine.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


