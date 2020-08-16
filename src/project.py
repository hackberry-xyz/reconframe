from sqlalchemy import create_engine, sessionmaker
from sqlalchemy import MetaData
from .models import http

class Project:
    def __init__(self, config={}, models=[]):
        try:
            self.name = config['name']
            self.dsn = config['dsn']
            self.models = models
        except KeyError:
            self.name = 'Temporary Project'
            self.dsn = 'sqlite://'
            self.models = [http]

        self.engine = create_engine(self.dsn, echo = False)

        for model in self.models:
            model.Base.metadata.create_all(self.engine)

        Session = sessionmaker(bind = self.engine)
        self.session = Session()

    def addinfo(self, obj):
        if isinstance(obj, list):
            self.session.add_all(obj)
        else:
            self.session.add(obj)

    def save(self):
        self.session.commit()
