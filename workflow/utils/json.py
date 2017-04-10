import json
from json import JSONEncoder as BaseJsonEncoder


class JsonEncoder(BaseJsonEncoder):
    def default(self, obj):
        return obj.__dict__


def dumps(*args, **kwargs):
    return json.dumps(*args, cls=JsonEncoder, **kwargs)


def loads(*args, **kwargs):
    return json.loads(*args, cls=JsonEncoder, **kwargs)
