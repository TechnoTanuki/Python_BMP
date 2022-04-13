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
#
#ps:created out of extreme boredom during the COVID-19 pandemic.
#
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        mx=1024
        my=768
        file='Hello_3D.bmp'
        bmp=b.newBMP(mx,my,24)
        maxpt,cenpt=b.bottomrightcoord(bmp),b.centercoord(bmp) #bitmap dependent coords
        c,cf,lum=b.getcolorname2RGBdict(),b.getRGBfactors(),b.getdefaultlumrange() #color info
        b.adjustcolordicttopal(bmp,c)
        
        d,tvect=200,[0,0,100]#be careful with these variables or object goes offscreen
        sd=b.getshapesidedict()
        pts=b.tetrahedravert(80)
        shapes=[[[b.trans(b.cubevert(30),pts[3]),sd["cube"]],cf["darkblue"],True,c['black']],[[b.trans(b.tetrahedravert(30),pts[2]),sd["tetrahedra"]],cf["darkred"],True,c['white']],[[b.trans(b.octahedravert(20),pts[1]),sd["octahedra"]],cf["yellow"],True,c['darkgray']],[[b.trans(b.hexahedravert(30),pts[0]),sd["hexahedra"]],cf["darkgreen"],True,c['darkgreen']]]
        for s in shapes:
                b.plot3Dsolid(bmp,s[0],True,s[1],s[2],s[3],b.rotvec3D(10,5,5),tvect,d,b.addvect(cenpt,[-160,-10]))
                b.plot3Dsolid(bmp,b.decahedvertandsurface(25),True,cf['brightred'],False,0,b.rotvec3D(7,77,20),tvect,d,b.addvect(cenpt,[280,-250]))
                b.plot3Dsolid(bmp,b.dodecahedvertandsurface(25),True,cf['brightwhite'],False,0,b.rotvec3D(70,7,20),tvect,d,b.addvect(cenpt,[+60,-130]))
                b.plot3Dsolid(bmp,b.spherevertandsurface([5,0,0],60,10),True,cf['brightwhite'],False,0,b.rotvec3D(190,145,70),tvect,d,b.addvect(cenpt,[300,-50]))
                b.plot3Dsolid(bmp,b.cylindervertandsurface([1,0,0],20,10,5),True,cf['brightyellow'],True,b.RGB2int(20,20,0),b.rotvec3D(60,74,72),tvect,d,b.addvect(cenpt,[-200,-50]))
                b.plot3Dsolid(bmp,b.conevertandsurface([1,0,0],20,15,5),True,cf['brightorange'],False,b.RGB2int(20,20,0),b.rotvec3D(6,67,2),tvect,d,b.addvect(cenpt,[-300,-150]))
                b.plot3Dsolid(bmp,b.surfplot3Dvertandsurface (-35,-35,35,35,15,5),True,cf['brightcyan'],True,0,b.rotvec3D(20,67,30),tvect,d,b.addvect(cenpt,[-420,-25]))
                b.saveBMP(file,bmp)
        print('Saved '+ file )
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()


