# coding: utf-8

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import urlopen
import bs4 as BeautifulSoup
import re

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class YsParser:

    url = ''
    soup = ''
    data = ''

    url_array = []
    mails = []
    contactPage = ''

    def __init__(self, url):
        self.url = url
        html = requests.get(self.url, verify=False).text
        # html = urlopen(self.url).read()
        self.soup = BeautifulSoup.BeautifulSoup(html)
        self.data = self.soup.prettify()

    # # param = 0 for all links, param = 1 for unique ones
    # def setUrls(self, param):
    #     if param == 0:
    #         for link in self.soup.find_all('a'):
    #             self.url_array.append(link.get('href'))
    #     if param == 1:
    #         for link in self.soup.find_all('a'):
    #             if link not in self.url_array:
    #                 self.url_array.append(link.get('href'))
    #
    # def cleanUrls(self):
    #     # URL_REG = "(?P<url>http(s)?://[^\s]+)"
    #     URL_REG = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    #     for u in self.url_array:
    #         if not re.match(URL_REG, u):
    #             self.url_array.remove(u)
    #
    # # param = 0 for all links, param = 1 for unique ones
    # def setUrlsR(self, param):
    #     URL_REG = "(?P<url>https?://[^\s]+)"
    #     if param == 0:
    #         self.url_array = re.findall(URL_REG, self.data)
    #     if param == 1:
    #         self.url_array = set(re.findall(URL_REG, self.data))
    #
    # # Getters
    # def getUrls(self):
    #     return self.url_array
    #
    # # 0 for html.parsed links, 1 for regex ones
    # def displayUrls(self, param):
    #     if param == 0:
    #         c_url = self.urls
    #     if param == 1:
    #         c_url = self.urlsReg
    #     for link in c_url:
    #         print link
    #
    # def setMails(self):
    #     MAIL_REG = r'[\w\.-]+@[\w\.-]+'
    #     self.mails = set(re.findall(MAIL_REG, self.data))
    #
    # def setContactPage(self, url_array):
    #     for link in url_array:
    #         test = re.search('contact', link)
    #         if test is not None:
    #             self.contactPage = link
    #
    # def getInside(self, data, borneInf, borneSup):
    #     temp = data.split(borneInf)
    #     temp2 = temp[1].split(borneSup)
    #     return temp2[0]
    #
    # def saveData(self, fileName, data_array):
    #     file = open(fileName, 'w')
    #     for line in data_array:
    #         file.write(line)
    #         file.write('\n')
    #         print 'writing ... ' + line
    #     file.close()
    #
    #     # WEBSITE REGEX PHP
    #     # "/(http(s?):\/\/)?(www\.)+[a-zA-Z0-9\.\-\_]+(\.[a-zA-Z]{2,3})+(\/[a-zA-Z0-9\_\-\s\.\/\?\%\#\&\=]*)?/i";
    #     # WEBSITE REGEX PYTHON1
    #     # http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
    #
    #     # MAIL REGEX
    #     # "/[a-z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}/i";
