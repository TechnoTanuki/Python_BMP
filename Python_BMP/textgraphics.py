from BITMAPlib import getcolorbits,getmaxy,getxcharcount,gethdrsize,iif

def plotbitsastext(bits):
    mask=128
    while mask>0:
        if (mask & bits)==0: print(' ',end='')
        else: print('*',end='')
        mask=mask>>1

def plotbmpastext(bmp):#cant output 24 bit bmp
    bits,my,r,offset=getcolorbits(bmp),getmaxy(bmp)-1,getxcharcount(bmp),gethdrsize(bmp)
    for y in range(my,0,-1):
        for x in range(0,r):
            if bits==1: plotbitsastext(bmp[offset+r*y+x])
            if bits==4:
                c0,c1=divmod(bmp[offset+r*y+x],16)
                print(chr(97+c0)+chr(97+c1),end='')
            if bits==8: print(chr(bmp[offset+r*y+x]),end='')
        print()

def plot8bitpatternastext(bitpattern,onechar,zerochar):
    s=""
    for bits in bitpattern:
        mask=128
        while mask>0:
            s+=iif(mask & bits>0,onechar,zerochar)
            mask=mask>>1
        s+='\n'
    return s
