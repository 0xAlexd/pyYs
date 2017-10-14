# coding: utf-8
# !/usr/bin/python3
import sys
import os
import os.path
import re
import time
from ys_db_manager import *
from config import SCRIPT, DATABASE


class YellowSpider:

    DATABASE = None

    def __init__(self):
        pass

    def choose_menu(self):
        mode = False
        while not mode:
            self.menu_display()
            mode = str(raw_input())
            if mode.isdigit():
                if 1 <= int(mode) <= 4:
                    return int(mode)
                else:
                    print('Wrong number')
                    mode = False
            else:
                print('Wrong input')
                mode = False
        return mode

    def set_database(self):
        db = YsDatabaseMysql()
        connected = False
        while not connected:
            self.database_settings()
            connected = db.connect(DATABASE.MYSQL_HOST, DATABASE.MYSQL_USER, DATABASE.MYSQL_PASS)
            self.DATABASE = db
        return connected

    @staticmethod
    def database_settings():
        host = raw_input('Set database host : ')
        user = raw_input('Set database user : ')
        pasw = raw_input('Set database password : ')

        DATABASE.MYSQL_HOST = host
        DATABASE.MYSQL_USER = user
        DATABASE.MYSQL_PASS = pasw

    def start(self):
        if not self.choose_menu():
            raise Exception('Error menu')
        if not self.set_database():
            raise Exception('Error database')

    # UI display
    @staticmethod
    def menu_display():
        print(u'=== Starting {0} V{1} ==='.format(SCRIPT.VERSION, SCRIPT.NAME))
        print(u'(1) Abord script')
        print(u'(2) : Specific website')
        print(u'(3) : Launch YellowSpider')
        print(u'(4) : Exit')

    @staticmethod
    def save_logs(string):
        f = open('logs.txt', 'a')
        f.write(string)
        f.close()

if __name__ == '__main__':
    ys = YellowSpider()
    ys.start()
