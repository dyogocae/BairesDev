from flask import Flask
from flask_restplus import Api

class Server():
    def __init__(self, ):
        self.app = Flask(__name__, template_folder='../templates')
        self.api = Api(self.app,
            version="1.0",
            title="Flask Api",
            description="My first Flask Api",
            doc="/"
        )

    def run(self, ):
        self.app.run(
            debug=True
        )

server = Server()        