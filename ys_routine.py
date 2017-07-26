# coding: utf-8
# !/usr/bin/python3


class YsRoutine:

    def __init__(self):
        print('init')

        #
        #     print colored.green('[OK]		') + 'Launching scan...'
        #     con = pymysql.connect(bd_host, bd_user, bd_pass, 'pys')
        #     cursor = con.cursor()
        #
        #     newWebsite_array = getUnchecked(cursor) 	#uncheckedFromDB = Tous les sites checked = 0
        #     allWebsite_array = getAll(cursor)				#allFromDB = tous les sites en database
        #
        #     print colored.cyan('[CRAWLER]	') + '%s unchecked websites in queue' % (colored.yellow(len(newWebsite_array)))
        #
        #     while len(newWebsite_array) > 0:
        #         for newWebsite in newWebsite_array:
        #             print colored.green('[INFO]		') + 'checking %s' % (newWebsite[0])
        #             ws = ys(newWebsite[0])
        #             ws.setUrls(1)
        #             ws.cleanUrls()
        #             ws.setMails()
        #             print colored.cyan('[CRAWLER]	') + 'Found %s urls & %s mails for %s' % (colored.yellow(len(ws.url_array)), colored.yellow(len(ws.mails)), colored.yellow(newWebsite[0]))
        #
        #             #On check tous les sites trouvés sur la cible
        #             for nWebsite in ws.url_array:
        #                 if nWebsite not in allWebsite_array:
        #                     print ' %s SHOULD BE ADDED !!!' % (nWebsite)
        #                     now = int(time.time())
        #                     #url_split = nWebsite.split('.')
        #                     #extension = url_split[len(url_split)-1]
        #                     row = (cursor, nWebsite, '', '', '', '', 0, 0, now)
        #                     insertWebsite(*row)
        #
        #             setChecked(cursor, ws.url)
        #
        #     #Tous les sites ont été check
        #
        # else:
        #     print time.time()