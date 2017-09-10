# coding: utf-8
# !/usr/bin/python3
try:
    import pymysql
except Exception as e:
    print('ERROR_IMPORTING_PYMYSQL_MODULE_{}'.format(e[1]))

try:
    import re
except Exception as e:
    print('ERROR_IMPORTING_RE_MODULE_{}'.format(e[1]))

try:
    import os
except Exception as e:
    print('ERROR_IMPORTING_OS_MODULE_{}'.format(e[1]))


class YsDatabase(object):

    CURSOR = None
    HOST = None
    USER = None
    PASS = None
    CONNECTION = None
    CONNECTED = False

    def __init__(self):
        return

    def connect(self):
        return

    def url_exist(self):
        return


class YsDatabaseMysql(YsDatabase):

    def __init__(self):
        super(YsDatabaseMysql, self).__init__()

    def connect(self, host, user, pasw):
        try:
            self.HOST = host
            self.USER = user
            self.PASS = pasw
            self.CONNECTION = pymysql.connect(self.HOST, self.USER, self.PASS)
            self.CURSOR = self.CONNECTION.cursor()
            return True
        except pymysql.err.OperationalError as e:
            print('ERROR_MYSQL_CONNECTION_REFUSED_{0}@{1}_{2}'.format(self.USER, self.HOST, e[1]))
            return False

    def url_exist(self, url):
        query = "SELECT count(*) FROM ys2websites WHERE website == '{}'".format(url)
        res = self.CURSOR.execute(query)
        self.CURSOR.close()
        return True if res > 0 else False

    def insert_url(self, ys_url):
        if self.CONNECTED:
            if not self.url_exist(ys_url.getUrl()):
                query = "INSERT INTO ys2websites(website, " \
                        "                        title, " \
                        "                        description, " \
                        "                        languageCode, " \
                        "                        checked, " \
                        "                        mail_count, " \
                        "                        date)" \
                        " VALUES('{0}', '{1}','{2}','{3}', '{4}', '{5}')"\
                        .format(
                                ys_url.get_url(),
                                ys_url.get_extension(),
                                ys_url.get_title(),
                                ys_url.get_country(),
                                0,
                                ys_url.get_mail_count(),
                                ys_url.get_date())
                self.CURSOR.execute(query)
                self.CURSOR.commit()
                self.CURSOR.close()
                return True
            return True
        else:
            return False

    def set_checked(self, url):
        if self.CONNECTED:
            query = "UPDATE ys_website SET checked = 1 WHERE url = '{0}'".format(url)
            self.CURSOR.execute(query)
            self.CURSOR.commit()
            self.CURSOR.close()
            return True
        else:
            return False

    # A REVOIR
    def exec_sql_file(self, sql_file):
        statement = ''
        for line in open(sql_file):
            if re.match(r'--', line):
                continue
            if not re.search(r'[^-;]+;', line):
                statement = statement + line
            else:
                statement = statement + line
                self.CURSOR.execute(statement)
                statement = ''

    def get_unchecked_websites(self):
        if self.CONNECTED:
            query = "SELECT website, checked FROM ys2websites WHERE checked = '0'"
            self.CURSOR.execute(query)
            self.CURSOR.commit()
            res = self.CURSOR.fetchall()
            self.CURSOR.close()
            return res
        else:
            print('ERROR_DATABASE_NOT_CONNECTED')
            return None

    def is_schema_ok(self):
        query = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'pys'"
        database_exist = self.CURSOR.execute(query)
        return True if database_exist else False

    def import_schema(self):
        if self.CONNECTED:
            if os.path.isfile('pyYellowSpider.sql'):
                query = "CREATE DATABASE pys"
                self.CURSOR.execute(query)
                self.CURSOR.close()
                self.CONNECTION = pymysql.connect(self.HOST, self.USER, self.PASS, 'pys')
                self.CURSOR = self.CONNECTION.cursor()
                self.exec_sql_file('pyYellowSpider.sql')
                # A AJOUTER AU SCHEMA + DELETE
                self.CURSOR.execute("INSERT INTO ys2websites VALUES(1,'http://www.lemonde.fr', '', '', '', '', 0, 0, 000000000)");
                self.CONNECTION.commit()
                self.CURSOR.close()
                return True
            else:
                print('ERROR_MYSQL_YS_SCHEMA_NOT_FOUND')
                return False
        else:
            print('ERROR_DATABASE_NOT_CONNECTED')
            return False

