#
#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#
#We make no warranty of any kind, expressed or implied.
#
#The primary author and any subsequent code contributors shall not
#be liable in any event for incidental or consquential damages
#in connection with, or arising out of the use of this code
#in current form or with modifications.
#
#Contact primary author if you plan to use this in a commercial product at
# joelalcarez1975@gmail.com.

from .mathlib import sqrt,distance,sin,cos,adddimz,radians,roundvect,computerotvec,trans,addvect,getnormvec,iif,subvect,cylindrical2rectcoord3D,spherical2rectcoord3D
from .primitives2D import floatregpolygonvert,regpolygonvert,iterline,rectboundarycoords
from .messages import sysmsg

def getshapesidedict(): return {"tetrahedra":((2,1,0),(2,3,1),(0,3,2),(3,0,1)),"cube":((1,2,3,0),(5,6,7,4),(0,3,6,5),(4,7,2,1),(4,1,0,5),(2,7,6,3)),"hexahedra":((2,3,1),(0,3,2),(3,0,1),(1,4,2),(2,4,0),(1,0,4)),"octahedra":((1,2,0),(4,1,0),(3,4,0),(2,3,0),(2,1,5),(1,4,5),(4,3,5),(3,2,5))}

def tetrahedravert(x):
    x_sqr,halfx=x*x,x/2
    return [[0,0,0],[halfx,sqrt(x_sqr/2),0],[x,0,0],[halfx,halfx,sqrt(3/8*x_sqr)]]

def cubevert(x): return [[0,0,0],[0,x,0],[x,x,0],[x,0,0],[0,x,x],[0,0,x],[x,0,x],[x,x,x]]

def hexahedravert(x):
    x_sqr,halfx=x*x,x/2,
    z=sqrt(3/8*x_sqr)
    return [[0,0,0],[halfx,sqrt(x_sqr/2),0],[x,0,0],[halfx,halfx,z],[halfx,halfx,-z]]

def octahedravert(x):
    halfx=x/2
    return [[halfx,halfx,halfx],[0,0,0],[x,0,0],[x,x,0],[0,x,0],[halfx,halfx,-halfx]]

def decahedvertandsurface(x):
    pts=regpolygonvert(0,0,x,5,0)
    z=sqrt(distance(pts[0],pts[1])**2-x*x)
    return [[[0,0,-z]]+adddimz(pts,0)+[[0,0,z]],((1,2,0),(5,1,0),(3,4,0),(2,3,0),(4,5,0),(2,1,6),(1,5,6),(4,3,6),(3,2,6),(5,4,6))]

def dodecahedvertandsurface(x):#don't edit this it took much computation to make
    pts,pts1=floatregpolygonvert(0,0,x,5,0),floatregpolygonvert(0,0,x,5,36)
    z=sqrt(distance(pts[0],pts[1])**2-x*x)
    z1=2*x-z
    return [[[0,0,-z]]+adddimz(pts,0)+adddimz(pts1,z1-z)+[[0,0,z1]],((1,2,0),(5,1,0),(3,4,0),(2,3,0),(4,5,0),(2,1,6),(1,5,10),(4,3,8),(3,2,7),(5,4,9),(6,7,2),(7,8,3),(8,9,4),(9,10,5),(10,6,1),(7,6,11),(9,8,11),(8,7,11),(10,9,11),(6,10,11))]

def rotvec3D(roll,pitch,yaw): return (computerotvec(roll),computerotvec(pitch),computerotvec(yaw))

def perspective(vlist,rotvec,dispvec,d):#translated from C code by Roger Stevens
    rotvlist,projvlist=[],[]
    sroll,croll=rotvec[0][0],rotvec[0][1]
    spitch,cpitch=rotvec[1][0],rotvec[1][1]
    syaw,cyaw=rotvec[2][0],rotvec[2][1]
    for p in vlist:
        px,py,pz=p[0],p[1],p[2]
        x1=-cyaw*px-syaw*pz
        y1=croll*py-sroll*x1
        z1=-syaw*px+cyaw*pz
        x,y,z=croll*x1+sroll*py,spitch*z1+cpitch*y1,cpitch*z1-spitch*y1
        x+=dispvec[0]
        y+=dispvec[1]
        z+=dispvec[2]
        rotvlist.append([x,y,z])
        projvlist.append([-d*x/z,-d*y/z])
    return (rotvlist,projvlist)

def fillpolydata(polybnd,xlim,ylim):#may be slow if polygon goes offscreen
    filld,bnd={},rectboundarycoords(polybnd)
    minx,miny,maxx,maxy=bnd[0][0],bnd[0][1],bnd[1][0]+1,bnd[1][1]+1
    if (minx>=0 and miny>=0) and (maxx<=xlim and maxy<=ylim):
        for y in range(miny,maxy):
            filld.setdefault(y,[])
            for x in range(minx,maxx):
                if [x,y] in polybnd: filld[y]+=[x]
    else:
        print(bnd)
        print(sysmsg['regionoutofbounds'])
        filld=[]
    return filld

def polyboundary(vertlist):
    px,vertcount=[],len(vertlist)
    for i in range(0,vertcount):
        if i>0:
            v1,v2=roundvect(vertlist[i-1]),roundvect(vertlist[i])
            for p in iterline(v1,v2):
                if p not in px: px.append(p)
    v2,v1=roundvect(vertlist[0]),roundvect(vertlist[vertcount-1])
    for p in iterline(v1,v2):
        if p not in px: px.append(p)
    return px

def gensides(pointlists,transvect,sides):
    plist,slist,polylist,normlist=pointlists[0],pointlists[1],[],[]
    for sidepts in sides:
        u,v,w=plist[sidepts[0]],plist[sidepts[1]],plist[sidepts[2]]
        if surfacetest(u,v,w)<=0:
            polylist.append(trans([slist[i] for i in sidepts],transvect))
            normlist.append(getnormvec(u,v,w))
    return (polylist,normlist)

def spherevert(vcen,r,deganglestep):
    plist=[]
    for theta in range(0,360,deganglestep):
        for phi in range(0,180,deganglestep):
            p=addvect(vcen,spherical2rectcoord3D([r,radians(theta),radians(phi)]))
            if p not in plist: plist.append(p)
    p=[0,0,-r]
    if p not in plist: plist.append(p)
    return plist

def zlevelcoords(verlist):#we have a 3D object and we take z slices
    zlist,zord=[],{}
    for p in verlist:
        pind,z=[verlist.index(p)],p[2]
        if z not in zord:
            zord.setdefault(z,pind)
            zlist.append(z)
        else: zord[z]+=pind
    return (zlist,zord)

def genspheresurfaces(zlevelcoord):
    zl,vl=zlevelcoord[0],zlevelcoord[1]
    surf,levels=[],len(zl)-1
    northpole,southpole=vl[zl[0]][0],vl[zl[levels]][0]
    npts,spts=vl[zl[1]],vl[zl[levels-1]]
    lpts=len(npts)
    maxp,i=lpts-1,0
    for i in range(0,lpts):
        j=iif(i==maxp,0,i+1)
        surf+=[[northpole,npts[j],npts[i]],[southpole,spts[i],spts[j]]]
    if levels>2:
        mxlv=levels-1
        for k in range(1,mxlv):
            pts,adjpts=vl[zl[k]],vl[zl[k+1]]
            lpts,maxadjpts=len(pts),len(adjpts)
            maxp,i=lpts-1,0
            for i in range(0,lpts):
                j=iif(i==maxp,0,i+1)
                surf+=[[adjpts[j%maxadjpts],adjpts[i%maxadjpts],pts[i],pts[j]]]
    return surf

def spherevertandsurface(vcen,r,deganglestep):
    s=spherevert(vcen,r,deganglestep)
    return (s,genspheresurfaces(zlevelcoords(s)))

def cylindervertandsurface(vcen,r,zlen,deganglestep):
    z,i,plist,top,bottom,side=zlen/2,0,[],[],[],[]
    maxang=360+(deganglestep<<1)
    for theta in range(0,maxang,deganglestep):
        plist.append(addvect(vcen,cylindrical2rectcoord3D([r,radians(theta),-z])))
        plist.append(addvect(vcen,cylindrical2rectcoord3D([r,radians(theta),z])))
        top.append(i)
        bottom.append(i+1)
        if i>2:
            j=i-2
            side.append([i,i+1,j+1,j])
        i+=2
    top.reverse()
    return (plist,[top]+side+[bottom])

def conevertandsurface(vcen,r,zlen,deganglestep):
    z,i,bottom,side=zlen/2,1,[],[]
    maxang=360+(deganglestep<<1)
    plist=[subvect(vcen,[0,0,z])]
    for theta in range(0,maxang,deganglestep):
        plist.append(addvect(vcen,cylindrical2rectcoord3D([r,radians(theta),z])))
        bottom.append(i)
        if i>2: side.append([0,i,i-1])
        i+=1
    return (plist,side+[bottom])

def surfplot3Dvertandsurface(x1,y1,x2,y2,zscale,step):
    vlist,surf=[],[]
    for y in range(y1,y2,step):
        for x in range(x1,x2,step):
            z=x&y
            vlist.append([x,y,z])
    dx=abs(x2-x1)//step
    dx1,vl=dx-1,len(vlist)
    for v in vlist:
        i=vlist.index(v)
        idx=i+dx
        idx1=idx+1
        if (vl-idx1)>=0 and (i % dx)<dx1: surf.append([idx,idx1,i+1,i])
    return (vlist,surf)

def surfacetest(p1,p2,p3): return p1[0]*(p3[1]*p2[2]-p2[1]*p3[2])-p2[0]*(p3[1]*p1[2]-p1[1]*p3[2])-p3[0]*(p1[1]*p2[2]-p2[1]*p1[2])
