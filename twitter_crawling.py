from bs4 import BeautifulSoup # pip intall beautifulsoup4 로 설치 해야 함
import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
import datetime as dt

# 파이어폭스로 크롤링
binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
browser = webdriver.Firefox(executable_path='C:/Users/MIS/Downloads/dj/Python/AnalysisWithPython/geckodriver.exe',firefox_binary=binary)

# 19.2.6.부터 19.2.10.까지
startdate = dt.date(year=2019,month=2,day=6)
untildate = dt.date(year=2019,month=2,day=7)
enddate = dt.date(year=2019,month=2,day=10)

totalfreq = []
while not enddate==startdate: # enddate==startdate일 때까지 반복
    url = 'https://twitter.com/search?q=삼겹살%20since%3A'+str(startdate)+'%20until%3A'+str(untildate)+'&amp;amp;amp;amp;amp;amp;lang=eg'
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html,'html.parser')

    lastHeight = browser.execute_script("return document.body.scrollHeight") # 스크롤링

    while True:
            dailyfreq = {'Date':startdate}
        # i=0 i는 페이지수
            wordfreq = 0
            tweets = soup.find_all("p", {"class": "TweetTextSize"})
            wordfreq += len(tweets)

            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 스크롤링
            time.sleep(1)

            newHeight = browser.execute_script("return document.body.scrollHeight") # 스크롤링
            print(newHeight)
            if newHeight != lastHeight:
                html = browser.page_source
                soup = BeautifulSoup(html,'html.parser')
                tweets = soup.find_all("p", {"class": "TweetTextSize"})
                wordfreq = len(tweets)
            else:
                dailyfreq['Frequency']=wordfreq
                wordfreq = 0
                totalfreq.append(dailyfreq)
                startdate = untildate
                untildate += dt.timedelta(days=1)
                dailyfreq = {}
                break
            # i+=1
            lastHeight = newHeight

print('=' * 50)
import pandas as pd
df = pd.DataFrame(totalfreq)
print(df.head())

print('=' * 50)
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
plt.xticks(rotation=90)
plt.scatter(df.Date,df.Frequency)