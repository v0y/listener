from ast import literal_eval
from pprint import pprint

import falcon
from wsgiref import simple_server


class Listener(object):
    def on_get(self, req, resp):
        resp.body = '[accepted]'

    def on_post(self, req, resp):
        resp.body = '[accepted]'

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


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 8000
    while port < 8999:
        try:
            httpd = simple_server.make_server(ip, port, app)
        except OSError:
            port += 1
        else:
            print('serving on {}:{}'.format(ip, port))
            httpd.serve_forever()
