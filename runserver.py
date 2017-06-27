import os
from apache_flask import app
from config import DEFAULT_HOST, DEFAULT_PORT, DEBUG


def runserver():
	port = int(os.environ.get('PORT', DEFAULT_PORT))
	app.run(host=DEFAULT_HOST, port=port, debug=DEBUG)


app.api.add_resource(app.HelloWorld, '/')

if __name__ == '__main__':
    runserver()
