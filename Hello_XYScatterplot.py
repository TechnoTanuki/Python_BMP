#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        mx,my=600,600 #bitmap size
        bmp=b.newBMP(mx,my,4)
        file='HelloXYScatterplot.bmp' #file name
        XYdata=[[20,80,5,15,True],[40,110,5,15,True],[50,10,5,15,True]]
        XYcoordinfo=b.XYaxis(bmp,[80,570],[40,40],[570,18],[0,0],[10,10],15,11,True,10)
        b.XYscatterplot(bmp,XYdata,XYcoordinfo,True,12)
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


