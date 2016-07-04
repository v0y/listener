from pprint import pprint

import falcon


class Notifications(object):
    def on_post(self, req, resp):
        body = req.stream.read()
        print('*' * 40)
        for k, v in req.headers.items():
            print('{}: {}'.format(k, v))
        print('=' * 40)
        pprint(body)
        print('*' * 40)


app = falcon.API()

notifications = Notifications()

app.add_route('/', notifications)
