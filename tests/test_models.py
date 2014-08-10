
import pytest
import tempfile
import json

from flask import Flask
from flask.ext.saresource import SAResource

from sqlalchemy import create_engine
from models import sqlalchemy_session
from models import Base
from models import Todo

@pytest.fixture()
def app_fixture(request):
    fapp = Flask('test')
    fapp.testing = True
    app = fapp.test_client()

    db_fd, db_fn = tempfile.mkstemp()
    db_uri = 'sqlite:///%s' % db_fn
    db_engine = create_engine(db_uri)
    db_session = sqlalchemy_session(db_uri)
    Base.metadata.create_all(bind=db_engine)

    # add model API
    api = SAResource(fapp, db_session)
    api.add_resource(Todo)

    def fin():
        # close and delete sqlite db file
        Base.metadata.drop_all(bind=db_engine)
    request.addfinalizer(fin)
    return app

def test_get(app_fixture):
    rv = app_fixture.get('/api/todos')
    assert rv.data == '[]'

def test_post(app_fixture):
    rv = app_fixture.get('/api/todos')
    assert rv.data == '[]'

    data = { 'task': 'eat icecream' }
    rv = app_fixture.post('/api/todos', data=data)
    assert 'id' in rv.data
    assert 'eat icecream' in rv.data

    rv = app_fixture.get('/api/todos')
    assert 'eat icecream' in rv.data
    assert len(json.loads(rv.data)) == 1

def test_put(app_fixture):
    data = { 'task': 'eat icecream' }
    rv = json.loads(app_fixture.post('/api/todos', data=data).data)
    assert rv['task'] == 'eat icecream'

    datad = { 'task': 'do NOT eat icecream' }
    rv = json.loads(app_fixture.put('/api/todos/1', data=datad).data)
    assert rv['task'] == datad['task']

    rv = app_fixture.get('/api/todos')
    assert 'eat icecream' in rv.data
    assert len(json.loads(rv.data)) == 1

def test_delete(app_fixture):
    data = { 'task': 'eat icecream' }
    rv = json.loads(app_fixture.post('/api/todos', data=data).data)
    assert rv['task'] == 'eat icecream'

    rv = app_fixture.delete('/api/todos/1')

    rv = app_fixture.get('/api/todos')
    assert len(json.loads(rv.data)) == 0

