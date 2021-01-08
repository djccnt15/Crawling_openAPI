import pandas as pd
from bs4 import BeautifulSoup
import requests

startnumber=1
endnumber=1000
CommerceInfor = {}

codelist = []
codenamelist = []
totalnumberlist = []
maletotallist = []
femaletotallist = []
agrade_10list = []
agrade_20list = []
agrade_30list = []
agrade_40list = []
agrade_50list = []
above_60list = []

while endnumber<=2000:
     url='http://openapi.seoul.go.kr:8088/인증키/ xml/   InfoTrdarFlpop/' +str(startnumber)+'/ '+str(endnumber)+ '/201711'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    codenumber = soup.find_all('trdar_cd')
    codename = soup.find_all('trdar_cd_nm')
    totalnumber = soup.find_all('tot_flpop_co')
    maletotal = soup.find_all('ml_flpop_co')
    femaletotal = soup.find_all('fml_flpop_co')
    agrade_10 = soup.find_all('agrde_10_flpop_co')
    agrade_20 = soup.find_all('agrde_20_flpop_co')
    agrade_30 = soup.find_all('agrde_30_flpop_co')
    agrade_40 = soup.find_all('agrde_40_flpop_co')
    agrade_50 = soup.find_all('agrde_50_flpop_co')
    above_60 = soup.find_all('agrde_60_above_flpop_co')

    for code in codenumber:
        codelist.append(code.text)
    for code in codename:
        codenamelist.append(code.text)
    for code in totalnumber:
        totalnumberlist.append(code.text)
    for code in maletotal:
        maletotallist.append(code.text)
    for code in femaletotal:
        femaletotallist.append(code.text)
    for code in agrade_10:
        agrade_10list.append(code.text)
    for code in agrade_20:
        agrade_20list.append(code.text)
    for code in agrade_30:
        agrade_30list.append(code.text)
    for code in agrade_40:
        agrade_40list.append(code.text)
    for code in agrade_50:
        agrade_50list.append(code.text)
    for code in above_60:
        above_60list.append(code.text)
        
startnumber+=1000
endnumber+=1000
