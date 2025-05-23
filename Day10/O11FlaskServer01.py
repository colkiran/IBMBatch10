from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

    # get is used to retrieve or read data from the server
    def get(self):
        return {"Message" : "Hello World"}


api.add_resource(HelloWorld, "/helloworld")

if __name__ == '__main__':
    app.run(debug=True, use_reloader = True)