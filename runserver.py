import os
from apache_flask import app, api, HelloWorld
from config import DEFAULT_HOST, DEFAULT_PORT, DEBUG


def runserver():
	port = int(os.environ.get('PORT', DEFAULT_PORT))
	app.run(host=DEFAULT_HOST, port=port, debug=DEBUG)


api.add_resource(HelloWorld, '/HelloWorld/')

if __name__ == '__main__':
    runserver()
