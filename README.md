Flask-SAResource
===========

Introduction
------------

Flask-SAResource leverages SQLAlchemy declarative models to create RESTful API endpoints on 
your [Flask](http://flask.pocoo.org/) application.

Flask-SAResource relies heavily on [Flask-Restful](https://github.com/twilio/flask-restful) 
to expose your SQLAlchemy models as class-based views, with an easier API for 
adding pre- and post-processors than [Flask-Restless](https://github.com/jfinkels/flask-restless)
provides.

Examples
--------
Check the *examples* folder. Contributions are welcome via GitHub as pull-requests.

```
#models.py:

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    task = Column(String(255))

# app.py:

from flask import Flask
from flask.ext.resource import SAResource
from models import Todo, db_session

app = Flask(__name__)
api = SAResource(app, db_session, url_prefix='/api/v0.1')
api.add_resource(Todo)

app.run(debug=True)
```

Now you have the following available as RESTful API endpoints:

```
$ python
>> import requests, json
>> requests.get('http://localhost:5000/todos').json()
[]

>> requests.post('http://localhost:5000/todos',
                 headers={'Content-Type': 'application/json'},
                 data=json.dumps({'task': 'go outside!'})).json()
{u'id': 1, u'task': u'go outside!', u'uri': u'http://localhost:5000/todos/1'}

>> requests.get('http://localhost:5000/todos/1').json()
{u'id': 1, u'task': u'go outside!', u'uri': u'http://localhost:5000/todos/1'}

>> requests.put('http://localhost:5000/todos/1',
                headers={'Content-Type': 'application/json'},
                data=json.dumps({'task': 'go to the gym'})).json()
{u'id': 1, u'task': u'go to the gym', u'uri': u'http://localhost:5000/todos/1'}

>> requests.delete('http://localhost:5000/todos/1')
>> requests.get('http://localhost:5000/todos').json()
[]
```

Installation
------------
To install Flask-SAResource, simply:

    pip install Flask-SAResource

To make sure you have the latest version, run:

    pip install -U Flask-SAResource

Or alternatively, you can download the repository and install manually by doing:

    git clone git@github.com:mmautner/flask-saresource.git
    cd flask-saresource
    python setup.py install

Tests
-----
Run tests using the py.test test-runner:

    /path/to/project$ pip install pytest
    /path/to/project$ py.test
    
Testing and issue contributions are welcome!
