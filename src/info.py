from abc import ABC, abstractmethod
from sqlalchemy.ext.declarative import declarative_base
from reconframe import variables

class Info(ABC):
    """An information object"""
    _base = declarative_base()

    def register(self, engine=False):
        if(engine):
            return self._base.metadata.create_all(engine)
        return _base

    @abstractmethod
    def pattern(information):
        return True


class InfoNode:
    """An Information node pointing to connected nodes"""

    def __init__(self, info):
        self._info = inform(info)
        self._connections = set()


    def connect(self, info_node):
        """Connect to another node"""
        if(isinstance(info_node, InfoNode)):
            self._connections.add(info_node)
        else:
            info_node = InfoNode(info_node)
            self._connections.add(info)

    def disconnect(self, info_node):
        self._connections.remove(info)

    def connections(self):
        return self._connections


class InfoGraph:
    """An Information node cluster denoting information about the cluster"""
    pass

def register_info_type(infotype):
    if(issubclass(infotype, Info)):
        variables.__info_types__.add(Info)
        variables.__info_types__ = variables.__info_types__ - {Info}
    else:
        raise Exception("Not an Info Type")


def inform(information):
    """parse information and guess the Info type using patterns"""
    for info_type in _info_types:
        if(info_type.pattern(information)):
            return info_type(information)
        else:
            return Info(information)