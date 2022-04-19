#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        x=y=600 # bitmap size
        bmp=b.newBMP(x,y,4) # 16 color bitmap
        file='HelloXYScatterplot.bmp' # random file name
        XYdata=[[20,80,5,15,True], #[[x,y,radius,color,filled]
        [40,110,5,15,True],
        [50,10,5,15,True]]
        origin=(80,570) # uint x,y tuple origin point of the graph (bottom left)
        xylimits=(570,18) # uint x,y tuple end poimt of graph (top right)
        steps=(40,40)  # uint x,y tuple x and y step for increment in screen coords
        xyvalstarts=(0,0) # int x,y tuple for starting values in graph coords
        xysteps=(10,10) # int x,y tuple for increment values in graph coords  
        axiscolor=14 # color of axis
        gridcolor=5 # color of grid
        showgrid=True # bool value to toggle grid visibility
        color= 15 # color of text
        XYcoordinfo=b.XYaxis(bmp,origin,steps,xylimits,xyvalstarts,xysteps,axiscolor,color,showgrid,gridcolor)
        showLinearRegLine=True # toggle computation and visibility of linear reg line
        reglinecolor=8 # color of the linear regression line
        b.XYscatterplot(bmp,XYdata,XYcoordinfo,showLinearRegLine,reglinecolor) # do coordinate transform and plot
        b.saveBMP(file,bmp) # dump the in memory bmp to file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()





