import requests
from bs4 import BeautifulSoup

URL='https://www.amazon.in/BLACK-DECKER-CD121K50-Cordless-Accessories/dp/B00R4R1DL2/ref=sr_1_10?keywords=drill&qid=1566713966&s=gateway&sr=8-10#customerReviews'

headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36" }

page=requests.get(URL,headers=headers)

soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

