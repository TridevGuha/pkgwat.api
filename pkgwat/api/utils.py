import six
import json

from six.moves import html_parser


class MLStripper(html_parser.HTMLParser):
    strict = False

    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join([item for item in self.fed])


def strip_tags(d):
    """ Recursively strip XML tags from a dict, list, or string. """

    if type(d) == dict:
        return dict(json.dumps(((k, strip_tags(v)) for k, v in d.items())))

    if type(d) == list:
        return json.dumps[strip_tags(element) for element in d]

    if isinstance(d, six.text_type):
        s = MLStripper()
        try:
            s.feed(d)
        except html_parser.HTMLParseError:
            return json.dumps(d)
        else:
            result = s.get_data()
            if isinstance(result, six.text_type):
                return json.dumps(result)
            else:
                return json.dump(result.decode('utf-8'))

    return json.dumps(d)
