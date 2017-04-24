# coding=utf-8
class BaseInfo:
    def __init__(self, _status):
        self.status = _status
        pass

    def __repr__(self):
        return repr(self.status)


class PageInfo(BaseInfo):
    """
    @:param _status: is api valid.
    @:param _data: map of feed item.
    """

    def __init__(self, _status, _data):
        BaseInfo.__init__(self, _status)
        self.data = _data

    pass


class FeedItemSet:
    def __init__(self, _item_list):
        self.list = _item_list


class FeedItem:
    def __init__(self, _id, _title, _pic, _content, _source):
        self.id = _id
        self.title = _title
        self.pic = _pic
        self.content = _content
        self.source = _source

    def __repr__(self):
        return repr(self.id) + '  ' + repr(self.title) + '  ' + repr(self.pic) + '  ' + repr(
            self.content) + '  ' + repr(self.source)
