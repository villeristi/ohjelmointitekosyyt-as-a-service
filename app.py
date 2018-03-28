from flask import Flask, make_response, url_for, jsonify
import random
from excuses import *

app = Flask(__name__)


def response_with(response, status=200):
    """
    Format response to JSON
    :param response: dict
    :param status: integer
    :return: Response
    """
    return make_response(jsonify(response), status)


def get_random_excuse():
    """
    Get random from list
    :return:
    """
    return excuses[random.randint(1, len(excuses) - 1)]


@app.route('/', methods=['GET'])
def index():
    """
    Display routes
    :return Response:
    """
    res = {
        'routes': {
            '/random': {
                'endpoint': url_for('get_random', _external=True),
                'description': 'Random tekosyy'
            },
            '/list': {
                'endpoint': url_for('list_all', _external=True),
                'description': 'Kaikki tekosyyt'
            },
            '/search': {
                'endpoint': url_for('filtered_list', query='markkinointi', _external=True),
                'description': 'Filtteröi hakusanalla'
            }
        },
        'original_idea_by': {
            'name': 'Ville Säävuori',
            'twitter': '@uninen'
        },
        'rest_functionality_by': {
            'name': 'Ville R.',
            'twitter': '@villeristi'
        }
    }
    return response_with(res)


@app.route('/random', methods=['GET'])
def get_random():
    """
    Random excuse
    :return Response:
    """
    res = {'excuse': get_random_excuse()}
    return response_with(res)


@app.route('/list', methods=['GET'])
def list_all():
    """
    List all
    :return Response:
    """
    return response_with(excuses)


@app.route('/filter/<query>', methods=['GET'])
def filtered_list(query):
    """
    Search
    :return Response:
    """
    filtered = [ex for ex in excuses if query in ex.lower()]

    if len(filtered) == 0:
        return response_with({'excuse': 'Sry, ei tekosyitä termille: {}'.format(query)})

    res = {'excuses': filtered}
    return response_with(res)


if __name__ == '__main__':
    app.run()
