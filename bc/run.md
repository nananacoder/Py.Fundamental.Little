### test

1. fire up the server:
```commandline
$ python3 flask_server.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

2. make a POST request:
```commandline
$ curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new"
```