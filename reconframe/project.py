from sqlalchemy import create_engine
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
