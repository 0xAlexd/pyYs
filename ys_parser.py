# coding: utf-8

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import bs4 as BeautifulSoup
import re
from config import REGEX

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class YsUrl:

    URL = None
    HTML_CODE = None
    SOUP = None

    def __init__(self, url):

        self.URL = url
        try:
            html = requests.get(self.URL, verify=False).text
            self.SOUP = BeautifulSoup.BeautifulSoup(html, 'html.parser')
            self.HTML_CODE = self.SOUP.prettify()
        except requests.exceptions.ConnectionError:
            self.URL = None
            self.HTML_CODE = None
            self.SOUP = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__['URL'] == other.__dict__['URL']
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    # 
    def is_valid(self):
        return True if self.URL is not None else False

    def get_protocol(self):
        if self.URL is not None:
            valid_protocol = ['HTTP', 'HTTPS', 'FTP']
            url_protocol = self.URL.split('://')[0]
            if url_protocol.upper() in valid_protocol:
                return url_protocol
            else:
                print('ERROR_PROTOCOL_NOT_VALID')
                return None
        else:
            print('ERROR_URL_NOT_VALID')
            return None

    def get_body(self):
        return

    def get_extension(self):
        if self.URL is not None:
            return

    def get_extension_country(self):
        return

    def get_html_code(self):
        return self.HTML_CODE

    def get_cms(self):
        return

    def get_author(self):
        return

    def get_keywords(self):
        return

    def get_urls(self):
        if self.URL is not None:
            parsed_urls = []

            # Finding urls with soup parser
            for link in self.SOUP.find_all('a'):
                parsed_urls.append(link.get('href'))

            # Finding urls with regex
            regex_urls = re.findall(REGEX.URL, self.HTML_CODE)

            # Distinct urls
            return list(set(parsed_urls + regex_urls))
        else:
            print('ERROR_URL_NOT_VALID')
            return None

    def get_emails(self):
        if self.URL is not None:
            return set(re.findall(REGEX.MAIL, self.HTML_CODE))
        else:
            print('ERROR_URL_NOT_VALID')

    # TODO_____________________
    def get_contact_page(self):
        for link in self.get_urls():
            test = re.search('contact', link)
            contact_page = link if test is not None else None
        return contact_page


class YsUrlCollection:

    URLS = []

    def __init__(self):
        pass

    def add_url(self, new_url):
        self.URLS.append(new_url)

    def add_url_list(self, url_list):
        self.URLS = list(set(self.URLS + url_list))

    def count(self):
        return len(self.URLS)
