import csv
from bs4 import BeautifulSoup
from splinter import Browser
import webbrowser
import re
import time
import codecs
import os
import sys
import requests

browser = ''

def main():
    fp = open('tt.csv', "r")
    start_browser()
    while True:
        link = fp.readline()  # type: str
        if link == '':
            break
        #print(link) #to check weather its reading or not
        page = requests.get(link)
        take_screenshot(link)
    fp.close()

def start_browser():
    global browser
    # Start browser
    chromedriver_path = 'chromedriver' if os.name == 'nt' else './chromedriver'
    executable_path = {'executable_path': chromedriver_path}
    browser = Browser('chrome', **executable_path, headless=True)

def get_browser():
    global browser
    return browser

def take_screenshot(url):
    browser = get_browser()
    # TODO: make sure url is correct
    browser.visit(url)
    cwd = os.getcwd()
    #  We will add tilde at the end to distinguish the url from random characters
    #  splittin the url after http:// or https:// because cannot have // in file name
    file_name = "www." + url.split('www.')[1].replace('/', '*') + "~"
    screenshot_path = browser.screenshot(cwd + '/testscreen/' + file_name, full=True)
    return screenshot_path


if __name__ == "__main__" :
    main()
