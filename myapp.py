import requests
import json

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.get(url = 'http://127.0.0.1:8000/studentapi/',headers=headers,data = json_data)
    data =  r.json()
    print(data)

# get_data()

def post_data():
    data = {
        'name':'sakib',
        'roll':10,
        'sub':'sakib cse',
    }

    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.post(url = 'http://127.0.0.1:8000/studentapi/',headers=headers,data = json_data)
    data =  r.json()
    print(r)

# post_data()


def update_data():
    data = {
        'id':20,
        'name':'ccccsakib',
        'sub':'sakib cse',
    }

    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.put(url = 'http://127.0.0.1:8000/studentapi/',headers=headers,data = json_data)
    data =  r.json()
    print(r)

# update_data()

def delete_data():
    data = {
        'id':21,
    }

    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.delete(url = 'http://127.0.0.1:8000/studentapi/',headers=headers,data = json_data)
    data =  r.json()
    print(data)

delete_data()