import pandas as pd
from bs4 import BeautifulSoup # pip intall beautifulsoup4 로 설치 해야 함
import requests

startnumber=1
endnumber=10
CommerceInfor = {}

ROW_NUMlist = []
Datelist = []
Area_namelist = []
Area_codelist = []
Market_namelist = []
Market_codelist = []
Product_namelist = []
Product_detail_namelist = []
DISTB_STEPlist = []
Gradelist = []
Standardlist = []
Pricelist = []


while endnumber<=100:
    url='http://211.237.50.150:7080/openapi/'your personal key'/xml/Grid_20141217000000000090_1/' +str(startnumber)+'/ '+str(endnumber)+ '?EXAMIN_DE=20190520'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    Row_num = soup.find_all('row_num')
    Date = soup.find_all('examin_de')
    Area_name = soup.find_all('examin_area_nm')
    Area_code = soup.find_all('examin_area_cd')
    Market_name = soup.find_all('examin_mrkt_nm')
    Market_code = soup.find_all('examin_area_cd')
    Product_name = soup.find_all('prdlst_nm')
    Product_detail_name = soup.find_all('prdlst_detail_nm')
    DISTB_STEP = soup.find_all('distb_step')
    Grade = soup.find_all('grad')
    Standard = soup.find_all('stndrd')
    Price = soup.find_all('examin_amt')

    for code in Row_num:
        ROW_NUMlist.append(code.text)
    for code in Date:
        Datelist.append(code.text)
    for code in Area_name:
        Area_namelist.append(code.text)
    for code in Area_code:
        Area_codelist.append(code.text)
    for code in Market_name:
        Market_namelist.append(code.text)
    for code in Market_code:
        Market_codelist.append(code.text)
    for code in Product_name:
        Product_namelist.append(code.text)
    for code in Product_detail_name:
        Product_detail_namelist.append(code.text)
    for code in DISTB_STEP:
        DISTB_STEPlist.append(code.text)
    for code in Grade:
        Gradelist.append(code.text)
    for code in Standard:
        Standardlist.append(code.text)
    for code in Price:
        Pricelist.append(code.text)

    startnumber+=10
    endnumber+=10

# CommerceInfor['Row'] = ROW_NUMlist
CommerceInfor['Date'] = Datelist
CommerceInfor['Area_name'] = Area_namelist
# CommerceInfor['Area code'] = Area_codelist
CommerceInfor['Market_name'] = Market_namelist
# CommerceInfor['Market code'] = Market_codelist
CommerceInfor['Product_name'] = Product_namelist
CommerceInfor['Product_detail_name'] = Product_detail_namelist
CommerceInfor['DISTB_STEP'] = DISTB_STEPlist
CommerceInfor['Grade'] = Gradelist
CommerceInfor['Standard'] = Standardlist
CommerceInfor['Price'] = Pricelist

df = pd.DataFrame(CommerceInfor)
df = df[['Date', 'Area_name', 'Market_name', 'DISTB_STEP', 'Product_name', \
'Product_detail_name', 'Grade', 'Standard', 'Price']]
print(df)
df.to_csv("api sample.csv")
