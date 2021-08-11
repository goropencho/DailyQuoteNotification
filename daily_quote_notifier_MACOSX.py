from bs4 import BeautifulSoup
import requests
from pync import Notifier
import random

url = requests.get("https://www.brainyquote.com/topics/daily-quotes").text
soup = BeautifulSoup(url, 'lxml')

tag = soup.find('div',id=f"pos_1_{random.randint(1,2)}",class_="grid-item qb clearfix bqQt").a.text
tag = tag.lstrip().rstrip()

Notifier.notify(tag, title="Daily Quote")