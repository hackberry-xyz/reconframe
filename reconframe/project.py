from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from . import core
from prompt_toolkit import prompt
import json

class Project:
    def __init__(self, config={}, info_types = []):
        try:
            self.name = config['name']
            self.dsn = config['dsn']
            self.config = config
            self.session = None

        except KeyError:
            self.name = 'Temporary Project'
            self.dsn = 'sqlite://'
            self.config = config

        self.engine = create_engine(self.dsn, echo = False)


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

    def __repr__(self):
        return "<\"{}\" at \"{}\">".format(self.name, self.dsn)

class Scope:
    def parseFile(file):
        with open(file, 'r') as jsonFile:
            Scope.parseJson(jsonFile.read())

    def parseJson(json_string):
        parsedJson = json.loads(json_string)
        return parsedJson

class Strategy:
    pass

