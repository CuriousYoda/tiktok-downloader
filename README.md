# TikTok-Downloader
Simple Python+Selenium script to download TikTok videos for a given user or hashtag without water marks. 
This uses [TikTokAPI](https://davidteather.github.io/TikTok-Api/docs/) to fetch relevant data and https://snaptik.app/ to generate videos without watermarks. 
All credits to developers of those two modules. 


## Features
- Takes a Tiktok user name or a hashtag and downloads X TikToks starting from most recent ones
  - You can define how many TikToks to be downloaded
  

## Git Installtion
```
# clone the repo
$ git clone https://github.com/CuriousYoda/tiktok-downloader.git

# change the working directory to Facebook-Video-Downloader
$ cd tiktok-downloader

# install the requirements
$ pip3 install -r requirements.txt
```

## Required Properties/Dependencies
- You need to have chrome browser installed.
- Set up the folder path to download tiktoks in the properties file

## Usage
```
# With exe (Only for Windows systems) //DOES NOT WORK FOR THE MOMENT
$ Double click on exe or Open a CMD prompt and run "insta-scraper.exe"

# Through script
$ python tik-tok-scraper.py

```

## Development & Packaging
- PyInstaller is used to package the exe

## Known Issues
- If you get a Captcha error, please set up a custom verifyfp value in the property file. Here is [how to create a verifyfp](https://www.youtube.com/watch?v=MgjorCvPzxg)
- Right now, exe is not working. It seems to be an [issue](https://github.com/davidteather/TikTok-Api/issues/591) with PlayWright and Pyinstaller. Need to investigate further. 

Copyright (c) [2021] [[@CuriousYoda](https://twitter.com/CuriousYoda)]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
