import os
from flask import Flask, request, redirect, url_for, Response
from werkzeug.utils import secure_filename
from flask_restful import Resource, Api
import json
from flask_cors import CORS


UPLOAD_FOLDER = 'upload/'
ALLOWED_EXTENSIONS = set(['wav'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)
api = Api(app)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class HelloWorld(Resource):
	def get(self):
		response = Response(
		    response=json.dumps(dict(err='no file')), 
		    status=400, mimetype='application/json')
		return response

	def post(self):
		print(request.form)
		file = request.files['file']
		# if user does not select file, browser also
		# submit a empty part without filename
		if file.filename == '':
		    print('No selected file')
		    return redirect(request.url)
		if file and allowed_file(file.filename):
		    filename = secure_filename(file.filename)
		    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		    return redirect(url_for('uploaded_file',
		                            filename=filename))
		response = Response(
		    response=json.dumps(dict(kuy='nivit')), 
		    status=400, mimetype='application/json')
		return response


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
	app.run(debug=True)