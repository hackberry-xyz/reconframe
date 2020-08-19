import click
import proxy as proxy_py

class Proxy:
    def __init__(self, port=8899):
        self.config = [
            '--port', str(port),
            '--log-level', 'CRITICAL',
        ]

        self.address = "0.0.0.0:{}".format(port)

    def start(self, callback=False, **kwargs):
        if(callable(callback)):
            with proxy_py.start(self.config):
                return callback(**kwargs)

        proxy_py.main(self.config)
