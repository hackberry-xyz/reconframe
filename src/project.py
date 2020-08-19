from sqlalchemy import create_engine, sessionmaker
from sqlalchemy import MetaData
from reconframe import http

class Project:
    def __init__(self, config={}):
        try:
            self.name = config['name']
            self.dsn = config['dsn']
        except KeyError:
            self.name = 'Temporary Project'
            self.dsn = 'sqlite://'

        self.engine = create_engine(self.dsn, echo = False)

        Session = sessionmaker(bind = self.engine)
        self.session = Session()

    def addinfo(self, obj):
        obj.register(self.engine)

        if isinstance(obj, list):
            [info.register(self.engine) for info in obj]
            self.session.add_all(obj)
        else:
            obj.register(self.engine)
            self.session.add(obj)

    def save(self):
        self.session.commit()


class Strategy:
    pass