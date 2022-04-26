
def dict2descorderlist(d: dict) -> list:
    l=[]
    for k in d: l.append([d[k],k])
    l.sort()
    l.reverse()
    return l