#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        mx,my=500,80 #bitmap size
        bmp=b.newBMP(mx,my,24)
        file='HelloLinearGradient.bmp' #file name
        rf,gf,bf=0,.5,1 # floats for r,g,b 0 to 1
        minval,maxval=0,255 #=gradient range int 0 to 255
        b.fillbackgroundwithgrad(bmp,[minval,maxval],[rf,gf,bf],0) #last param alters orientation 0 or 1 
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


