from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from reconframe.info import register_info_type
from reconframe.http import Request, Response, Host, Endpoint, Body, Header
from prompt_toolkit import prompt
import json

class Project:
    def __init__(self, config={}, info_types = []):
        try:
            self.name = config['name']
            self.dsn = config['dsn']
            self.config = config
        except KeyError:
            self.name = 'Temporary Project'
            self.dsn = 'sqlite://'
            self.config = config

        self.engine = create_engine(self.dsn, echo = False)

        
        [register_info_type(info_type) for info_type in info_types]

    def addinfo(self, obj):
        obj.register(self.engine)

        if(not self.session):
            Session = sessionmaker(bind = self.engine)
            self.session = Session()

        if isinstance(obj, list):
            [info.register(self.engine) for info in obj]
            self.session.add_all(obj)
        else:
            obj.register(self.engine)
            self.session.add(obj)

    def save(self):
        if(not self.session):
            return False
        self.session.commit()
        return True

    def toJson(self):
        return json.dumps(self.config)


class Strategy:
    pass

