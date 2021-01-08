import requests
from bs4 import BeautifulSoup

URL = 'http://211.237.50.150:7080/openapi/3ee0ccf85e3198812547d2f3757388be90459f980189e445873108740afb2580/xml/Grid_20141217000000000090_1/1/1?EXAMIN_DE=20190520'
req = requests.get(URL)
# print(response.status_code)
# print(response.text)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
codenumber = soup.find_all('prdlst_detail_nm')
# print(html)
print(soup)
# print(codenumber)
