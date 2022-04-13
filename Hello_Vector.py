#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        mx,my=200,200 # bitmap size
        bmp=b.newBMP(mx,my,1) # 1 bit or mono
        p1=(5,5) # (x,y) point 1 or origin
        p2=[mx-5,my-5] # (x,y) point 2 or where the vector points
        arrowhead=0 # 0=auto other value will set length
        color=1
        b.drawvec(bmp,p1,p2,arrowhead,color)
        file='HelloVector.bmp' # file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


