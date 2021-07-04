from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
import sys
from TikTokApi import TikTokApi
import os
import configparser
import logging
from selenium.webdriver.common.keys import Keys

__author__ = "@CuriousYoda"
__copyright__ = "Copyright (C) 2021 @CuriousYoda"
__license__ = "MIT"
__version__ = "1.0"

level = logging.ERROR
logger = logging.getLogger()
logger.setLevel(level)


def readProperty(propertyValue):
    config = configparser.RawConfigParser()
    config_file = open('tik-tok-scraper.properties', encoding="utf-8")
    config.read_file(config_file)
    value = config.get("UserInput", propertyValue)
    if not value:
        print("Missing property value: " + propertyValue)
        sys.exit()
    return value


def getTwitterDownloadWebsite():
    website = readProperty("DOWNLOAD_SITE")
    return website


def initiateDriver():
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument('log-level=3')
    browser = webdriver.Chrome(
        ChromeDriverManager().install(),
        options=chrome_options)
    return browser


api = TikTokApi()
browser = initiateDriver()
session = requests.Session()


def getFolderPath(username):
    folderPath = readProperty("BASE_FOLDER") + "/" + username
    if not os.path.isdir(folderPath):
        os.makedirs(folderPath)
    return folderPath


def downloadTikTok(filePath, url):
    print("Downloading...: " + url)
    response = requests.get(url, headers={
                                'User-Agent': 'Mozilla/5.0 (Macintosh;'
                                'Intel Mac OS X 10_9_3) AppleWebKit/537.36'
                                '(KHTML, like Gecko) Chrome/35.0.1916.47'
                                'Safari/537.36'})

    with open(filePath, 'wb') as f:
        f.write(response.content)
        f.close()


username = input("Enter the tik tok user name: ")
videosToDownload = int(input("Enter the number of tiktoks to download: "))
userPosts = api.byUsername(username, count=videosToDownload)


for post in userPosts:
    print("\nDownloading TikTok: " + str(post['id']))

    videoId = str(post['id'])
    videoPageUrl = "https://www.tiktok.com/@" + username + "/video/" + videoId
    filePath = getFolderPath(username) + "/" + videoId + ".mp4"

    browser.get(getTwitterDownloadWebsite())
    urlField = browser.find_element_by_id("url")
    urlField.send_keys(videoPageUrl)
    urlField.send_keys(Keys.ENTER)
    browser.implicitly_wait(5)
    downloadBlock = browser.find_element_by_id("download-block")
    downloadLinkElement = downloadBlock.find_element_by_tag_name("a")
    downloadLink = downloadLinkElement.get_attribute("href")

    downloadTikTok(filePath, downloadLink)

    print("Downloaded TikTok: " + videoId)

browser.close()
