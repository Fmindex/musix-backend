from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('bofy')

class HelloWorld(Resource):
	def post(self):
		args = parser.parse_args()
		print(args)
		return "POST", 200

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
	app.run(debug=True)