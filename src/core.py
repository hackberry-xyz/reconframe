from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from reconframe import variables

Base = declarative_base()

class Info:
    """An Information type"""

    class Model(Base):
        """Database representation of info type Info."""
        __tablename__ = "basic_info"

        id = Column(
            Integer,
            primary_key=True,
            nullable=False
        )
        info = Column(
            Text,
            nullable=False
        )

    def __init__(self, information):
        self._connections = set()
        self._raw = self.Model()
        self._raw.info = str(information)


    def register(self, engine=False):
        if(engine):
            return Base.metadata.create_all(engine)
        
        return Base

    def pattern(information):
        return True

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

    def __str__(self):
        return self._raw.info

    def __repr__(self):
        return 'Information Type: <{}>\nRaw Data: "{}"'.format(type(self).__name__, self._raw.info)
