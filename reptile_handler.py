# coding=utf-8
import urllib2
from bs4 import BeautifulSoup

import page_info
import util

id_prefix = 'juejin'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
}

reptile_host = {
    'juejin': 'https://juejin.im/'
}


def get_feed_list():
    return get_juejin_item()


def get_juejin_item():
    global img, title
    img = None
    title = None
    item_set = []
    request = urllib2.Request(reptile_host['juejin'], headers=headers)
    response = urllib2.urlopen(request)
    soup = BeautifulSoup(response.read())
    # find tag by class.
    feed_box = soup.select('.conetnt-box')
    _id = None
    for i in feed_box:
        child = i.children
        for j in child:
            if cmp('None', str(j.contents[0].get('src'))) != 0:
                img = _get_img_url(str(j.contents[0].get('src')))
            title = None
            for k in j.children:
                title = k.text
                break
        if title is None:
            break
        _id = id_prefix + '-' + util.get_md5_str(title)[:15]
        item = page_info.FeedItem(_id, title, img, 'empty', 'juejin')
        item_set.append(item)

    # print item_set
    # print json.dumps(item_set, default=lambda o: o.__dict__)
    return item_set


def _get_img_url(_img):
    if _img is not None and cmp(_img, 'None') != 0 and 'http' in _img:
        return _img
    else:
        return 'empty'
