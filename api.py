from flask import Flask
from flask_restful import Resource, Api
from app.HelloWorld.hello_world import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/hello_world', '/hello', '/helloworld')

if __name__ == '__main__':
    app.run(debug=True)