from flask import Flask
from .dictionary import Lookup

app = Flask(__name__)

@app.route('/correct/<word>', methods=['GET'])
def index(word):
    correction = Lookup(word)

    return '{"correction": "%s"}' % correction
