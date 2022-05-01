#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|--------------------------------------------------------------------------|
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#|--------------------------------------------------------------------------|
#|    The primary author and any subsequent code contributors shall not     |
#|    be liable  in any event  for  incidental or consquential  damages     |
#|    in connection with,  or arising out  from  the  use of  this code     |
#|    in current form or with any modifications.                            |
#|--------#--------------------------------------------------------#--------|
#|        |  Contact primary author if you plan to use this        |        |
#|        |  in a commercial product at joelalcarez1975@gmail.com  |        |
#|--------#--------------------------------------------------------#--------|
#|    Educational or hobby use highly encouraged... have fun coding !       |
#|    ps:created out of extreme boredom during the COVID-19 pandemic.       |
#|--------#--------------------------------------------------------#--------|
#|        |  Note: This graphics library outputs to a bitmap file. |        |
#\--------#--------------------------------------------------------#--------/

from array import array
from os.path import isfile
from math import sin,cos,radians
from random import random
from .proctimer import functimer
from .mathlib import cosaffin,distance,vmag,iif,roundvect,addvect,addvectinlist,subvect,setminmax,isinrange,swapif,setmin,setmax,anglebetween2Dlines,polar2rectcoord2D,range2baseanddelta,mirror,xorvect,andvect,rotatebits,LSMslope,LSMYint,trans,intscalarmulvect,swapxy,centerpoint,getdatalisttotal,genpiechartdata,enumbits
from .primitives2D import iterline,iterparallelogram,itercirclepartlineedge,itercirclepartvertlineedge,itercircle,itercirclepart,iterellipserot,iterellipsepart,iterellipse,iterbeziercurve,iterbspline,recvert,horizontalvert,verticalvert,arcvert,rectboundarycoords,regpolygonvert,bsplinevert,itergetneighbors,spiralcontrolpointsvert,sortrecpoints,isinrectbnd,listinrecbnd,entirecircleisinboundary,entireellipseisinboundary,ellipsevert
from .solids3D import gensides,perspective,getshapesidedict,tetrahedravert,cubevert,hexahedravert,octahedravert,decahedvertandsurface,icosahedvertandsurface,fillpolydata,polyboundary,surfplot3Dvertandsurface,cylindervertandsurface,spherevertandsurface,rotvec3D,conevertandsurface
from .fonts import font8x8,font8x14,getcharfont
from .colors import bmpvalidcolorbits,isvalidcolorbit,bmpstdpal,getdefaultbitpal,colormix,RGBtoBGRarr,int2RGBlist,RGBfactors2RGB,int2BGRarr,RGB2int,int2RGBarr,int2RGB,getcolorname2RGBdict,getdefaultlumrange,getRGBfactors,matchRGBtopal,brightnessadjust,monochromepal,colorfiltertoBGRbuf,gammaBGRbuf,applymonochromefiltertoBGRbuf,applycolorfiltertoBGRbuf,applygammaBGRbuf,probplotRGBto1bit,thresholdadjust,colorfilter,monochrome,gammacorrect,monochromefiltertoBGRbuf,RGBfactorstoBaseandRange,invertbitsinbuffer,applybrightnessadjtoBGRbuf,applythresholdadjtoBGRbuf,RGB2BGRbuf,makeBGRbuf
from .fractals import getIFSparams,mandelparamdict
from .buffersplit import altsplitbuf,altsplitbuf3way,altsplitbufnway
from .chartools import char2int,enumletters,enumreverseletters
from .inttools import readint,writeint,int2buf,buf2int
from .dicttools import dict2descorderlist
from .textgraphics import plotbitsastext,plot8bitpatternastext
from .messages import sysmsg

# BMP constants do not edit!!!
bmpheaderid,bmpfilesize,bmphdrsize,bmpcolorbits,bmpx,bmpy,bmppal=array('B',[66,77]),2,10,28,18,22,54
bmpheadersize={1:62,4:118,8:1078,24:54}
        
def checklink(func):
    """Decorator to test if first parameter in a function is a valid file

    Args:
        function
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        if isfile(args[0]):  
            return(func(*args,**kwargs))
        else: 
            print(sysmsg['filenotexist'])
    return(callf)

def checklinks(func):
    """Decorator to test if two parameters in a function are valid files

    Args:
        function
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        if isfile(args[0]) and isfile(args[1]):  
            return(func(*args,**kwargs))
        else: 
            print(sysmsg['filenotexist'])
    return(callf)

def intcircleparam(func):
    """Decorator to test if the 2nd,3rd,4th parameters in a function that renders circle are ints 

    Args:
        function(bmp:array,x,y,r....)
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        if (type(args[1])==int and type(args[2])==int) and type(args[3])==int: 
            return(func(*args,**kwargs))
        else:  
            print(sysmsg['inttypereq'])
    return(callf)

def intcircleparam24bitonly(func):
    """Decorator to test if 2nd,3rd,4th parameters in a function that renders circle are ints
        and restrict  the use of  this function to only 24 bit or RGB bitmaps (1st parameter)

    Args:
        function(bmp:array,x,y,r....)
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        if args[0][bmpcolorbits]!=24 : 
            print(sysmsg['not24bit'])
        else:
            if (type(args[1])==int and type(args[2])==int) and type(args[3])==int: 
                return(func(*args,**kwargs))
            else:  
                print(sysmsg['inttypereq'])
    return(callf)

def func24bitonly(func):
    """Decorator to restrict the use of this function to only 24 bit or RGB bitmaps (1st parameter)

    Args:
        function(bmp:array,...)
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        if args[0][bmpcolorbits]!=24 : 
            print(sysmsg['not24bit'])
        else: 
            return(func(*args,**kwargs))
    return(callf)

def func24bitonlyandentirerectinboundary(func):
    """Decorator to restrict the use of this function to only 24 bit or RGB bitmaps (1st parameter)  
        and ensure that the 2nd, 3rd, 4th and 5th parameters are ints whose values when interpreted 
        as x and y coordinates lay within the RGB bitmap.

    Args:
        function(bmp:array,x1:int,y2:int,x2:int,y2:int...)
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        bmp,x1,y1,x2,y2=args[0],args[1],args[2],args[3],args[4]
        if bmp[bmpcolorbits]!=24 : 
            print(sysmsg['not24bit'])
        else:
            if (type(x1)==int and type(x2)==int) and (type(y1)==int and type(y2)==int):
                if not (isinBMPrectbnd(bmp,x1,y1) and isinBMPrectbnd(bmp,x2,y2)):
                    print(sysmsg['regionoutofbounds'])
                else: 
                    return(func(*args,**kwargs))
            else:  
                print(sysmsg['inttypereq'])
    return(callf)

def func24bitonlyandentirecircleinboundary(func):
    """Decorator to restrict the use of this function toonly 24 bit or RGB bitmaps (1st parameter)  
        and ensure that  the 2nd, 3rd, 4th parameters are ints  whose values  when interpreted  as 
        x,y and radius of a circle lay within the RGB bitmap.

    Args:
        function(bmp:array,x:int,y:int,r:int...)
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        bmp,x,y,r=args[0],args[1],args[2],args[3]
        if bmp[bmpcolorbits]!=24: 
            print(sysmsg['not24bit'])
        else:
            if (type(x)==int and type(y)==int) and type(r)==int:
                if entirecircleisinboundary(x,y,-1,getmaxx(bmp),-1,getmaxy(bmp),r): 
                    return(func(*args,**kwargs))
                else: 
                    print(sysmsg['regionoutofbounds'])
            else:  
                print(sysmsg['inttypereq'])
    return(callf)

def func8and24bitonlyandentirecircleinboundary(func):
    """Decorator to restrict the use of this function toonly 24 bit or 8 bit bitmaps (1st parameter)  
        and  ensure that  the 2nd, 3rd, 4th  parameters are ints  whose values  when interpreted  as  
        x,y and radius of a circle lay within the RGB bitmap.

    Args:
        function(bmp:array,x:int,y:int,r:int...)
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        bmp,x,y,r=args[0],args[1],args[2],args[3]
        if bmp[bmpcolorbits] not in [24,8]: 
            print(sysmsg['not24or8bit'])
        else:
            if (type(x)==int and type(y)==int) and type(r)==int:
                if entirecircleisinboundary(x,y,-1,getmaxx(bmp),-1,getmaxy(bmp),r): 
                    return(func(*args,**kwargs))
                else: 
                    print(sysmsg['regionoutofbounds'])
            else:  
                print(sysmsg['inttypereq'])
    return(callf)

def func8and24bitonly(func):
    """Decorator to restrict the use of this function to only 24 bit or 8 bit bitmaps (1st parameter)

    Args:
        function(bmp:array,...)
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        if args[0][bmpcolorbits] not in [24,8]: 
            print(sysmsg['not24or8bit'])
        else: 
            return(func(*args,**kwargs))
    return(callf)

def func8and24bitonlyandentirerectinboundary(func):
    """Decorator to restrict the use of this function to only 24 bit or 8 bit bitmaps (1st parameter) 
        and ensure that  the 2nd, 3rd, 4th and 5th parameters are ints  whose values when interpreted 
        as x and y coordinates of a rectangle lay within the RGB bitmap.

    Args:
        function(bmp:array,x1:int,y2:int,x2:int,y2:int...)
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        bmp,x1,y1,x2,y2=args[0],args[1],args[2],args[3],args[4]
        if bmp[bmpcolorbits] not in [24,8]: 
            print(sysmsg['not24or8bit'])
        else:
            if (type(x1)==int and type(x2)==int) and (type(y1)==int and type(y2)==int):
                if not (isinBMPrectbnd(bmp,x1,y1) and isinBMPrectbnd(bmp,x2,y2)):
                    print(sysmsg['regionoutofbounds'])
                else: 
                    return(func(*args,**kwargs))
            else:  
                print(sysmsg['inttypereq'])
    return(callf)

def entirerectinboundary(func):
    """Decorator to ensure that the 2nd, 3rd, 4th and 5th parameters are ints whose values when 
        interpreted as x and y coordinates of a rectangle lay within the bitmap.

    Args:
        function(bmp:array,x1:int,y2:int,x2:int,y2:int...)
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        bmp,x1,y1,x2,y2=args[0],args[1],args[2],args[3],args[4]
        if (type(x1)==int and type(x2)==int) and (type(y1)==int and type(y2)==int):
            if not (isinBMPrectbnd(bmp,x1,y1) and isinBMPrectbnd(bmp,x2,y2)):
                print(sysmsg['regionoutofbounds'])
            else: 
                return(func(*args,**kwargs))
        else:  
            print(sysmsg['inttypereq'])
    return(callf)

def entirecircleinboundary(func):
    """Decorator to ensure that the 2nd, 3rd, 4th parameters are ints whose values when interpreted 
        as the centerpoint x,y and radius r of a circle lay within the RGB bitmap.

    Args:
        function(bmp:array,x:int,y:int,r:int...)
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        bmp,x,y,r=args[0],args[1],args[2],args[3]
        if (type(x)==int and type(y)==int) and type(r)==int:
            if entirecircleisinboundary(x,y,-1,getmaxx(bmp),-1,getmaxy(bmp),r): 
                return(func(*args,**kwargs))
            else: 
                print(sysmsg['regionoutofbounds'])
        else:  
            print(sysmsg['inttypereq'])
    return(callf)

def adjustbufsize(bufsize:int,bits:int) -> int :
    """Adjust buffer size to account for bit depth

    Args:
        bufsize: initial estimate of buffer size
        bits   : bit depth of bitmap (1,4,8,24)
        
    Returns:
        An adjusted int value of the buffer size

    """
    if bits==24: 
        bufsize*=3
    elif bits==4: 
        bufsize=bufsize>>1
    elif bits==1: 
        bufsize=bufsize>>3
    return bufsize

def setmaxx(bmp:array,xmax:int):
    """Sets the x value stored in the windows bmp header

    Args:
        bmp: unsigned byte array with bmp format
        int: value of x dimension

    Returns:
        byref modified byte array with x dimension

    """
    writeint(bmpx,4,bmp,xmax)

def getmaxx(bmp:array) -> int:
    """Gets the x value stored in the windows bmp header

    Args:
        bmp: unsigned byte array with bmp format

    Returns:
        int value of x bmp dimension

    """
    return readint(bmpx,4,bmp)

def setmaxy(bmp:array,ymax:int):
    """Sets the y value stored in the windows bmp header

    Args:
        bmp: unsigned byte array with bmp format
        int: value of y dimension
     
    Returns:
        byref modified byte array with y dimension

    """
    writeint(bmpy,4,bmp,ymax)

def getmaxy(bmp:array) -> int:
    """Gets the y value stored in the windows bmp header

    Args:
        bmp: unsigned byte array with bmp format

    Returns:
        int value of y bmp dimension

    """
    return readint(bmpy,4,bmp)

def getmaxxy(bmp:array) -> tuple:
    """Gets the max x and y values stored in the windows bmp header

    Args:
        bmp: unsigned byte array with bmp format

    Returns:
        tuple (x:int,y:int) 

    """
    return (readint(bmpx,4,bmp),readint(bmpy,4,bmp))

def bottomrightcoord(bmp:array) -> tuple:
    """Gets the maximum bottom right coordinates of a windows bitmap

    Args:
        bmp: An unsigned byte array with bmp format

    Returns:
        tuple (x:int,y:int) 

    """
    return (readint(bmpx,4,bmp)-1,readint(bmpy,4,bmp)-1)

def centercoord(bmp:array) -> tuple:
    """Gets the central coordinates of a windows bitmap

    Args:
        bmp: An unsigned byte array with bmp format

    Returns:
        tuple (x:int,y:int) 

    """
    return ((readint(bmpx,4,bmp)-1)>>1,(readint(bmpy,4,bmp)-1)>>1)

def isinBMPrectbnd(bmp:array,x:int,y:int)->bool:
    """Checks if (x,y) coordinates are within the rectangular bounds of a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int value of location in x axis and y axis

    Returns:
        True if within bounds, False if out of bounds 

    """
    return (x<readint(bmpx,4,bmp) and y<readint(bmpy,4,bmp)) and (x>-1 and y>-1)

def listinBMPrecbnd(bmp:array,xylist:list) -> bool:
    """Checks if a list of (x,y) coordinates are within the rectangular bounds of a bitmap

    Args:
        bmp   : unsigned  byte array with bmp format
        xylist: list of (x,y) coordinates to be checked

    Returns:
        True if within bounds, False if out of bounds 

    """
    retval=True
    for v in xylist:
        if isinBMPrectbnd(bmp,v[0],v[1])==False: 
            break
    return retval

def setcolorbits(bmp:array,bits:int):
    """Set the bit depth of a windows bitmap

    Args:
        bmp: An unsigned  byte array with bmp format
        int: value of bit depth (1,4,8,24)
        
    Returns:
        byref modified byte array with new file size

    """
    bmp[bmpcolorbits]=bits

def getcolorbits(bmp:array) -> int:
    """Get the bit depth of a windows bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        int value of bit depth (1,4,8,24)

    """
    return bmp[bmpcolorbits]

def getxcharcount(bmp:array) -> int:
    """Get the chars or bytes in row of a bitmap

    Args:
        bmp: unsigned  byte array with bmp format
        
    Returns:
        count of bytes or chars in a row (x dim)

    """
    return computexbytes(readint(18,4,bmp),bmp[bmpcolorbits])

def setfilesize(bmp:array,size:int):
    """Set the header size of a windows bitmap

    Args:
        bmp  : unsigned  byte array with bmp format
        size : unsigned int value of size of the bmp file
        
    Returns:
        byref modified byte array with new file size

    """
    writeint(bmpfilesize,8,bmp,size)

def getfilesize(bmp:array) -> int:
    """Get the header size of a windows bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        unsigned int value of size of the bmp header

    """
    return readint(bmpfilesize,8,bmp)

def sethdrsize(bmp:array,hdsize:int):
    """Set the header size of a windows bitmap

    Args:
        bmp   : unsigned byte array with bmp format
        hdsize: unsigned int value of size of the bmp header
        
    Returns:
        byref modified byte array with new header size

    """
    writeint(bmphdrsize,4,bmp,hdsize)

def gethdrsize(bmp:array) -> int:
    """Get the header size of a windows bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        int value of header size

    """
    return readint(bmphdrsize,4,bmp)

def getimageinfo(bmp:array):
    """Gets metadata in a windows bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        4 int values

    """
    return readint(bmpy,4,bmp),bmp[bmpcolorbits],getxcharcount(bmp),readint(bmphdrsize,4,bmp)

def getmaxcolors(bmp:array) -> int:
    """Get the maximum number of colors supported by a windows bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        int value

    """
    return 1<<bmp[bmpcolorbits]

def compute24bitBMPoffset(bmp:array,x:int,y:int) -> int:
    """Get the offset in a byte array with RGB data given x and y

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int value of location in x axis and y axis

    Returns:
        int value of offset to that data in byte array

    """
    return (x*3)+((readint(bmpy,4,bmp)-y-1)*computexbytes(readint(bmpx,4,bmp),24))

def compute24bitBMPoffsetwithheader(bmp:array,x:int,y:int) -> int:
    """Get the offset in a byte array with RGB data given x and y
        with bitmap header size also taken into account 

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int value of location in x axis and y axis

    Returns:
        int value of offset to that data in byte array

    """
    return (x*3)+((readint(bmpy,4,bmp)-y-1)*computexbytes(readint(bmpx,4,bmp),24))+54

def compute8bitBMPoffset(bmp:array,x:int,y:int) -> int:
    """Get the offset in a byte array with 8 bit color data given x and y data

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int value of location in x axis and y axis

    Returns:
        int value of offset to that data in byte array

    """
    return x+((readint(bmpy,4,bmp)-y-1)*computexbytes(readint(bmpx,4,bmp),8))

def compute8bitBMPoffsetwithheader(bmp:array,x:int,y:int) -> int:
    """Get the offset in a byte array with 8 bit color data 
        given x and y with adjustments made due to bitmap header 

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int value of location in x axis and y axis

    Returns:
        int value of offset to that data in byte array

    """
    return x+((readint(bmpy,4,bmp)-y-1)*computexbytes(readint(bmpx,4,bmp),8))+1078

def compute4bitBMPoffset(bmp:array,x:int,y:int) -> int:
    """Get the offset in a byte array with 4 bit color data given x and y data

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int value of location in x axis and y axis

    Returns:
        int value of offset to that data in byte array

    """
    return (x>>1)+((readint(bmpy,4,bmp)-y-1)*computexbytes(readint(bmpx,4,bmp),4))

def compute1bitBMPoffset(bmp:array,x:int,y:int) -> int:
    """Get the offset in a byte array with 1 bit color data given x and y data

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int value of location in x axis and y axis

    Returns:
        int value of offset to that data in byte array

    """
    return (x>>3)+((readint(bmpy,4,bmp)-y-1)*computexbytes(readint(bmpx,4,bmp),1))

def compute4bitBMPoffsetwithheader(bmp:array,x:int,y:int) -> int:
    """Get the offset in a byte array with 4 bit color data 
        given x and y with adjustments made due to a header 

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int value of location in x axis and y axis

    Returns:
        int value of offset to that data in byte array

    """
    return (x>>1)+((readint(bmpy,4,bmp)-y-1)*computexbytes(readint(bmpx,4,bmp),4))+118

def compute1bitBMPoffsetwithheader(bmp: array,x:int,y:int) -> int:
    """Get the offset in a byte array with 1 bit color data 
        given x and y with adjustments made due to a header 

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int value of location in x axis and y axis

    Returns:
        int value of offset to that data in byte array

    """
    return (x>>3)+((readint(bmpy,4,bmp)-y-1)*computexbytes(readint(bmpx,4,bmp),1))+62

def getcomputeBMPoffsetwithheaderfunc(bmp:array):
    """Returns the correct function to use in computing offsets with headers given a bitmap

    Args:
        bmp: An unsigned byte array with bmp format

    Returns:
        function to compute offsets with headera

    """
    return {24:compute24bitBMPoffsetwithheader,8:compute8bitBMPoffsetwithheader,4:compute4bitBMPoffsetwithheader,1:compute1bitBMPoffsetwithheader}[bmp[bmpcolorbits]]

def getcomputeBMPoffsetfunc(bmp:array):
    """Returns the correct function to use in computing offset given a bitmap

    Args:
        bmp: An unsigned byte array with bmp format

    Returns:
        function to compute offsets

    """
    return {24:compute24bitBMPoffset,8:compute8bitBMPoffset,4:compute4bitBMPoffset,1:compute1bitBMPoffset}[bmp[bmpcolorbits]]

def computeBMPoffset(bmp:array,x:int,y:int) -> int:
    """Returns the offset given a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int location in x axis and y axis

    Returns:
        unsigned int offset to data in buffer

    """
    f=getcomputeBMPoffsetfunc(bmp)
    return f(bmp,x,y)

def computeBMPoffsetwithheader(bmp:array,x:int,y:int) -> int:
    """Returns the offset given a bitmap with header considered

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int location in x axis and y axis

    Returns:
        unsigned int offset to data in buffer

    """
    f=getcomputeBMPoffsetwithheaderfunc(bmp)
    return f(bmp,x,y)

def getmaxxyandbits(bmp:array) -> tuple:
    """Returns bitmap metadata (x dimension,y dimension, bit depth)

    Args:
        bmp: unsigned byte array with bmp format

    Returns:
        (x dimension,y dimension, bit depth)

    """
    return (((readint(bmpx,4,bmp),readint(bmpy,4,bmp)),bmp[bmpcolorbits]))

def computeuncompressedbmpfilesize(bmp:array) -> int:
    """Returns the uncompressed file size of a bitmap

    Args:
        bmp: unsigned byte array with bmp format

    Returns:
        unsigned int file size in bytes

    """
    return computeBMPfilesize(getmaxx(bmp),getmaxy(bmp),bmp[bmpcolorbits])

def isbmpcompressed(bmp:array) -> bool:
    """Test if bitmap is compressed

    Args:
        bmp: unsigned byte array with bmp format

    Returns:
        True if compressed, False if uncompressed

    """
    return computeuncompressedbmpfilesize(bmp)>getfilesize(bmp)

def compute24bitoffset(x:int,y:int,mx:int,my:int) -> int:
    """Get the offset in a byte array with 24 bit color data 

    Args:
        bmp  : unsigned byte array with bmp format
        x,y  : unsigned int pixel location 
        mx,my: unsigned int size in x dimension and y dimension
        
    Returns:
        int value of offset to that data in byte array

    """
    return (x*3)+((my-y-1)*computexbytes(mx,24))

def computexbytes(x:int,bits:int) -> int:
    """Get the number of bytes in a bmp row given x dimension and bit depth

    Args:
        x   : unsigned int value of x dimension
        bits: unsigned int value of bit depth (1,4,8,24)

    Returns:
        int value of number of bytes in a row

    """
    if bits<=8:
        xperbyte=8//bits
        xbytes,rem=divmod(x,xperbyte)
        if rem>0: xbytes+=1
    if bits==24:
        xbytes=x*3
    rem=xbytes&3
    if rem>0: 
        xbytes=xbytes+(4-rem)
    return xbytes

def computepadbytes(x:int,bits:int) -> int:
    """Get the number of bytes used to pad for 32 bit alignment given x dimension and bit depth

    Args:
        x   : unsigned int value of x dimension
        bits: unsigned int value of bit depth (1,4,8,24)

    Returns:
        int value of number of pad bytes

    """
    if bits<=8:
        xperbyte=8//bits
        xbytes,rem=divmod(x,xperbyte)
        if rem>0: 
            xbytes+=1
    if bits==24:
        xbytes=x*3
    rem=xbytes&3
    return iif(rem>0,4-rem,0)

def getdefaultBMPhdrsize(bits:int) -> int:
    """Gets default bitmap header size

    Args:
        bits: bit depth (1,4,8,24)

    Returns:
        unsigned int value of header size

    """
    return bmpheadersize[bits]

def computeBMPfilesize(x:int,y:int,bits:int) -> int:
    """computes bitmap file size

    Args:
        x,y : unsigned int value of x dimension and y dimension
        bits: bit depth (1,4,8,24)

    Returns:
        int value of file size

    """
    return computexbytes(x,bits)*y+bmpheadersize[bits]

def compute_bmpmetadata(x:int,y:int,bits:int) -> tuple:
    """computes bitmap meta data

    Args:
        x,y  : unsigned int value of x dimension and y dimension
        bits : bit depth (1,4,8,24)

    Returns:
        uint values for (filesize,headersize,xdim,ydim,bitdepth) 

    """
    return (computeBMPfilesize(x,y,bits),bmpheadersize[bits],x,y,bits)

def isdefaultpal(bmp: array) -> bool:
    """Checks if bitmap has a default RGB color palette

    Args:
        bmp: unsigned byte array with bmp format

    Returns:
        True if default, False if not default

    """
    return getdefaultbitpal(getcolorbits(bmp))==getallRGBpal(bmp)

def getBMPimgbytes(bmp: array) -> list:
    """Gets the raw image buffer of a bitmap without the header

    Args:
        bmp: unsigned byte array with bmp format

    Returns:
        list of unsigned bytes

    """
    return bmp[gethdrsize(bmp):getfilesize(bmp)]

def setBMPimgbytes(bmp:array,buf:array):
    """Sets the raw image buffer of a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        buf: array of unsigned bytes

    Returns:
        byref modified unsigned byte array

    """
    bmp[gethdrsize(bmp):getfilesize(bmp)]=buf

def setbmppal(bmp: array,pallist: list):
    """Sets the RGB palette of a bitmap

    Args:
        bmp    : unsigned byte array with bmp format
        pallist: [(r:byte,g:byte,b:byte),...]

    Returns:
        byref modified unsigned byte array

    """
    c=0
    if len(pallist)==getmaxcolors(bmp):
        for p in pallist:
            setRGBpal(bmp,c,p[0],p[1],p[2])
            c+=1

def getallRGBpal(bmp:array) -> list:
    """Gets the RGB palette of a bitmap

    Args:
        bmp: unsigned byte array with bmp format

    Returns:
        [(r:byte,g:byte,b:byte),...]

    """
    colors=getmaxcolors(bmp)
    return [getRGBpal(bmp,c) for c in range(0,colors)]

def getRGBpal(bmp:array,c:int) -> list:
    """Gets the [R,G,B] values of color c in a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        c  : unsigned int color 

    Returns:
        [R:byte,G:byte,B:byte]

    """
    i=bmppal+(c<<2)
    return [bmp[i+2],bmp[i+1],bmp[i]]

def setRGBpal(bmp:array,c:int,r:int,g:int,b:int):
    """Sets the r,g,b values of color c in a bitmap

    Args:
        bmp   : unsigned byte array with bmp format
        r,g,b : unsigned byte values for red, green and blue
        c     : unsigned int color 

    Returns:
        byref modified unsigned byte array

    """
    start=bmppal+(c<<2)
    end=start+3
    bmp[start:end]=RGBtoBGRarr(r,g,b)

def colorhistorgram(bmp:array) -> list:
    """Creates a color histogram 

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        list sorted in descending order of color frequencies

    """
    d={}
    for v in iterimagecolor(bmp,sysmsg['colorhist'],'*',sysmsg['done']):
        c=v[1]
        if c not in d: 
            d.setdefault(c,1)
        else: 
            d[c]+=1
    return  dict2descorderlist(d)

def makenewpalfromcolorhist(chist:list,colors:int,similaritythreshold:float) -> list:
    """Creates a new palatte based on a color histogram

    Args:
        chist              : list sorted in descending order of color frequencies
        colors             : maximum of colors of new palette
        similaritythreshold: controls how close palette entries can be
        
    Returns:
        unsigned byte array with bmp format

    """
    newpal,palcnt,colorcount=[[0,0,0]],1,len(chist)
    for i in range(0,colorcount):
        rgb=int2RGBlist(chist[i][1])
        addcl=True
        for palentry in newpal:
            if distance(palentry,rgb)<similaritythreshold: addcl=False
        if addcl:
            print(palcnt, '=' ,rgb)
            newpal.append(rgb)
            palcnt+=1
        if palcnt==colors: break
    return newpal

def copyBMPhdr(bmp:array) -> array:
    """Copies the bitmap header of an in-memory bmp to a new unsigned byte array

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        unsigned byte array with bmp format

    """
    hdrsize,newbmp=gethdrsize(bmp),array('B',[0]*getfilesize(bmp))
    newbmp[0:hdrsize]=bmp[0:hdrsize]
    return newbmp

def copyRGBpal(sourceBMP:array,destBMP:array):
    """Copies the RGB palette info from a source unsigned byte array 
        to a destination unsigned byte array

    Args:
        sourceBMP,destBMP : unsigned byte array with bmp format
        
    Returns:
        byRef modified destBMP (unsigned byte array)

    """
    hdl=gethdrsize(sourceBMP)
    destBMP[bmppal:hdl]=sourceBMP[bmppal:hdl]

def setbmp_properties(bmpmeta:list) -> array:
    """Creates a new bitmap with the properties set by bmpmeta to a new unsigned byte array

    Args:
        bmpmeta: list composed of 5 unsigned ints
        
    Returns:
        unsigned byte array with bmp format

    """
    bmp,filesize,hdrsize,x,y,bits=array('B'),bmpmeta[0],bmpmeta[1],bmpmeta[2],bmpmeta[3],bmpmeta[4]
    bmp.frombytes(b'\x00'*(filesize))
    bmp[0:2]=bmpheaderid
    setfilesize(bmp,filesize)
    sethdrsize(bmp,hdrsize)
    setmaxx(bmp,x)
    setmaxy(bmp,y)
    bmp[bmpcolorbits]=bits
    bmp[14]=40 #required
    if bits<24: 
        setbmppal(bmp,getdefaultbitpal(bits))
    return bmp

def setnewpalfromsourcebmp(sourcebmp:array,newbmp:array,similaritythreshold:float) -> list:
    """Copies the RGB palette info from a source unsigned byte array 
        to a destination unsigned byte array source and  destination 
        can have different bit depths

    Args:
        sourceBMP,newBMP   : unsigned byte arrays with bmp format
        similaritythreshold: how close can a color in a palette entry be to another
        
    Returns:
        byRef modified newBMP (unsigned byte array)
        list of new palette entries based on source bitmap

    """
    newpal=makenewpalfromcolorhist(colorhistorgram(sourcebmp),getmaxcolors(newbmp),similaritythreshold)
    setbmppal(newbmp,newpal)
    return newpal

def RGBpalbrightnessadjust(bmp:array,percentadj:float)-> list:
    """Copies the RGB palette info from a source unsigned byte array  
        to a destination unsigned byte array

    Args:
        bmp       : unsigned byte array with bmp format
        percentadj: signed float brightness adjustment in %
        
    Returns:
        list of modified RGB values

    """
    return [brightnessadjust(c,percentadj) for c in getallRGBpal(bmp)]

def setBMP2monochrome(bmp:array,RGBfactors:list) -> list:
    """Sets a bitmap to use a monochrome palette

    Args:
        bmp       : unsigned byte array with bmp format
        RGBfactors: (r:float,g:float,b:float) all values range from 0 to 1
        
    Returns:
        list of modified RGB values
        byref modified byte array

    """    
    newpal=monochromepal(getcolorbits(bmp),RGBfactors)
    setbmppal(bmp,newpal)
    return newpal

def newBMP(x:int,y:int,colorbits:int) -> array:
    """Creates a new in memory bitmap

    Args:
        x,y      : unsigned int values of x dimension and y dimension
        colorbits: bit depth (1,4,8,24)

    Returns:
        unsigned byte array with bitmap layout

    """
    return setbmp_properties(compute_bmpmetadata(x,y,colorbits))

def CopyBMPxydim2newBMP(bmp:array,newbits:int) -> array:
    """Creates a new bitmap with the same dimensions as bmp

    Args:
        bmp    : unsigned byte array with bmp format
        newbits: bit depth (1,4,8,24)

    Returns:
        unsigned byte array with bitmap layout

    """
    return newBMP(getmaxx(bmp),getmaxy(bmp),newbits)

@checklink
def loadBMP(filename:str) -> array:
    """Load bitmap to a byte array

    Args:
        filename: full path to the file to be loaded
        
    Returns:
        byte array with bmp file contents

    """
    a=array('B')
    with open(filename,'rb') as f: #ucompressed BMP only
        hd=f.read(2)
        if hd!=b'BM': 
            print(sysmsg['notBMP'])
        else:
            fsize=char2int(f.read(8))
            f.seek(0)
            a.frombytes(f.read(fsize))
        f.close()
    return a

def saveBMP(filename:str,bmp:array):
    """Saves bitmap to file

    Args:
        filename: full path to the file to be saved
        bmp     : unsigned byte array with the layout of bmp file 

    """
    with open(filename,'wb') as f:
        f.write(bmp)
        f.close()

def BMPbitBLTput(bmp:array,offset:int,arraybuf:array):
    """Sets offset in array to arraybuf

    Args:
        bmp     : unsigned byte array with bmp format
        offset  : unsigned int address in buffer
        arraybuf: unsigned byte array

    Returns:
        byref modified unsigned byte array

    """
    hdrsize,bufsize=gethdrsize(bmp),len(arraybuf)
    startoff=hdrsize+offset
    endoff=startoff+bufsize
    if offset>=0 and endoff<=getfilesize(bmp): 
        bmp[startoff:endoff]=arraybuf
    else: 
        print (sysmsg['invalidoffset'])

def BMPbitBLTget(bmp:array,offset:int,bufsize:int) -> array:
    """Gets [offset:offset+bufsize] to a new array 

    Args:
        bmp    : unsigned byte array with bmp format
        offset : unsigned int address in buffer
        bufsize: unsigned int size of buffer

    Returns:
        unsigned byte array

    """
    hdrsize,retval=gethdrsize(bmp),array('B',[])
    startoff=hdrsize+offset
    endoff=startoff+bufsize
    if (offset>=0 and bufsize>0 ) and endoff<=getfilesize(bmp): 
        retval=bmp[startoff:endoff]
    else: 
        print(sysmsg['invalidoffset'])
    return retval

def vertBMPbitBLTget(bmp:array,x:int,y1:int,y2:int) -> array:
    """Gets vertical slice to a new array 

    Args:
        bmp     : unsigned byte array with bmp format
        x,y1,y2 : unsigned int x coordinate and y coordinates of vertical slice

    Returns:
        unsigned byte array

    """
    bits=bmp[bmpcolorbits]
    r,m,c=getxcharcount(bmp),getmaxxy(bmp),getcomputeBMPoffsetwithheaderfunc(bmp)
    if isinrange(x,m[0],-1):
        y1,y2=swapif(y1,y2,y1>y2)
        y1,y2=setmin(y1,0),setmax(y2,m[1]-1)
        s,e=c(bmp,x,y2),c(bmp,x,y1)+r
        if bits==24: 
            return makeBGRbuf(bmp[s:e-2:r],bmp[s+1:e-1:r],bmp[s+2:e:r])
        else: 
            return bmp[s:e:r]
    else: 
        print(sysmsg['lineoutofbnd'])

def applyfuncwithparam2vertBMPbitBLTget(bmp:array,x:int,y1:int,y2:int,func,funcparam):
    """Apply a user defined function to vertical slices

    Args:
        bmp       : unsigned byte array with bmp format
        x,y1,y2   : unsigned int x coordinate and y coordinates of vertical slice
        func      : user defined function func
        funcparam : parameters of the user defined function

    Returns:
        byref modified unsigned byte array

    """
    bits=bmp[bmpcolorbits]
    r,m,c=getxcharcount(bmp),getmaxxy(bmp),getcomputeBMPoffsetwithheaderfunc(bmp)
    if isinrange(x,m[0],-1):
        y1,y2=swapif(y1,y2,y1>y2)
        y1,y2=setmin(y1,0),setmax(y2,m[1]-1)
        s,e=c(bmp,x,y2),c(bmp,x,y1)+r
        if bits==24: 
            bmp[s:e-2:r],bmp[s+1:e-1:r],bmp[s+2:e:r]=func(bmp[s:e-2:r],funcparam),func(bmp[s+1:e-1:r],funcparam),func(bmp[s+2:e:r],funcparam)
        else: 
            bmp[s:e:r]=func(bmp[s:e:r],funcparam)
    else: 
        print(sysmsg['lineoutofbnd'])

def plotRGBxybit(bmp: array,x: int,y: int,rgb: list):
    """Sets pixel at x,y in a bitmap to [R,G,B]

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int locations in x and y
        rgb: [R:byte,G:byte,B:byte] 

    Returns:
        byref modified unsigned byte array

    """
    if isinBMPrectbnd(bmp,x,y):
        if bmp[bmpcolorbits]==24:
            offset=compute24bitBMPoffsetwithheader(bmp,x,y)
            endoffset=offset+3
            bmp[offset:endoffset]= array('B',[rgb[2],rgb[1],rgb[0]])
        else: 
            plotxybit(bmp,x,y,matchRGBtopal(rgb,getallRGBpal(bmp)))

def plotxybit(bmp:array,x:int,y:int,c:int):
    """Sets pixel at x,y in a bitmap to color c

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int locations in x and y
        c  : unsigned int color

    Returns:
        byref modified unsigned byte array

    """
    if isinBMPrectbnd(bmp,x,y):
        offset,bits=computeBMPoffsetwithheader(bmp,x,y),bmp[bmpcolorbits]
        if bits==24:
            bmp[offset:offset+3]=int2BGRarr(c)
        elif bits==8:
            bmp[offset]=c&0xff
        elif bits==4:
            if c>15: 
                c&=0xf
            if x&1==1: 
                bmp[offset]=(bmp[offset] & 0xf0)+c
            else: 
                bmp[offset]=(c<<4)+(bmp[offset] & 0xf)
        elif bits==1:
            b,mask=bmp[offset],1<<(7-(x%8))
            if c>1: 
                c=1
            if c==1: 
                b=b | mask
            else:
                if b & mask>0: b=b ^ mask
            bmp[offset]=b

def getxybit(bmp:array,x:int,y:int) -> int:
    """Gets color of pixel at x,y in a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int locations in x and y

    Returns:
        unsigned int color value

    """
    retval=0
    if isinBMPrectbnd(bmp,x,y):
        offset,bits=computeBMPoffsetwithheader(bmp,x,y),bmp[bmpcolorbits]
        if bits==1:
            mask=7-(x%8)
            retval=(bmp[offset] & (1<<mask))>>mask
        elif bits==4:
            if x&1==1: 
                retval=(bmp[offset] & 0xf)
            else: 
                retval=(bmp[offset] & 0xf0)>>4
        elif bits==8: 
            retval=bmp[offset]
        elif bits==24:
            retval=RGB2int(bmp[offset+2],bmp[offset+1],bmp[offset])
    else: 
        retval=-1
    return retval

def getRGBxybitvec(bmp:array,v:list) -> int:
    """Gets [R:byte,G:byte,B:byte] of pixel at (x,y) in a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        v  : (x:int,y:int)
        
    Returns:
        [R:byte,G:byte,B:byte]

    """
    return getRGBxybit(bmp,v[0],v[1])

def getRGBxybit(bmp: array,x: int,y: int) -> list:
    """Gets [R:byte,G:byte,B:byte] of pixel at x,y in a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        x,y: unsigned int locations in x and y 
        
    Returns:
        [R:byte,G:byte,B:byte]

    """
    retval=[]
    if isinBMPrectbnd(bmp,x,y):
        if getcolorbits(bmp)==24:
            i=compute24bitBMPoffsetwithheader(bmp,x,y)
            retval=[bmp[i+2],bmp[i+1],bmp[i]]
        else: 
            retval=getRGBpal(bmp,getxybit(bmp,x,y))
    return retval

def getxybitvec(bmp:array,v:list) -> int:
    """Gets color of pixel at (x,y) in a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        v  : (x:int,y:int)
        
    Returns:
        unsigned int color value

    """
    return getxybit(bmp,v[0],v[1])

def intplotvecxypoint(bmp:array,v:list,c:int):
    """Sets color of pixel at (x,y) in a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        v  : (x:int,y:int)
        c  : unsigned int color value
        
    Returns:
        byref modified unsigned byte array

    """
    plotxybit(bmp,v[0],v[1],c)

def plotvecxypoint(bmp:array,v:list,c:int):
    """Sets color of pixel at (x,y) in a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        v  : (x:float,y:float)
        c  : unsigned int color value
        
    Returns:
        byref modified unsigned byte array

    """
    v=roundvect(v)
    plotxybit(bmp,v[0],v[1],c)

def plotRGBxybitvec(bmp:array,v:list,rgb:list):
    """Sets [R,G,B] of pixel at (x,y) in a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        v  : (x:float,y:float)
        rgb: [R:byte,G:byte,B:byte]
        
    Returns:
        byref modified unsigned byte array

    """
    plotRGBxybit(bmp,v[0],v[1],rgb)

def plotxypointlist(bmp:array,vlist:list,penradius:int,color:int):
    """Draws a circle or a point depending on penradius
        of a given color for all points in a point list

    Args:
        bmp      : unsigned byte array with bmp format
        vlist    : [(x:uint,y:uint) ,...] list of points
        penradius: radius of the pen in pixels
        color    : color of the pen
        
    Returns:
        byref modified unsigned byte array

    """
    for v in vlist: 
        roundpen(bmp,v,penradius,color)

def roundpen(bmp:array,point:list,penradius:int,color:int):
    """Draws a circle or a point depending on penradius of a given color

    Args:
        bmp      : unsigned byte array with bmp format
        point    : (x:uint,y:uint) centerpoint
        penradius: radius of the pen in pixels
        color    : color of the pen
        
    Returns:
        byref modified unsigned byte array

    """
    x,y=point[0],point[1]
    if penradius<=1: 
        plotxybit(bmp,x,y,color)
    else: 
        circle(bmp,x,y,penradius,color,True)

def swapcolors(bmp:array,p1:list,p2:list):
    """Swaps the colors of two points in a bitmap 

    Args:
        bmp  : unsigned byte array with bmp format
        p1,p2: endpoints of the line(x:uint,y:uint)
        
    Returns:
        byref modified unsigned byte array

    """
    c=getxybitvec(bmp,p1)
    intplotvecxypoint(bmp,p1,getxybitvec(bmp,p2))
    intplotvecxypoint(bmp,p2,c)

def line(bmp:array,x1:int,y1:int,x2:int,y2:int,color:int):
    """Creates a line in a bitmap 

    Args:
        bmp            : unsigned byte array with bmp format
        x1,y1 and x2,y2: endpoints of the line
        color          : color of the line
        
    Returns:
        byref modified unsigned byte array

    """
    m=getmaxxy(bmp)
    mx,my=m[0]-1,m[1]-1
    x1,x2,y1,y2=setminmax(x1,0,mx),setminmax(x2,0,mx),setminmax(y1,0,my),setminmax(y2,0,my)
    if x1==x2: 
        vertline(bmp,x1,y1,y2,color)
    elif y1==y2: 
        horiline(bmp,y1,x1,x2,color)
    else:
        bits=bmp[bmpcolorbits]
        c=getcomputeBMPoffsetwithheaderfunc(bmp)
        if bits==24:
            buf=int2BGRarr(color)
            for p in iterline((x1,y1),(x2,y2)):
                s=c(bmp,p[0],p[1])
                bmp[s:s+3]=buf
        elif bits==8:
            color&=0xff
            for p in iterline((x1,y1),(x2,y2)): 
                bmp[c(bmp,p[0],p[1])]=color
        elif bits==4:
            if color>15: 
                color&=0xf
            for p in iterline((x1,y1),(x2,y2)):
                s=c(bmp,p[0],p[1])
                if p[0]&1==1: 
                    bmp[s]=(bmp[s]&0xf0)+color
                else: 
                    bmp[s]=(color<<4)+(bmp[s]&0xf)
        elif bits==1:
            if color>1: 
                color&=0x1
            for p in iterline((x1,y1),(x2,y2)):
                s=c(bmp,p[0],p[1])
                b,mask=bmp[s],1<<(7-(p[0]%8))
                if color==1: 
                    b=b | mask
                else:
                    if b & mask>0: b=b ^ mask
                bmp[s]=b

def horiline(bmp:array,y:int,x1:int,x2:int,color:int):
    """Creates a horizontal line in a bitmap 

    Args:
        bmp  : unsigned byte array with bmp format
        y    : constant y value of the line
        x1,x2: line starts at x1 and ends at x2
        color: color of the line
        
    Returns:
        byref modified unsigned byte array

    """
    bits,m=bmp[bmpcolorbits],getmaxxy(bmp)
    if isinrange(y,m[1],-1):
        x1,x2=swapif(x1,x2,x1>x2)
        x1,x2=setmin(x1,0),setmax(x2,m[0]-1)
        dx=x2-x1+1
        s=computeBMPoffsetwithheader(bmp,x1,y)
        if bits==24:
            e=s+(dx*3)
            rgb=int2RGBlist(color)
            bmp[s:e]=array('B',[rgb[2],rgb[1],rgb[0]]*dx)
        elif bits==8:
            e=s+dx
            color&=0xff
            bmp[s:e]=array('B',[color]*dx)
        elif bits==4:
            dx>>=1
            e=s+dx
            color&=0xf
            c1,c2=-1,(color<<4)+color
            if x1&1==1: 
                c1=(bmp[s] & 0xf0)
            bmp[s:e]=array('B',[c2]*dx)
            if c1!=-1: 
                bmp[s]=c1+(bmp[s] & 0xf)
            if x2&1==1: 
                plotxybit(bmp,x2-1,y,color)
        elif bits==1:
            x2+=1
            for x in range(x1,x2): 
                plotxybit(bmp,x,y,color)
    else: 
        print(sysmsg['lineoutofbnd'])

def vertline(bmp:array,x:int,y1:int,y2:int,color:int):
    """Creates a vertical line in a bitmap 

    Args:
        bmp  : unsigned byte array with bmp format
        x    : constant x value of the line
        y1,y2: line starts at y1 and ends at y2
        color: color of the line
        
    Returns:
        byref modified unsigned byte array

    """
    bits=bmp[bmpcolorbits]
    if bits not in [24,8]:
        y1,y2=swapif(y1,y2,y1>y2)
        y2+=1
        for y in range(y1,y2): 
            plotxybit(bmp,x,y,color)
    else:
        r,m,c=getxcharcount(bmp),getmaxxy(bmp),getcomputeBMPoffsetwithheaderfunc(bmp)
        if isinrange(x,m[0],-1):
            y1,y2=swapif(y1,y2,y1>y2)
            y1,y2=setmin(y1,0),setmax(y2,m[1]-1)
            dy,rgb=y2-y1+1,int2RGBlist(color)
            s,e=c(bmp,x,y2),c(bmp,x,y1)+r
            if bits==24: 
                bmp[s:e-2:r],bmp[s+1:e-1:r],bmp[s+2:e:r]=array('B',[rgb[2]]*dy),array('B',[rgb[1]]*dy),array('B',[rgb[0]]*dy)
            elif bits==8: 
                bmp[s:e:r]=array('B',[color%256]*dy)
        else: 
            print(sysmsg['lineoutofbnd'])

def fillbackgroundwithgrad(bmp:array,lumrange:list,RGBfactors:list,direction:int):
    """Fills entire bitmap with a linear gradient

    Args:
        bmp       : unsigned byte array with bmp format
        lumrange  : [byte,byte] that define range of gradient
        RGBfactors: [r:float,g:float,b:float] each float 0 to 1
        direction : 0 - vertical or 1 - horizontal gradient
        
    Returns:
        byref modified unsigned byte array

    """
    filledgradrect(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1,lumrange,RGBfactors,direction)

@func8and24bitonlyandentirerectinboundary
def filledgradrect(bmp:array,x1:int,y1:int,x2:int,y2:int,lumrange:list,
                   RGBfactors:list,direction:int):
    """Creates a filled rectangle with a linear gradient in a bitmap 

    Args:
        bmp         : unsigned byte array with bmp format
        x1,y1,x2,y2 : defines the rectangle
        lumrange    : [byte,byte] that define range of gradient
        RGBfactors  : [r:float,g:float,b:float] each float 0 to 1
        direction   : 0 - vertical or 1 - horizontal gradient
        
    Returns:
        byref modified unsigned byte array

    """
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)   
    dx,dy=x2-x1+1,y2-y1+1
    base,lrange=RGBfactorstoBaseandRange(lumrange,RGBfactors)
    if direction==0:
        xlim=x2+1
        for x in range(x1,xlim):
            f=x/dx
            c=RGB2int(round(base[0]+lrange[0]*f),round(base[1]+lrange[1]*f),round(base[2]+lrange[2]*f))
            if bmp[bmpcolorbits]!=24:
                c=matchRGBtopal(int2RGBarr(c),getallRGBpal(bmp))
            if c<0: 
                c=0
            vertline(bmp,x,y1,y2,c)
    else:
        ylim=y2+1
        for y in range(y1,ylim):
            f=y/dy
            c=RGB2int(round(base[0]+lrange[0]*f),round(base[1]+lrange[1]*f),round(base[2]+lrange[2]*f))
            if bmp[bmpcolorbits]!=24:
                c=matchRGBtopal(int2RGBarr(c),getallRGBpal(bmp))
            if c<0: 
                c=0
            horiline(bmp,y,x1,x2,c)

@entirerectinboundary            
def itercopyrect(bmp:array,x1:int,y1:int,x2:int,y2:int) -> array:
    """Creates a filled rectangle with a linear gradient in a bitmap 

    Args:
        bmp         : unsigned byte array with bmp format
        x1,y1,x2,y2 : defines the rectangle
         
    Yields:
        unsigned byte array scanlines of the area

    """
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    bufsize,r=adjustbufsize(x2-x1+1,bmp[28]),getxcharcount(bmp)
    offset=computeBMPoffset(bmp,x1,y2)
    lim=computeBMPoffset(bmp,x2,y1)+r
    while (offset+bufsize)<=lim:
        yield BMPbitBLTget(bmp,offset,bufsize)
        offset+=r
    
def intlinevec(bmp:array,u:list,v:list,color:int):
    """Creates a line in a bitmap 

    Args:
        bmp   : unsigned byte array with bmp format
        u,v   : (x:int,y:int) endpoints that defines the line 
        color : color of the line
        
    Returns:
        byref modified unsigned byte array

    """
    line(bmp,u[0],u[1],v[0],v[1],color)

def linevec(bmp:array,u:list,v:list,color:int):
    """Creates a line in a bitmap 

    Args:
        bmp   : unsigned byte array with bmp format
        u,v   : (x:float,y:float) endpoints of the line 
        color : color of the line
        
    Returns:
        byref modified unsigned byte array

    """
    intlinevec(bmp,roundvect(u),roundvect(v),color)

def filledparallelogram(bmp:array,p1:list,p2:list,p3:list,color:int):
    """Creates a filled parallelogram in a bitmap defined by 3 points

    Args:
        bmp     : unsigned byte array with bmp format
        p1,p2,p3: (x:float,y:float) points that define a parallelogram
        color   : color of filled parallelgram
        
    Returns:
        byref unsigned modified byte array

    """
    for v in iterparallelogram(p1,p2,p3): 
        linevec(bmp,v[0],v[1],color)

def drawvec(bmp:array,u:list,v:list,headsize0fordefault:int,color:int):
    """Draws a vector or line segment with arrow head

    Args:
        bmp     : unsigned byte array with bmp format
        u       : (x:float,y:float) point 1 origin
        v       : (x:float,y:float) point 2 has arrow
        headsize0fordefault: size of arrow 
        color   : color of vector
        
    Returns:
        byref modified unsigned byte array

    """
    vm,anginc=vmag(subvect(u,v)),0.39269908169872414
    hm=iif(headsize0fordefault==0,vm/5,headsize0fordefault)
    a=anglebetween2Dlines(u,v)
    a1,a2=a-anginc,a+anginc
    linevec(bmp,u,v,color)
    def hdaddvect(bmp,v,hm,a1,a2):
        linevec(bmp,v,addvect(v,polar2rectcoord2D([hm,a1])),color)
        linevec(bmp,v,addvect(v,polar2rectcoord2D([hm,a2])),color)
    def hdsubvect(bmp,v,hm,a1,a2):
        linevec(bmp,v,subvect(v,polar2rectcoord2D([hm,a1])),color)
        linevec(bmp,v,subvect(v,polar2rectcoord2D([hm,a2])),color)
    if u[0]<v[0] and u[1]<v[1]: 
        hdsubvect(bmp,v,hm,a1,a2)
    elif u[0]>v[0] and u[1]>v[1]: 
        hdaddvect(bmp,v,hm,a1,a2)
    elif v[1]==u[1] and u[0]<v[0]: 
        hdsubvect(bmp,v,hm,a1,a2)
    elif v[1]==u[1] and u[0]>v[0]: 
        hdaddvect(bmp,v,hm,a1,a2)
    elif v[0]==u[0] and u[1]>v[1]: 
        hdsubvect(bmp,v,hm,a1,a2)
    elif v[0]==u[0] and u[1]<v[1]: 
        hdaddvect(bmp,v,hm,a1,a2)
    elif u[0]<v[0] and u[1]>v[1]: 
        hdsubvect(bmp,v,hm,a1,a2)
    else: 
        hdaddvect(bmp,v,hm,a1,a2)

def thickroundline(bmp:array,p1:list,p2:list,penradius:int,color:int):
    """Creates a thick rounded line in a bitmap 

    Args:
        bmp       : unsigned byte array with bmp format
        p1,p2     : (x,y) endpoints of the line
        penradius : radius of pen in pixels
        color     : color of the line
        
    Returns:
        byref modified unsigned byte array

    """
    for p in iterline(p1,p2): 
        circle(bmp,p[0],p[1],penradius,color,True)

def gradthickroundline(bmp:array,p1:list,p2:list,penradius:int,lumrange:list,RGBfactors:list):
    """Creates a thick rounded line in a bitmap 

    Args:
        bmp       : unsigned byte array with bmp format
        p1,p2     : (x,y) endpoints of the line
        penradius : radius of pen in pixels
        lumrange  : list of two byte values [gradstart,gradend]
        RGBfactors: [r,g,b] as unsigned float from 0 to 1
        
    Returns:
        byref modified unsigned byte array

    """
    lum1,lumrang=range2baseanddelta(lumrange)
    for i in range(penradius,0,-1):
        c=colormix(int(lum1+(lumrang*i/penradius)),RGBfactors)
        if bmp[bmpcolorbits]!=24:
            c=matchRGBtopal(int2RGBarr(c),getallRGBpal(bmp))
        thickroundline(bmp,p1,p2,i,c)

@intcircleparam24bitonly        
def applynoparam24bitfunctocircregion(bmp:array,x:int,y:int,r:int,func):
    """Apply a no parameter function func to a circular region 
        with center defined by x,y with a radius r to a 24-bit bitmap
        
    Args:
        bmp   : unsigned byte array with bmp format
        x,y,r : center (x,y) and radius r of region
        func  : function to apply
        
    Returns:
        byref modified unsigned byte array

    """
    c=getcomputeBMPoffsetwithheaderfunc(bmp)
    if entirecircleisinboundary(x,y,-1,getmaxx(bmp),-1,getmaxy(bmp),r):
        for v in itercirclepartlineedge(r):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            s1,e1,s2,e2=c(bmp,x1,y1),c(bmp,x2,y1),c(bmp,x1,y2),c(bmp,x2,y2)
            bmp[s1:e1]=func(bmp[s1:e1])
            if y1!=y2: 
                bmp[s2:e2]=func(bmp[s2:e2])
    else:
        xmax,ymax=getmaxx(bmp),getmaxy(bmp)
        for v in itercirclepartlineedge(r):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            x1,x2=setmin(x1,0),setmax(x2,xmax-1)
            if isinrange(y2,ymax,-1):
                s2,e2=c(bmp,x1,y2),c(bmp,x2,y2)
                bmp[s2:e2]=func(bmp[s2:e2])
            if isinrange(y1,ymax,-1) and y2!=y1:
                s1,e1=c(bmp,x1,y1),c(bmp,x2,y1)
                bmp[s1:e1]=func(bmp[s1:e1])

@intcircleparam24bitonly       
def apply24bitfunctocircregion(bmp:array,x:int,y:int,r:int,func,funcparam):
    """Apply function func to a circular region with center defined by 
        x,y with a radius r that is within a 24-bit bitmap
        
    Args:
        bmp       : unsigned byte array with bmp format
        x,y,r     : center (x,y) and radius r of region
        func      : function to apply
        funcparam : parameters of the function
        
    Returns:
        byref modified unsigned byte array

    """
    c=getcomputeBMPoffsetwithheaderfunc(bmp)
    if entirecircleisinboundary(x,y,-1,getmaxx(bmp),-1,getmaxy(bmp),r):
        for v in itercirclepartlineedge(r):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            s1,e1,s2,e2=c(bmp,x1,y1),c(bmp,x2,y1),c(bmp,x1,y2),c(bmp,x2,y2)
            bmp[s1:e1]=func(bmp[s1:e1],funcparam)
            if y2!=y1: 
                bmp[s2:e2]=func(bmp[s2:e2],funcparam)
    else:
        xmax,ymax=getmaxx(bmp),getmaxy(bmp)
        for v in itercirclepartlineedge(r):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            x1,x2=setmin(x1,0),setmax(x2,xmax-1)
            if isinrange(y2,ymax,-1):
                s2,e2=c(bmp,x1,y2),c(bmp,x2,y2)
                bmp[s2:e2]=func(bmp[s2:e2],funcparam)
            if isinrange(y1,ymax,-1) and y2!=y1:
                s1,e1=c(bmp,x1,y1),c(bmp,x2,y1)
                bmp[s1:e1]=func(bmp[s1:e1],funcparam)

@entirecircleinboundary
def copycircregion2buf(bmp:array,x:int,y:int,r:int) -> list:
    """Copies a circular region to a buffer which is defined by centerpoint (x,y) and radius r

    Args:
        bmp   : unsigned byte array with bmp format
        x,y,r : center (x,y) and radius r of region

    Returns:
        list with buffer of circular region

    """
    copybuf,c=[getcolorbits(bmp),r],getcomputeBMPoffsetwithheaderfunc(bmp)
    for v in itercirclepartlineedge(r):
        x1,x2=mirror(x,v[0])
        y1,y2=mirror(y,v[1])
        copybuf+=[[bmp[c(bmp,x1,y1):c(bmp,x2,y1)],bmp[c(bmp,x1,y2):c(bmp,x2,y2)]]]
    return copybuf

def pastecirularbuf(bmp:array,x:int,y:int,circbuf:list):
    """Paste a circular buffer with a given radius to a centerpoint (x,y)

    Args:
        bmp    : unsigned byte array with bmp format
        x,y    : center of circular region
        circbuf: list generated by copycircregion2buf
        
    Returns:
        byref modified unsigned byte array

    """
    if circbuf!=None:
        r,c=circbuf[1],getcomputeBMPoffsetwithheaderfunc(bmp)
        if entirecircleisinboundary(x,y,-1,getmaxx(bmp),-1,getmaxy(bmp),r):
            if getcolorbits(bmp)!=circbuf[0]: 
                raise(sysmsg['bitsnotequal'])
            else:
                i=2
                for v in itercirclepartlineedge(r):
                    x1,x2=mirror(x,v[0])
                    y1,y2=mirror(y,v[1])
                    bmp[c(bmp,x1,y1):c(bmp,x2,y1)],bmp[c(bmp,x1,y2):c(bmp,x2,y2)]=circbuf[i][0],circbuf[i][1]
                    i+=1
        else: 
            print(sysmsg['regionoutofbounds'])
    else: 
        print(sysmsg['invalidbuf'])

def copycircregion(bmp:array,x:int,y:int,r:int,newxy:list):
    """Copy a circular buffer at x,y with a radius r to a centerpoint newxy [x,y]

    Args:
        bmp   : unsigned byte array with bmp format
        x,y,r : center (x,y) and radius r of region
        newxy : center of circular area to paste
        
    Returns:
        byref modified unsigned byte array

    """
    pastecirularbuf(bmp,newxy[0],newxy[1],copycircregion2buf(bmp,x,y,r))

@intcircleparam
def applynoparamfunctocircregion(bmp:array,x:int,y:int,r:int,func):
    """Apply a no parameter function to a circular region with center defined by x,y with a radius r
        
    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region
        func : function to apply
        
    Returns:
        byref modified unsigned byte array

    """
    c=getcomputeBMPoffsetwithheaderfunc(bmp)
    if entirecircleisinboundary(x,y,-1,getmaxx(bmp),-1,getmaxy(bmp),r):
        for v in itercirclepartlineedge(r):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            s1,e1,s2,e2=c(bmp,x1,y1),c(bmp,x2,y1),c(bmp,x1,y2),c(bmp,x2,y2)
            bmp[s1:e1]=func(bmp[s1:e1])
            if y1!=y2: 
                bmp[s2:e2]=func(bmp[s2:e2])
    else:
        xmax,ymax=getmaxx(bmp),getmaxy(bmp)
        for v in itercirclepartlineedge(r):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            x1,x2=setmin(x1,0),setmax(x2,xmax-1)
            if isinrange(y2,ymax,-1):
                s2,e2=c(bmp,x1,y2),c(bmp,x2,y2)
                bmp[s2:e2]=func(bmp[s2:e2])
            if isinrange(y1,ymax,-1) and y2!=y1:
                s1,e1=c(bmp,x1,y1),c(bmp,x2,y1)
                bmp[s1:e1]=func(bmp[s1:e1])

@entirecircleinboundary        
def flipXYcircregion(bmp:array,x:int,y:int,r:int):
    """Flip the X and Y coordinates of a circular region with center defined by x,y with a radius r
        to rotate by 90 degrees
        
    Args:
        bmp   : unsigned byte array with bmp format
        x,y,r : center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    bits,c=bmp[bmpcolorbits],getcomputeBMPoffsetwithheaderfunc(bmp)
    if bits not in [24,8]:
        n=flipXY(bmp)
        for v in itercirclepartlineedge(r):
            x3,x4=mirror(y,v[0])
            y3,y4=mirror(x,v[1])
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            bmp[c(bmp,x1,y1):c(bmp,x2,y1)],bmp[c(bmp,x1,y2):c(bmp,x2,y2)]=n[c(n,x3,y3):c(n,x4,y3)],n[c(n,x3,y4):c(n,x4,y4)]
    else:
        c,buf=getcomputeBMPoffsetwithheaderfunc(bmp),[]
        for v in itercirclepartlineedge(r):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            x2+=1
            x3,x4=mirror(x,v[1])
            y3,y4=mirror(y,v[0])
            buf+=[[x1,y1,x2,y2,vertBMPbitBLTget(bmp,x3,y3,y4),vertBMPbitBLTget(bmp,x4,y3,y4)]]
        for b in buf:
            x1,y1,x2,y2=b[0],b[1],b[2],b[3]
            bmp[c(bmp,x1,y1):c(bmp,x2,y1)],bmp[c(bmp,x1,y2):c(bmp,x2,y2)]=b[4],b[5]

def fliphoricircregion(bmp:array,x:int,y:int,r:int):
    """Flips horizontally a circular region with a center x,y with a radius r
        
    Args:
        bmp   : unsigned byte array with bmp format
        x,y,r : center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    horitransformincircregion(bmp,x,y,r,'F')

@func8and24bitonlyandentirecircleinboundary
def horitransformincircregion(bmp:array,x:int,y:int,r:int,trans:str):
    """Applies a horizontal transform to circular region with a center x,y with a radius r
        
    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region
        trans: single letter transform code
        'L' mirror left 'R' mirror right 'F' flip
        
    Returns:
        byref modified unsigned byte array

    """
    def flip24():  
        bmp[s1:e1-2:k],bmp[s2:e2-2:k],bmp[s1+1:e1-1:k],bmp[s2+1:e2-1:k],bmp[s1+2:e1:k],bmp[s2+2:e2:k]=bmp[s2:e2-2:k],bmp[s1:e1-2:k],bmp[s2+1:e2-1:k],bmp[s1+1:e1-1:k],bmp[s2+2:e2:k],bmp[s1+2:e1:k]
    def flip8(): 
        bmp[s1:e1:k],bmp[s2:e2:k]=bmp[s2:e2:k],bmp[s1:e1:k]
    def mirror24R(): 
        bmp[s1:e1-2:k],bmp[s1+1:e1-1:k],bmp[s1+2:e1:k]=bmp[s2:e2-2:k],bmp[s2+1:e2-1:k],bmp[s2+2:e2:k]
    def mirror8R(): 
        bmp[s1:e1:k]=bmp[s2:e2:k]
    def mirror24L(): 
        bmp[s2:e2-2:k],bmp[s2+1:e2-1:k],bmp[s2+2:e2:k]=bmp[s1:e1-2:k],bmp[s1+1:e1-1:k],bmp[s1+2:e1:k]
    def mirror8L(): 
        bmp[s2:e2:k]=bmp[s1:e1:k]
    bits,c=bmp[bmpcolorbits],getcomputeBMPoffsetwithheaderfunc(bmp)
    if trans=='L':
        if bits==24: 
            f=mirror24L
        elif bits==8: 
            f=mirror8L
    elif trans=='R':
        if bits==24: 
            f=mirror24R
        elif bits==8: 
            f=mirror8R
    elif trans=='F':
        if bits==24: 
            f=flip24
        elif bits==8: 
            f=flip8
    for v in itercirclepartvertlineedge(r):
        x1,x2=mirror(x,v[0])
        y1,y2=mirror(y,v[1])
        k=getxcharcount(bmp)
        s1,e1,s2,e2=c(bmp,x1,y2),c(bmp,x1,y1)+k,c(bmp,x2,y2),c(bmp,x2,y1)+k
        f()
    
def mirrorleftincircregion(bmp:array,x:int,y:int,r:int):
    """Mirrors the top left of a circular region defined by centerpoint (x,y) and radius r

    Args:
        bmp   : unsigned byte array with bmp format
        x,y,r : center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    horitransformincircregion(bmp,x,y,r,'L')

def mirrorrightincircregion(bmp:array,x:int,y:int,r:int):
    """Mirrors the right half of a circular region defined by  centerpoint (x,y) and radius r

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified byte unsigned array

    """
    horitransformincircregion(bmp,x,y,r,'R')

def flipvertcircregion(bmp:array,x:int,y:int,r:int):
    """Does a vertical flip of a circular region defined by centerpoint (x,y) and radius r

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    verttransformincircregion(bmp,x,y,r,'F')

@entirecircleinboundary
def verttransformincircregion(bmp:array,x:int,y:int,r:int,trans:str):
    """Applies a vertical transform to circular region with a center x,y with a radius r
        
    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region
        trans: single letter transform code
               'T' mirror top 'B' mirror bottom 'F' flip
        
    Returns:
        byref modified unsigned byte array

    """
    def mirrorT(): 
        bmp[s2:e2]=bmp[s1:e1]
    def mirrorB(): 
        bmp[s1:e1]=bmp[s2:e2]
    def flip(): 
        bmp[s1:e1],bmp[s2:e2]=bmp[s2:e2],bmp[s1:e1]
    if trans=='T': 
        f=mirrorT
    elif trans=='B': 
        f=mirrorB
    elif trans=='F': 
        f=flip
    c=getcomputeBMPoffsetwithheaderfunc(bmp)
    for v in itercirclepartlineedge(r):
        x1,x2=mirror(x,v[0])
        y1,y2=mirror(y,v[1])
        s1,e1,s2,e2=c(bmp,x1,y1),c(bmp,x2,y1),c(bmp,x1,y2),c(bmp,x2,y2)
        f()
    
def mirrortopincircregion(bmp:array,x:int,y:int,r:int):
    """Mirrors the top half of a circular region defined by centerpoint (x,y) and radius r

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    verttransformincircregion(bmp,x,y,r,'T')

def mirrorbottomincircregion(bmp:array,x:int,y:int,r:int):
    """Mirrors the bottom half of a circular region defined by centerpoint (x,y) and radius r

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    verttransformincircregion(bmp,x,y,r,'B')

def mirrortopleftincircregion(bmp:array,x:int,y:int,r:int):
    """Mirrors the top left  of a circular region defined by centerpoint (x,y) and radius r
        
    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    mirrorleftincircregion(bmp,x,y,r)
    mirrortopincircregion(bmp,x,y,r)

def mirrortoprightincircregion(bmp:array,x:int,y:int,r:int):
    """Mirrors the top right of a circular region defined by centerpoint (x,y) and radius r
        
    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    mirrorrightincircregion(bmp,x,y,r)
    mirrortopincircregion(bmp,x,y,r)

def mirrorbottomleftincircregion(bmp:array,x:int,y:int,r:int):
    """Mirrors the bottom left of a circular region defined by centerpoint (x,y) and radius r

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    mirrorleftincircregion(bmp,x,y,r)
    mirrorbottomincircregion(bmp,x,y,r)

def mirrorbottomrightincircregion(bmp:array,x:int,y:int,r:int):
    """Mirrors the bottom right of a circular region defined by centerpoint (x,y) and radius r

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    mirrorrightincircregion(bmp,x,y,r)
    mirrorbottomincircregion(bmp,x,y,r)

@func24bitonlyandentirecircleinboundary  
def vertbrightnessgrad2circregion(bmp:array,x:int,y:int,r:int,lumrange:list):
    """Applies a vertical brightness gradient adjustment with lumrange
        to a circular region with a center x,y with a radius r
        
    Args:
        bmp     : unsigned byte array with bmp format
        x,y,r   : center (x,y) and radius r of region        
        lumrange: [byte,byte] defines range of luminosity
        
    Returns:
        byref modified unsigned byte array

    """
    c,f=getcomputeBMPoffsetwithheaderfunc(bmp),applybrightnessadjtoBGRbuf
    l,dl,b,=lumrange[0],(lumrange[1]-lumrange[0])/(2*r),y-r
    for v in itercirclepartlineedge(r):
        x1,x2=mirror(x,v[0])
        y1,y2=mirror(y,v[1])
        l1,l2=l+(y1-b)*dl,l+(y2-b)*dl
        s1,e1,s2,e2=c(bmp,x1,y1),c(bmp,x2,y1),c(bmp,x1,y2),c(bmp,x2,y2)
        bmp[s1:e1],bmp[s2:e2]=f(bmp[s1:e1],l1),f(bmp[s2:e2],l2)

@func24bitonlyandentirecircleinboundary     
def horibrightnessgrad2circregion(bmp:array,x:int,y:int,r:int,lumrange:list):
    """Applies a horizontal brightness gradient adjustment with lumrange
        to a circular region with a center x,y with a radius r
        
    Args:
        bmp     : unsigned byte array with bmp format
        x,y,r   : center (x,y) and radius r of region
        lumrange: [byte,byte] defines range of luminosity
        
    Returns:
        byref modified unsigned byte array

    """

    f=applybrightnessadjtoBGRbuf
    l,dl,b=lumrange[0],(lumrange[1]-lumrange[0])/(2*r),x-r
    for v in itercirclepartvertlineedge(r):
        x1,x2=mirror(x,v[0])
        y1,y2=mirror(y,v[1])
        applyfuncwithparam2vertBMPbitBLTget(bmp,x1,y1,y2,f,l+(x1-b)*dl)
        if x1!=x2: 
            applyfuncwithparam2vertBMPbitBLTget(bmp,x2,y1,y2,f,l+(x2-b)*dl)

@intcircleparam    
def outlinecircregion(bmp:array,x:int,y:int,r:int):
    """Outlines the area within a circular region defined by centerpoint (x,y) and radius r

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified byte array

    """
    bits,c=bmp[bmpcolorbits],getcomputeBMPoffsetwithheaderfunc(bmp)
    if entirecircleisinboundary(x,y,-1,getmaxx(bmp),-1,getmaxy(bmp),r):
        for v in itercirclepartlineedge(r):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            s1,e1,s2,e2=c(bmp,x1,y1),c(bmp,x2,y1),c(bmp,x1,y2),c(bmp,x2,y2)
            if bits==24:
                bmp[s1:e1]=array('B',xorvect(bmp[s1:e1],bmp[s1+3:e1+3]))
                if y1!=y2: 
                    bmp[s2:e2]=array('B',xorvect(bmp[s2:e2],bmp[s2+3:e2+3]))
            else:
                bmp[s1:e1]=array('B',xorvect(bmp[s1:e1],bmp[s1+1:e1+1]))
                if y1!=y2: 
                    bmp[s2:e2]=array('B',xorvect(bmp[s2:e2],bmp[s2+1:e2+1]))
    else:
        xmax,ymax=getmaxx(bmp),getmaxy(bmp)
        for v in itercirclepartlineedge(r):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            x1,x2=setmin(x1,0),setmax(x2,xmax-1)
            if isinrange(y2,ymax,-1):
                s2,e2=c(bmp,x1,y2),c(bmp,x2,y2)
                if bits==24:  
                    bmp[s2:e2]=array('B',xorvect(bmp[s2:e2],bmp[s2+3:e2+3]))
                else: 
                    bmp[s2:e2]=array('B',xorvect(bmp[s2:e2],bmp[s2+1:e2+1]))
            if isinrange(y1,ymax,-1) and y2!=y1:
                s1,e1=c(bmp,x1,y1),c(bmp,x2,y1)
                if bits==24: 
                    bmp[s1:e1]=array('B',xorvect(bmp[s1:e1],bmp[s1+3:e1+3]))
                else: 
                    bmp[s1:e1]=array('B',xorvect(bmp[s1:e1],bmp[s1+1:e1+1]))

def monocircle(bmp:array,x:int,y:int,r:int):
    """Applies a monochrome filter to a circular region defined by centerpoint (x,y) and radius r

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified byte array

    """
    applynoparam24bitfunctocircregion(bmp,x,y,r,monochromefiltertoBGRbuf)

def colorfiltercircregion(bmp:array,x:int,y:int,r:int,rgbfactors:list):
    """Applies a color filter defined by rgbfactors to a circular region
        defined by centerpoint (x,y) and radius r

    Args:
        bmp       : unsigned byte array with bmp format
        x,y,r     : center (x,y) and radius r of region
        rgbfactors: [r,g,b]  range of r,g and b are 0 min to 1 max
        
    Returns:
        byref modified byte array

    """
    apply24bitfunctocircregion(bmp,x,y,r,colorfiltertoBGRbuf,rgbfactors)

def gammacorrectcircregion(bmp:array,x:int,y:int,r:int,gamma:float):
    """Applies gamma correction gamma to a circular region defined by centerpoint (x,y) and radius r 
    
    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region
        gamma: float value of gamma adjustment
        
    Returns:
        byref modified byte array

    """
    apply24bitfunctocircregion(bmp,x,y,r,gammaBGRbuf,gamma)

def brightnessadjcircregion(bmp:array,x:int,y:int,r:int,percentadj:float):
    """Applies brightness adjustment percentadj to a circular region defined by centerpoint (x,y) and radius r 

    Args:
        bmp       : unsigned byte array with bmp format
        x,y,r     : center (x,y) and radius r of region
        percentadj: float percent brightness adjustment
        
    Returns:
        byref modified unsigned byte array

    """
    apply24bitfunctocircregion(bmp,x,y,r,applybrightnessadjtoBGRbuf,percentadj)

def invertbitsincircregion(bmp:array,x:int,y:int,r:int):
    """Inverts the bits in a circular region defined by centerpoint (x,y) and radius r 

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r of region

    Returns:
        byref modified unsigned byte array

    """
    applynoparamfunctocircregion(bmp,x,y,r,invertbitsinbuffer)

def circlevec(bmp:array,v:list,r:int,color:int,isfilled:bool=None):
    """Draws a circle defined by centerpoint v and radius r with a given color

    Args:
        bmp     : unsigned byte array with bmp format
        v       : (x,y) coordinates of circular region
        r       : radius of circular region
        color   : color of the circle
        isfilled: toggles if circle is filled
        
    Returns:
        byref modified unsigned byte array

    """
    v=roundvect(v)
    circle(bmp,v[0],v[1],r,color,isfilled)

def filledcircle(bmp:array,x:int,y:int,r:int,color:int):
    """Draws a filled circle defined by centerpoint (x,y) and radius r with a given color

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r
        color: color of the circle
        
    Returns:
        byref modified unsigned byte array

    """
    bits=bmp[bmpcolorbits]
    if bits<8:
        for v in itercirclepartlineedge(r):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            horiline(bmp,y1,x1,x2,color)
            horiline(bmp,y2,x1,x2,color)
    else:
        m=getmaxxy(bmp)
        if bits==24:
            for v in itercirclepartlineedge(r):
                x1,x2=mirror(x,v[0])
                y1,y2=mirror(y,v[1])
                x1,x2=setmin(x1,0),setmax(x2,m[0]-1)
                dx,ymax=x2-x1+1,m[1]
                rgb=int2RGBlist(color)
                colorbuf=array('B',[rgb[2],rgb[1],rgb[0]]*dx)
                lbuf=dx*3
                if isinrange(y2,ymax,-1):
                    s=compute24bitBMPoffsetwithheader(bmp,x1,y2)
                    bmp[s:s+lbuf]=colorbuf
                if isinrange(y1,ymax,-1):
                    s=compute24bitBMPoffsetwithheader(bmp,x1,y1)
                    bmp[s:s+lbuf]=colorbuf
        elif bits==8:
            for v in itercirclepartlineedge(r):
                x1,x2=mirror(x,v[0])
                y1,y2=mirror(y,v[1])
                x1,x2=setmin(x1,0),setmax(x2,m[0]-1)
                dx,ymax=x2-x1+1,m[1]
                colorbuf=array('B',[color&0xff]*dx)
                if isinrange(y2,ymax,-1):
                    s=compute8bitBMPoffsetwithheader(bmp,x1,y2)
                    bmp[s:s+dx]=colorbuf
                if isinrange(y1,ymax,-1):
                    s=compute8bitBMPoffsetwithheader(bmp,x1,y1)
                    bmp[s:s+dx]=colorbuf

def circle(bmp:int,x:int,y:int,r:int,color:int,isfilled:bool=None):
    """Draws a circle defined by centerpoint (x,y) and radius r with a given color

    Args:
        bmp     : unsigned byte array with bmp format
        x,y,r   : center (x,y) and radius r
        color   : color of the circle
        isfilled: toggles if circle is filled
        
    Returns:
        byref modified unsigned byte array

    """
    if isfilled: 
        filledcircle(bmp,x,y,r,color)
    else:
        m,bits,c=getmaxxy(bmp),bmp[bmpcolorbits],getcomputeBMPoffsetwithheaderfunc(bmp)
        dobndcheck=not entirecircleisinboundary(x,y,-1,m[0],-1,m[1],r)
        if bits==24:
            color=int2BGRarr(color)
            if dobndcheck:
                for p in itercircle(x,y,r):
                    px,py=p[0],p[1]
                    if isinBMPrectbnd(bmp,px,py):
                        s=c(bmp,px,py)
                        bmp[s:s+3]=color
            else:
                for p in itercirclepart(r):
                    x1,x2=mirror(x,p[0])
                    y1,y2=mirror(y,p[1])
                    x3,x4=mirror(x,p[1])
                    y3,y4=mirror(y,p[0])
                    s1,s2,s3,s4,s5,s6,s7,s8=c(bmp,x1,y1),c(bmp,x2,y2),c(bmp,x1,y2),c(bmp,x2,y1),c(bmp,x3,y3),c(bmp,x4,y4),c(bmp,x3,y4),c(bmp,x4,y3)
                    bmp[s1:s1+3]=bmp[s2:s2+3]=bmp[s3:s3+3]=bmp[s4:s4+3]=bmp[s5:s5+3]=bmp[s6:s6+3]=bmp[s7:s7+3]=bmp[s8:s8+3]=color
        elif bits==8:
            if dobndcheck:
                for p in itercircle(x,y,r):
                    px,py=p[0],p[1]
                    if isinBMPrectbnd(bmp,px,py): 
                        bmp[c(bmp,px,py)]=color
            else:
                for p in itercirclepart(r):
                    x1,x2=mirror(x,p[0])
                    y1,y2=mirror(y,p[1])
                    bmp[c(bmp,x1,y1)]=bmp[c(bmp,x2,y2)]=bmp[c(bmp,x1,y2)]=bmp[c(bmp,x2,y1)]=color
        else:
            for p in itercircle(x,y,r): 
                plotxybit(bmp,p[0],p[1],color)

def thickcircle(bmp:array,x:int,y:int,r:int,penradius:int,color:int):
    """Draws a thick circle defined by centerpoint (x,y) and radius r 
        with a given color using a pen with radius penradius

    Args:
        bmp      : unsigned byte array with bmp format
        x,y,r    : center (x,y) and radius r
        penradius: radius of round pen 
        color    : color of the circle
        
    Returns:
        byref modified unsigned byte array

    """
    for p in itercircle(x,y,r): 
        circle(bmp,p[0],p[1],penradius,color,True)

def gradthickcircle(bmp:array,x:int,y:int,radius:int,penradius:int,lumrange:list,RGBfactors:list):
    """Draws a thick circle with gradient lumrange 
        defined by centerpoint (x,y) and radius r 
        using a pen with radius penradius 
        and color defined by RGBfactors

    Args:
        bmp       : unsigned byte array with bmp format
        x,y,r     : center (x,y) and radius r
        penradius : radius of round pen 
        lumrange  : [byte,byte] range of the gradient
        rgbfactors: [r,g,b]  all values in list are ufloat
                    range of r, g and b are 0 min to 1 max
        
    Returns:
        byref modified unsigned byte array

    """
    lum1,lumrang=range2baseanddelta(lumrange)
    for i in range(penradius,0,-1):
        c=colormix(int(lum1+(lumrang*i/penradius)),RGBfactors)
        if bmp[bmpcolorbits]!=24:
            c=matchRGBtopal(int2RGBarr(c),getallRGBpal(bmp))
        thickcircle(bmp,x,y,radius,i,c)

def gradcircle(bmp:array,x:int,y:int,radius:int,lumrange:list,RGBfactors:list):
    """Draws a filled circle with gradient lumrange defined by centerpoint (x,y) 
        and radius r and color defined by RGBfactors

    Args:
        bmp       : unsigned byte array with bmp format
        x,y,r     : center (x,y) and radius r
        lumrange  : [byte,byte] range of the gradient
        rgbfactors: [r,g,b]  all values in list are ufloat
                    range of r, g and b are 0 min to 1 max
        
    Returns:
        byref modified unsigned byte array

    """
    lum1,lumrang=range2baseanddelta(lumrange)
    for r in range(radius-1,0,-1):
        c=colormix(int(lum1+(lumrang*r/radius)),RGBfactors)
        if bmp[bmpcolorbits]!=24:
            c=matchRGBtopal(int2RGBarr(c),getallRGBpal(bmp))
        thickcircle(bmp,x,y,r,2,c)

def thickellipserot(bmp:array,x:int,y:int,b:int,a:int,degrot:float,
                    penradius:int,color:int):
    """Draws an thick ellipse with a defined pen radius
        defined by centerpoint (x,y) and major and minor axis (b,a) 
        and rotated by degrot degrees

    Args:
        bmp       : unsigned byte array with bmp format
        x,y       : center of ellipse
        b,a       : major amd minor axis
        degrot    : rotation of the ellipse in degrees
        penradius : defines the thickness of the pen
        color     : color of the ellipse

    Returns:
        byref modified byte array

    """
    for p in iterellipserot(x,y,b,a,degrot): 
        circle(bmp,p[0],p[1],penradius,color,True)

def gradthickellipserot(bmp:array,x:int,y:int,b:int,a:int,degrot:float,
                        penradius:int,lumrange:list,RGBfactors:list):
    """Draws an thick ellipse with a defined pen radius
        defined by centerpoint (x,y) and major and minor axis (b,a) 
        and rotated by degrot degrees with a gradient fill 

    Args:
        bmp       : unsigned byte array with bmp format
        x,y       : center of ellipse
        b,a       : major amd minor axis
        degrot    : rotation of the ellipse in degrees
        penradius : defines the thickness of the pen
        lumrange  : [byte:byte] 
                    controls the range of the gradient
        rgbfactors: [r,g,b]  all values in list are ufloat
                    range of r, g and b are 0 min to 1 max

    Returns:
        byref modified byte array

    """                        
    lum1,lumrang=range2baseanddelta(lumrange)
    for i in range(penradius,0,-1):
        c=colormix(int(lum1+(lumrang*i/penradius)),RGBfactors)
        if bmp[bmpcolorbits]!=24:c=matchRGBtopal(int2RGBarr(c),getallRGBpal(bmp))
        thickellipserot(bmp,x,y,b,a,degrot,i,c)

def filledellipse(bmp:array,x:int,y:int,b:int,a:int,color:int):
    """Draws an filled ellipse defined by centerpoint (x,y) and major and minor axis (b,a) 
        
    Args:
        bmp  : unsigned byte array with bmp format
        x,y  : center of ellipse
        b,a  : major amd minor axis
        color: color of the ellipse

    Returns:
        byref modified byte array

    """
    bits=bmp[bmpcolorbits]
    if bits<8:
        for v in iterellipsepart(b,a):
            x1,x2=mirror(x,v[0])
            y1,y2=mirror(y,v[1])
            horiline(bmp,y1,x1,x2,color)
            horiline(bmp,y2,x1,x2,color)
    else:
        m=getmaxxy(bmp)
        if bits==24:
            for v in iterellipsepart(b,a):
                x1,x2=mirror(x,v[0])
                y1,y2=mirror(y,v[1])
                x1,x2=setmin(x1,0),setmax(x2,m[0]-1)
                dx,ymax=x2-x1+1,m[1]
                rgb=int2RGBlist(color)
                colorbuf=array('B',[rgb[2],rgb[1],rgb[0]]*dx)
                lbuf=dx*3
                if isinrange(y2,ymax,-1):
                    s=compute24bitBMPoffsetwithheader(bmp,x1,y2)
                    bmp[s:s+lbuf]=colorbuf
                if isinrange(y1,ymax,-1):
                    s=compute24bitBMPoffsetwithheader(bmp,x1,y1)
                    bmp[s:s+lbuf]=colorbuf
        elif bits==8:
            for v in iterellipsepart(b,a):
                x1,x2=mirror(x,v[0])
                y1,y2=mirror(y,v[1])
                x1,x2=setmin(x1,0),setmax(x2,m[0]-1)
                dx,ymax=x2-x1+1,m[1]
                colorbuf=array('B',[color&0xff]*dx)
                if isinrange(y2,ymax,-1):
                    s=compute8bitBMPoffsetwithheader(bmp,x1,y2)
                    bmp[s:s+dx]=colorbuf
                if isinrange(y1,ymax,-1):
                    s=compute8bitBMPoffsetwithheader(bmp,x1,y1)
                    bmp[s:s+dx]=colorbuf

def ellipse(bmp:array,x:int,y:int,b:int,a:int,color:int,isfilled:bool=None):
    """Draws an ellipse defined by centerpoint (x,y) and major and minor axis (b,a) 
        
    Args:
        bmp     : unsigned byte array with bmp format
        x,y     : center of ellipse
        b,a     : major amd minor axis
        color   : color of the ellipse
        isfilled: True -> filled ellipse  
                 False -> one pixel thick ellipse

    Returns:
        byref modified unsigned byte array

    """
    if isfilled: 
        filledellipse(bmp,x,y,b,a,color)
    else:
        m,bits,c=getmaxxy(bmp),bmp[bmpcolorbits],getcomputeBMPoffsetwithheaderfunc(bmp)
        dobndcheck=not entireellipseisinboundary(x,y,-1,m[0],-1,m[1],b,a)
        if bits==24:
            color=int2BGRarr(color)
            if dobndcheck:
                for p in iterellipse(x,y,b,a):
                    px,py=p[0],p[1]
                    if isinBMPrectbnd(bmp,px,py):
                        s=c(bmp,px,py)
                        bmp[s:s+3]=color
            else:
                for p in iterellipse(x,y,b,a):
                    s=c(bmp,p[0],p[1])
                    bmp[s:s+3]=color
        elif bits==8:
            if dobndcheck:
                for p in iterellipse(x,y,b,a):
                    px,py=p[0],p[1]
                    if isinBMPrectbnd(bmp,px,py): 
                        bmp[c(bmp,px,py)]=color
            else:
                for p in iterellipse(x,y,b,a):
                    bmp[c(bmp,p[0],p[1])]=color
        else:
            for p in iterellipse(x,y,b,a): 
                plotxybit(bmp,p[0],p[1],color)

def gradellipse(bmp:array,x:int,y:int,b:int,a:int,lumrange:list,RGBfactors:list):
    """Draws an ellipical gradient defined by centerpoint (x,y) and major and minor axis (b,a) 
        
    Args:
        bmp       : An unsigned byte array with bmp format
        x,y       : center of ellipse
        b,a       : major amd minor axis
        lumrange  : [byte:byte] controls the range of the gradient
        rgbfactors: [r,g,b]  all values in list are ufloat
                    range of r, g and b are 0 min to 1 max

    Returns:
        byref modified unsigned byte array

    """     
    lum1,lumrang=range2baseanddelta(lumrange)
    r=iif(a>b,a,b)
    a-=r
    b-=r
    for i in range(r,0,-1):
        c=colormix(int(lum1+(lumrang*i/r)),RGBfactors)
        if bmp[bmpcolorbits]!=24:c=matchRGBtopal(int2RGBarr(c),getallRGBpal(bmp))
        ellipse(bmp,x,y,b+i,a+i,c,True)
        
@intcircleparam
def drawarc(bmp:array,x:int,y:int,r:int,startdegangle:float,enddegangle:float,
            color:int,showoutline:bool,fillcolor:int,isfilled:bool):
    """Draws an arc centered at point (x,y) with radius r and specified start and end angles in degrees
        
    Args:
        bmp         : unsigned byte array with bmp format
        x,y,r       : defines a circle that contain the arc
        color       : color of arc
        showoutline : True -> draw arc outline
        fillcolor   : color of arc filling
        isfilled    : True -> set area inside arc to fillcolor

    Returns:
        byref modified unsigned byte array

    """
    av=arcvert(x,y,r,startdegangle,enddegangle,showoutline)
    for p in av: 
        plotxybit(bmp,p[0],p[1],color)
    if isfilled: 
        fillboundary(bmp,fillpolydata(av,getmaxx(bmp),getmaxy(bmp)),fillcolor)

def rectangle(bmp:array,x1:int,y1:int,x2:int,y2:int,color:int):
    """Draws a rectangle of a given color

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle        
        color      : color of the rectangle
        
    Returns:
        byref modified unsigned byte array

    """
    plotpoly(bmp,recvert(x1,y1,x2,y2),color)

@entirerectinboundary    
def filledrect(bmp:array,x1:int,y1:int,x2:int,y2:int,color:int):
    """Draws a filled rectangle of a given color

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        color      : color of the rectangle
        
    Returns:
        byref modified unsigned byte array

    """
    bits=bmp[bmpcolorbits]
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    if bits not in [8,24]:
        y2+=1
        for y in range(y1,y2): 
            horiline(bmp,y,x1,x2,color)
    else:
        dx,r,rgb,c=x2-x1+1,getxcharcount(bmp),int2RGB(color),getcomputeBMPoffsetwithheaderfunc(bmp)
        if bits==24: buf=array('B',[rgb[2],rgb[1],rgb[0]]*dx)
        elif bits==8: buf=array('B',[matchRGBtopal(rgb,getallRGBpal(bmp))]*dx)
        offset,lim,bufsize,fsize=c(bmp,x1,y2),c(bmp,x2,y1),len(buf),getfilesize(bmp)
        while (offset<=lim) and ((offset+bufsize)<=fsize):
            bmp[offset:offset+bufsize]=buf
            offset+=r

def beziercurve(bmp:array,pntlist:list,penradius:int,color:int):
    """Draws a bezier curve of a given color and thickness

    Args:
        bmp      : unsigned byte array with bmp format
        pntlist  : [(x,y)...] list of control points
        penradius: radius of pen in pixels
        color    : color of bezier curve
        
    Returns:
        byref modified unsigned byte array

    """
    for v in iterbeziercurve(pntlist): 
        roundpen(bmp,v,penradius,color)

def bspline(bmp:array,pntlist:list,penradius:int,color:int,isclosed:bool,curveback:bool):
    """Draws a bspline of a given color and thickness

    Args:
        bmp      : An unsigned byte array with bmp format
        pntlist  : [(x,y)...] list of control points
        penradius: radius of pen in pixels
        color    : color of bezier curve
        isclosed : True means the curve is closed 
        curveback: True means extra computation
                   for curve to loop back on itself                 
    Returns:
        byref modified unsigned byte array

    """
    for v in iterbspline(pntlist,isclosed,curveback): 
        roundpen(bmp,v,penradius,color)

def plotrotated8bitpattern(bmp:array,x:int,y:int,bitpattern:list,scale:int,pixspace:int,color:int):
    """Draws a 8-bit pattern with the bits rotated

    Args:
        bmp       : unsigned byte array with bmp format
        x,y       : where to draw the pattern
        bitpattern: list of bytes that make a pattern
        scale     : control how big the pattern is
        pixspace  : space between each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array

    """
    inc=scale-1-pixspace
    for bits in bitpattern:
        ox,mask=x,128
        bits=rotatebits(bits)
        while mask>0:
            if (mask & bits)>0:
                if scale==1 or inc<=0: 
                    plotxybit(bmp,x,y,color)
                else: 
                    filledrect(bmp,x,y,x+inc,y+inc,color)
            mask=mask>>1
            x+=scale
        y+=scale
        x=ox

def plot8bitpattern(bmp:array,x:int,y:int,bitpattern:list,scale:int,pixspace:int,color:int):
    """Draws a 8-bit pattern

    Args:
        bmp       : unsigned byte array with bmp format
        x,y       : where to draw the pattern
        bitpattern: list of bytes that make a pattern
        scale     : control how big the pattern is
        pixspace  : space between each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array

    """    
    inc=scale-1-pixspace
    for bits in bitpattern:
        ox,mask=x,128
        while mask>0:
            if (mask & bits)>0:
                if scale==1 or inc<=0: 
                    plotxybit(bmp,x,y,color)
                else: 
                    filledrect(bmp,x,y,x+inc,y+inc,color)
            mask=mask>>1
            x+=scale
        y+=scale
        x=ox

def plot8bitpatternupsidedown(bmp:array,x:int,y:int,bitpattern:list,scale:int,pixspace:int,color:int):
    """Draws a 8-bit pattern upsidedown

    Args:
        bmp       : unsigned byte array with bmp format
        x,y       : where to draw the pattern
        bitpattern: list of bytes that make a pattern
        scale     : control how big the pattern is
        pixspace  : space between each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array

    """
    inc=scale-1-pixspace
    i=len(bitpattern)-1
    while i>-1:
        bits=bitpattern[i]
        ox,mask=x,128
        while mask>0:
            if (mask & bits)>0:
                if scale==1 or inc<=0: 
                    plotxybit(bmp,x,y,color)
                else: 
                    filledrect(bmp,x,y,x+inc,y+inc,color)
            mask=mask>>1
            x+=scale
        y+=scale
        x=ox
        i-=1

def plot8bitpatternsideway(bmp:array,x:int,y:int,bitpattern:list,scale:int,pixspace:int,color:int):
    """Draws a 8-bit pattern sideways

    Args:
        bmp       : unsigned byte array with bmp format
        x,y       : where to draw the pattern
        bitpattern: list of bytes that make a pattern
        scale     : control how big the pattern is
        pixspace  : space between each bit in pixels
        color     : color of the pattern

    Returns:
        byref modified unsigned byte array

    """
    inc=scale-1-pixspace
    for bits in bitpattern:
        oy,mask=y,128
        while mask>0:
            if (mask & bits)>0:
                if scale==1 or inc<=0: 
                    plotxybit(bmp,x,y,color)
                else: 
                    filledrect(bmp,x,y,x+inc,y+inc,color)
            mask=mask>>1
            y-=scale
        x+=scale
        y=oy

def plotstringfunc(bmp:array,x:int,y:int,str2plot:str,scale:int,pixspace:int,
        spacebetweenchar:int,color:int,fontbuf:list,orderfunc,fontrenderfunc):
    """Draws a string

    Args:
        bmp             : unsigned byte array with bmp format
        x,y             : where to draw the string
        str2plot        : string to draw
        scale           : control how big the font is
        pixspace        : space between each bit in pixels
        spacebetweenchar: space between the characters
        color           : color of the font
        fontbuf         : the font ...see fonts.py
        orderfunc       : function that enumerates each char in string
        fontrenderfunc  : function that renders the font
        
    Returns:
        byref modified unsigned byte array

    """        
    if spacebetweenchar==0:spacebetweenchar=1
    ox,xstep,ypixels=x,(scale<<3)+spacebetweenchar,fontbuf[0] #x factor 8 since 8 bits in byte
    ystep=ypixels*scale+spacebetweenchar #possible to have 8x16 chars
    for c in orderfunc(str2plot):
        if c=='\n':
            y+=ystep
            x=ox
        elif c=='\t': 
            x+=xstep<<2
        else:
            fontrenderfunc(bmp,x,y,getcharfont(fontbuf,c),scale,pixspace,color)
            x+=xstep

def plotstring(bmp:array,x:int,y:int,str2plot:str,scale:int,
                pixspace:int,spacebetweenchar:int,color:int,fontbuf:list):
    """Draws a string

    Args:
        bmp             : unsigned byte array with bmp format
        x,y             : where to draw the string
        str2plot        : string to draw
        scale           : control how big the font is
        pixspace        : space between each bit in pixels
        spacebetweenchar: space between the characters
        color           : color of the font
        fontbuf         : the font ...see fonts.py
        
    Returns:
        byref modified unsigned byte array

    """
    plotstringfunc(bmp,x,y,str2plot,scale,pixspace,spacebetweenchar,color,fontbuf,enumletters,plot8bitpattern)

def plotstringupsidedown(bmp,x,y,str2plot,scale,pixspace,spacebetweenchar,color,fontbuf):
    """Draws a string upsidedown

    Args:
        bmp             : unsigned byte array with bmp format
        x,y             : where to draw the string
        str2plot        : string to draw
        scale           : control how big the font is
        pixspace        : space between each bit in pixels
        spacebetweenchar: space between the characters
        color           : color of the font
        fontbuf         : the font ...see fonts.py
        
    Returns:
        byref modified unsigned byte array

    """
    plotstringfunc(bmp,x,y,str2plot,scale,pixspace,spacebetweenchar,color,fontbuf,enumletters,plot8bitpatternupsidedown)

def plotreversestring(bmp,x,y,str2plot,scale,pixspace,spacebetweenchar,color,fontbuf):
    """Draws a string reversed

    Args:
        bmp             : unsigned byte array with bmp format
        x,y             : where to draw the string
        str2plot        : string to draw
        scale           : control how big the font is
        pixspace        : space between each bit in pixels
        spacebetweenchar: space between the characters
        color           : color of the font
        fontbuf         : the font ...see fonts.py
        
    Returns:
        byref modified unsigned byte array

    """
    plotstringfunc(bmp,x,y,str2plot,scale,pixspace,spacebetweenchar,color,fontbuf,enumreverseletters,plotrotated8bitpattern)

def plotstringsideway(bmp,x,y,str2plot,scale,pixspace,spacebetweenchar,color,fontbuf):
    """Draws a string sideways

    Args:
        bmp             : unsigned byte array with bmp format
        x,y             : where to draw the string
        str2plot        : string to draw
        scale           : control how big the font is
        pixspace        : space between each bit in pixels
        spacebetweenchar: space between the characters
        color           : color of the font
        fontbuf         : the font ...see fonts.py
        
    Returns:
        byref modified unsigned byte array

    """
    if spacebetweenchar==0:spacebetweenchar=1
    oy,xstep,ypixels=y,(scale<<3)+spacebetweenchar,fontbuf[0]
    ystep=ypixels*scale+spacebetweenchar
    for c in enumletters(str2plot):
        if c=='\n':
            x+=ystep #we swap x and y since sideways
            y=oy
        elif c=='\t': y-=xstep<<2 #we swap x and y since sideways
        else:
            plot8bitpatternsideway(bmp,x,y,getcharfont(fontbuf,c),scale,pixspace,color)
            y-=xstep

def plotstringvertical(bmp,x,y,str2plot,scale,pixspace,spacebetweenchar,color,fontbuf):
    """Draws a string vertically

    Args:
        bmp             : unsigned byte array with bmp format
        x,y             : where to draw the string
        str2plot        : string to draw
        scale           : control how big the font is
        pixspace        : space between each bit in pixels
        spacebetweenchar: space between the characters
        color           : color of the font
        fontbuf         : the font ...see fonts.py
        
    Returns:
        byref modified unsigned byte array

    """
    if spacebetweenchar==0:spacebetweenchar=1
    oy,ypixels=y,fontbuf[0]
    xstep,ystep=(scale<<3)+spacebetweenchar,ypixels*scale+spacebetweenchar
    for c in enumletters(str2plot):
        if c=='\n':
            x+=xstep
            y=oy
        elif c=='\t': y+=ystep<<2
        else:
            plot8bitpattern(bmp,x,y,getcharfont(fontbuf,c),scale,pixspace,color)
            y+=ystep

def fillboundary(bmp:array,bndfilldic:dict,color:int):
    """Draws lines in a boundary to fill it

    Args:
        bmp        : unsigned byte array with bmp format
        bndfilldic : boundary dictionary
        color      : color of bezier curve

    Returns:
        byref modified unsigned byte array

    """
    for y in bndfilldic:
        yint=len(bndfilldic[y])
        if yint==1: 
            plotxybit(bmp,bndfilldic[y][0],y,color)
        else:
            for j in range(1,yint):
                x1,x2=bndfilldic[y][j-1],bndfilldic[y][j]
                horiline(bmp,y,x1,x2,color)

def plotpolyfill(bmp:array,vertlist:list,color:int):
    """Draws a filled polygon with a given color

    Args:
        bmp      : unsigned byte array with bmp format
        vertlist : [(x,y)...] list of vertices
        color    : color of bezier curve

    Returns:
        byref modified unsigned byte array

    """
    fillboundary(bmp,fillpolydata(polyboundary(vertlist),getmaxx(bmp),getmaxy(bmp)),color)

def thickplotpoly(bmp:array,vertlist:list,penradius:int,color:int):
    """Draws a polygon of a given color and thickness

    Args:
        bmp      : unsigned byte array with bmp format
        vertlist : [(x,y)...] list of vertices
        penradius: radius of pen in pixels
        color    : color of bezier curve

    Returns:
        byref modified unsigned byte array

    """
    vertcount=len(vertlist)
    for i in range(0,vertcount):
        if i>0: 
            thickroundline(bmp,vertlist[i-1],vertlist[i],penradius,color)
    thickroundline(bmp,vertlist[0],vertlist[vertcount-1],penradius,color)

def gradthickplotpoly(bmp:array,vertlist:list,penradius:int,lumrange:list,RGBfactors:list):
    """Draws a polygon of a given gradient and thickness

    Args:
        bmp        : unsigned byte array with bmp format
        vertlist   : [(x,y)...] list of vertices
        penradius  : radius of pen in pixels
        lumrange   : [byte,byte] range of the gradient
        RGBfactors : [r:float,g:float,b:float]
                     r,g,b all range in value from 0 to 1 

    Returns:
        byref modified unsigned byte array

    """
    lum1,lumrang=range2baseanddelta(lumrange)
    for i in range(penradius,0,-1):
        c=colormix(int(lum1+(lumrang*i/penradius)),RGBfactors)
        if bmp[bmpcolorbits]!=24:
            c=matchRGBtopal(int2RGBarr(c),getallRGBpal(bmp))
        thickplotpoly(bmp,vertlist,i,c)
        
def plotlines(bmp:array,vertlist:list,color:int):
    """Draws connected lines defined by a list of vertices

    Args:
        bmp      : unsigned byte array with bmp format
        vertlist : [(x:uint,y:uint),...] list of vertices
        color    : color of the lines
        
    Returns:
        byref modified unsigned byte array

    """
    vertcount=len(vertlist)
    for i in range(0,vertcount):
        if i>0: linevec(bmp,vertlist[i-1],vertlist[i],color)

def plotpoly(bmp:array,vertlist:list,color:int):
    """Draws a polygon defined by a list of vertices

    Args:
        bmp      : unsigned byte array with bmp format
        vertlist : [(x:uint,y:uint),...] list of vertices
        color    : color of the lines
        
    Returns:
        byref modified unsigned byte array

    """
    plotlines(bmp,vertlist,color)
    linevec(bmp,vertlist[0],vertlist[len(vertlist)-1],color)

def plotpolylist(bmp,polylist,color):
    """Draws a list of polygons of a given color

    Args:
        bmp      : unsigned byte array with bmp format
        polytlist: [[(x:uint,y:uint),...],...] list of polygons  
        color    : color of the lines
        
    Returns:
        byref modified umsigned byte array

    """
    for poly in polylist: 
        plotpoly(bmp,poly,color)

def plotpolyfillist(bmp:array,sides:list,RGBfactors:list):
    """3D polygon rendering function

    Args:
        bmp        : unsigned byte array with bmp format
        sides      : list of polygons and normals
        RGBfactors : [r:float,g:float,b:float]
                     r,g,b all range in value from 0 to 1 
        
    Returns:
        byref modified unsigned byte array

    """
    polylist,normlist,i=sides[0],sides[1],0
    for poly in polylist:
        c=colormix(int(cosaffin(normlist[i],[0,0,1])*128)+127,RGBfactors)
        if bmp[bmpcolorbits]!=24:
            c=matchRGBtopal(int2RGBarr(c),getallRGBpal(bmp))
        plotpolyfill(bmp,poly,c)
        i=i+1

def plot3d(bmp:array,sides:list,issolid:bool,RGBfactors:list,showoutline:bool,outlinecolor:int):
    """3D rendering function

    Args:
        bmp         : unsigned byte array with bmp format
        sides       : list of polygons and normals
        isolid      : toggles solid render
        RGBfactors  : [r:float,g:float,b:float] r,g,b all range in value from 0 to 1
        showoutine  : toggles  polygon outline
        outlinecolor: color of polygon outline
        
    Returns:
        byref modified unsigned byte array

    """
    if issolid: 
        plotpolyfillist(bmp,sides,RGBfactors)
    if showoutline: 
        plotpolylist(bmp,sides[0],outlinecolor)

def plot3Dsolid(bmp:array,vertandsides:list,issolid:bool,RGBfactors:list,
    showoutline:bool,outlinecolor:int,rotvect:list,transvect3D:list,d:int,transvect:list):
    """3D solid rendering function

    Args:
        bmp         : unsigned byte array with bmp format
        sides       : list of polygons and normals
        isolid      : toggles solid render
        RGBfactors  : [r:float,g:float,b:float] r,g,b all range in value from 0 to 1
        showoutine  : toggles  polygon outline
        outlinecolor: color of polygon outline
        rotvect     : rotation vector
        transvect3D : 3D translation vector
        d           : distance of observer from screen
        transvect   : translatoin vector for screen positioning
        
    Returns:
        byref modified unsigned byte array

    """
    plot3d(bmp,gensides(perspective(vertandsides[0],rotvect,transvect3D,d),transvect,vertandsides[1]),issolid,RGBfactors,showoutline,outlinecolor)

def gradvert(bmp:array,vertlist:list,penradius:int,lumrange:list,RGBfactors:list):
    """Draws a list of 2d vertices as spheres of a given color

    Args:
        bmp       : unsigned byte array with bmp format
        vertlist  : [(x,y),...] list of verticea
        penradius : radius of the spheres
        lumrange  : [byte,byte] controls the gradient
        RGBfactors: (r:float,b:float,g:float) 
                    values of r,g and b -> min 0 to 1 max 
        
    Returns:
        byref modified byte array

    """
    lum1,lumrang=range2baseanddelta(lumrange)
    for i in range(penradius,0,-1):
        c=colormix(int(lum1+(lumrang*i/penradius)),RGBfactors)
        if bmp[bmpcolorbits]!=24:c=matchRGBtopal(int2RGBarr(c),getallRGBpal(bmp))
        for point in vertlist: roundpen(bmp,point,i,c)

@entirerectinboundary        
def xygrid(bmp:array,x1:int,y1:int,x2:int,y2:int,xysteps:list,color:int):
    """Draws a grid

    Args:
        bmp         : unsigned byte array with bmp format
        x1,y1,x2,y2 : sets limits of grid
        xysteps     : [x,y] -> sets the increment in x and y
        color       : sets the color of the grid
        
    Returns:
        byref modified byte array

    """
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    xstep,ystep=xysteps[0],xysteps[1]
    for x in range(x1,x2,xstep): 
        vertline(bmp,x,y1,y2,color)
    for y in range(y1,y2,ystep): 
        horiline(bmp,y,x1,x2,color)

def xygridvec(bmp:array,u:list,v:list,steps:list,gridcolor:int):
    """Draws a grid using (x,y) pairs u and v

    Args:
        bmp         : unsigned byte array with bmp format
        u,v         : (x,y) sets limits of grid
        steps       : [x,y] -> sets the increment in x and y
        color       : sets the color of the grid
        
    Returns:
        byref modified byte array

    """
    xygrid(bmp,u[0],u[1],v[0],v[1],steps,gridcolor)

def numbervert(bmp,vlist,xadj,yadj,scale,valstart,valstep,pixspace,spacebetweenchar,color,fontbuf,suppresszero,suppresslastnum,rightjustify):
    plot,maxv=False,len(vlist)-1
    for v in vlist:
        i=vlist.index(v)
        if i>0:
            plot=True
        else:
            plot=not suppresszero
        if i==maxv and suppresslastnum:
            plot=False
        stval=str(valstart+i*valstep)
        rjust=0
        if rightjustify:
            rjust=(len(stval)-1)<<3
        if plot: 
            plotstring(bmp,v[0]+xadj-rjust,v[1]+yadj,stval,scale,pixspace,spacebetweenchar,color,fontbuf)

def vertlinevert(bmp:array,vlist:list,linelen:int,yadj:int,color:int):
    """Draws vertical line marks at vertices in vlist

    Args:
        bmp    : unsigned byte array with bmp format
        vlist  : [(x,y),...] list of vertices
        linelen: lenght of vertical lines
        yadj   : sets an adjustment of y coordinates
        color  : color of the line
        
    Returns:
        byref modified unsigned byte array

    """
    for v in vlist: 
        vertline(bmp,v[0],v[1],v[1]+linelen+yadj,color)

def horilinevert(bmp:array,vlist:list,linelen:int,xadj:int,color:int):
    """Draws horizontal line marks at vertices in vlist

    Args:
        bmp    : unsigned byte array with bmp format
        vlist  : [(x,y),...] list of vertices
        linelen: lenght of vertical lines
        xadj   : sets an adjustment of x coordinates
        color  : color opf the line
        
    Returns:
        byref modified unsigned byte array

    """
    for v in vlist: 
        horiline(bmp,v[1],v[0],v[0]+linelen+xadj,color)

def XYaxis(bmp,origin,steps,xylimits,xyvalstarts,xysteps,color,textcolor,showgrid,gridcolor):
    hvert=horizontalvert(origin[1],origin[0],xylimits[0],steps[0])
    vvert=verticalvert(origin[0],origin[1],xylimits[1],-steps[1])
    if showgrid:xygridvec(bmp,origin,xylimits,steps,gridcolor)
    drawvec(bmp,origin,[origin[0],xylimits[1]],10,color)
    drawvec(bmp,origin,[xylimits[0],origin[1]],10,color)
    vertlinevert(bmp,hvert,5,-2,color)
    horilinevert(bmp,vvert,-3,0,color)
    font=font8x14
    numbervert(bmp,vvert,-15,-4,1,xyvalstarts[1],xysteps[1],0,0,textcolor,font,False,False,True)
    numbervert(bmp,hvert,-4,7,1,xyvalstarts[0],xysteps[0],0,0,textcolor,font,False,False,False)
    xvalmax,yvalmax=xyvalstarts[0]+(len(hvert)-1)*xysteps[0],xyvalstarts[1]+(len(vvert)-1)*xysteps[1]
    return (origin,steps,xylimits,xyvalstarts,xysteps,(xvalmax,yvalmax))

def userdef2Dcooordsys2screenxy(x,y,lstcooordinfo):
    origin,steps,xylimits,xyvalstarts,xysteps=lstcooordinfo[0],lstcooordinfo[1],lstcooordinfo[2],lstcooordinfo[3],lstcooordinfo[4]
    x,y=[origin[0]+((x-xyvalstarts[0])/xysteps[0])*steps[0],origin[1]-((y-xyvalstarts[0])/xysteps[1])*steps[1]]
    if x>xylimits[0] or y<xylimits[1]:
        x,y=-1,-1
        print(sysmsg['regionoutofbounds'])
    return [x,y]

def XYscatterplot(bmp,XYdata,XYcoordinfo,showLinearRegLine,reglinecolor):
    for v in XYdata:#[[x,y,radius (max rad 5 ),isfilled],...]
        r,w=v[2],userdef2Dcooordsys2screenxy(v[0],v[1],XYcoordinfo)
        if r>1: circlevec(bmp,w,setmax(r,5),v[3],v[4])
        else: plotvecxypoint(bmp,w,v[3])
    if showLinearRegLine:
        m,b=LSMslope(XYdata),LSMYint(XYdata)
        xmin,xmax=XYcoordinfo[3][0],XYcoordinfo[5][0]
        ymin,ymax=xmin*m+b,xmax*m+b
        u=userdef2Dcooordsys2screenxy(xmin,ymin,XYcoordinfo)
        w=userdef2Dcooordsys2screenxy(xmax,ymax,XYcoordinfo)
        if w==[-1,-1]:
            ymax=XYcoordinfo[5][1]
            xmax=(ymax-b)/m
            w=userdef2Dcooordsys2screenxy(xmax,ymax,XYcoordinfo)
        linevec(bmp,u,w,reglinecolor)

def getneighborlist(v,mx,my,includecenter): 
    return [u for u in itergetneighbors(v,mx,my,includecenter)]

def getneighborcolorlist(bmp,v): 
    return [getRGBxybitvec(bmp,u) for u in itergetneighbors(v,getmaxx(bmp),getmaxy(bmp),True)]

def isimgedge(bmp,v,mx,my,similaritythreshold):
    retval,rgb=False,getRGBxybitvec(bmp,v)
    for u in itergetneighbors(v,mx,my,False):
        if distance(getRGBxybitvec(bmp,u),rgb)>similaritythreshold:
            retval=True
            break
    return retval

def iterimagedgevert(bmp,similaritythreshold):
    m=getmaxxy(bmp)
    for v in iterimageRGB(bmp,sysmsg['edgedetect'],'*',sysmsg['done']):
        for u in itergetneighbors(v[0],m[0],m[1],False):
            if distance(getRGBxybitvec(bmp,u),v[1])>similaritythreshold:
                yield u
                break

def iterimageregionvertbyRGB(bmp:array,rgb:list,similaritythreshold:int):
    """RGB Color selection by similarity

    Args:
        bmp                : unsigned byte array with bmp format
        rgb                : (r:byte,g:byte,b:byte) 
        similaritythreshold: how close to the color before we yield it
        
    Yeilds:
        ((x:int,y:int),(r:byte,g:byte,b:byte))

    """  
    for v in iterimageRGB(bmp,sysmsg['edgedetect'],'*',sysmsg['done']):
        if distance(rgb,v[1])<similaritythreshold: yield v[0]

def getimageregionbyRGB(bmp,rgb,similaritythreshold):
    """Select a region by color

    Args:
        bmp                 : unsigned byte array with bmp format
        rgb                 : (r:byte,g:byte,b:byte)
        similaritythreshold : controls edge detection sensitivity
        
    Returns:
        list of vertices

    """
    return [v for v in iterimageregionvertbyRGB(bmp,rgb,similaritythreshold)]

def getimagedgevert(bmp,similaritythreshold): 
    return [v for v in iterimagedgevert(bmp,similaritythreshold)]

def plotimgedges(bmp:array,similaritythreshold:int,edgeradius:int,edgecolor:int):
    """Draw edges 

    Args:
        bmp                 : unsigned byte array with bmp format
        similaritythreshold : controls edge detection sensitivity
        edgeradius,edgecolor: radius and color of pen used to draw the edge
        
    Returns:
        byref modified unsigned byte array

    """
    plotxypointlist(bmp,getimagedgevert(bmp,similaritythreshold),edgeradius,edgecolor)

def getBGRpalbuf(bmp):
    """Gets bitmap palette info as stored 

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        unsigned byte array (BGR)

    """   
    return bmp[bmppal:gethdrsize(bmp)]

def convertbufto24bit(buf,bgrpalbuf,bits):
    retval=[]
    for b in buf:
        if bits==8:
            s=b<<2
            retval+=bgrpalbuf[s:s+3]
        elif bits==4:
            s1,s2=divmod(b,16)
            s1<<=2
            s2<<=2
            retval+=bgrpalbuf[s1:s1+3]+bgrpalbuf[s2:s2+3]
        elif bits==1:
            for i in enumbits(b):
                s=i<<2
                retval+=bgrpalbuf[s:s+3]
    return array('B',retval)

def upgradeto24bitimage(bmp:array):
    """Upgrade an image to 24 bits

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    bits=bmp[bmpcolorbits]
    if bits==24:
        print(sysmsg['is24bit'])
        nbmp=bmp
    else:
        nbmp,bgrpal,mx,my=CopyBMPxydim2newBMP(bmp,24),getBGRpalbuf(bmp),getmaxx(bmp)-1,getmaxy(bmp)-1
        offset,r=computeBMPoffset(nbmp,0,my),getxcharcount(nbmp)
        for buf in itercopyrect(bmp,0,0,mx,my):
            BMPbitBLTput(nbmp,offset,convertbufto24bit(buf,bgrpal,bits))
            offset+=r
    return nbmp

def iterimageRGB(bmp:array,waitmsg:str,rowprocind:str,finishmsg:str):
    """Yields (r,g,b) information for entire bitnap

    Args:
        bmp       : unsigned byte array with bmp format
        waitmsg   : what to display in terminal at start
        rowprocind: char to display as a row is processed
        finishmsg : what to display in terminal at end

    Yields:
        ((x:int,y:int),(r:byte,g:byte,b:byte))

    """
    if waitmsg!='': print(waitmsg)
    r,y,offset,b=getxcharcount(bmp),getmaxy(bmp)-1,0,getBMPimgbytes(bmp)
    maxoffset,x,mx,bits=len(b),0,getmaxx(bmp),bmp[28]
    if bits<24: 
        p=getallRGBpal(bmp)
        doff=1
    else:doff=3
    while offset<maxoffset:
        if bits==1:
            c=b[offset]
            bit=7
            while bit>-1:
                if x<mx: yield ((x,y),p[(c & 1<<bit)>>bit])
                x+=1
                bit-=1
        elif bits==4:
            c0,c1=divmod(b[offset],16)
            if x<mx: yield ((x,y),p[c0])
            x+=1
            if x<mx: yield ((x,y),p[c1])
            x+=1
        elif bits==8:
            if x<mx: yield ((x,y),p[b[offset]])
            x+=1
        elif bits==24:
            if x<mx: yield ((x,y),(b[offset+2],b[offset+1],b[offset]))
            x+=1
        if offset%r==0:
            x=0
            y-=1
            if rowprocind!='': print(rowprocind,end='')
        offset+=doff
    print('\n')
    if finishmsg!='': print(finishmsg)

def iterimagecolor(bmp,waitmsg,rowprocind,finishmsg):
    """Yields color information for entire bitnap

    Args:
        bmp       : unsigned byte array with bmp format
        waitmsg   : what to display in terminal at start
        rowprocind: char to display as a row is processed
        finishmsg : what to display in terminal at end

    Yields:
        ((x:int,y:int),color:int)

    """
    if waitmsg!='': 
        print(waitmsg)
    r,y,offset,b=getxcharcount(bmp),getmaxy(bmp)-1,0,getBMPimgbytes(bmp)
    maxoffset,x,mx,bits=len(b),0,getmaxx(bmp),bmp[bmpcolorbits]
    if bits==24: doff=3
    else: doff=1
    while offset<maxoffset:
        if bits==1:
            c=b[offset]
            bit=7
            while bit>-1:
                if x<mx: yield ((x,y),(c & 1<<bit)>>bit)
                x+=1
                bit-=1
        elif bits==4:
            c0,c1=divmod(b[offset],16)
            if x<mx: yield ((x,y),c0)
            x+=1
            if x<mx: yield ((x,y),c1)
            x+=1
        elif bits==8:
            if x<mx: yield ((x,y),b[offset])
            x+=1
        elif bits==24:
            if x<mx: yield ((x,y),(b[offset+2]<<16)+(b[offset+1]<<8)+b[offset])
            x+=1
        if offset%r==0:
            x=0
            y-=1
            if rowprocind!='': print(rowprocind,end='')
        offset+=doff
    print('\n')
    if finishmsg!='': print(finishmsg)

@entirerectinboundary
def copyrect(bmp:array,x1:int,y1:int,x2:int,y2:int) -> array:
    """Copy a rectangular region to a buffer

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        custom unsigned byte array
        
    """
    retval=array('B',[bmp[bmpcolorbits]])
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    retval+=int2buf(2,x2-x1+2)
    retval+=int2buf(2,y2-y1+1)
    retval+=int2buf(2,adjustbufsize(x2-x1+1,bmp[28]))
    for buf in itercopyrect(bmp,x1,y1,x2,y2):
        retval+=buf
    return retval

def pasterect(bmp:array,buf:array,x1:int,y1:int):
    """Paste a rectangular area defined in buf in a bitmap 

    Args:
        bmp  : unsigned byte array with bmp format
        buf  : rectangular image buffer
        x1,y1: point to paste the buffer
    
    Returns:
        byref modified unsigned byte array

    """
    if bmp[bmpcolorbits]!=buf[0]:
        print(sysmsg['bitsnotequal'])
    else:
        x2,y2,r=x1+buf2int(buf[1:3]),y1+buf2int(buf[3:5]),getxcharcount(bmp)
        if listinBMPrecbnd(bmp,((x1,y1),(x2,y2))):
            offset=computeBMPoffset(bmp,x1,y2)
            br=buf2int(buf[5:7])
            startoff,endoff,bufsize=7,br+7,len(buf)
            while startoff<bufsize:
                BMPbitBLTput(bmp,offset,buf[startoff:endoff])
                offset+=r
                startoff=endoff
                endoff+=br
        else: 
            print(sysmsg['regionoutofbounds'])

def convertselection2BMP(buf:array):
    """ converts acustom unsigned byte array to bitmap format

    Args:
        buf: unsigned byte array with buf format
        
    Returns:
        unsigned byte array with bmp format
        
    """
    bmp,bits=-1,buf[0]
    if not isvalidcolorbit(bits): print (sysmsg['invalidbuf'])
    else:
        bmp=newBMP(buf2int(buf[1:3])+1,buf2int(buf[3:5])+1,bits)
        pasterect(bmp,buf,0,0)
    return bmp

def invertimagebits(bmp:array):
    """Inverts the bits a bitmap 

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    offset,maxoffset=gethdrsize(bmp),getfilesize(bmp)
    while offset<maxoffset:
        bmp[offset]=~bmp[offset]
        offset+=1

def erasealternatehorizontallines(bmp:array,int_eraseeverynline:int,int_eraseNthline:int,bytepat:int):
    """Erase every nth line

    Args:
        bmp                : unsigned byte array with bmp format
        int_eraseeverynline: erase every nth line in the region
        int_eraseNthline   : control which line every n lines to erase
        bytepat            : byte pattern to overwrite erased lines

    Returns:
        byref modified unsigned byte array

    """   
    bufsize,s1=getxcharcount(bmp),gethdrsize(bmp),
    s2=getfilesize(bmp)-bufsize
    bytepat&=0xff
    blank=array('B', [bytepat]*bufsize)
    i=1
    while s2>s1:
        if i%int_eraseeverynline==int_eraseNthline: 
            bmp[s2:s2+bufsize]=blank
        s2-=bufsize
        i+=1

def eraseeverynthhorizontalline(bmp:array,n:int):
    """Erase every nth horizontal line

    Args:
        bmp: unsigned byte array with bmp format
        n  : erase every nth line
        
    Returns:
        byref modified unsigned byte array

    """
    erasealternatehorizontallines(bmp,n,0,0)

@entirecircleinboundary
def erasealternatehorizontallinesincircregion(bmp,x,y,r,int_eraseeverynline,int_eraseNthline,bytepat):
    """Erase every nth line in a circular region

    Args:
        bmp                : unsigned byte array with bmp format
        x,y,r              : defines the circular region
        int_eraseeverynline: erase every nth line in the region
        int_eraseNthline   : control which line every n lines to erase
        bytepat            : byte pattern to overwrite erased lines

    Returns:
        byref modified unsigned byte array

    """   
    c=getcomputeBMPoffsetwithheaderfunc(bmp)
    bytepat&=0xff
    for v in itercirclepartlineedge(r):
        x1,x2=mirror(x,v[0])
        y1,y2=mirror(y,v[1])
        s1,e1,s2,e2=c(bmp,x1,y1),c(bmp,x2,y1),c(bmp,x1,y2),c(bmp,x2,y2)
        if y1%int_eraseeverynline==int_eraseNthline:
            bmp[s1:e1]=array('B', [bytepat]*(e1-s1))
        if y2%int_eraseeverynline==int_eraseNthline:
            bmp[s2:e2]=array('B', [bytepat]*(e2-s2))

def eraseeverynthhorizontallineinccircregion(bmp:array,x:int,y:int,r:int,n:int):
    """Erase every nth horizontal line in a circular region

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r        
        n    : erase every nth line
        
    Returns:
        byref modified unsigned byte array

    """
    erasealternatehorizontallinesincircregion(bmp,x,y,r,n,0,0)

@entirerectinboundary
def erasealternatehorizontallinesinregion(bmp:array,x1:int,y1:int,x2:int,y2:int,
                        int_eraseeverynline:int,int_eraseNthline:int,bytepat:int):
    """Erase every nth line in a rectangular region

    Args:
        bmp                : unsigned byte array with bmp format
        x1,y1,x2,y2        : defines the rectangular region
        int_eraseeverynline: erase every nth line in the region
        int_eraseNthline   : control which line every n lines to erase
        bytepat            : byte pattern to overwrite erased lines

    Returns:
        byref modified unsigned byte array

    """    
    bytepat&=0xff
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    bufsize,r,f=adjustbufsize(x2-x1+1,bmp[28]),getxcharcount(bmp),getcomputeBMPoffsetwithheaderfunc(bmp)
    s1,s2=f(bmp,x1,y2),f(bmp,x1,y1)
    blank=array('B', [bytepat]*bufsize)
    i=1
    while s2>s1:
        if i%int_eraseeverynline==int_eraseNthline: bmp[s2:s2+bufsize]=blank
        s2-=r
        i+=1

def eraseeverynthhorilineinregion(bmp:array,x1:int,y1:int,x2:int,y2:int,n:int):
    """Erase every nth line in a rectangular region

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangular region
        n          : erase every nth line in the region
        
    Returns:
        byref modified unsigned byte array

    """
    erasealternatehorizontallinesinregion(bmp,x1,y1,x2,y2,n,0,0)

def verttrans(bmp,trans):
    """Do vertical image transforms in a bitmap 

    Args:
        bmp : unsigned byte array with bmp format
        tran: single letter transform code
              'T' - mirror top half 'B' - mirror bottom half 'F' - flip
    
    Returns:
        byref modified unsigned byte array

    """
    def flip(): 
        bmp[s1:e1],bmp[s2:e2]=bmp[s2:e2],bmp[s1:e1]
    def mirrortop(): 
        bmp[s1:s1+bufsize]=bmp[s2:s2+bufsize]
    def mirrorbottom(): 
        bmp[s2:s2+bufsize]=bmp[s1:s1+bufsize]
    if trans=='F': 
        f=flip
    elif trans=='T': 
        f=mirrortop
    elif trans=='B': 
        f=mirrorbottom
    bufsize,s1=getxcharcount(bmp),gethdrsize(bmp)
    s2=getfilesize(bmp)-bufsize
    while s1<s2:
        e1,e2=s1+bufsize,s2+bufsize
        f()
        s1+=bufsize
        s2-=bufsize

def flipvertical(bmp):
    """Does an in-memory vertical flip of a bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified byte array

    """
    verttrans(bmp,'F')

def mirrortop(bmp):
    """Mirrors the top half of an in-memory bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified byte array

    """
    verttrans(bmp,'T')

def mirrorbottom(bmp):
    """Mirrors the bottom half of an in-memory bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified byte array

    """
    verttrans(bmp,'B')

@entirerectinboundary
def verttransregion(bmp:array,x1:int,y1:int,x2:int,y2:int,trans:str):
    """Do vertical image transforms in a bitmap in a rectangular region 

    Args:
        bmp         : unsigned byte array with bmp format
        x1,y1,x2,y2 : defines the rectangle
        trans       : single letter transform code
                      'T' - mirror top half 'B' - mirror bottom half 'F' - flip
    
    Returns:
        byref modified unsigned byte array

    """
    def flip(): 
        bmp[s1:e1],bmp[s2:e2]=bmp[s2:e2],bmp[s1:e1]
    def mirrortop(): 
        bmp[s1:s1+bufsize]=bmp[s2:s2+bufsize]
    def mirrorbottom(): 
        bmp[s2:s2+bufsize]=bmp[s1:s1+bufsize]
    if trans=='F': 
        f=flip
    elif trans=='T': 
        f=mirrortop
    elif trans=='B': 
        f=mirrorbottom
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    bufsize,r,c=adjustbufsize(x2-x1+1,bmp[28]),getxcharcount(bmp),getcomputeBMPoffsetwithheaderfunc(bmp)
    s1,s2=c(bmp,x1,y2),c(bmp,x1,y1)
    while s1<s2:
        e1,e2=s1+bufsize,s2+bufsize
        f()
        s1+=r
        s2-=r

def flipverticalregion(bmp:array,x1:int,y1:int,x2:int,y2:int):
    """Flips vertical a rectangular region in a bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle

    Returns:
        byref modified unsigned byte array

    """
    verttransregion(bmp,x1,y1,x2,y2,'F')

def mirrorbottominregion(bmp:array,x1:int,y1:int,x2:int,y2:int):
    """Mirror the bottom half of a rectangular region in a bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle

    Returns:
        byref modified unsigned byte array

    """
    verttransregion(bmp,x1,y1,x2,y2,'B')

def mirrortopinregion(bmp:array,x1:int,y1:int,x2:int,y2:int):
    """Mirror the top half of a rectangular region in a bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle

    Returns:
        byref modified unsigned byte array

    """
    verttransregion(bmp,x1,y1,x2,y2,'T')
    
@entirerectinboundary        
def fliphorzontalpixelbased(bmp,x1,y1,x2,y2):
    """Flips horizontal a rectangular region in a bitmap using pixel addressing (slightly slow)

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle

    Returns:
        byref modified unsigned byte array

    """
    m=x1+((x2-x1)>>1)
    while x1<=m:
        y=y1
        while y<=y2:
            swapcolors(bmp,(x1,y),(x2,y))
            y+=1
        x1+=1
        x2-=1

@entirerectinboundary    
def fliphverticalalpixelbased(bmp,x1,y1,x2,y2):
    """Flips vertical a rectangular region in a bitmap using pixel addressing

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle

    Returns:
        byref modified unsigned byte array

    """
    m=y1+((y2-y1)>>1)
    while y1<=m:
        x=x1
        while x<=x2:
            swapcolors(bmp,(x,y1),(x,y2))
            x+=1
        y1+=1
        y2-=1

def flipnibbleinbuf(buf:array) -> array:
    """Flips a 4 bit image buffer

    Args:
        buf : unsigned byte array
        
    Returns:
        unsigned byte array

    """    
    return array('B',[(b>>4)+((b%16)<<4) for b in buf])

def rotatebitsinbuf(buf:array) -> array: 
    return array('B',[ rotatebits(b) for b in buf])

def flipbuf(buf:array,bits:int) -> array:
    """Flips/rotates bits in buffer

    Args:
        buf : unsigned byte array
        bits: (1,4,8,24)
        
    Returns:
        unsigned byte array

    """  
    if bits==24: 
        buf=flip24bitbuf(buf)
    else: 
        buf.reverse()
    if bits==4: 
        buf=flipnibbleinbuf(buf)
    if bits==1: 
        buf=rotatebitsinbuf(buf)
    return buf

@entirerectinboundary    
def horizontalbulkswap(bmp:array,x1:int,y1:int,x2:int,y2:int,swapfunc):
    """Applies function swapfunc to a rectangular area in a bitmap 

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Returns:
        byref modified unsigned byte array

    """
    dx={24:1,8:1,4:2,1:8}[bmp[bmpcolorbits]]
    c,r=getcomputeBMPoffsetwithheaderfunc(bmp),getxcharcount(bmp)
    y1,y2=swapif(y1,y2,y1>y2)
    x1,x2=swapif(x1,x2,x1>x2)
    while x1<x2:
        swapfunc(bmp,c(bmp,x1,y2),c(bmp,x1,y1)+r,c(bmp,x2,y2),c(bmp,x2,y1)+r,r)
        x1+=dx
        x2-=dx

def fliphorizontalregion(bmp:array,x1:int,y1:int,x2:int,y2:int):
    """Does a horizontal flip of a rectangular area in a bitmap 

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Returns:
        byref modified unsigned byte array 

    """
    def swap24bit(bmp,s1,e1,s2,e2,r): 
        bmp[s1:e1-2:r],bmp[s2:e2-2:r],bmp[s1+1:e1-1:r],bmp[s2+1:e2-1:r],bmp[s1+2:e1:r],bmp[s2+2:e2:r]=bmp[s2:e2-2:r],bmp[s1:e1-2:r],bmp[s2+1:e2-1:r],bmp[s1+1:e1-1:r],bmp[s2+2:e2:r],bmp[s1+2:e1:r]
    def swap8bit(bmp,s1,e1,s2,e2,r): 
        bmp[s1:e1:r],bmp[s2:e2:r]=bmp[s2:e2:r],bmp[s1:e1:r]
    def swap4bit(bmp,s1,e1,s2,e2,r): 
        bmp[s1:e1:r],bmp[s2:e2:r]=flipnibbleinbuf(bmp[s2:e2:r]),flipnibbleinbuf(bmp[s1:e1:r])
    def swap1bit(bmp,s1,e1,s2,e2,r): 
        bmp[s1:e1:r],bmp[s2:e2:r]=rotatebitsinbuf(bmp[s2:e2:r]),rotatebitsinbuf(bmp[s1:e1:r])
    horizontalbulkswap(bmp,x1,y1,x2,y2,{24:swap24bit,8:swap8bit,4:swap4bit,1:swap1bit}[bmp[bmpcolorbits]])

def mirrorleftinregion(bmp:array,x1:int,y1:int,x2:int,y2:int):
    """Mirrors the left half of a rectangular area in a bitmap 

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Returns:
        byref modified unsigned byte array

    """
    def swap24bit(bmp,s1,e1,s2,e2,r): 
        bmp[s2:e2-2:r],bmp[s2+1:e2-1:r],bmp[s2+2:e2:r]=bmp[s1:e1-2:r],bmp[s1+1:e1-1:r],bmp[s1+2:e1:r]
    def swap8bit(bmp,s1,e1,s2,e2,r): 
        bmp[s2:e2:r]=bmp[s1:e1:r]
    def swap4bit(bmp,s1,e1,s2,e2,r): 
        bmp[s2:e2:r]=flipnibbleinbuf(bmp[s1:e1:r])
    def swap1bit(bmp,s1,e1,s2,e2,r): 
        bmp[s2:e2:r]=rotatebitsinbuf(bmp[s1:e1:r])
    horizontalbulkswap(bmp,x1,y1,x2,y2,{24:swap24bit,8:swap8bit,4:swap4bit,1:swap1bit}[bmp[bmpcolorbits]])

def mirrorrightinregion(bmp:array,x1:int,y1:int,x2:int,y2:int):
    """Mirrors the right half of a rectangular area in a bitmap 

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Returns:
        byref modified unsigned byte array

    """
    def swap24bit(bmp,s1,e1,s2,e2,r): 
        bmp[s1:e1-2:r],bmp[s1+1:e1-1:r],bmp[s1+2:e1:r]=bmp[s2:e2-2:r],bmp[s2+1:e2-1:r],bmp[s2+2:e2:r]
    def swap8bit(bmp,s1,e1,s2,e2,r): 
        bmp[s1:e1:r]=bmp[s2:e2:r]
    def swap4bit(bmp,s1,e1,s2,e2,r): 
        bmp[s1:e1:r]=flipnibbleinbuf(bmp[s2:e2:r])
    def swap1bit(bmp,s1,e1,s2,e2,r): 
        bmp[s1:e1:r]=rotatebitsinbuf(bmp[s2:e2:r])
    horizontalbulkswap(bmp,x1,y1,x2,y2,{24:swap24bit,8:swap8bit,4:swap4bit,1:swap1bit}[bmp[bmpcolorbits]])

def mirrorleft(bmp):
    """Mirrors the left half of an in-memory bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    mirrorleftinregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1)

def mirrorright(bmp):
    """Mirrors the right half of an in-memory bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    mirrorrightinregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1)

def mirrortopleftinregion(bmp:array,x1:int,y1:int,x2:int,y2:int):
    """Mirrors the top left of a rectangular region defined by (x1,y1) and (x2,y2)

    Args:
        bmp         : unsigned byte array with bmp format
        x1,y1,x2,y2 : defines the rectangle
        
    Returns:
        byref modified unsigned byte array

    """
    mirrorleftinregion(bmp,x1,y1,x2,y2)
    mirrortopinregion(bmp,x1,y1,x2,y2)

def mirrortoprightinregion(bmp,x1,y1,x2,y2):
    """Mirrors the top right of a rectangular region defined by (x1,y1) and (x2,y2)

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Returns:
        byref modified unsigned byte array

    """
    mirrorrightinregion(bmp,x1,y1,x2,y2)
    mirrortopinregion(bmp,x1,y1,x2,y2)

def mirrorbottomleftinregion(bmp,x1,y1,x2,y2):
    """Mirrors the bottom left of a rectangular region defined by (x1,y1) and (x2,y2)

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Returns:
        byref modified unsigned byte array

    """
    mirrorleftinregion(bmp,x1,y1,x2,y2)
    mirrorbottominregion(bmp,x1,y1,x2,y2)

def mirrorbottomrightinregion(bmp,x1,y1,x2,y2):
    """Mirrors the bottom right of a rectangular region defined by (x1,y1) and (x2,y2)

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Returns:
        byref modified unsigned byte array

    """
    mirrorrightinregion(bmp,x1,y1,x2,y2)
    mirrorbottominregion(bmp,x1,y1,x2,y2)

def mirrortopleft(bmp):
    """Mirrors the top left part of an in-memory bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    mirrorleftinregion(bmp,0,0,getmaxx(bmp)-1,(getmaxy(bmp)-1)//2)
    mirrortop(bmp)

def mirrortopright(bmp):
    """Mirrors the top right part of an in-memory bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    mirrorrightinregion(bmp,0,0,getmaxx(bmp)-1,(getmaxy(bmp)-1)//2)
    mirrortop(bmp)

def mirrorbottomleft(bmp):
    """Mirrors the bottom left part of an in-memory bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    ymax=getmaxy(bmp)-1
    mirrorleftinregion(bmp,0,ymax//2,getmaxx(bmp)-1,ymax)
    mirrorbottom(bmp)

def mirrorbottomright(bmp):
    """Mirrors the bottom right part of an in-memory bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    ymax=getmaxy(bmp)-1
    mirrorrightinregion(bmp,0,ymax//2,getmaxx(bmp)-1,ymax)
    mirrorbottom(bmp)

def fliphorizontal(bmp):
    """Does a horizontal flip of an in-memory bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    fliphorizontalregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1)

def flipXY(bmp):
    """Flips the x and y coordinates of an in-memory bitmap for a 90 degree rotation

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    mx,my,bits=getmaxy(bmp),getmaxx(bmp),bmp[bmpcolorbits]
    nbmp=newBMP(mx,my,bits)
    if bits not in [8,24]:
        copyRGBpal(bmp,nbmp)
        for v in iterimagecolor(bmp,sysmsg['flipXY'],'*',sysmsg['done']): plotxybit(nbmp,v[0][1],v[0][0],v[1])
    else:
        r,offset=getxcharcount(nbmp),0
        mx-=1
        if bits<24: copyRGBpal(bmp,nbmp)
        for y in range(0,my):
            BMPbitBLTput(nbmp,offset,array('B',vertBMPbitBLTget(bmp,y,0,mx)))
            offset+=r
    return nbmp

@entirerectinboundary                  
def itergetcolorfromrectregion(bmp,x1,y1,x2,y2):
    """Yields color info of a rectangular area in a bitmap 

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Yields:
        ((x:int,y:int),color:int) -> for all points in area

    """
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    x,y=x1,y1
    while y<=y2:
        x=x1
        while x<=x2:
            yield ((x,y),getxybit(bmp,x,y))
            x+=1
        y+=1

@entirerectinboundary              
def crop(bmp:array,x1:int,y1:int,x2:int,y2:int):
    """Crops the image to a rectangular region defined by (x1,y1) and (x2,y2)
    
    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Returns:
        unsigned byte array with bitmap layout

    """
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    bits=bmp[bmpcolorbits]
    nbmp=newBMP(x2-x1+1,y2-y1+1,bits)
    if bits<8:
        copyRGBpal(bmp,nbmp)
        for v in itergetcolorfromrectregion(bmp,x1,y1,x2,y2):
            intplotvecxypoint(nbmp,subvect(v[0],(x1,y1)),v[1])
    else:
        offset,r=0,getxcharcount(nbmp)
        for buf in itercopyrect(bmp,x1,y1,x2,y2):
            BMPbitBLTput(nbmp,offset,buf)
            offset+=r
    return nbmp

@entirerectinboundary    
def invertregion(bmp:array,x1:int,y1:int,x2:int,y2:int):
    """Inverts the bits in a rectangular region defined by (x1,y1) and (x2,y2)
        
    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Returns:
        byref modified unsigned byte array

    """
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    bits=bmp[bmpcolorbits]
    if bits<8:
        c=getmaxcolors(bmp)-1
        for v in itergetcolorfromrectregion(bmp,x1,y1,x2,y2):
            intplotvecxypoint(bmp,v[0],getxybitvec(bmp,v[0])^c)
    else:
        offset=iif(bits==24,compute24bitBMPoffset(bmp,x1,y2),compute8bitBMPoffset(bmp,x1,y2))
        r=getxcharcount(bmp)
        for buf in itercopyrect(bmp,x1,y1,x2,y2):
            BMPbitBLTput(bmp,offset,invertbitsinbuffer(buf))
            offset+=r

def monofilterto24bitregion(bmp,x1,y1,x2,y2):
    """Applies a monochrome filter to a rectangular area defined by (x1,y1) and (x2,y2) in a 24 bit bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        
    Returns:
        byref modified byte array

    """
    applybyrefnoparamfuncto24bitregion(bmp,x1,y1,x2,y2,applymonochromefiltertoBGRbuf)

def monofilterto24bitimage(bmp:array):
    """Applies a mono filter to a 24 bit in-memory bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    monofilterto24bitregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1)

def horizontalbrightnessgradto24bitimage(bmp:array,lumrange:list):
    """Applies a horizontal brightness gradient to a 24-bit in-memory bitmap

    Args:
        bmp     : An unsigned byte array with bmp format
        lumrange: [byte,byte] range of luminosity for gradient
        
    Returns:
        byref modified unsigned byte array

    """
    horizontalbrightnessgradto24bitregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1,lumrange)

def flip24bitbuf(buf):
    """Flips a 24 bit buffer
    
    Args:
        buf: unsigned byte array
        
    Returns:
        unsigned byte array

    """
    buf.reverse()
    RGB2BGRbuf(buf)
    return array('B',buf)

def unpack4bitbuf(buf):
    """Unpacks a 4-bit buffer into a list
    
    Args:
        buf: unsigned byte array
        
    Returns:
        list 

    """
    retval=[]
    for b in buf:
        retval+=[b//16, b&0xf]
    return retval

def unpack4bitbufresizeNtimesbigger(buf:array,n:int):
    """unpacks a 4-bit buffer into a list and repeats 4-bit units to resize
    
    Args:
        buf: An unsigned byte array
        n  : unsigned int multiplier to resize buffer
        
    Returns:
        list 

    """
    retval=[]
    for b in buf:
        retval+=[b>>4]*n
        retval+=[b&0xf]*n
    return retval

def pack4bitbuf(unpackedbuf:list) -> list:
    """Packs an unpacked 4-bit buffer into a list
    
    Args:
        buf: An unsigned byte array or list
        
    Returns:
        list 

    """
    retval=[]
    j,i=len(unpackedbuf)-1,0
    while i<j:
        retval+=[(unpackedbuf[i]<<4)+unpackedbuf[i+1]]
        i+=2
    return retval

def resize4bitbufNtimesbigger(buf:array,n:int) -> array:
    """Resize a 4-bit buffer n times bigger
    
    Args:
        buf: An unsigned byte array
        n  : buffer multiplier 
        
    Returns:
        unsigned byte array

    """
    return array('B',pack4bitbuf(unpack4bitbufresizeNtimesbigger(buf,n)))

def resize8bitbufNtimesbigger(buf:array,n:int):
    """Resize a 8-bit buffer n times bigger
    
    Args:
        buf: unsigned byte array
        n  : buffer multiplier 
        
    Returns:
        unsigned byte array

    """
    retval=[]
    for b in buf:
        retval+=[b]*n
    return array('B',retval)

def resize24bitbufNtimesbigger(buf:array,n:int):
    """Resize a 24-bit buffer n times bigger
    
    Args:
        buf: unsigned byte array
        n  : buffer multiplier 
        
    Returns:
        unsigned byte array

    """
    c,r=altsplitbuf3way(buf),resize8bitbufNtimesbigger
    return makeBGRbuf(r(c[0],n),r(c[1],n),r(c[2],n))

def resize1bitbufNtimesbigger(buf,n):
    """Resize a 1-bit buffer n times bigger
    
    Args:
        buf: unsigned byte array
        n  : buffer multiplier 
        
    Returns:
        unsigned byte array

    """
    retval=[]
    for b in buf: retval+=packbitlisttobuf(resizebitpattenNtimesbigger(b,n))
    return array('B',retval)

def resizebitpattenNtimesbigger(byteval:int,n:int):
    """Resize byte n times bigger bit wise
    
    Args:
        buf: unsigned byte
        n  : buffer multiplier 
        
    Returns:
        list of ones and zeroes

    """
    retval=[]
    for bit in enumbits(byteval): retval+=[bit]*n
    return retval

def packbitlisttobuf(blist):
    """Packs literal list of ones and zeros to a list of bytes
    
    Args:
        blist: literal list of ones and zeros
        
    Returns:
        list 

    """
    retval,j,i,b=[],len(blist)+1,1,0
    while i<j:
        m=i%8
        b+=blist[i-1]<<(7-m)
        if m==0 and i>1:
            retval+=[b]
            b=0
        i+=1
    return retval

def resizebufNtimesbigger(buf:array,n:int,bits:int):
    """Resize a buffer  n times bigger given a particular bit depth n
    
    Args:
        buf : array to resize
        n   : resize factor
        bits: bit depth of color info (1,4,8,24)
        
    Returns:
        list 

    """
    f={24:resize24bitbufNtimesbigger,8:resize8bitbufNtimesbigger,4:resize4bitbufNtimesbigger,1:resize1bitbufNtimesbigger}[bits]
    return f(buf,n)

def resizeNtimesbigger(bmp:array,n:int):
    """Resize an in-memory bmp n times bigger given a particular bit depth n
    
    Args:
        buf : array to resize
        n   : resize factor
        bits: bit depth of color info (1,4,8,24)
        
    Returns:
        unsigned byte array

    """
    bits=bmp[bmpcolorbits]
    m=getmaxxy(bmp)
    nx,ny=m[0]*n,m[1]*n
    nbmp,mx,my=newBMP(nx,ny,bits),m[0]-1,m[1]-1
    ny-=1
    if bits<24:copyRGBpal(bmp,nbmp)
    offset,r=computeBMPoffset(nbmp,0,ny),getxcharcount(nbmp)
    for buf in itercopyrect(bmp,0,0,mx,my):
        nbuf=resizebufNtimesbigger(buf,n,bits)
        i=0
        while i<n:
            BMPbitBLTput(nbmp,offset,nbuf)
            offset+=r
            i+=1
    return nbmp

def colorfilterto24bitregion(bmp,x1,y1,x2,y2,rgbfactors):
    """Applies a color filter to a rectangular area defined by (x1,y1) and (x2,y2) in a 24-bit bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        rgbfactors : color filter (r:float,g:float,b:float) r,g and b values are 0 to 1
        
    Returns:
        byref modified unsigned byte array

    """
    applybyreffuncto24bitregion(bmp,x1,y1,x2,y2,applycolorfiltertoBGRbuf,rgbfactors)

def colorfilterto24bitimage(bmp,rgbfactors):
    """Applies a color filter to a whole image in an in-memory 24 bit bitmap

    Args:
        bmp       : An unsigned byte array with bmp format
        rgbfactors: color filter (r:float,g:float,b:float) r,g and b values are 0 to 1
        
    Returns:
        byref modified byte array

    """
    colorfilterto24bitregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1,rgbfactors)

def brightnesseadjto24bitregion(bmp:array,x1:int,y1:int,x2:int,y2:int,percentadj:float):
    """Applies a brightness adjustment to a rectangular region in an in-memory 24 bit bitmap

    Args:
        bmp        \: unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        percentadj : float percentage adjustment can be positive or negative
        
    Returns:
        byref modified unsigned byte array

    """
    applyfuncto24bitregion(bmp,x1,y1,x2,y2,applybrightnessadjtoBGRbuf,percentadj)

def thresholdadjto24bitregion(bmp:array,x1:int,y1:int,x2:int,y2:int,lumrange:int):
    """Applies a threshold adjustment to a rectangular region in an in-memory 24-bit bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines the rectangle
        lumrange   : (byte:byte) threshold adjustment
        
    Returns:
        byref modified unsigned byte array

    """
    applyfuncto24bitregion(bmp,x1,y1,x2,y2,applythresholdadjtoBGRbuf,lumrange)

def thresholdadjcircregion(bmp,x,y,r,lumrange):
    """Applies a threshold adjustment to a circular region in an in-memory 24-bit bitmap

    Args:
        bmp      : An unsigned byte array with bmp format
        x,y,r    : defines the circular region 
        lumrange : (byte:byte) threshold adjustment
        
    Returns:
        byref modified byte array

    """
    apply24bitfunctocircregion(bmp,x,y,r,applythresholdadjtoBGRbuf,lumrange)

def brightnesseadjto24bitimage(bmp,percentadj):
    """Applies a brightness adjustment to a whole image in an in-memory 24-bit bitmap

    Args:
        bmp       : unsigned byte array with bmp format
        percentadj: float percentange adjustment can be positive or negative
        
    Returns:
        byref modified unsigned byte array

    """
    brightnesseadjto24bitregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1,percentadj)

def thresholdadjto24bitimage(bmp,lumrange):
    """Applies a threshold adjustment in an in-memory 24-bit bitmap

    Args:
        bmp     : unsigned byte array with bmp format
        lumrange: (byte:byte) threshold adjustment
        
    Returns:
        byref modified unsigned byte array

    """
    thresholdadjto24bitregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1,lumrange)

def verticalbrightnessgradto24bitimage(bmp,lumrange):
    """Applies a vertical brightness gradient 

    Args:
        bmp     : unsigned byte array with bmp format
        lumrange: (byte:byte) the brightness gradient to apply
        
    Returns:
        byref modified unsigned byte array

    """
    verticalbrightnessgradto24bitregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1,lumrange)

def mandelbrot(bmp:array,x1:int,y1:int,x2:int,y2:int,mandelparam:list,RGBfactors:list,maxiter:int):
    """Draw a Mandelbrot set 

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: rectangular area to draw in
        mandelparam: see fractals.py [float,float,float,float]
        rgbfactors : [r:float,b:float,g:float] ...r,g,b values 0 min -> 1 max
        maxiter    : when to break computing for color
        
    Returns:
        byref modified unsigned byte array

    """
    maxcolors=getmaxcolors(bmp)
    mcolor=maxcolors-1
    Pmax,Pmin,Qmax,Qmin=mandelparam[0],mandelparam[1],mandelparam[2],mandelparam[3]
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    maxx,maxy=x2-x1,y2-y1
    dp,dq,max_size=(Pmax-Pmin)/maxx,(Qmax-Qmin)/maxy,4
    for y in range(y1,y2,1):
        Q=Qmin+(y-y1)*dq
        for x in range(x1,x2,1):
            P,xp,yp,c,Xsq,Ysq=Pmin+(x-x1)*dp,0,0,0,0,0
            while (Xsq+Ysq)<max_size:
                 xp,yp=Xsq-Ysq+P,2*xp*yp+Q
                 Xsq,Ysq=xp*xp,yp*yp
                 c+=1
                 if c>maxiter: break
            if bmp[bmpcolorbits]==24:c=colormix(((255-c)*20)%256,RGBfactors)
            else: c=mcolor-c%maxcolors
            plotxybit(bmp,x,y,c)

def IFS(bmp:array,IFStransparam:list,x1:int,y1:int,x2:int,y2:int,
        xscale:int,yscale:int,xoffset:int,yoffset:int,color:int,maxiter:int):
    """Draw a Interated Function System  (IFS) fractal

    Args:
        bmp            : unsigned byte array with bmp format
        IFStransparam  : see fractals.py 
        x1,y1,x2,y2    : rectangular area to draw in
        xscale,yscale  : scaling factors
        xoffset,yoffset: used to move the fractal
        color          : color of fractal
        maxiter        : when to break computing for color
        
    Returns:
        byref modified unsigned byte array

    """        
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    af,p,x,y=IFStransparam[0],IFStransparam[1],x1,y1
    dy,i=y2-y1,0
    while i<maxiter:
        j=random()
        t=af[iif(j<p[0],0,iif(j<p[1],1,iif(j<p[2],2,3)))]
        nx=t[0]*x+t[1]*y+t[4]
        x,y=nx,t[2]*x+t[3]*y+t[5]
        px,py=int(x*xscale+xoffset+x1),int((dy-y*yscale+yoffset)+y1)
        if isinrectbnd(px,py,x1,y1,x2,y2): plotxybit(bmp,px,py,color)
        i+=1

def plotflower(bmp,cx,cy,r,petals,angrot,lumrange,RGBfactors):
    """Draw a flower

    Args:
        bmp       : unsigned byte array with bmp format
        cx,cy,r   : center (cx,cy) and radius r
        petals    : number of petals
        angrot    : angle of rotation
        lumrange  : (byte:byte) range of brightness for gradient
        rgbfactors: [r:float,b:float,g:float] ...r,g,b values 0 min -> 1 max
        
    Returns:
        byref modified unsigned byte array

    """
    maxcolors=getmaxcolors(bmp)
    mcolor=maxcolors-1
    lum1,dlum=range2baseanddelta(lumrange)
    p,angmax,angrot=petals/2,360*petals,radians(angrot)
    for a in range(0,angmax):
        ang=radians(a/petals)
        f,rang=cos(p*ang)**2,ang+angrot
        x,y=int(cx-r*sin(rang)*f),int(cy-r*cos(rang)*f)
        c=colormix(setmax(abs(int(lum1+dlum*(distance([x,y],[cx,cy])/r))),255),RGBfactors)
        if bmp[bmpcolorbits]!=24: c=mcolor-c%maxcolors
        plotxybit(bmp,x,y,c)

def plotfilledflower(bmp,cx,cy,r,petals,angrot,lumrange,RGBfactors):
    """Draw a filled flower

    Args:
        bmp       : unsigned byte array with bmp format
        cx,cy,r   : center (cx,cy) and radius r
        petals    : number of petals
        angrot    : angle of rotation
        lumrange  : (byte:byte) range of brightness for gradient
        rgbfactors: [r:float,b:float,g:float] ...r,g,b values 0 min -> 1 max
        
    Returns:
        byref modified unsigned byte array

    """
    for nr in range (r,2,-1): plotflower(bmp,cx,cy,nr,petals,angrot,lumrange,RGBfactors)

def plotbmpastext(bmp:array):
    """Plot a bitmap as text (cannot output 24-bit bmp)

    Args:
        bmp : unsigned byte array with bmp format
        
    Returns:
        console text output for debug and ascii art

    """
    bits,my,r,offset=getcolorbits(bmp),getmaxy(bmp)-1,getxcharcount(bmp),gethdrsize(bmp)
    for y in range(my,0,-1):
        for x in range(0,r):
            if bits==1: plotbitsastext(bmp[offset+r*y+x])
            if bits==4:
                c0,c1=divmod(bmp[offset+r*y+x],16)
                print(chr(97+c0)+chr(97+c1),end='')
            if bits==8: print(chr(bmp[offset+r*y+x]),end='')
        print()

def piechart(bmp:array,x:int,y:int,r:int,dataandcolorlist:list):
    """Apply func to a rectangular area in a 24-bit bitmap

    Args:
        bmp              : unsigned byte array with bmp format
        x,y,r            : center (x,y) and radius r
        dataandcolorlist : stuff to plot + color
        
    Returns:
        byref modified unsigned byte array

    """
    alist,big=genpiechartdata(dataandcolorlist)
    if big>-1:#for speed more computions in drawarc
            circle(bmp,x,y,r,alist[big][2],True)
    for a in alist:
        if a[4]<50: 
            drawarc(bmp,x,y,r,a[0],a[1],a[2],True,a[2],True)
    return [alist,big]

@func24bitonlyandentirerectinboundary
def applybyrefnoparamfuncto24bitregion(bmp:array,x1:int,y1:int,x2:int,y2:int,func):
    """Apply func to a rectangular area in a 24-bit bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines rectangular area
        func       : user defined function
        
    Returns:
        byref modified unsigned byte array

    """
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    offset,r=compute24bitBMPoffset(bmp,x1,y2),getxcharcount(bmp)
    for buf in itercopyrect(bmp,x1,y1,x2,y2):
        func(buf)
        BMPbitBLTput(bmp,offset,buf)
        offset+=r
    
@func24bitonlyandentirerectinboundary
def applybyreffuncto24bitregion(bmp:array,x1:int,y1:int,x2:int,y2:int,func,funcparam):
    """Apply byref func(funcparam) to a rectangular area in a 24-bit bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines rectangular area
        func       : user defined function
        funcparam  : parameters of the function
        
    Returns:
        byref modified unsigned byte array

    """
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    offset,r=compute24bitBMPoffset(bmp,x1,y2),getxcharcount(bmp)
    for buf in itercopyrect(bmp,x1,y1,x2,y2):
        func(buf,funcparam)
        BMPbitBLTput(bmp,offset,buf)
        offset+=r

@func24bitonlyandentirerectinboundary
def applyfuncto24bitregion(bmp:array,x1:int,y1:int,x2:int,y2:int,func,funcparam):
    """Apply func(funcparam) to a rectangular area in a 24-bit bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines rectangular area
        func       : user defined function
        funcparam  : parameters of the function
        
    Returns:
        byref modified unsigned byte array

    """
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    offset,r=compute24bitBMPoffset(bmp,x1,y2),getxcharcount(bmp)
    for buf in itercopyrect(bmp,x1,y1,x2,y2):
        BMPbitBLTput(bmp,offset,func(buf,funcparam))
        offset+=r

@func24bitonlyandentirerectinboundary
def verticalbrightnessgradto24bitregion(bmp:array,x1:int,y1:int,x2:int,y2:int,lumrange:list):
    """Apply a vertical brightness gradient to a rectangular area in a 24-bit bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines rectangular area
        lumrange   : (byte:byte) defines the gradient
        
    Returns:
        byref modified unsigned byte array

    """
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    offset,r=compute24bitBMPoffset(bmp,x1,y2),getxcharcount(bmp)
    lum=lumrange[1]
    dlum=(lumrange[0]-lumrange[1])/(y2-y1)
    for buf in itercopyrect(bmp,x1,y1,x2,y2):
        BMPbitBLTput(bmp,offset,applybrightnessadjtoBGRbuf(buf,lum))
        offset+=r
        lum+=dlum

@func24bitonlyandentirerectinboundary
def horizontalbrightnessgradto24bitregion(bmp:array,x1:int,y1:int,x2:int,y2:int,lumrange:list):
    """Apply a horizontal brightness gradient to a rectangular area in a 24-bit bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines rectangular area
        lumrange   : (byte:byte) defines the gradient
        
    Returns:
        byref modified unsigned byte array

    """
    r,c=getxcharcount(bmp),getcomputeBMPoffsetwithheaderfunc(bmp)
    x1,y1,x2,y2=sortrecpoints(x1,y1,x2,y2)
    xlim,f=x2+1,applybrightnessadjtoBGRbuf
    l=lumrange[0]
    dl=(lumrange[1]-lumrange[0])/(x2-x1)
    for x in range(x1,xlim):
        s,e=c(bmp,x,y2),c(bmp,x,y1)
        bmp[s:e-2:r],bmp[s+1:e-1:r],bmp[s+2:e:r]=f(bmp[s:e-2:r],l),f(bmp[s+1:e-1:r],l),f(bmp[s+2:e:r],l)
        l+=dl

@func24bitonlyandentirecircleinboundary 
def magnifyNtimescircregion(bmp:array,x:int,y:int,r:int,n:int):
    """Magnify a circular region in a bitmap file by n

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r
        n    : int magnification factor
        
    Returns:
        byref modified unsigned byte array

    """
    nx,ny,b,c=x*n,y*n,resizeNtimesbigger(bmp,n),computeBMPoffsetwithheader
    for v in itercirclepartlineedge(r):
        x1,x2=mirror(x,v[0])
        y1,y2=mirror(y,v[1])
        x3,x4=mirror(nx,v[0])
        y3,y4=mirror(ny,v[1])
        bmp[c(bmp,x1,y1):c(bmp,x2,y1)],bmp[c(bmp,x1,y2):c(bmp,x2,y2)]=b[c(b,x3,y3):c(b,x4,y3)],b[c(b,x3,y4):c(b,x4,y4)]

@func24bitonlyandentirecircleinboundary 
def pixelizenxncircregion(bmp:array,x:int,y:int,r:int,n:int):
    """Pixelizze a circular region in a bitmap file by n

    Args:
        bmp  : unsigned byte array with bmp format
        x,y,r: center (x,y) and radius r
        n    : integer pixellation dimension
        
    Returns:
        byref modified unsigned byte array

    """
    b,c=pixelizenxn(bmp,n),computeBMPoffsetwithheader
    for v in itercirclepartlineedge(r):
        x1,x2=mirror(x,v[0])
        y1,y2=mirror(y,v[1])
        bmp[c(bmp,x1,y1):c(bmp,x2,y1)],bmp[c(bmp,x1,y2):c(bmp,x2,y2)]=b[c(b,x1,y1):c(b,x2,y1)],b[c(b,x1,y2):c(b,x2,y2)]

def resizesmaller24bitbuf(buflist):
    n,a,m,s=len(buflist),addvectinlist,intscalarmulvect,altsplitbufnway
    c,f=altsplitbuf3way(a(buflist)),1/(n*n)
    return  makeBGRbuf(m(a(s(c[0],n)),f),m(a(s(c[1],n)),f),m(a(s(c[2],n)),f))

@func24bitonly
def resizeNtimessmaller(bmp:array,n:int) -> array:
    """Resize a whole image by n times smaller (in-memory 24-bit bitmap)

    Args:
        bmp: unsigned byte array with bmp format
        n  : size of pixel blur
        
    Returns:
        byref modified byte array

    """
    bits,nbmp=bmp[bmpcolorbits],-1
    m=getmaxxy(bmp)
    nx,ny=m[0]//n,m[1]//n
    nbmp,mx,my=newBMP(nx,ny,bits),m[0]-1,m[1]-1
    ny-=1
    offset,r=compute24bitBMPoffset(nbmp,0,ny),getxcharcount(nbmp)
    i,bufl,y=1,[],0
    for buf in itercopyrect(bmp,0,0,mx,my):
        j=i%n
        bufl+=[buf]
        if j==0:
            BMPbitBLTput(nbmp,offset,resizesmaller24bitbuf(bufl))
            offset+=r
            bufl=[]
            y+=1
            if y>ny: break
        i+=1
    return nbmp

def pixelizenxn(bmp:array,n:int) -> array:
    """Pixelize a whole image with n by n areas in which colors are averaged

    Args:
        bmp: unsigned byte array with bmp format
        n  : size of pixel blur
        
    Returns:
        byref modified byte array

    """
    return resizeNtimesbigger(resizeNtimessmaller(bmp,n),n)

def adjustcolordicttopal(bmp:array,colordict:dict):
    if getcolorbits(bmp)<24:
        for color in colordict:
            colordict[color]=matchRGBtopal(int2RGBarr(colordict[color]),getallRGBpal(bmp))

def gammaadjto24bitregion(bmp:array,x1:int,y1:int,x2:int,y2:int,gamma:float):
    """Applies a gamma correction to a rectangular region in a 24-bit bitmap

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines rectangular area 
        gamma      : gamma correction
        
    Returns:
        byref modified byte array

    """
    applybyreffuncto24bitregion(bmp,x1,y1,x2,y2,applygammaBGRbuf,gamma)

def gammaadjto24bitimage(bmp:array,gamma:float):
    """Applies a gamma correction to an in-memory 24-bit bitmap

    Args:
        bmp  : unsigned byte array with bmp format
        gamma: gamma correction
        
    Returns:
        byref modified unsigned byte array

    """
    gammaadjto24bitregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1,gamma)

@entirerectinboundary
def compareimglines(bmp:array,x1:int,y1:int,x2:int,y2:int,func):
    offset,r=computeBMPoffset(bmp,x1,y2),getxcharcount(bmp)
    oldbuf=[]
    for buf in itercopyrect(bmp,x1,y1,x2,y2):
        if oldbuf!=[]:
            BMPbitBLTput(bmp,offset,array('B',func(buf,oldbuf)))
            offset+=r
        oldbuf=buf
    BMPbitBLTput(bmp,offset,array('B',func(buf,oldbuf)))

def outlineregion(bmp:array,x1:int,y1:int,x2:int,y2:int):
    """Outines area in rectangular region in a bitmap file

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: defines rectangular area
        
    Returns:
        byref modified unsigned byte array

    """
    compareimglines(bmp,x1,y1,x2,y2,xorvect)

def outline(bmp:array):
    """Applies an outline filter to an in-memory 24 bit bitmap

    Args:
        bmp: unsigned byte array with bmp format
        
    Returns:
        byref modified unsigned byte array

    """
    outlineregion(bmp,0,0,getmaxx(bmp)-1,getmaxy(bmp)-1)

@intcircleparam
def sphere(bmp:array,x:int,y:int,r:int,rgbfactors:list):
    """Draws a rendered sphere

    Args:
        bmp       : unsigned byte array with bmp format
        x,y       : center of sphere in the image
        r         : radius of sphere in pixels
        rgbfactors: (r:float,g:float,b:float) 
                   r,g and b values are 0 to 1 
        
    Returns:
        byref modified unsigned byte array

    """
    gradcircle(bmp,x,y,r,[255,0],rgbfactors)

@intcircleparam
def thickencirclearea(bmp:array,x:int,y:int,r:int,rgbfactors:list): 
    gradthickcircle(bmp,x,y,r,8,[255,0],rgbfactors)

@entirerectinboundary
def fern(bmp:array,x1:int,y1:int,x2:int,y2:int,color:int):
    """Draws a fern

    Args:
        bmp        : unsigned byte array with bmp format
        x1,y1,x2,y2: rectangular area to draw fern in
        color      : color of the fern
        
    Returns:
        byref modified unsigned byte array

    """
    IFS(bmp,getIFSparams()['fern'],x1,y1,x2,y2,abs(y2-y1)//10,abs(y2-y1)//10,abs(x2-x1)//2,0,color,100000)

@checklink
def applybyreffuncwithparamtoregionandsave(ExistingBMPfile:str,NewBMPfile:str,
                                            x1:int,y1:int,x2:int,y2:int,func,funcparam):
    """Apply a 24-bit by-ref function to a rectangular area and save

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        func           : user defined function
        funcparam      : function parameters
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        func(bmp,x1,y1,x2,y2,funcparam)
        saveBMP(NewBMPfile,bmp)
        print(sysmsg['savedareafunc']%(func.__name__,x1,y1,x2,y2,ExistingBMPfile,NewBMPfile))

@checklink
def applybyref24bitcolorfunctoregionandsave(ExistingBMPfile:str,NewBMPfile:str,
                                            x1:int,y1:int,x2:int,y2:int,func,funcparam):
    """Apply a 24-bit by-ref color function to a rectangular area and save

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        func           : user defined function
        funcparam      : function parameters
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        if bmp[bmpcolorbits]!=24 : 
            print(sysmsg['not24bit'])
        else:
            func(bmp,x1,y1,x2,y2,funcparam)
            saveBMP(NewBMPfile,bmp)
            print(sysmsg['savedareafunc']%(func.__name__,x1,y1,x2,y2,ExistingBMPfile,NewBMPfile))

@checklink        
def applybyref24bitfunctoregionandsave(ExistingBMPfile:str,NewBMPfile:str,x1:int,y1:int,x2:int,y2:int,func):
    """Apply a 24-bit by-ref function with no parameters to a rectangular area and save

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        func           : user defined function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        if bmp[bmpcolorbits]!=24: 
            print(sysmsg['not24bit'])
        else:
            func(bmp,x1,y1,x2,y2)
            saveBMP(NewBMPfile,bmp)
            print(sysmsg['savedareafunc']%( func.__name__,x1,y1,x2,y2,ExistingBMPfile,NewBMPfile))

@checklink
def applybyreffunctoregionandsave(ExistingBMPfile:str,NewBMPfile:str,x1:int,y1:int,x2:int,y2:int,func):
    """Apply a by-ref function with no parameters to a rectangular region and save

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        func           : user defined function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        func(bmp,x1,y1,x2,y2)
        saveBMP(NewBMPfile,bmp)
        print(sysmsg['savedareafunc']%( func.__name__,x1,y1,x2,y2,ExistingBMPfile,NewBMPfile))

@checklink    
def applyfunctoregionandsave(ExistingBMPfile:str,NewBMPfile:str,x1:int,y1:int,x2:int,y2:int,func):
    """Apply a function with no parameters to a rectangular region and save

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        func           : user defined function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        bmp=func(bmp,x1,y1,x2,y2)
        if bmp!=None:
            saveBMP(NewBMPfile,bmp)
            print(sysmsg['savedareafunc']%( func.__name__,x1,y1,x2,y2,ExistingBMPfile,NewBMPfile))

@checklink
def applybyreffuncandsave(ExistingBMPfile:str,NewBMPfile:str,func):
    """Apply a by-ref function with no parameters and save

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        func           : user defined function
        
    Returns:
        new bitmap file

    """    
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        func(bmp)
        saveBMP(NewBMPfile,bmp)
        print(sysmsg['savefunc']%(func.__name__ ,ExistingBMPfile,NewBMPfile))

@checklink    
def applybyreffuncwithparamandsave(ExistingBMPfile:str,NewBMPfile:str,func,funcparam):
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:    
        func(bmp,funcparam)
        saveBMP(NewBMPfile,bmp)
        print(sysmsg['savesingleparamfunc']%(func.__name__,str(funcparam),ExistingBMPfile,NewBMPfile))

@checklink
def applyfuncandsave(ExistingBMPfile:str,NewBMPfile:str,func):
    """Apply a function with no parameters and save

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        func           : user defined function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        saveBMP(NewBMPfile,func(bmp))
        print(sysmsg['savefunc']%(func.__name__ ,ExistingBMPfile,NewBMPfile))

@checklink
def apply24bitfuncandsave(ExistingBMPfile:str,NewBMPfile:str,func):
    """Apply a 24-bit only function with no parameters and save

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        func           : user defined function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        if bmp[bmpcolorbits]!=24: 
            print(sysmsg['not24bit'])
        else:
            saveBMP(NewBMPfile,func(bmp))
            print(sysmsg['savefunc']%(func.__name__ ,ExistingBMPfile,NewBMPfile))

@checklink
def apply24bitfuncwithparamandsave(ExistingBMPfile:str,NewBMPfile:str,func,funcparam):
    """Apply a 24-bit only function with parameters and save

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        func           : user defined function
        funcparam      : parameters  of the function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        if bmp[bmpcolorbits]!=24: 
            print(sysmsg['not24bit'])
        else:
            saveBMP(NewBMPfile,func(bmp,funcparam))
            print(sysmsg['savesingleparamfunc']%(func.__name__,str(funcparam),ExistingBMPfile,NewBMPfile))

@checklink
def apply8bitabovefuncandsave(ExistingBMPfile:str,NewBMPfile:str,func):
    """Apply a function for 8 and 24-bit bmp with no parameters and save

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        func           : user defined function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        if bmp[bmpcolorbits] not in [8,24]: 
            print(sysmsg['not24or8bit'])
        else:
            saveBMP(NewBMPfile,func(bmp))
            print(sysmsg['savefunc']%(func.__name__ ,ExistingBMPfile,NewBMPfile))

@checklink
def applyfunctocircregion(ExistingBMPfile:str,NewBMPfile:str,func,x:int,y:int,r:int):
    """Apply a user provided function (no parameters) to a circular area

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x,y,r          : center (x,y) and radius r
        func           : user defined function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        func(bmp,x,y,r)
        saveBMP(NewBMPfile,bmp)
        print(sysmsg['savecircfunc']%(func.__name__ ,x,y,r,ExistingBMPfile,NewBMPfile))

@checklink
def applyfunctocircregionwithparam (ExistingBMPfile:str,NewBMPfile:str,func,x:int,y:int,r:int,funcparam):
    """Apply a user provided function with parameters to a circular area

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x,y,r          : center (x,y) and radius r
        func           : user defined function
        funcparam      : parameters  of the function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        func(bmp,x,y,r,funcparam)
        saveBMP(NewBMPfile,bmp)
        print(sysmsg['savecircfuncwithparam']%(func.__name__ ,x,y,r,funcparam,ExistingBMPfile,NewBMPfile))

@checklink
def apply24bitcoloradjfunctocircregion(ExistingBMPfile:str,NewBMPfile:str,func,x:int,y:int,r:int):
    """Apply a no parameter color adjustment function to a circular area (24 bit only)

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x,y,r          : center (x,y) and radius r
        func           : user defined function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        if bmp[bmpcolorbits]!=24: print(sysmsg['not24bit'])
        else:
            func(bmp,x,y,r)
            saveBMP(NewBMPfile,bmp)
            print(sysmsg['savecircfunc']%(func.__name__ ,x,y,r,ExistingBMPfile,NewBMPfile))

@checklink
def apply24bitcoloradjfuncwithparam2circregion(ExistingBMPfile:str,NewBMPfile:str,
                                                func,x:int,y:int,r:int,funcparam):
    """Apply a user provided color adjustment function to a circular area (24 bit only)

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x,y,r          : center (x,y) and radius r
        func           : user defined function
        funcparam      : parameters  of the function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        if bmp[bmpcolorbits]!=24: print(sysmsg['not24bit'])
        else: 
            func(bmp,x,y,r,funcparam)
            saveBMP(NewBMPfile,bmp)
            print(sysmsg['savecircfuncwithparam']%(func.__name__ ,x,y,r,funcparam,ExistingBMPfile,NewBMPfile))

@checklink
def applycoloradjfunc(ExistingBMPfile:str,NewBMPfile:str,func,funcparam):
    """Apply a user provided color adjustment function to an existing bitmap

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        func           : user defined function
        funcparam      : parameters  of the function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        if bmp[bmpcolorbits]!=24: 
            setbmppal(bmp,[func(c,funcparam) for c in getallRGBpal(bmp)])
        else:
            if func.__name__=='colorfilter': 
                colorfilterto24bitimage(bmp,funcparam)
            elif func.__name__=='brightnessadjust':  
                brightnesseadjto24bitimage(bmp,funcparam)
            elif func.__name__=='gammacorrect': 
                gammaadjto24bitimage(bmp,funcparam)
            elif func.__name__=='thresholdadjust': 
                thresholdadjto24bitimage(bmp,funcparam)
            else:
                for v in iterimageRGB(bmp,sysmsg['coloradj'],'*',sysmsg['done']):  
                    plotRGBxybitvec(bmp,v[0], func(v[1],funcparam))
        saveBMP(NewBMPfile,bmp)
        print(sysmsg['savesingleparamfunc']%(func.__name__,str(funcparam),ExistingBMPfile,NewBMPfile))

@checklink
def apply24bitcoloradjfunc(ExistingBMPfile:str,NewBMPfile:str,func,funcparam):
    """Apply a user provided color adjustment function to a 24-bit bitmap

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        func           : user defined function
        funcparam      : parameters  of the function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        if bmp[bmpcolorbits]!=24: 
            print(sysmsg['not24bit'])
        else:
            func(bmp,funcparam)
            saveBMP(NewBMPfile,bmp)
            print(sysmsg['savesingleparamfunc']%(func.__name__,str(funcparam),ExistingBMPfile,NewBMPfile))

@checklink        
def applynoparamcoloradjfunc(ExistingBMPfile:str,NewBMPfile:str,func):
    """Apply a user provided no parameter color adjustment function
        to an existing bitmap

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        func           : user defined function
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        if bmp[bmpcolorbits]!=24: setbmppal(bmp,[func(c) for c in getallRGBpal(bmp)])
        else:
            if func.__name__=='monochrome': 
                monofilterto24bitimage(bmp)
            else:
                for v in iterimageRGB(bmp,sysmsg['coloradj'],'*',sysmsg['done']):  
                    plotRGBxybitvec(bmp,v[0], func(v[1]))
        saveBMP(NewBMPfile,bmp)
        print(sysmsg['savenoparamfunc']%(func.__name__,ExistingBMPfile,NewBMPfile))

@checklink
def cropBMPandsave(ExistingBMPfile:str,NewBMPfile:str,
                        x1:int,y1:int,x2:int,y2:int):
    """Crops and saves a rectangular area to a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectagular region
                  
    Returns:
        new bitmap file

    """
    applyfunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,crop)

@checklink
def cropBMPandsaveusingrectbnd(ExistingBMPfile:str,NewBMPfile:str,rectbnd:list):
    """Crops and saves a rectangular area to a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        rectbnd        : list definining a rectabgular area
                         [(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
        
    Returns:
        new bitmap file

    """
    applyfunctoregionandsave(ExistingBMPfile,NewBMPfile,rectbnd[0][0],rectbnd[0][1],rectbnd[1][0]+1,rectbnd[1][1]+1,crop)

@checklinks
def imagecomp(inputfile1:str,inputfile2:str,diff_file:str,func):
    """Perform a bitwise comparison  of two bitmap files
        with  the same x and y dimensions  and bit depth
        using a user defined bitwise comparator function

    Args:
        Inputfile1,Inputfile2: Whole paths  to existing files
        diff_file            : New file  to  save changes  in
        func                 : User provided bitwise function

    Returns:
        new bitmap file

    """
    bmp1,bmp2=loadBMP(inputfile1),loadBMP(inputfile2)
    if len(bmp1)>54 and len(bmp2)>54:
        s1,s2=getmaxxyandbits(bmp1),getmaxxyandbits(bmp2)
        if s1!=s2: print(sysmsg['cantcomparefiles']%(s1,s2))
        else:
            bits=s1[1]
            nbmp=CopyBMPxydim2newBMP(bmp1,bits)
            if bits<24:
                pal1,pal2=getallRGBpal(bmp1),getallRGBpal(bmp2)
                if pal1!=pal2: print(sysmsg['diffpal'])
                copyRGBpal(bmp1,nbmp)
            setBMPimgbytes(nbmp,array('B',func(getBMPimgbytes(bmp1),getBMPimgbytes(bmp2))))
            saveBMP(diff_file,nbmp)
            print(sysmsg['savdifffile']%diff_file)
    
@checklink
@functimer
def reduce24bitimagebits(Existing24BMPfile:str,NewBMPfile:str,newbits:int,
                        similaritythreshold:float,usemonopal:bool,
                        RGBfactors:list):
    """Reduce the bits used to encode color in a 24-bit bitmap file

    Args:
        ExistingBMPfile     : Whole path to existing file
        NewBMPfile          : New file to save changes in
        newbits             : can be 1,4 or 8
        similaritythreshold : how close can a color be to another
        usemonopal          : True -> image will be monochrome
        RGBfactors          : (r:float,b:float,g:float) 
                              value of r,g,b range from 0 to 1
                              used only  if usemonopal is True
    Returns:
        new bitmap file

    """                        
    sbmp=loadBMP(Existing24BMPfile)
    if len(sbmp)>54:
        if sbmp[bmpcolorbits]!=24: print(sysmsg['not24bit'])
        else:
            bmp=CopyBMPxydim2newBMP(sbmp,newbits)
            if newbits>1:
                if usemonopal: 
                    newpal=setBMP2monochrome(bmp,RGBfactors)
                else: 
                    newpal=setnewpalfromsourcebmp(sbmp,bmp,similaritythreshold)
            for v in iterimageRGB(sbmp,sysmsg['colorquant'],'*',sysmsg['done']):
                    if newbits==1: 
                        c=probplotRGBto1bit(v[1],2)
                    else: 
                        c=matchRGBtopal(v[1],newpal)
                    intplotvecxypoint(bmp,v[0],c)
            saveBMP(NewBMPfile,bmp)
            print(sysmsg['savemod']%(Existing24BMPfile,NewBMPfile))

@checklink
@functimer
def imgregionbyRGB2file(ExistingBMPfile:str,NewBMPfile:str,edgeradius:int,edgecolor:int,
                        rgb:list,similaritythreshold:float,showedgeonly:bool):
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54:
        edge=getimageregionbyRGB(bmp,rgb,similaritythreshold)
        if showedgeonly:
            bmp=copyBMPhdr(bmp)
        plotxypointlist(bmp,edge,edgeradius,edgecolor)
        saveBMP(NewBMPfile,bmp)
        print(sysmsg['savemod']%(ExistingBMPfile,NewBMPfile))

@functimer
def invertbits2file(ExistingBMPfile:str,NewBMPfile:str):
    """Inverts bits in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,invertimagebits)

@functimer
def flipvertical2file(ExistingBMPfile:str,NewBMPfile:str):
    """Flips a bitmap file vertically

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,flipvertical)

@functimer
def mirrortop2file(ExistingBMPfile:str,NewBMPfile:str):
    """Mirrors the top half of a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,mirrortop)

@functimer
def mirrortopleft2file(ExistingBMPfile:str,NewBMPfile:str):
    """Mirrors the top left of a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,mirrortopleft)

@functimer
def mirrortopright2file(ExistingBMPfile:str,NewBMPfile:str):
    """Mirrors the top right of a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,mirrortopright)

@functimer
def mirrorbottomleft2file(ExistingBMPfile:str,NewBMPfile:str):
    """Mirrors the bottom left of a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,mirrorbottomleft)

@functimer
def mirrorbottomright2file(ExistingBMPfile:str,NewBMPfile:str):
    """Mirrors the bottom right of a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,mirrorbottomright)

@functimer
def mirrorbottom2file(ExistingBMPfile:str,NewBMPfile:str):
    """Mirrors the bottom half of a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,mirrorbottom)

@functimer
def mirrorleft2file(ExistingBMPfile:str,NewBMPfile:str):
    """Mirrors the left half of a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,mirrorleft)

@functimer
def mirrorright2file(ExistingBMPfile:str,NewBMPfile:str):
    """Mirrors the right half of a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,mirrorright)

@functimer
def fliphorizontal2file(ExistingBMPfile:str,NewBMPfile:str):
    """Flips horizontally the image in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,fliphorizontal)

@functimer
def flipXY2file(ExistingBMPfile:str,NewBMPfile:str):
    """Flips the x and y coordinates to rotate by 90 degrees
        the image in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        
    Returns:
        new bitmap file

    """
    applyfuncandsave(ExistingBMPfile,NewBMPfile,flipXY)

@functimer
def flipverticalregion2file(ExistingBMPfile:str,NewBMPfile:str,
                            x1:int,y1:int,x2:int,y2:int):
    """Flips vertically a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
                  
        
    Returns:
        new bitmap file

    """
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,flipverticalregion)

@functimer
def fliphorizontalregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                    x1:int,y1:int,x2:int,y2:int):
    """Flips horizontally a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,fliphorizontalregion)

@functimer
def mirrorleftinregion2file(ExistingBMPfile:str,NewBMPfile:str,
                            x1:int,y1:int,x2:int,y2:int):
    """Mirrors the left half region in a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """                            
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,mirrorleftinregion)

@functimer
def mirrorrightinregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                    x1:int,y1:int,x2:int,y2:int):
    """Mirrors the right half region in a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """                                    
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,mirrorrightinregion)

@functimer
def mirrortopinregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                x1:int,y1:int,x2:int,y2:int):
    """Mirrors the top half region in a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """                                
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,mirrortopinregion)

@functimer
def mirrorbottominregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                    x1:int,y1:int,x2:int,y2:int):
    """Mirrors the bottom half region in a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """                                    
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,mirrorbottominregion)

@functimer
def mirrortopleftinregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                    x1:int,y1:int,x2:int,y2:int):
    """Mirrors the top left region in a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """                                    
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,mirrortopleftinregion)

@functimer
def mirrortoprightinregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                x1:int,y1:int,x2:int,y2:int):
    """Mirrors the top right region in a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """                                
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,mirrortoprightinregion)

@functimer
def mirrorbottomleftinregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                        x1:int,y1:int,x2:int,y2:int):
    """Mirrors the bottom left region in a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """                                        
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,mirrorbottomleftinregion)

@functimer
def mirrorbottomrightinregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                        x1:int,y1:int,x2:int,y2:int):
    """Mirrors the bottom right region in a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,mirrorbottomrightinregion)

@functimer
def invertregion2file(ExistingBMPfile:str,NewBMPfile:str,
                            x1:int,y1:int,x2:int,y2:int):
    """Inverts the bits in a rectangular area in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """                            
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,invertregion)

@functimer
def autocropimg2file(ExistingBMPfile:str,NewBMPfile:str,similaritythreshold:float):
    """Perform an auto crop to the image in a bitmap file

    Args:
        ExistingBMPfile    : Whole path to existing file
        NewBMPfile         : New file to save changes in
        similaritythreshold: used to tune autocrop
        
    Returns:
        new bitmap file

    """
    bmp=loadBMP(ExistingBMPfile)
    if len(bmp)>54: 
        cropBMPandsaveusingrectbnd(ExistingBMPfile,NewBMPfile,rectboundarycoords(getimagedgevert(bmp,similaritythreshold)))

@functimer
def adjustbrightness2file(ExistingBMPfile:str,NewBMPfile:str,percentadj:float):
    """Apply a brightness adjustment to the image in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes in
        percentadj     : can be a positive or negative value
        
    Returns:
        new bitmap file

    """
    applycoloradjfunc(ExistingBMPfile,NewBMPfile,brightnessadjust,percentadj)

@functimer
def thresholdadjust2file(ExistingBMPfile:str,NewBMPfile:str,lumrange:list): 
    applycoloradjfunc(ExistingBMPfile,NewBMPfile,thresholdadjust,lumrange)

@functimer
def adjustbrightnessinregion2file(ExistingBMPfile:str,NewBMPfile:str,
                        x1:int,y1:int,x2:int,y2:int,percentadj:float):
    """Applies a brightness adjustment to rectangular area in a 24-bit bitmap

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectangular region
        percentadj     : can be a positive or negative adjustment
        
    Returns:
        new bitmap file

    """
    applybyref24bitcolorfunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,brightnesseadjto24bitregion,percentadj)

@functimer
def adjustthresholdinregion2file(ExistingBMPfile:str,NewBMPfile:str,x1:int,y1:int,x2:int,y2:int,lumrange:list):
    """Apply a threshold to a rectangular region in a 24-bit bitmap

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectangular region        
        lumrange       : (byte:byte) threshold to apply
        
    Returns:
        new bitmap file

    """
    applybyref24bitcolorfunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,thresholdadjto24bitregion,lumrange)

@functimer
def colorfilter2file(ExistingBMPfile:str,NewBMPfile:str,rgbfactors:list):
    """Applies color filter rgbfactors to a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        rgbfactors     : (r:float,g:float,b:float) 
                       r,g,b values range from 0 to 1
    Returns:
        new bitmap file

    """
    applycoloradjfunc(ExistingBMPfile,NewBMPfile,colorfilter,rgbfactors)

@functimer
def monochrome2file(ExistingBMPfile:str,NewBMPfile:str):
    """Applies a monochrome filter to a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        
    Returns:
        new bitmap file

    """
    applynoparamcoloradjfunc(ExistingBMPfile,NewBMPfile,monochrome)

@functimer
def colorfilterinregion2file(ExistingBMPfile:str,NewBMPfile:str,x1:int,y1:int,x2:int,y2:int,rgbfactors:list):
    """Apply a color filter to rectangular region in a 24-bit bitmap

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectangular region        
        rgbfactors     : (r:float,g:float,b:float) 
                       r,g,b values range from 0 to 1
        
    Returns:
        new bitmap file

    """
    applybyref24bitcolorfunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,colorfilterto24bitregion,rgbfactors)

@functimer
def monofilterinregion2file(ExistingBMPfile:str,NewBMPfile:str,x1:int,y1:int,x2:int,y2:int):
    """Applies a monochrome filter to rectangular region in a 24-bit bitmap

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """
    applybyref24bitfunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,monofilterto24bitregion)

@functimer
def pixelizenxntofile(ExistingBMPfile:str,NewBMPfile:str,n:int):
    """Pixellate a bitmap file with n x n pixel areas by averaging

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        
    Returns:
        new bitmap file

    """
    apply24bitfuncwithparamandsave(ExistingBMPfile,NewBMPfile,pixelizenxn,n)

@functimer
def resizeNtimessmaller2file(ExistingBMPfile:str,NewBMPfile:str,n:int):
    """Resize a bitmap file n times smaller

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        
    Returns:
        new bitmap file

    """
    apply24bitfuncwithparamandsave(ExistingBMPfile,NewBMPfile,resizeNtimessmaller,n)

@functimer
def resizeNtimesbigger2file(ExistingBMPfile:str,NewBMPfile:str,n:int):
    """Resize a bitmap file n times bigger

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        
    Returns:
        new bitmap file

    """
    apply24bitfuncwithparamandsave(ExistingBMPfile,NewBMPfile,resizeNtimesbigger,n)

@functimer
def upgradeto24bitimage2file(ExistingBMPfile:str,NewBMPfile:str):
    """Upgrades a bitmap file (1,4,8 bits color depth) to 24-bits

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        
    Returns:
        new bitmap file

    """
    applyfuncandsave(ExistingBMPfile,NewBMPfile,upgradeto24bitimage)

@functimer
def gammaadj2file(ExistingBMPfile:str,NewBMPfile:str,gamma:float):
    """Applies a gamma correction

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        gamma          : gamma correction
        
    Returns:
        new bitmap file

    """
    applycoloradjfunc(ExistingBMPfile,NewBMPfile,gammacorrect,gamma)

@functimer
def gammaadjtoregion2file(ExistingBMPfile:str,NewBMPfile:str,
                    x1:int,y1:int,x2:int,y2:int,gamma:float):
    """Applies a gamma correction to rectangular region

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectangular region
        gamma          : gamma correction
        
    Returns:
        new bitmap file

    """
    applybyref24bitcolorfunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,gammaadjto24bitregion,gamma)

@functimer
def eraseeverynthhorilineinregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                        x1:int,y1:int,x2:int,y2:int,n:int):
    """Erase every nth line in a rectangular region

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectangular region
        n              : erase every nth line
        
    Returns:
        new bitmap file

    """
    applybyreffuncwithparamtoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,eraseeverynthhorilineinregion,n)

@functimer
def rectangle2file(ExistingBMPfile:str,NewBMPfile:str,x1:int,y1:int,x2:int,y2:int,color:int):
    """Draws a rectangle

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectangular region
        color          : color of rectangle

    Returns:
        new bitmap file

    """
    applybyreffuncwithparamtoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,rectangle,color)

@functimer
def fern2file(ExistingBMPfile:str,NewBMPfile:str,x1:int,y1:int,x2:int,y2:int,color:int):
    """Draws a fern fractal in a bounding rectangle

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectangular region
        color          : color of fern fractal

    Returns:
        new bitmap file

    """
    applybyreffuncwithparamtoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,fern,color)

@functimer
def eraseeverynthhoriline2file(ExistingBMPfile:str,NewBMPfile:str,n:int):
    """Erase every nth line

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        n              : erase every nth line
        
    Returns:
        new bitmap file

    """
    applybyreffuncwithparamandsave(ExistingBMPfile,NewBMPfile,eraseeverynthhorizontalline,n)

@functimer
def outlineregion2file(ExistingBMPfile:str,NewBMPfile:str,x1:int,y1:int,x2:int,y2:int): 
    """Applies an outline filter to rectangular region

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : defines the rectangular region
        
    Returns:
        new bitmap file

    """
    applybyreffunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2, outlineregion)

@functimer
def outline2file(ExistingBMPfile:str,NewBMPfile:str):
    """Applies an outline filter

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        
    Returns:
        new bitmap file

    """
    applybyreffuncandsave(ExistingBMPfile,NewBMPfile,outline)

@functimer
def imagediff(inputfile1:str,inputfile2:str,diff_file:str):
    """Compares 2 files and saves diff to a bitmap file

    Args:
        inputfile1,inputfile2: Whole paths to existing files
        diff_file            : New file to store diff
        
    Returns:
        new bitmap file

    """
    imagecomp(inputfile1,inputfile2,diff_file,xorvect)

@functimer
def showsimilarparts(inputfile1:str,inputfile2:str,diff_file:str):
    """Compares 2 files and saves similar parts to a bitmap file

    Args:
        inputfile1,inputfile2: Whole paths to existing files
        diff_file            : New file to store similar parts
        
    Returns:
        new bitmap file

    """
    imagecomp(inputfile1,inputfile2,diff_file,andvect)

@functimer
def monochromecircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Applies a monochrome filter to a circular region

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    apply24bitcoloradjfunctocircregion(ExistingBMPfile,NewBMPfile,monocircle,x,y,r)

@functimer
def invertbitsincircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Inverts bits in a circular region

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,invertbitsincircregion,x,y,r)

@functimer
def colorfiltercircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int,rgbfactors:list):
    """Applies color filter rgbfactors to a circular region in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        rgbfactors     : (r:float,g:float,b:float)
                       r,g,b values range from 0 to 1
         
    Returns:
        new bitmap file

    """
    apply24bitcoloradjfuncwithparam2circregion(ExistingBMPfile,NewBMPfile,colorfiltercircregion,x,y,r,rgbfactors)

@functimer
def thresholdadjcircregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                x:int,y:int,r:int,lumrange:list):
    """Applies threshold adjustment to a circular region in a 24-bit bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        lumrange       : (byte:byte) threshold range
        
    Returns:
        new bitmap file

    """                                
    apply24bitcoloradjfuncwithparam2circregion(ExistingBMPfile,NewBMPfile,thresholdadjcircregion,x,y,r,lumrange)

@functimer
def gammacorrectcircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int,gamma:float):
    """Applies gamma correction to a circular region in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        gamma          : gamma adjustment
        
    Returns:
        new bitmap file

    """
    apply24bitcoloradjfuncwithparam2circregion(ExistingBMPfile,NewBMPfile,gammacorrectcircregion,x,y,r,gamma)

@functimer
def sphere2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int,rgbfactors:list):
    """Renders a sphere in a circular region in a bitmap file  with color defined by rgbfactors 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        rgbfactors     : (r:float,g:float,b:float) 
                     r,g,b values range from 0 to 1
        
    Returns:
        new bitmap file

    """
    apply24bitcoloradjfuncwithparam2circregion(ExistingBMPfile,NewBMPfile,sphere,x,y,r,rgbfactors)

@functimer
def filledcircle2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int,color:int):
    """Draws a filled circle in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        color          : color of circular region
        
    Returns:
        new bitmap file

    """
    applyfunctocircregionwithparam(ExistingBMPfile,NewBMPfile,filledcircle,x,y,r,color)

@functimer
def circle2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int,color:int):
    """Draws a circle in a bitmap file

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        color          : color of circle
        
    Returns:
        new bitmap file

    """
    applyfunctocircregionwithparam(ExistingBMPfile,NewBMPfile,circle,x,y,r,color)

@functimer
def thickencirclearea2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int,rgbfactors:list): 
    apply24bitcoloradjfuncwithparam2circregion(ExistingBMPfile,NewBMPfile,thickencirclearea,x,y,r,rgbfactors)

@functimer
def brightnessadjcircregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                x:int,y:int,r:int,percentadj:float):
    """Applies brightness gradient lumrange to a circular region

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        lumrange       : (byte:byte) the brightness gradient
        
    Returns:
        new bitmap file

    """
    apply24bitcoloradjfuncwithparam2circregion(ExistingBMPfile,NewBMPfile,brightnessadjcircregion,x,y,r,percentadj)

@functimer
def vertbrightnessgrad2circregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                        x:int,y:int,r:int,lumrange:list):
    """Applies a vertical brightness gradient to a circular region

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        lumrange       : (byte:byte) defines the brightness gradient
        
    Returns:
        new bitmap file

    """
    apply24bitcoloradjfuncwithparam2circregion(ExistingBMPfile,NewBMPfile,vertbrightnessgrad2circregion,x,y,r,lumrange)

@functimer
def horibrightnessgrad2circregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                        x:int,y:int,r:int,lumrange:list):
    """Applies a horizontal brightness gradient to a circular region

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        lumrange       : (byte:byte) the brightness gradient
        
    Returns:
        new bitmap file

    """
    apply24bitcoloradjfuncwithparam2circregion(ExistingBMPfile,NewBMPfile,horibrightnessgrad2circregion,x,y,r,lumrange)

@functimer
def flipvertcircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Does a vertical flip of a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r

    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,flipvertcircregion,x,y,r)

@functimer
def eraseeverynthhorilineinccircregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                            x:int,y:int,r:int,n:int):
    """Erase every nth horzontal line in a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        n              : omit every nth line in bmp
        
    Returns:
        new bitmap file

    """
    applyfunctocircregionwithparam(ExistingBMPfile,NewBMPfile,eraseeverynthhorizontallineinccircregion,x,y,r,n)

@functimer
def mirrortopincircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Mirrors the top half of a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r

    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,mirrortopincircregion,x,y,r)

@functimer
def mirrorbottomincircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Mirrors the bottom half of a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,mirrorbottomincircregion,x,y,r)

@functimer
def mirrorleftincircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Mirrors the left half of a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,mirrorleftincircregion,x,y,r)

@functimer
def mirrorrightincircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Mirrors the right half of a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,mirrorrightincircregion,x,y,r)

@functimer
def mirrortopleftincircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Mirrors the top left of a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,mirrortopleftincircregion,x,y,r)

@functimer
def mirrorbottomleftincircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Mirrors the bottom left of a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,mirrorbottomleftincircregion,x,y,r)

@functimer
def mirrortoprightincircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Mirrors the top right of a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,mirrortoprightincircregion,x,y,r)

@functimer
def mirrorbottomrightincircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Mirrors the bottom right of a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,mirrorbottomrightincircregion,x,y,r)

@functimer
def fliphoricircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Does a horizontal flip of a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,fliphoricircregion,x,y,r)

@functimer
def outlinecircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Outlines the area in a circular region 

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,outlinecircregion,x,y,r)

@functimer
def flipXYcircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int):
    """Flips the x and y coordinates of a circular region to cause a 90 degree rotation

    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        
    Returns:
        new bitmap file

    """
    applyfunctocircregion(ExistingBMPfile,NewBMPfile,flipXYcircregion,x,y,r)

@functimer
def magnifyNtimescircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int,intmagfactor:int):
    """Magnifies of a circular region by n times
        
    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        intmagfactor   : magnification factor
        
    Returns:
        new bitmap file

    """
    applyfunctocircregionwithparam(ExistingBMPfile,NewBMPfile,magnifyNtimescircregion,x,y,r,intmagfactor)

@functimer
def pixelizenxncircregion2file(ExistingBMPfile:str,NewBMPfile:str,x:int,y:int,r:int,intpixsize:int): 
    """Applies a pixel blur by averaging to a circular region
        
    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x,y,r          : center (x,y) and radius r
        intpixsize     : n x n pixel blur size
        
    Returns:
        new bitmap file

    """
    applyfunctocircregionwithparam(ExistingBMPfile,NewBMPfile,pixelizenxncircregion,x,y,r,intpixsize)

@functimer
def copycircregion2file(ExistingBMPfile:str,NewBMPfile:str,
                    x:int,y:int,r:int,newxycenterpoint:list):
    """Does a copy/paste of a circular region in a bitmap file
        
    Args:
        ExistingBMPfile : Whole path to existing file
        NewBMPfile      : New file to save changes to
        x,y,r           : center (x,y) and radius r
        newxycenterpoint: (x:int,y:int) where to paste
        
    Returns:
        new bitmap file

    """
    applyfunctocircregionwithparam(ExistingBMPfile,NewBMPfile,copycircregion,x,y,r,newxycenterpoint)

@functimer
def horizontalbrightnessgrad2file(ExistingBMPfile:str,NewBMPfile:str,lumrange:list):
    """Applies a horizontal brightness gradient to a bitmap file
        
    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        lumrange       : (byte:byte) defines the gradient
        
    Returns:
        new bitmap file

    """
    apply24bitcoloradjfunc(ExistingBMPfile,NewBMPfile,horizontalbrightnessgradto24bitimage,lumrange)

@functimer
def horizontalbrightnessgradregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                x1:int,y1:int,x2:int,y2:int,lumrange:list):
    """Applies a horizontal brightness gradient to a rectangular area
        
    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : Defines rectangular area
        lumrange       : (byte:byte) defines the gradient
        
    Returns:
        new bitmap file

    """
    applybyref24bitcolorfunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,horizontalbrightnessgradto24bitregion,lumrange)

@functimer
def verticalbrightnessgrad2file(ExistingBMPfile:str,NewBMPfile:str,lumrange:list):
    """Applies a vertical brightness gradient
        
    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        lumrange       : (byte:byte) defines the gradient
        
    Returns:
        new bitmap file

    """
    apply24bitcoloradjfunc(ExistingBMPfile,NewBMPfile,verticalbrightnessgradto24bitimage,lumrange)

@functimer
def verticalbrightnessgradregion2file(ExistingBMPfile:str,NewBMPfile:str,
                                        x1:int,y1:int,x2:int,y2:int,lumrange:list):
    """Applies a verticaal brightness gradient to a rectangular area
        
    Args:
        ExistingBMPfile: Whole path to existing file
        NewBMPfile     : New file to save changes to
        x1,y1,x2,y2    : Defines rectangular area
        lumrange       : (byte:byte) defines the gradient
        
    Returns:
        new bitmap file

    """
    applybyref24bitcolorfunctoregionandsave(ExistingBMPfile,NewBMPfile,x1,y1,x2,y2,verticalbrightnessgradto24bitregion,lumrange)
