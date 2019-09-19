#!/usr/bin/python
# -*- coding: utf-8 -*-
# python3.6

import os
from configparser import ConfigParser

BASE_DIR = os.path.dirname(__file__)
CONFIG_FILE_PATH = os.path.join(BASE_DIR, 'config.ini')


class TestConfig:
    def __init__(self):

        config = ConfigParser()
        config.read(CONFIG_FILE_PATH)

        self.type = config.get('default', 'type')

        self.host = config.get('mysql', 'host')
        self.port = config.get('mysql', 'port')
        self.username = config.get('mysql', 'username')
        self.password = config.get('mysql', 'password')


if __name__ == '__main__':
    t = TestConfig()
    print(t.type)

