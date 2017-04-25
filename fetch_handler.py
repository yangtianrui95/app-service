import json
import sys
import urllib2

import page_info
import util

reload(sys)
# noinspection PyUnresolvedReferences
sys.setdefaultencoding("utf-8")

host = 'http://www.toutiao.com'
base_url = host + '/api/pc/feed/?category='
id_prefix = 'toutiao'

params = {
    'category': ''
}

# Return different feed list according to the category.
categories = {
    'toutiao': '__all__',
    'hot': 'news_hot',
    'video': 'video',
    'society': 'news_society',
    'yule': 'news_entertainment',
    'tech': 'news_tech',
    'sport': 'news_sport',
    'car': 'news_car',
    'finance': 'news_finance',
    'funny': 'funny'
}


class _ToutiaoObj:
    def __init__(self, _data):
        self.__dict__ = _data

    def __repr__(self):
        return repr(self.__dict__)


def _get_content(_url):
    if 'http' in _url:
        return _url
    else:
        return host + _url


# noinspection PyDefaultArgument
def _get_response(url, headers={}):
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request)


def get_toutiao_news_list(_category, _url=base_url):
    """
    get news list from toutiao api, if the category is not in valid set, we return None.

    :param _category: news category.
    :param _url: api host.
    :return: news list or None.
    """
    if _category not in categories.keys():
        return None
    else:
        # Value is the actual requested parameter.
        _category = categories.get(_category)
    request_url = _url + _category
    response = _get_response(request_url)
    body = response.read()
    json_string = json.loads(body, object_hook=_ToutiaoObj)
    data = json_string.__dict__['data']

    feed_set = []
    for item in data:
        _set = item.__dict__
        _id = None
        if _set.has_key('title'):
            _id = util.get_md5_str(_set['title'])
            _id = id_prefix + '-' + _id[:15]
        else:
            continue

        _title = _set['title']
        _pic = None
        _source = 'toutiao'
        _content = None

        if _set.has_key('media_avatar_url'):
            _pic = _set['media_avatar_url']
        if _set.has_key('source_url'):
            _content = _get_content(_set['source_url'])
        feed_item = page_info.FeedItem(_id, _title, _pic, _content, _source)
        feed_set.append(feed_item)

    return feed_set
