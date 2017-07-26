# coding: utf-8
# !/usr/bin/python3


class YsDatabase:

    def __init__(self):
        print('init')

    # def setChecked(cursor, website):
    #     try:
    #         req = "UPDATE ys2websites SET checked = 1 WHERE website = '%s'" % (website)
    #         cursor.execute(req)
    #         print colored.cyan('OK UPDATE ?')
    #     except:
    #         print colored.red('[ERROR]		Updating checked failed... Infinite loop incoming')
    #
    # def getUnchecked(cursor):
    #     cursor.execute("SELECT website, checked FROM ys2websites WHERE checked = '0'")
    #     return cursor.fetchall()
    #
    # def getAll(cursor):
    #         cursor.execute("SELECT website FROM ys2websites")
    #         return cursor.fetchall()
    #
    # def insertWebsite(cursor, website, extension, title, description, languageCode, checked, mail_count, date):
    #     try:
    #         req = "INSERT INTO ys2websites(website, title, description, languageCode, checked, mail_count, date) VALUES('%s','%s','%s','%d', '%d', '%d')" % (website, extension, title, description, languageCode, checked, mail_count, date)
    #         cursor.execute(req)
    #         print colored.green('[OK]		') + "New website added : %s" % (website)
    #     except:
    #         print colored.red('[ERROR]		') + 'Website "%s" not added' % (website)
    #         #print 	'Website = %s\ntitle = %s\ndescription = %s\nlanguageCode = %s\nchecked = %d\nmail_count= %d\ndate= %d\n' % (website, title, description, languageCode, checked, mail_count, date)
    #
    #
    # def exec_sql_file(cursor, sql_file):
    #     statement = ''
    #     for line in open(sql_file):
    #         if re.match(r'--', line):
    #             continue
    #         if not re.search(r'[^-;]+;', line):
    #             statement = statement + line
    #         else:
    #             statement = statement + line
    #             cursor.execute(statement)
    #             statement = ""

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