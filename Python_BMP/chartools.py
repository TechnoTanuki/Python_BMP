def enumletters(st):
    c,i=len(st),0
    while i<c:
        yield st[i:i+1]
        i+=1

def enumreverseletters(st):
    i=len(st)-1
    while i>-1:
        yield st[i:i+1]
        i-=1

def char2int(charcodestr):
    place,strhash=0,0
    for c in enumletters(charcodestr):
        strhash=strhash+ord(c)*(256**place)
        place+=1
    return strhash