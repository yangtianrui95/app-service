import json

from flask import (Flask, jsonify,
                   abort, make_response)

import fetch_handler
import page_info
import reptile_handler


def create_app():
    app = Flask(__name__)
    return app


application = create_app()


@application.route('/news/<category>', methods=['GET'])
def get_news_list(category):
    _list = fetch_handler.get_toutiao_news_list(category)
    if not _list:
        abort(400)
    if _list.__len__() > 0:
        _status = 0
    else:
        _status = 1
    response = make_response(json.dumps(page_info.PageInfo(_status, _list), default=lambda o: o.__dict__))
    response.headers['Content-Type'] = "application/json"
    return response


@application.route('/news', methods=['GET'])
def get_default_list():
    return get_news_list(fetch_handler.categories.keys()[0])


# todo delete me !!!
@application.route('/news/', methods=['GET'])
def get_default_list_():
    return get_news_list(fetch_handler.categories.keys()[0])


@application.route('/feed', methods=['GET'])
def get_feed_list():
    _list = reptile_handler.get_feed_list()
    if not _list:
        abort(400)
    if _list.__len__() > 0:
        _status = 0
    else:
        _status = 1
    response = make_response(json.dumps(page_info.PageInfo(_status, _list), default=lambda o: o.__dict__))
    response.headers['Content-Type'] = "application/json"
    return response


@application.route('/', methods=['GET'])
def print_info():
    abort(404)


@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': u'Page not found, please access /news or /feed '}), 404)


@application.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': u'Bad request, please check your url '}))


if __name__ == '__main__':
    application.run(threaded=True)
