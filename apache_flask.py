from flask import Flask, make_response, render_template, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# #from commontools import log
#
#
# @app.route('/')
# def index():
# 	return render_template('index.html')
#
#
# @app.route('/hello')
# def hello():
#     return render_template('hello.html')
#
#
# @app.errorhandler(500)
# def internal_error(error):
# 	reply = []
# 	return jsonify(reply)
#
#
# @app.errorhandler(404)
# def not_found(error):
# 	return make_response(jsonify( { 'error': 'Not found' } ), 404)
