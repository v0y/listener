from ast import literal_eval
from pprint import pprint

import falcon


class Listener(object):
    def on_get(self, req, resp):
        resp.body = '(ﾉ´ヮ´)ﾉ*:･ﾟ✧'

    def on_post(self, req, resp):
        body = req.stream.read()
        print('*' * 40)

        for k, v in req.headers.items():
            print('{}: {}'.format(k, v))

        print('=' * 40)

        try:
            pprint(literal_eval(body.decode("utf-8")))
        except:
            print(body)
        print('*' * 40)


app = falcon.API()

listener = Listener()

app.add_route('/', listener)
