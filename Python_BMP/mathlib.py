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

from math import sqrt,sin,cos,acos,atan,pi,degrees,radians
from random import randint,random
from functools import reduce

def setmaxvec(vlist,maxval): return [setmax(v,maxval) for v in vlist]

def setminmaxvec(vlist,minval,maxval): return [setminmax(v,minval,maxval) for v in vlist]

def intsetminmaxvec(vlist,minval,maxval):  return [intsetminmax(v,minval,maxval) for v in vlist]

def range2baseanddelta(lst_range): return lst_range[0],lst_range[1]-lst_range[0]

def roundvect(v): return [round(n) for n in v]

def roundvectlist(vlist): return [roundvect(v) for v in vlist]

def addvect(u,v): return [i+j for i,j in zip(u,v)]

def trans(vlist,u): return [addvect(v,u) for v in vlist]

def subvect(u,v): return [i-j for i,j in zip(u,v)]

def mulvect(u,v): return [i*j for i,j in zip(u,v)]

def divvect(u,v):  return [i/j for i,j in zip(u,v)]

def scalarmulvect(vec,scalarval): return [s*scalarval for s in vec]

def intscalarmulvect(vec,scalarval): return [round(s*scalarval) for s in vec]

def mean(v): return sum(v)/len(v)

def meanlist(vlist): return [mean(v) for v in vlist]

def pivotlist(vlist):
    j=len(vlist[0])
    return [[v[i] for v in vlist] for i in range(0,j)]

def variance(v):
    ave=mean(v)
    return [n-ave for n in v]

def permutation(n):
    p=1
    while n>1:
        p*=n
        n-=1
    return p

def combination(n,i):
    nm,dm,=1,1
    while i>0:
        nm*=n
        dm*=i
        i-=1
        n-=1
    return nm//dm

def isinrange(value,highlimit,lowlimit): return (value>lowlimit) and (value<highlimit)

def setmax(val,maxval):
    if val>maxval: val=maxval
    return val

def setmin(val,minval):
    if val<minval: val=minval
    return val

def setminmax(val,minval,maxval):
    if val>maxval: val=maxval
    if val<minval: val=minval
    return val

def intsetminmax(val,minval,maxval):
    val=round(val)
    if val>maxval: val=maxval
    if val<minval: val=minval
    return val

def sign(intval):
    retval=0
    if intval>0: retval=1
    elif intval==0: retval=0
    else: retval=-1
    return retval

def LSMslope(XYdata):#first twovalues inlist must be [[x and y...]...]
    XY,N=pivotlist(XYdata),len(XYdata)
    X,Y=XY[0],XY[1]
    EX,EY,EXY,EsqX=sum(X),sum(Y),sum(mulvect(X,Y)),sum(mulvect(X,X))
    return ((N*EXY)-(EX*EY))/((N*EsqX)-(EX**2))

def LSMYint(XYdata):
    XY=pivotlist(XYdata)
    meanX,meanY=mean(XY[0]),mean(XY[1])
    return meanY-LSMslope(XYdata)*meanX

def PearsonsR(XYdata):#first twovalues inlist must be [[x and y...]...]
    XY,N=pivotlist(XYdata),len(XYdata)
    X,Y=XY[0],XY[1]
    EX,EY,EXY=sum(X),sum(Y),sum(mulvect(X,Y))
    EsqX,EsqY=sum(mulvect(X,X)),sum(mulvect(Y,Y))
    return ((N*EXY)-(EX*EY))/sqrt(abs(((N*EsqX)-(EX**2)))*abs(((N*EsqY)-(EY**2))))

def Rsquare(XYdata): return PearsonsR(XYdata)**2

def TTest(XYdata):
    r=PearsonsR(XYdata)
    return r*sqrt((len(XYdata)-2)/(1-r**2))

def StdDev(v):
    vr=variance(v)
    return sqrt(sum(mulvect(vr,vr))/len(v))

def slope(u,v): return (v[1]-u[1])/(v[0]-u[0])

def coefvar(v): return StdDev(v)/mean(v)

def vectiszero(v):
    b=True
    for i in v:
        if i>0:
            b=False
            break
    return b

def isorthogonal(u,v): return vectiszero(mulvect(u,v))

def crossprod3d(u,v):
    x,y,z=0,0,0
    if len(u)==3 and len(v)==3:
        x=u[1]*v[2]-u[2]*v[1]
        y=u[2]*v[0]-u[0]*v[2]
        z=u[0]*v[1]-u[1]*v[0]
    return [x,y,z]

def getnormvec(p1,p2,p3): return crossprod3d(subvect(p2,p1),subvect(p3,p1))

def dotprod(u,v): return sum(mulvect(u,v))

def vmag(v):
    s=0
    for i in v: s+=i*i
    return sqrt(s)

def distance(u,v): return vmag(subvect(u,v))

def distancetable(vertlist):
    dlist=[]
    for v in vertlist:
        for u in vertlist:
            if u!=v: dlist.append([vertlist.index(v),vertlist.index(u),distance(u,v)])
    return dlist

def countdist(distlist):
    d={}
    for i in distlist:
        dist=i[2]
        if dist not in d: d.setdefault(dist,1)
        else: d[dist]+=1
    return d

def det3D(a1,a2,a3): return a1[0]*a2[1]*a3[2]+a1[1]*a2[2]*a3[0]+a1[2]*a2[0]*a3[1]-a1[0]*a2[2]*a3[1]-a1[1]*a2[0]*a3[2]-a1[2]*a2[1]*a2[0]

def cosaffin(u,v): return dotprod(u,v)/(vmag(u)*vmag(v))

def dircos(v):
    mag=vmag(v)
    return [i/mag for i in v]

def diracos(dcos): return [acos(d) for d in dcos]

def dirdeg(raddir): return [degrees(d) for d in raddir]

def rect2sphericalcoord3D(v):
    p=vmag(v)
    azimuth,colatitude=atan(v[1]/v[0]),acos(v[2]/p)
    return [p,azimuth,colatitude]

def spherical2rectcoord3D(vspherecoord3D):
    p,theta,phi=vspherecoord3D[0],vspherecoord3D[1],vspherecoord3D[2]
    sinphi=sin(phi)
    return [p*sinphi*cos(theta),p*sinphi*sin(theta),p*cos(phi)]

def rect2cylindricalcoord3D(v): return [vmag(v),atan(v[1]/v[0]),v[2]]

def cylindrical2rectcoord3D(vcylindcoord3D):
    r,theta=vcylindcoord3D[0],vcylindcoord3D[1]
    return [r*cos(theta),r*sin(theta),vcylindcoord3D[2]]

def polar2rectcoord2D(vpolarcoord2D):
    r,theta=vpolarcoord2D[0],vpolarcoord2D[1]
    return [r*cos(theta),r*sin(theta)]

def rect2polarcoord2D(v):
    p=vmag(v)
    a=atan(v[1]/v[0])
    return [p,a]

def polarcoordangle2D(v):
    a=acos(cosaffin(v,[0,-1]))
    if v[0]<0:a=2*pi-a
    return a

def rect2polarcoord2Dwithcenter(vcen,vpnt):
    v=subvect(vpnt,vcen)
    return [vmag(v),polarcoordangle2D(v)]

def computerotvec(degrot):
    a=radians(degrot)
    return (sin(a),cos(a))

def rotvec2D(v,rotvec): return [v[0]*rotvec[1]-v[1]*rotvec[0],v[0]*rotvec[0]+v[1]*rotvec[1]]

def mirrorx(p,x): return [p[0]-x,p[1]],[p[0]+x,p[1]]

def mirrory(p,y): return [p[0],p[1]-y],[p[0],p[1]+y]

def mirrorvec(vcen,v): return [subvect(vcen,v),addvect(vcen,v)]

def mirror(pt,delta): return pt-delta,pt+delta

def randomvect(minrnd,maxrnd): return [randint(minrnd,maxrnd),randint(minrnd,maxrnd),randint(minrnd,maxrnd)]

def addrndtovert(vertlist,minrnd,maxrnd): return [addvect(pt,randomvect(minrnd,maxrnd)) for pt in vertlist]

def adddimz(vlist2D,value): return [[v[0],v[1],value] for v in vlist2D]

def anglebetween2Dlines(u,v):
    if u[0]!=v[0]: a=atan(slope(u,v))
    else: a=iif(u[0]<v[0],1.5707963267948966,4.71238898038469)
    return a

def rotatebits(bits):
    bit,retval=7,0
    while bit>0:
        retval+=((bits & (1<<bit))>>bit)<<(7-bit)
        bit-=1
    return retval

def mirror1stquad(x,y,v):
    xmin,xmax=mirror(x,v[0])
    ymin,ymax=mirror(y,v[1])
    return [[xmin,ymax],[xmax,ymax],[xmin,ymin],[xmax,ymin]]

def xorvect(u,v): return [i^j for i,j in zip(u,v)]

def andvect(u,v): return [i&j for i,j in zip(u,v)]

def bitmaskvect(v,bitmask): return [b & bitmask for b in v ]

def orvect(u,v): return [i|j for i,j in zip(u,v)]

def gammacorrectbyte(lumbyte,gamma): return int(((lumbyte/255)**gamma)*255)

def addvectinlist(vlist): return reduce(addvect,vlist)

def addvectpairlist(vpair): return addvect(vpair[0],vpair[1])

def addvecttripletlist(vtriplet): return addvect(addvect(vtriplet[0],vtriplet[1]),vtriplet[2])

def addvectlist(vlist1,vlist2): return [addvect(u,v) for u,v in zip(vlist1,vlist2)]

def mapfunctolist(func,vlist): return [func(v) for v in vlist]

def iif(boolcond,trueval,falseval):
    r=falseval
    if boolcond: r=trueval
    return r

def swapif(val1,val2,boolcond):
    if boolcond: val1,val2=val2,val1
    return val1,val2

def swapxy(v): return [v[1],v[0]]


