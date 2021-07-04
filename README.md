# TikTok-Downloader
Simple Python+Selenium script to download TikTok videos for a given user without water marks. 
This uses [TikTokAPI](https://davidteather.github.io/TikTok-Api/docs/) to fetch relevant data and https://snaptik.app/ to generate videos without watermarks. 
All credits to developers of those two modules. 


## Features
- Takes a Tiktok user name and downloads X TikToks starting from most recent ones
  - You can define how many TikToks to be downloaded

## How to use
- You need to have chrome browser installed.
- Download the project as a zip file (it's around 11MB), unzip and go into the folder.
- Set up the folder path to download tiktoks in the properties file
- Run the tik-tok-scraper.exe either by double clicking or by opening CMD prompt and typing "insta-scraper.exe"
- TikToks will be downloaded to the folder you specified. User photos will be saved to a folder name with User Full Name and Hashtag photos to a folder named with that hashtag

## Development & Packaging
- PyInstaller is used to package the exe

## Next Steps
- Support for hashtags

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
