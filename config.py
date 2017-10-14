class COLORS:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class DATABASE:

	MYSQL_HOST = ''
	MYSQL_USER = ''
	MYSQL_PASS = ''


class SCRIPT:

	VERSION = ''
	NAME = ''
	DATA_LAST_UPDATE = '09/09/2017'


class FILE:

	MYSQL_SCHEMA = 'py....sql'


class REGEX:

    MAIL = r'[\w\.-]+@[\w\.-]+'
    URL = "(?P<url>https?://[^\s]+)"


    #     # WEBSITE REGEX PHP
    #     # "/(http(s?):\/\/)?(www\.)+[a-zA-Z0-9\.\-\_]+(\.[a-zA-Z]{2,3})+(\/[a-zA-Z0-9\_\-\s\.\/\?\%\#\&\=]*)?/i";
    #     # WEBSITE REGEX PYTHON1
    #     # http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
    #
    #     # MAIL REGEX
    #     # "/[a-z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}/i";