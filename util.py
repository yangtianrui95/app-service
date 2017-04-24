import md5


def get_md5_str(string):
    if not string:
        return None
    m1 = md5.new()
    m1.update(string)
    return m1.hexdigest()
