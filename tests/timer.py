import time as t
def elaspedtimeinseconds(inittime):
    return (t.process_time_ns()-inittime)/1000000000

def hhmmsselaspedtime(inittime):
        secs,ns=divmod((t.process_time_ns()-inittime),1000000000)
        mins,secs=divmod(secs,60)
        hrs,mins=divmod(mins,60)
        return str(hrs).zfill(2)+':'+str(mins).zfill(2)+':'+str(secs).zfill(2)+ '.'+str(ns)

def printelapsedtime(inittime):
    print("runtime:",hhmmsselaspedtime(inittime)) 

def functimer(func):
    def callf(*args,**kwargs):
        inittime=t.process_time_ns()
        r=func(*args,**kwargs)
        printelapsedtime(inittime)
        return(r)
    return(callf)

def funcreccount(func):
    def callf(*args,**kwargs):
        r=func(*args,**kwargs)
        print('Returned ',len(r),' item(s)')
        return(r)
    return(callf)