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

#Educational or hobby use highly encouraged.

from .mathlib import sign,subvect,addvect,mirror1stquad,computerotvec,roundvect,rotvec2D,combination,scalarmulvect,iif,setmax,radians,sin,cos,roundvectlist,rect2polarcoord2Dwithcenter,pivotlist

def itercirclepart(r):
    row,col,r_sqr=r,0,r*r
    two_r_sqr,four_r_sqr=r_sqr<<1,r_sqr<<2
    d=two_r_sqr*((row-1)*(row))+r_sqr+two_r_sqr*(1-r_sqr)
    while row>=col:
        yield([col,row])
        if row!=col: yield([row,col])
        if d>=0:
            row-=1
            d-=four_r_sqr*(row)
        d+=two_r_sqr*(3+(col<<1))
        col+=1

def itercirclepart1(r):
    row,col,r_sqr=r,0,r*r
    two_r_sqr,four_r_sqr=r_sqr<<1,r_sqr<<2
    d=two_r_sqr*((row-1)*(row))+r_sqr+two_r_sqr*(1-r_sqr)
    while row>=col:
        yield([col,row])
        if d>=0:
            row-=1
            d-=four_r_sqr*(row)
            d+=two_r_sqr*(3+(col<<1))
            col+=1

def itercirclepartlineedge(r):
    row,col,r_sqr=r,0,r*r
    two_r_sqr,four_r_sqr=r_sqr<<1,r_sqr<<2
    d=two_r_sqr*((row-1)*(row))+r_sqr+two_r_sqr*(1-r_sqr)
    y=[]
    while row>=col:
        if col not in y:
            yield([row,col])
            y+=[col]
        if d>=0:
            if row not in y:
                yield([col,row])
                y+=[row]
            row-=1
            d-=four_r_sqr*(row)
        d+=two_r_sqr*(3+(col<<1))
        col+=1

def itercirclepartvertlineedge(r):
    row,col,r_sqr=r,0,r*r
    two_r_sqr,four_r_sqr=r_sqr<<1,r_sqr<<2
    d=two_r_sqr*((row-1)*(row))+r_sqr+two_r_sqr*(1-r_sqr)
    x=[]
    while row>=col:
        if col not in x:
            yield([col,row])
            x+=[col]
        if row not in x:
            yield([row,col])
            x+=[row]
        if d>=0:
            row-=1
            d-=four_r_sqr*(row)
        d+=two_r_sqr*(3+(col<<1))
        col+=1

def iterline(p1,p2):
    p3=subvect(p2,p1)
    dx,dy=p3[0],p3[1]
    sdx,sdy,dxabs,dyabs=sign(dx),sign(dy),abs(dx),abs(dy)
    x,y,px,py=0,0,p1[0],p1[1]
    if dxabs>=dyabs:
        ilim=dxabs+1
        for i in range(0,ilim):
            y+=dyabs
            if y>=dxabs:
                y-=dxabs
                py+=sdy
            yield([px,py])
            px+=sdx
    else:
        ilim=dyabs+1
        for i in range(0,ilim):
            x+=dxabs
            if x>=dyabs:
                x-=dyabs
                px+=sdx
            yield([px,py])
            py+=sdy
    yield p2

def iterparallelogram(p1,p2,p3):
    p,q=lineseg(p1,p3),lineseg(p2,addvect(p3,subvect(p2,p1)))
    for u,v in zip(p,q): yield [u,v]

def lineseg(p1,p2): return [p for p in iterline(p1,p2)]

def iterellipsepart(b,a):
    row,col,a_sqr,b_sqr=b,0,a*a,b*b
    two_a_sqr,four_a_sqr=a_sqr<<1,a_sqr<<2
    two_b_sqr,four_b_sqr=b_sqr<<1,b_sqr<<2
    d=two_a_sqr*((row-1)*row)+a_sqr+two_b_sqr*(1-a_sqr)
    while row*a_sqr>=col*b_sqr:
        yield [col,row]
        if d>=0:
            row-=1
            d-=four_a_sqr*row
        d+=two_b_sqr*(3+(col<<1))
        col+=1
    d=two_b_sqr*((col-1)*(col))+two_a_sqr*(row*(row-2)+1)+(1-two_a_sqr)*b_sqr
    while (row+1)>0:
        yield [col,row]
        if d>=0:
            col+=1
            d-=four_b_sqr*col
        d+=two_a_sqr*(3+(row<<1))
        row-=1

def iterellipse(x,y,b,a):
    for p in iterellipsepart(b,a):
         for v in mirror1stquad(x,y,p): yield v

def iterellipserot(x,y,b,a,degrot):
    rotvec,c=computerotvec(degrot),[x,y]
    for p in iterellipsepart(b,a):
         for v in mirror1stquad(x,y,p): yield roundvect(addvect(rotvec2D(subvect(v,c),rotvec),c))

def itercircle(x,y,r):
    for p in itercirclepart(r):
         for v in mirror1stquad(x,y,p): yield v

def bezierblend(i,n,u): return combination(n,i)*(u**i)*((1-u)**(n-i))

def iterbeziercurve(pntlist):
    i,cnt,v=0,len(pntlist),pntlist[0]
    w,klim=v,cnt<<2
    while i<cnt:
        if i>cnt-2:
            last=i-1
            for k in range(0,klim):
                u,v=k/klim,[0,0]
                for j in range(0,i):
                    v=addvect(v,scalarmulvect(pntlist[j],bezierblend(j,last,u)))
                for pnt in iterline(roundvect(v),roundvect(w)): yield pnt
                w=v
        i+=1

def beziercurvevert(pntlist,isclosed,curveback): return [v for v in iterbeziercurve(pntlist)]

def iterbspline(pntlist,isclosed,curveback):
    i,cnt,v=0,len(pntlist),pntlist[0]
    w,klim,ilim,mx=v,cnt<<2,cnt+iif(isclosed,2,0),cnt-1
    while i<ilim:
        for k in range(0,klim):
            u,v=k/klim,[0,0]
            nc=bsplineblend(u)
            for j in range(0,4):
                k=i+j
                v=addvect(v,scalarmulvect(pntlist[iif(curveback,k%cnt,setmax(k,mx))],nc[j]))
            if i>1:
                for pnt in iterline(roundvect(v),roundvect(w)): yield pnt
            w=v
        i+=1

def bsplinevert(pntlist,isclosed,curveback): return [v for v in iterbspline(pntlist,isclosed,curveback)]

def bsplineblend(u):#dont edit this square shaped code
    u2,u3= u*u,u*u*u
    d,f = u3/6 , 1/6
    a=-d +u2/2-u/2+f
    b= u3/2 -u2 +2/3
    c=(-u3+u2+u)/2+f
    return (a,b,c,d)

def recvert(x1,y1,x2,y2): return [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]

def floatregpolygonvert(cx,cy,r,sides,angle):
    v,angle,anginc,maxang=[],radians(angle),360//sides,360
    for a in range(0,maxang,anginc):
        ang=angle+radians(a)
        v.append([int(cx-r*sin(ang)),int(cy-r*cos(ang))])
    return v

def regpolygonvert(cx,cy,r,sides,angle): return roundvectlist(floatregpolygonvert(cx,cy,r,sides,angle))

def horizontalvert(y,x1,x2,dx): return [[x,y] for x in range(x1,x2,dx)]

def verticalvert(x,y1,y2,dy): return [[x,y] for y in range(y1,y2,dy)]

def circlevert(x,y,r): return [v for v in itercircle(x,y,r)]

def arcvert(x,y,r,startdegangle,enddegangle,showoutline):
    v,tol,c,sa,ea=[],0.03,(x,y),radians(startdegangle),radians(enddegangle)
    for p in itercircle(x,y,r):
        pc=rect2polarcoord2Dwithcenter(c,p)
        a=pc[1]
        if a>=sa and a<=ea:
            v.append(p)
            if abs(a-sa)<tol or abs(a-ea)<tol: #for larger arcs tol may be >0.03
                for np in iterline(c,p): v.append(np)
    return v

def rectboundarycoords(vlist):
    u=pivotlist(vlist)
    x,y=u[0],u[1]
    return ((min(x),min(y)),(max(x),max(y)))
