notice = """
        XY Scatterplot Demo
 -----------------------------------
| Copyright 2022 by Joel C. Alcarez |
| [joelalcarez1975@gmail.com]       |
|-----------------------------------|
|    We make absolutely no warranty |
| of any kind, expressed or implied |
|-----------------------------------|
|   This graphics library outputs   |
|   to a bitmap file.               |
 -----------------------------------
"""

from Python_BMP.BITMAPlib import(
        newBMP,
        XYaxis,
        XYscatterplot,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        x = y = 600 # bitmap size
        bmp = newBMP(x, y, 4) # 16 color bitmap
        file = 'HelloXYScatterplot.bmp' # random file name
        XYdata = [[20, 80, 5, 15, True], #[[x,y,radius,color,filled]
                  [40, 110, 5, 15, True],
                  [50, 10, 5, 15,True]]

        XYcoordinfo = \
            XYaxis(bmp,
             (80, 570), # uint x,y tuple origin point of the graph (bottom left)
              (40, 40), # uint x,y tuple x and y step for increment in screen coords
             (570, 18), # uint x,y tuple end poimt of graph (top right)
                (0, 0), # int x,y tuple for starting values in graph coords
              (10, 10), # int x,y tuple for increment values in graph coords
                    14, # color of axis
                    15, # color of text
                  True, # bool value to toggle grid visibility
                    5) # color of grid

        XYscatterplot(bmp, XYdata, XYcoordinfo, # do coordinate transform and plot
                     True, # toggle computation and visibility of linear reg line
                        8) # color of the linear regression line
        saveBMP(file, bmp) # dump bytearray to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()







