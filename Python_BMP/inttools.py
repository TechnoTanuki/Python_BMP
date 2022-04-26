from array import array

def writeint(offset,cnt,arr,value):
    j=cnt-1
    for i in range(0,j):
        b=value&0xff
        arr[offset+i]=b
        value=value>>8

def readint(offset,cnt,arr):
    v,j=0,cnt-1
    for i in range(0,j): v+=arr[offset+i]<<(i<<3)
    return v

def int2buf(cnt,value): return array('B',[(value>>(i*8))&0xff for i in range(0,cnt)])

def buf2int(buf):
    v,j=0,len(buf)-1
    for i in range(0,j): v+=buf[i]<<(i<<3)
    return v
