#!/usr/bin/env python

from flask import Flask
from flask.ext.resource import SAResource
from models import db_session
from models import Todo
 
app = Flask(__name__)

api = SAResource(app, db_session, url_prefix='/api/v0.1')

# registers GET/POST/DELETE/PUT endpoints at '/api/v0.1/todos' (tablename used for url by default)
api.add_resource(Todo)
 
app.run(debug=True)
