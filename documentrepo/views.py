from documentrepo import main

# default route
# add something meaningful here.
# 
@main.route('/')
@main.route('/index')
def index():
    return "Hello, World!"

@main.route('/docs')
def list_documents():
    return {}

@main.route('/docs/<document>')
def get_document(document):
    return document
