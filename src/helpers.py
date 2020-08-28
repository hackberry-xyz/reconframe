from reconframe import core
import inspect

def inform(information, info_types):
    """Parse information and guess the Info type using patterns. This function needs info_types defined. Please see help on reconframe.info_types"""
    for info_type in dir(info_types):
        if(inspect.isclass(info_type)):
            if(issubclass(info_type, core.Info)):
                if(info_type.pattern(information)):
                    return info_type(information)
   
    return core.Info(information)
