import pymysql
import re


def exec_sql_file(cursor, sql_file):
    statement = ""
    for line in open(sql_file):
        if re.match(r'--', line):
            continue
        if not re.search(r'[^-;]+;', line):
            statement = statement + line
        else:
            statement = statement + line
            cursor.execute(statement)
            statement = ""


try:
    con = pymysql.connect('localhost', 'root', '', 'pyYS')
    cur = con.cursor()
    # exec_sql_file(cur, 'pyYellowSpider.sql')
    cur.execute('''INSERT into FACTRESTTBL (id, city)
                  values (%s, %s)''',
                (id, city))
    cur.commit()

    print 'ok'
except:
    print 't'
