__author__ = "@CuriousYoda"
__copyright__ = "Copyright (C) 2021 @CuriousYoda"
__license__ = "MIT"
__version__ = "1.0"

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
from clint.textui import progress

level = logging.ERROR
logger = logging.getLogger()
logger.setLevel(level)
os.environ["WDM_LOG_LEVEL"] = str(logging.WARNING)


def readProperty(propertyValue, optional=False):
    config = configparser.RawConfigParser()
    config_file = open('tik-tok-scraper.properties', encoding="utf-8")
    config.read_file(config_file)
    value = config.get("UserInput", propertyValue)
    if not value:
        print("Missing property value: " + propertyValue)
        if not optional:
            sys.exit()
    return value


def getTwitterDownloadWebsite():
    website = readProperty("DOWNLOAD_SITE")
    return website


def initiateDriver():
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument('log-level=3')
    chrome_options.add_experimental_option(
        'excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(
        ChromeDriverManager().install(),
        options=chrome_options)
    return browser


def getVerifyFp():
    verifyFp = readProperty("VERIFY_FP", True)
    return verifyFp


print("Setting up the selenium headless Chrome Driver")
browser = initiateDriver()

print("Setting up a connection to unofficial TikTokAPI")
v = getVerifyFp()
if v:
    api = TikTokApi.get_instance(custom_verifyFp=v, use_test_endpoints=True)
else:
    api = TikTokApi.get_instance(use_test_endpoints=True)

print("Setting up the session for requests")
session = requests.Session()


def getFolderPath(folderName):
    folderPath = readProperty("BASE_FOLDER") + "/" + folderName
    if not os.path.isdir(folderPath):
        os.makedirs(folderPath)
    return folderPath


def requestUrl(url):
    response = requests.get(url, stream=True, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh;'
        'Intel Mac OS X 10_9_3) AppleWebKit/537.36'
        '(KHTML, like Gecko) Chrome/35.0.1916.47'
        'Safari/537.36'})

    return response


def requestAndSaveUrlInChunk(url, postFileName):
    response = requestUrl(url)
    with open(postFileName, 'wb') as f:
        total_length = int(response.headers.get('content-length'))
        for chunk in progress.bar(response.iter_content(
                chunk_size=1024), expected_size=(total_length / 1024) + 1):
            if chunk:
                f.write(chunk)
                f.flush()


def getWaitingTimeForDownloadLink():
    return readProperty("WAIT_TIME_IN_SECONDS")


def downloadPost(username, videoId, folderName):
    print("\nDownloading TikTok: " + videoId)

    videoPageUrl = "https://www.tiktok.com/@" + username + "/video/" + videoId
    filePath = getFolderPath(folderName) + "/" + videoId + ".mp4"
    waitTime = getWaitingTimeForDownloadLink()

    if os.path.isfile(filePath):
        print("Skipped. File Exists: " + videoId)
        return

    browser.get(getTwitterDownloadWebsite())
    urlField = browser.find_element_by_id("url")
    urlField.send_keys(videoPageUrl)
    urlField.send_keys(Keys.ENTER)
    browser.implicitly_wait(waitTime)
    downloadBlocks = browser.find_elements_by_id("download-block")

    if len(downloadBlocks) < 0:
        print("Download failed: " + videoId)
        failedWebPagePath = getFolderPath(folderName) + "/" + videoId + ".html"
        with open(failedWebPagePath, 'w') as f:
            f.write(browser.page_source)
        return

    downloadBlock = downloadBlocks[0]
    downloadLinkElement = downloadBlock.find_element_by_tag_name("a")
    downloadLink = downloadLinkElement.get_attribute("href")

    requestAndSaveUrlInChunk(downloadLink, filePath)

    print("Downloaded TikTok: " + videoId)


shouldContinue = True

while shouldContinue:
    choice = input(
        '\nDo you wish to download TikToks for a'
        '\n   1: User or\n   2: HashTag\n') or "1"

    if choice == "1":
        username = input("Enter the tik tok user name: ") or "tiktok"
        videosToDownload = int(
            input("Enter the number of tiktoks to download: ") or 10)
        userPosts = api.byUsername(username, count=videosToDownload)
        for post in userPosts:
            downloadPost(username, str(post['id']), username)

    elif choice == "2":
        hashTag = input("Enter the tik tok hashtag: #") or "tiktok"
        videosToDownload = int(
            input("Enter the number of tiktoks to download: ") or 10)
        hashTagPosts = api.byHashtag(hashTag, count=videosToDownload)
        for post in hashTagPosts:
            downloadPost(
                post['author']['uniqueId'], str(
                    post['id']), "#" + hashTag)

    else:
        continue

    choice = input('\nType exit and press Enter to quit: ')
    if choice == "exit":
        shouldContinue = False

browser.close()
