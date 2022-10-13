import os
import flask
from flask import jsonify, request, render_template
import redis
import uuid
import json

app = flask.Flask(__name__)
redisPort = port=os.getenv('REDIS_PORT')

# Create some test data for our catalog in the form of a list of dictionaries.
books = {
    'data': [
        {'id': 1,
         'title': 'The Ones Who Walk Away From Omelas',
         'author': 'Ursula K. Le Guin',
         'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
         'published': '1973'},
        {'id': 2,
         'title': 'Dhalgren',
         'author': 'Samuel R. Delany',
         'first_sentence': 'to wound the autumnal city.',
         'published': '1975'}
    ]
}

def createRedisClient(host: str, port: int, db=0):
    return redis.Redis(host=host, port=port, db=db)

@app.errorhandler(404)
def page_not_found(e): # e must be in there
    # note that we set the 404 status, this is what it catches
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def home():
    return '''Hello Flask\n'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/books', methods=['GET'])
def books():
    return jsonify({'id': 1,
         'title': 'The Ones Who Walk Away From Omelas',
         'author': 'Ursula K. Le Guin',
         'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
         'published': '1973'})

@app.route('/api/v1/books', methods=['POST'])
def createBook():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        id = str(uuid.uuid4())
        json['_id'] = id
        str_val = str(json)
        client = createRedisClient('redis', int(redisPort))
        client.set(id, str_val)
        return json
    else:
        return 'Content-Type not supported!'

@app.route('/api/v1/books/<id>', methods=['GET'])
def getBook(id: str):
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        client = createRedisClient('redis', int(redisPort))
        str_val = client.get(id).decode("UTF-8")
        if (str_val is not None):
            json_object = json.loads(json.dumps(str_val))
            return json_object
        return page_not_found()
    else:
        return 'Content-Type not supported!'



if __name__ == "__main___":
    app.run(debug=True, host='0.0.0.0')
