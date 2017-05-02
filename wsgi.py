import json
import sys

from flask import (Flask, jsonify,
                   abort, make_response, Response)

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


# mock for string request
@application.route('/string', methods=['GET'])
def mock_string_request():
    return 'request success.'


# mock for image request
@application.route('/jpeg', methods=['GET'])
def mock_img_request():
    # get current directory.
    image = file(sys.path[0] + "/img_rq.jpg")
    resp = Response(image, mimetype="image/jpeg")
    return resp


# https://www.fedepot.com/she-zhi-flask-xiang-ying-qing-qiu-tou-shi-xian-jing-tai-zi-yuan-chang-shi-huan-cun/?utm_source=tuicool&utm_medium=referral
@application.after_request
def app_after_request(response):
    print response
    # if Request.endpoint != 'static':
    #     return response

    response.cache_control.max_age = 15552000
    return response


@application.route('/channel', methods=['GET'])
def get_news_channel_list():
    _list = fetch_handler.categories.keys()
    _channel_list = page_info.PageInfo(0 if _list.__len__() >= 0 else -1, _list)
    response = make_response(json.dumps(_channel_list, default=lambda o: o.__dict__))
    response.headers['Content-Type'] = "application/json"
    return response


@application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': u'Page not found, please access /news or /feed '}), 404)


@application.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': u'Bad request, please check your url '}))


if __name__ == '__main__':
    application.run(threaded=True)
