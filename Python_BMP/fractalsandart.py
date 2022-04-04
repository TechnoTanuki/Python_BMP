from Python_BMP.BITMAPlib import getmaxcolors,plotxybit,sortrecpoints,bmpcolorbits,colormix,random,iif,isinBMPrectbnd,isinrectbnd,radians,cos,sin,range2baseanddelta,setmax,distance

def getIFSparams(): return {'fern':(((0,0,0,.16,0,0),(.2,-.26,.23,.22,0,1.6),(-.15,.28,.26,.24,0,.44),(.85,.04,-.04,.85,0,1.6)),(.009,.073,.137,1)),'tree':(((0,.2,0,.5,0,0),(.1,0,0,.1,0,.2),(.42,-.42,.42,.42,0,.2),(.42,.42,-.42,.42,0,.2)),(.05,.2,.6,1)),'cantortree':(((1/3,0,0,1/3,0,0),(1/3,0,0,1/3,1,0),(2/3,0,0,2/3,0.5,0.5),(0,0,0,0,0,0)),(1/3,2/3,1,1)),'sierpinskitriamgle':(((.5,0,0,.5,0,0),(.5,0,0,.5,1,0),(.5,0,0,.5,.5,.5),(0,0,0,0,0,0)),(1/3,2/3,1,1))}

def mandelparamdict(): return {'maxdefault':(1.75,-1.75,1.5,-1.5),'maxeqdim':(1.75,-1.75,1.75,-1.75),'middefault':(.75,-1.25,1.25,-1.25),'mindefault':(.75,-.75,.5,-.5),'mineqdim':(.5,-.5,.5,-.5),'custom1':(-.5,-.7,-.5,-.7)}

def mandelbrot(bmp,x1,y1,x2,y2,mandelparam,RGBfactors,maxiter):
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

def IFS(bmp,IFStransparam,x1,y1,x2,y2,xscale,yscale,xoffset,yoffset,color,maxiter):
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
    for nr in range (r,2,-1): plotflower(bmp,cx,cy,nr,petals,angrot,lumrange,RGBfactors)
