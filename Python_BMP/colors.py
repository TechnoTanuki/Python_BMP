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

from random import randint
from array import array
from .conditionaltools import iif
from .mathlib import (addvect, subvect, roundvect, scalarmulvect, distance, mean,
    setminmaxvec, mulvect, intsetminmaxvec, setminmax, intscalarmulvect)

bmpstdpal={1:[[0,0,0],[255,255,255]],4:[[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128], [128, 0, 128], [0, 128, 128], [128, 128, 128], [192, 192, 192], [255, 0, 0], [0, 255, 0], [255, 255, 0], [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]],8:[[0, 0, 0], [128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128], [128, 0, 128], [0, 128, 128], [192, 192, 192], [192, 220, 192], [166, 202, 240], [64, 32, 0], [96, 32, 0], [128, 32, 0], [160, 32, 0], [192, 32, 0], [224, 32, 0], [0, 64, 0], [32, 64, 0], [64, 64, 0], [96, 64, 0], [128, 64, 0], [160, 64, 0], [192, 64, 0], [224, 64, 0], [0, 96, 0], [32, 96, 0], [64, 96, 0], [96, 96, 0], [128, 96, 0], [160, 96, 0], [192, 96, 0], [224, 96, 0], [0, 128, 0], [32, 128, 0], [64, 128, 0], [96, 128, 0], [128, 128, 0], [160, 128, 0], [192, 128, 0], [224, 128, 0], [0, 160, 0], [32, 160, 0], [64, 160, 0], [96, 160, 0], [128, 160, 0], [160, 160, 0], [192, 160, 0], [224, 160, 0], [0, 192, 0], [32, 192, 0], [64, 192, 0], [96, 192, 0], [128, 192, 0], [160, 192, 0], [192, 192, 0], [224, 192, 0], [0, 224, 0], [32, 224, 0], [64, 224, 0], [96, 224, 0], [128, 224, 0], [160, 224, 0], [192, 224, 0], [224, 224, 0], [0, 0, 64], [32, 0, 64], [64, 0, 64], [96, 0, 64], [128, 0, 64], [160, 0, 64], [192, 0, 64], [224, 0, 64], [0, 32, 64], [32, 32, 64], [64, 32, 64], [96, 32, 64], [128, 32, 64], [160, 32, 64], [192, 32, 64], [224, 32, 64], [0, 64, 64], [32, 64, 64], [64, 64, 64], [96, 64, 64], [128, 64, 64], [160, 64, 64], [192, 64, 64], [224, 64, 64], [0, 96, 64], [32, 96, 64], [64, 96, 64], [96, 96, 64], [128, 96, 64], [160, 96, 64], [192, 96, 64], [224, 96, 64], [0, 128, 64], [32, 128, 64], [64, 128, 64], [96, 128, 64], [128, 128, 64], [160, 128, 64], [192, 128, 64], [224, 128, 64], [0, 160, 64], [32, 160, 64], [64, 160, 64], [96, 160, 64], [128, 160, 64], [160, 160, 64], [192, 160, 64], [224, 160, 64], [0, 192, 64], [32, 192, 64], [64, 192, 64], [96, 192, 64], [128, 192, 64], [160, 192, 64], [192, 192, 64], [224, 192, 64], [0, 224, 64], [32, 224, 64], [64, 224, 64], [96, 224, 64], [128, 224, 64], [160, 224, 64], [192, 224, 64], [224, 224, 64], [0, 0, 128], [32, 0, 128], [64, 0, 128], [96, 0, 128], [128, 0, 128], [160, 0, 128], [192, 0, 128], [224, 0, 128], [0, 32, 128], [32, 32, 128], [64, 32, 128], [96, 32, 128], [128, 32, 128], [160, 32, 128], [192, 32, 128], [224, 32, 128], [0, 64, 128], [32, 64, 128], [64, 64, 128], [96, 64, 128], [128, 64, 128], [160, 64, 128], [192, 64, 128], [224, 64, 128], [0, 96, 128], [32, 96, 128], [64, 96, 128], [96, 96, 128], [128, 96, 128], [160, 96, 128], [192, 96, 128], [224, 96, 128], [0, 128, 128], [32, 128, 128], [64, 128, 128], [96, 128, 128], [128, 128, 128], [160, 128, 128], [192, 128, 128], [224, 128, 128], [0, 160, 128], [32, 160, 128], [64, 160, 128], [96, 160, 128], [128, 160, 128], [160, 160, 128], [192, 160, 128], [224, 160, 128], [0, 192, 128], [32, 192, 128], [64, 192, 128], [96, 192, 128], [128, 192, 128], [160, 192, 128], [192, 192, 128], [224, 192, 128], [0, 224, 128], [32, 224, 128], [64, 224, 128], [96, 224, 128], [128, 224, 128], [160, 224, 128], [192, 224, 128], [224, 224, 128], [0, 0, 192], [32, 0, 192], [64, 0, 192], [96, 0, 192], [128, 0, 192], [160, 0, 192], [192, 0, 192], [224, 0, 192], [0, 32, 192], [32, 32, 192], [64, 32, 192], [96, 32, 192], [128, 32, 192], [160, 32, 192], [192, 32, 192], [224, 32, 192], [0, 64, 192], [32, 64, 192], [64, 64, 192], [96, 64, 192], [128, 64, 192], [160, 64, 192], [192, 64, 192], [224, 64, 192], [0, 96, 192], [32, 96, 192], [64, 96, 192], [96, 96, 192], [128, 96, 192], [160, 96, 192], [192, 96, 192], [224, 96, 192], [0, 128, 192], [32, 128, 192], [64, 128, 192], [96, 128, 192], [128, 128, 192], [160, 128, 192], [192, 128, 192], [224, 128, 192], [0, 160, 192], [32, 160, 192], [64, 160, 192], [96, 160, 192], [128, 160, 192], [160, 160, 192], [192, 160, 192], [224, 160, 192], [0, 192, 192], [32, 192, 192], [64, 192, 192], [96, 192, 192], [128, 192, 192], [160, 192, 192], [255, 251, 240], [160, 160, 164], [128, 128, 128], [255, 0, 0], [0, 255, 0], [255, 255, 0], [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 255]]}
bmpvalidcolorbits=[1,4,8,24]

def isvalidcolorbit(bits:int) -> bool:
    return bits in bmpvalidcolorbits

def getdefaultbitpal(bits:int) -> list: 
    return bmpstdpal[bits]

def colormix(lum:list,RGBfactors:list) -> int: 
    return RGB2int(int(RGBfactors[0]*lum),int(RGBfactors[1]*lum),int(RGBfactors[2]*lum))

def int2RGB(i:int): return i>>16,(i>>8)&0xff,i&0xff

def int2RGBlist(i:int) -> list: 
    return [i>>16,(i>>8)&0xff,i&0xff]

def RGBtoBGRarr(r:int,g:int,b:int) -> array:
    return array('B',[b,g,r])

def int2BGRarr(i:int) -> array: 
    return array('B',[i&0xff,(i>>8)&0xff,i>>16])

def int2RGBarr(i:int) -> array: 
    return array('B',[i>>16,(i>>8)&0xff,i&0xff])

def RGB2BGRarr(r:int,g:int,b:int) -> array:
    return array('B',[b,g,r])

def RGBfactors2RGB(RGBfactors:list,bytelum:list) -> list: 
    return roundvect(scalarmulvect(RGBfactors,bytelum))

def RGB2int(r:int,g:int,b:int) -> int: 
    return b+(g<<8)+(r<<16)

def getcolorname2RGBdict() -> dict:#define colors here
    return {'black':0,'blue':RGB2int(0,0,192),'green':RGB2int(0,192,0),
       'cyan':RGB2int(64,192,192),'red':RGB2int(192,0,0),'magenta':RGB2int(192,0,192),
       'brown':RGB2int(128,128,0),'white':RGB2int(222,222,222),'gray':RGB2int(128,128,128),
       'lightblue':RGB2int(128,128,192),'lightgreen':RGB2int(128,192,128),
       'lightcyan':RGB2int(128,192,192),'lightred':RGB2int(192,128,128),
       'yellow':RGB2int(222,222,0),'orange':RGB2int(192,128,0),
       'lightgray':RGB2int(165,165,165),'brightwhite':RGB2int(255,255,255),
       'brightblue':RGB2int(0,0,255),'brightcyan':RGB2int(128,255,255),
       'brightgreen':RGB2int(0,255,0),'brightred':RGB2int(255,0,0),
       'brightmagenta':RGB2int(255,0,255),'brightyellow':RGB2int(255,255,0),
       'brightorange':RGB2int(255,128,0),
       'darkgray':RGB2int(92,92,92),'darkblue':RGB2int(0,0,92),
       'darkgreen':RGB2int(0,92,0),'darkred':RGB2int(92,0,0),
       'darkmagenta':RGB2int(92,0,92),'darkbrown':RGB2int(92,92,0)
       }

def getdefaultlumrange() -> dict:
    return {'maxdesc':[255,0],'maxasc':[0,255],'middesc':[192,64],'midasc':[64,192],'upperdesc':[255,128],'upperasc':[128,255],'lowerdesc':[128,0],'lowerasc':[0,128]}

def getRGBfactors() -> dict:#used by functions that generate color gradients
    d={}
    colordict=getcolorname2RGBdict()
    for color in colordict:
        r,g,b=int2RGB(colordict[color])
        d.setdefault(color,[r/255,g/255,b/255])
    return d

def matchRGBtodefault4bitpal(RGB:list) -> int:
       r,g,b,color=RGB[0]>>6,RGB[1]>>6,RGB[2]>>6,0
       if r>1 or g>1 or b>1:color=8
       if r>=1:color+=4
       if g>=1:color+=2
       if b>=1:color+=1
       return color
   
def matchRGBtopal(RGB:list,pal:list) -> int:
       c,i,d=0,0,442
       if RGB in pal: c=pal.index(RGB)
       else:
           for p in pal:
               if p!=[0,0,0] and RGB!=[0,0,0]:
                   newd=distance(RGB,p)
                   if newd<d:
                       c=i
                       d=newd
               i+=1
       return c
   
def RGBtoRGBfactorsandlum(RGB:list) -> list:
       lum=max(RGB)
       if lum==0: lum=1
       return [[RGB[0]/lum,RGB[1]/lum,RGB[2]/lum],lum]

def probplotRGBto1bit(rgb:list,brightness:int) -> int: 
    return round(brightness*randint(0,sum(rgb))/768)

def probplotRGBto4bitpal(rgb:list) -> int:
    color,r,g,b=0,rgb[0],rgb[1],rgb[2]
    if round(randint(0,r)/256)==1: color+=4
    if round(randint(0,g)/256)==1: color+=2
    if round(randint(0,b)/256)==1: color+=1
    r,g,b=r>>6,g>>6,b>>6
    if r>1 or g>1 or b>1:color+=8
    return color

def monochromepal(bits:int,RGBfactors:list) -> list:
    inc=(256>>bits)+iif(bits==4,1,iif(bits==1,127,0))
    return [[round(RGBfactors[0]*c),round(RGBfactors[1]*c),round(RGBfactors[2]*c)] for c in range(0,256,inc)]

def monochrome(rgb:list) -> list: 
    return [round(mean(rgb))]*3

def gammacorrect(rgb:list,gamma:int) -> list:
    c=RGBtoRGBfactorsandlum(rgb)
    return setminmaxvec(RGBfactors2RGB(c[0],gammacorrectbyte(c[1],gamma)),0,255)

def brightnessadjust(rgb:list,percentadj:float) -> list:
    c=RGBtoRGBfactorsandlum(rgb)
    return setminmaxvec(RGBfactors2RGB(c[0],c[1]+c[1]*(percentadj/100)),0,255)

def thresholdadjust(rgb:list,lumrange:list) -> list:
    c,lumrange=RGBtoRGBfactorsandlum(rgb),intsetminmaxvec(lumrange,0,255)
    if lumrange[0]>lumrange[1]: lumrange[1],lumrange[0]=lumrange[0],lumrange[1]
    return RGBfactors2RGB(c[0],setminmax(c[1],lumrange[0],lumrange[1]))

def colorfilter(rgb:list,rgbfactors:list) -> list: 
    return intsetminmaxvec(mulvect(rgb,rgbfactors),0,255)

def applymonochromefiltertoBGRbuf(buf:array):
       m=len(buf)
       buf[0:m-2:3]=buf[1:m-1:3]=buf[2:m:3]=array('B',[int((b+g+r)/3) for b,g,r in zip(buf[0:m-2:3],buf[1:m-1:3],buf[2:m:3])])
   
def monochromefiltertoBGRbuf(buf:array) -> array:
       applymonochromefiltertoBGRbuf(buf)
       return buf
   
def applycolorfiltertoBGRbuf(buf:array,rgbfactors:list):
       m=len(buf)-1
       buf[0:m-2:3],buf[1:m-1:3],buf[2:m:3]=array('B',intscalarmulvect(buf[0:m-2:3],rgbfactors[2])),array('B',intscalarmulvect(buf[1:m-1:3],rgbfactors[1])),array('B',intscalarmulvect(buf[2:m:3],rgbfactors[0]))    
   
def colorfiltertoBGRbuf(buf:array,rgbfactors:list) -> array:
       applycolorfiltertoBGRbuf(buf,rgbfactors)
       return buf

def applygammaBGRbuf(buf:array,gamma:float):
       j,i=len(buf),0
       while i<j:
           b=buf[i:i+3]
           lum=max(b)
           if lum==0:lum=1
           f,i1,i2=int(((lum/255)**gamma)*255)/lum,i+1,i+2
           buf[i],buf[i1],buf[i2]=int(buf[i]*f)&0xff,int(buf[i1]*f)&0xff,int(buf[i2]*f)&0xff
           i+=3
   
def gammaBGRbuf(buf:array,gamma:float) -> array:
       applygammaBGRbuf(buf,gamma)
       return buf
   
def gammacorrectbyte(lumbyte:int,gamma:float) -> int: 
    return int(((lumbyte/255)**gamma)*255)

def RGBfactorstoBaseandRange(lumrange:list,RGBfactors:list):
       baselum=scalarmulvect(RGBfactors,lumrange[0])
       lumrange=subvect(scalarmulvect(RGBfactors,lumrange[1]),baselum)
       return baselum,lumrange

def invertbitsinbuffer(buf:array) -> array: 
    return array('B',[b^0xFF for b in buf])

def applybrightnessadjtoBGRbuf(buf:array,percentadj:float) -> array: 
    return array('B',setminmaxvec(addvect(buf,intscalarmulvect(buf,percentadj/100)),0,255))

def applythresholdadjtoBGRbuf(buf:array,lumrange:list) -> array: 
    lummin,lummax,m,i=lumrange[0]&0xff,lumrange[1]&0xff,len(buf),0
    while i<m:
        lum,f=max(buf[i:i+3]),1
        if lummin>lummax: lummin,lummax=lummax,lummin
        if lum>0:
            if lum<lummin: f=lummin/lum
            if lum>lummax: f=lummax/lum
        if f!=1:
            buf[i]=int(f*buf[i])
            buf[i+1]=int(f*buf[i+1])
            buf[i+2]=int(f*buf[i+2])
        i+=3
    return buf

def RGB2BGRbuf(buf:array):
    m=len(buf)
    buf[0:m-2:3],buf[2:m:3]=buf[2:m:3],buf[0:m-2:3]

def makeBGRbuf(bbuf:array,gbuf:array,rbuf:array) -> array:
    buf=[]
    for b,g,r in zip(bbuf,gbuf,rbuf):
        buf+=[b,g,r]
    return array('B',buf)
