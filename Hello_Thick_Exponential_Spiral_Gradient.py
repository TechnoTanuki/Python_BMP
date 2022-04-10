#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        mx,my=300,300 #bitmap size
        bmp=b.newBMP(mx,my,24)
        b.gradvert(bmp,b.bsplinevert(b.spiralcontrolpointsvert(150,150,7,1.618,5),False,False),5,[255,0],[.9,.5,.9])
        file='HelloThickExpGradSpiral.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


