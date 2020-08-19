from reconframe.info import Info

class Request(Info):
    pass

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
	"""expects named arguments - method, url, headers and a body"""
	pass

def response(**kwargs):
	"""expects named arguments - method, url, headers and a body"""
	pass
