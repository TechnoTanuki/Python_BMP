from time import process_time_ns

def elaspedtimeinseconds(inittime):
    return (process_time_ns()-inittime)/1000000000
        
def hhmmsselaspedtime(inittime):
    secs,ns=divmod((process_time_ns()-inittime),1000000000)
    mins,secs=divmod(secs,60)
    hrs,mins=divmod(mins,60)
    return str(hrs).zfill(2)+':'+str(mins).zfill(2)+':'+str(secs).zfill(2)+ '.'+str(ns)
        
def functimer(func):
    def callf(*args,**kwargs):
        print('Applying '+func.__name__+ ' please wait...')
        inittime=process_time_ns()
        r=func(*args,**kwargs)
        print("Done in: "+hhmmsselaspedtime(inittime)) 
        return(r)
    return(callf)
