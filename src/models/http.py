from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from io import BytesIO
import pycurl


Base = declarative_base()

request_body = Table('request_body', Base.metadata,
    Column('request_id', Integer, ForeignKey('httprequests.id')),
    Column('body_id', Integer, ForeignKey('httpbody.id'))
)

response_body = Table('response_body', Base.metadata,
    Column('response_id', Integer, ForeignKey('httpresponses.id')),
    Column('body_id', Integer, ForeignKey('httpbody.id'))
)


class Host(Base):
    __tablename__ = 'hosts'
    id = Column(Integer, primary_key=True)
    domain = Column(String)
    port = Column(Integer)
    https = Column(Boolean)
    ip = Column(String)
    endpoints = relationship("Endpoint")

    def __repr__(self):
        return "{0}://{1}:{2} ({3})".format(("https" if self.https else "http"), self.domain, self.port, self.ip)
   

class Endpoint(Base):
    __tablename__ = 'endpoints'
    id = Column(Integer, primary_key=True)
    host = Column(Integer, ForeignKey('hosts.id'))
    path = Column(String)
    endpoints = relationship("Request")
    

class Body(Base):
    __tablename__ = 'httpbody'
    id = Column(Integer, primary_key=True)
    content = Column(String(16 * (10**6)))
    content_type = Column(String)                   
    requests = relationship("Request", secondary=request_body)
    responses = relationship("Response", secondary=response_body)


class RequestHeader(Base):
    __tablename__ = 'http_request_headers'
    id = Column(Integer, primary_key=True)
    header = Column(String)
    value = Column(String)
    request = Column(Integer, ForeignKey('httprequests.id'))

class ResponseHeader(Base):
    __tablename__ = 'http_response_headers'
    id = Column(Integer, primary_key=True)
    header = Column(String)
    value = Column(String)
    response = Column(Integer, ForeignKey('httpresponses.id'))


class Request(Base):
    __tablename__ = 'httprequests'
    id = Column(Integer, primary_key=True)
    method = Column(String)
    endpoint = Column(Integer, ForeignKey('endpoints.id'))
    response = relationship("Response")
    headers = relationship("RequestHeader")

    def prepare(self, url=False):
        self.buffer = BytesIO()
        self.curl = pycurl.Curl()
        self.curl.setopt(self.curl.URL, self.getUrl() if url else self.getIp())
        self.curl.setopt(self.curl.WRITEDATA, buffer)
        return self.curl        

    def dispatch(self):
        if(self.curl):
            self.curl.perform()
            self.curl.close()
            body = buffer.getvalue()
            print(body)
        else:
            raise Exception("cURL reqeust not ready!")

    def getUrl(self):
        return 'https://google.com'

    def getIp(self):
        return '127.0.0.1'


class Response(Base):
    __tablename__ = 'httpresponses'
    id = Column(Integer, primary_key=True)
    request = Column(Integer, ForeignKey('httprequests.id'))
    status = Column(Integer)
    headers = relationship("ResponseHeader")
