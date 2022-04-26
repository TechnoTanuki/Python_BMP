#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#\--------------------------------------------------------------------------/

def altsplitbuf(buf):
    m=len(buf)
    if m%2==0: m-=m&1
    return [buf[0:m-1:2],buf[1:m:2]]

def altsplitbuf3way(buf):
    m=len(buf)
    if m%3==0: m-=m&1
    return [buf[0:m-2:3],buf[1:m-1:3],buf[2:m:3]]

def altsplitbufnway(buf,n):
    retval,m,j,i=[],len(buf),n-1,0
    if m%n==0: m-=m&1
    while i<n:
        retval+=[buf[i:m-j:n]]
        i+=1
        j-=1
    return retval
