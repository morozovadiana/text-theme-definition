from flask import Flask, jsonify, request, json
import requests
from queries import Queries
from utils import Orient
from flask_restful import Resource, Api

app = Flask(__name__)
app.queries = Queries()
api = Api(app)

def search_for_transcription(word):
    with Orient() as client:
        word = client.command(app.queries.FIND_BY_ORIGINAL.format(word))
        word = word[0].oRecordData
        return word

def query(theme):
    with Orient() as client:
        origins = client.command(app.queries.GET_ALL_ORIGINS_FROM_THEME.format(theme.capitalize()))
        origins = [x.oRecordData for x in origins]
        origins = origins[0]['origin']
    with open('text', 'r') as file:
        _content = file.read()
    result = {}
    for word in origins:
        if word in _content:
            _find = search_for_transcription(word)
            _find = {**_find, **{"count": _content.count(word)}}
            result.update({word: _find})
    return json.dumps(result)


@app.route('/find/<string:theme>')
def orient(theme):
    return query(theme)

@app.route('/search', methods=["POST"])
def search():
    data = json.loads(request.data)
    data = data["words"]
    with Orient() as client:
        themes = client.command(app.queries.GET_THEME.format(data))
    themes = [x.oRecordData['theme'] for x in themes]
    return json.dumps(themes)

if __name__ == '__main__':
    app.run()
