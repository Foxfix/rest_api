from flask import Flask 
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

class Link(Resource):
	def get(self, url):
		return {'link': url}


api.add_resource(Student, '/link/<string:url>')

app.run(port=5000)