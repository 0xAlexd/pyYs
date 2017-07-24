# coding: utf-8
# !/usr/bin/python3

from ys_routine import YsRoutine
from clint.textui import colored
import pymysql
import sys
import os
import os.path
import re
import time
from ys import ys

class yellowSpider:

    SCRIPT_VERSION = 1.2
    SCRIPT_NAME = u'pYellowSpider'

    def __init__(self, args):
        if args[0] == 1:
            self.crawlSpecificWebsite(args[1])
        elif args[0] == 2:
            self.spiderStart()

    def saveLogs(string):
        f = open('logs.txt', 'a')
        f.write(string)
        f.close()

    def chooseMenu()
        print('=== Starting {0} V{1} ==='.format(colored.yellow(SCRIPT_NAME), colored.yellow(SCRIPT_VERSION)))

        print('{0} : abord script'.format(colored.cyan('(0)'))
        print colored.cyan('(1)') + ' 	: Crawl a specific website'
        print colored.cyan('(2)') + ' 	: launch YellowSpider'

        mode = raw_input()

    ###################CORE SCRIPT###################
    os.system('clear')
    print ' === Starting ' + colored.yellow(s) + ' Ver : ' + colored.yellow(script_version) + ' === '
    print('=== Starting {0} V{1} ==='.format(colored.yellow(SCRIPT_NAME), colored.yellow(SCRIPT_VERSION)))

    print('{0} : abord script'.format(colored.cyan('(0)'))
    print colored.cyan('(1)')	+' 	: Crawl a specific website'
    print colored.cyan('(2)')	+' 	: launch YellowSpider'

    mode = raw_input()

    if int(mode) == 0:
        print 'exit'

    elif int(mode) == 1:
        base_url = raw_input(colored.cyan('Site web de départ : '))
        print 'instanciating ...'
        c_website = ys(base_url)
        print 'Setting up links ...'
        c_website.setUrlsREG(0)

        fileName = raw_input('Entrez un nom de fichier de sauvegarde : ')
        c_website.saveData(fileName,c_website.getUrlsReg)

    elif int(mode) == 2:

        print colored.green('\rSetting-up database ...')
        con_flag = False
        bd_host = 'localhost'
        bd_user = 'root'
        bd_pass = ''

        while con_flag == False:
            try:
                con = pymysql.connect(bd_host, bd_user, bd_pass)
                cur = con.cursor()
                print colored.green('[OK]		') + 'Database @'+bd_host+' successfully connected.'
                con_flag = True
            except:
                print colored.red('[ERROR] ') + 'Failed to connect database. (MySQL database required to launch YS.)'
                bd_host = raw_input(colored.cyan('\rDatabase host :'))
                bd_user = raw_input(colored.cyan('\rDatabase user :'))
                db_pass = raw_input(colored.cyan('\rDatabase pass :'))

        print 'Checking Database structure...'
        DbExistQuery = ("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'pys'")
        DbExist = cur.execute(DbExistQuery)

        while not DbExist:
            print colored.red('[ERROR]		') + 'Database pys does not exist @'+bd_host+' for user ' + bd_user
            if os.path.isfile('pyYellowSpider.sql'):
                print colored.green('[OK] ') + 'pyYellowSpider.sql found. Creating database structure...'
                try:
                    DbCreateQuery = ("CREATE DATABASE pys")
                    cur.execute(DbCreateQuery)
                    cur.close()
                    con.close()
                    con = pymysql.connect(bd_host, bd_user, bd_pass, 'pys')
                    cur = con.cursor()
                    exec_sql_file(cur, 'pyYellowSpider.sql')
                    cur.execute("INSERT INTO ys2websites VALUES(1,'http://www.lemonde.fr', '', '', '', '', 0, 0, 000000000)");
                    con.commit()
                    DbExist = True
                    print colored.green('[OK]		') +  'Database struture created !'
                    cur.close()
                    con.close()
                except:
                    print colored.red('[ERROR]		') + 'Error creating Database Structure ! Press any key to retry.'
                    cur.execute(("DROP DATABASE pys"))
                    DbExist = False
                    raw_input()
            else:
                print colored.red('[ERROR]		') + 'pyYellowSpider.sql NOT FOUND!'
                DbExist = False

        print colored.green('[OK]		') + 'Launching scan...'
        con = pymysql.connect(bd_host, bd_user, bd_pass, 'pys')
        cursor = con.cursor()

        newWebsite_array = getUnchecked(cursor) 	#uncheckedFromDB = Tous les sites checked = 0
        allWebsite_array = getAll(cursor)				#allFromDB = tous les sites en database

        print colored.cyan('[CRAWLER]	') + '%s unchecked websites in queue' % (colored.yellow(len(newWebsite_array)))

        while len(newWebsite_array) > 0:
            for newWebsite in newWebsite_array:
                print colored.green('[INFO]		') + 'checking %s' % (newWebsite[0])
                ws = ys(newWebsite[0])
                ws.setUrls(1)
                ws.cleanUrls()
                ws.setMails()
                print colored.cyan('[CRAWLER]	') + 'Found %s urls & %s mails for %s' % (colored.yellow(len(ws.url_array)), colored.yellow(len(ws.mails)), colored.yellow(newWebsite[0]))

                #On check tous les sites trouvés sur la cible
                for nWebsite in ws.url_array:
                    if nWebsite not in allWebsite_array:
                        print ' %s SHOULD BE ADDED !!!' % (nWebsite)
                        now = int(time.time())
                        #url_split = nWebsite.split('.')
                        #extension = url_split[len(url_split)-1]
                        row = (cursor, nWebsite, '', '', '', '', 0, 0, now)
                        insertWebsite(*row)

                setChecked(cursor, ws.url)

        #Tous les sites ont été check

    else:
        print time.time()