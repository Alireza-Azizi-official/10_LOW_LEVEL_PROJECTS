#import libraries to scrape,work with notifier,get and work with image.
import requests
from bs4 import BeautifulSoup
import time
import subprocess
from plyer import notification
from PIL import Image

# Web scraping to get the price which we want as the message of the notifier.
site = requests.get("https://irarz.com/")
soup = BeautifulSoup(site.content, "html.parser")
dolor = soup.find("span", id="usdmax")
coin = soup.find("span", id="sekee")
bitcoin = soup.find("span", id="crypto-btc")

# Formatting prices and message
news = [dolor.text, coin.text, bitcoin.text]
message = f"DOLOR PRICE: {news[0]} RIAL\nCOIN PRICE: {news[1]} RIAL\nBITCOIN PRICE: {news[2]} DOLOR"

# making icon for the notifier
filename=r"D-NOTIFIER\news.ico"
img=Image.open(filename,'r')
img.save(r"D-NOTIFIER\news.ico")

# notification
notification.notify(
    title='BREAKING NEWS',
    app_name='NOTIFIER',
    message=message,
    app_icon=r"D-NOTIFIER\news.ico",
    timeout=10
)