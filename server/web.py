#!/usr/bin/env python

from __future__ import unicode_literals

import os, sys
import time
time.sleep(3)

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))
sys.path.append('libs')

import logging

# create our little application :)
import tornado
from tornado.options import define, options
from tornado.web import Application
from webserver.core import (HomeHandler, PokemonHandler, LoginHandler)
from tornado.httpserver import HTTPServer


define('port', default=8888, help='run on the given port', type=int)

# Global store dict, using as an application level store object
store = {}


def setupLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('Line %(lineno)d,%(filename)s - %(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


class MyApplication(Application):
    def __init__(self):
        handlers = [
            (r'/', HomeHandler, dict(store=store)),
            (r'/pokemon', PokemonHandler, dict(store=store)),
            (r'/login', LoginHandler, dict(store=store)),
        ]
        settings = dict(
            blog_title=u'Pokesistant',
            template_path=os.path.join(os.path.dirname(__file__), 'public/templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'public/static'),
            xsrf_cookies=False,
            cookie_secret='SfI#dfs)_9d8!235@&#%FLsfewidlsdfciE**',
            login_url='/login',
            debug=True,
        )
        super(MyApplication, self).__init__(handlers, **settings)


def main():
    tornado.options.parse_command_line()
    http_server = HTTPServer(MyApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
