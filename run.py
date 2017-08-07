#!flask/bin/python
"""RESTful simple document repository"""
import json
from documentrepo import store
from flask import Flask
from flask import abort

main = Flask(__name__)

def get_repo():
    localstore=store.store()
    return localstore

# default route
# add something meaningful here.
# 
@main.route('/')
@main.route('/index')
def index():
    return "Hello, World!"

# list all document items in collection
# 
@main.route('/docs')
def list_documents():
    return json.dumps(get_repo().list_docs())

# fetch a particular document item
#
@main.route('/docs/<document>')
def get_document(document):
    try:
        return json.dumps(get_repo().get_document(document))
    except KeyError as e:
        abort(404)




main.run(debug=True)