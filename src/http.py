from reconframe.core import Base, Info

class Request(Info):
    def pattern(information):
        return True

class Response(Info):
    pass

class Host(Info):
    pass

class Endpoint(Info):
    pass

class Body(Info):
    pass

class Header(Info):
    pass

def request(**kwargs):
    """This function builds up a Request info type by parsing a string, file or data yielded by a proxy (See help on reconframe.proxy.HTTP)."""
    pass

def response(**kwargs):
    """This function builds up a Response info type by parsing a string, file or data yielded by a proxy (See help on reconframe.proxy.HTTP)."""
    pass
