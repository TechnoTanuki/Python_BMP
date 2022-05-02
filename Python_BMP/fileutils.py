#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#\--------------------------------------------------------------------------/

from os.path import isfile
from .messages import sysmsg

def checklink(func):
    """Decorator to test if first parameter in a function is a valid file

    Args:
        function
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        if isfile(args[0]):  
            return(func(*args,**kwargs))
        else: 
            print(sysmsg['filenotexist'])
    return(callf)

def checklinks(func):
    """Decorator to test if two parameters in a function are valid files

    Args:
        function
        
    Returns:
        caller function

    """
    def callf(*args,**kwargs):
        if isfile(args[0]) and isfile(args[1]):  
            return(func(*args,**kwargs))
        else: 
            print(sysmsg['filenotexist'])
    return(callf)