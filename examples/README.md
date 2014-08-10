Examples
===================

1. Create tables:

    ./models.py

2. Run service:

    ./app.py

3. Give it a try:

```
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

Don't forget that you must pass a content-type header like 
"Content-Type: application/json" along w/ your request!
