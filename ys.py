# coding: utf-8
# !/usr/bin/python3

# from ys_routine import YsRoutine
from clint.textui import colored
import pymysql
import sys
import os
import os.path
import re
import time
from ys_db_manager import YsDatabase
# from ys_parser import YsParser


class YellowSpider:

    SCRIPT_VERSION = u'0.2'
    SCRIPT_NAME = u'pYellowSpider'

    DATABASE = None

    def __init__(self):
        pass

    def choose_menu(self):
        mode = False
        while not mode:
            self.menu_display(self.SCRIPT_NAME, self.SCRIPT_VERSION)
            mode = input()
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
        database = YsDatabase()
        connected = False
        while not connected:
            connected = database.mysql_connect()
            self.DATABASE = database
        return connected

    def start(self):
        try:
            if not self.choose_menu():
                raise Exception('Error menu')
            if not self.set_database():
                raise Exception('Error database')
        except Exception as e:
            print(e)

    # UI display
    @staticmethod
    def menu_display(script_name, script_version):
        print(u'=== Starting {0} V{1} ==='.format(colored.yellow(script_name), colored.yellow(script_version)))
        print(u'{0} : Abord script'.format(colored.cyan('(1)')))
        print(u'{0} : Specific website'.format(colored.cyan('(2)')))
        print(u'{0} : Launch YellowSpider'.format(colored.cyan('(3)')))
        print(u'{0} : Exit'.format(colored.cyan('(4)')))

    @staticmethod
    def save_logs(string):
        f = open('logs.txt', 'a')
        f.write(string)
        f.close()

if __name__ == '__main__':
    ys = YellowSpider()
    ys.start()
