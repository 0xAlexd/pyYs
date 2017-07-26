# coding: utf-8
# !/usr/bin/python3


class YsDatabaseManager:

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