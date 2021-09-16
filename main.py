from flask import Flask

import logging

app = Flask(__name__)


@app.route('/')
def helloWorld():
    logging.warning('TEST INITIATE LOGGING ... !')
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)