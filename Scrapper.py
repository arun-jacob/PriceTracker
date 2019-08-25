import requests
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.in/BLACK-DECKER-CD121K50-Cordless-Accessories/dp/B00R4R1DL2/ref=sr_1_10?keywords=drill&qid=1566713966&s=gateway&sr=8-10#customerReviews'

headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36" }

def clean(price):
    converted_price=price[1:].strip()
    converted_price=converted_price.replace(',','')
    return float(converted_price)

def send_mail(price):
    #cbaaddxrvkkpvfyb
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('arunzacharia007@gmail.com','cbaaddxrvkkpvfyb')

    subject = "Price has deceresed"
    body="The price has gotten below 3000 to :Rs/- "+ str(price)

    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail('arunzacharia007@gmail.com','arunzachariahjacob@gmail.com',msg)
    server.quit()
    print("Mail Send......!")
    
def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    price=soup.find(id="priceblock_ourprice").get_text()
    price=clean(price)
    if(price<=3000):
        send_mail(price)

check_price()
