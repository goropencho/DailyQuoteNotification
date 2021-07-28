from bs4 import BeautifulSoup
import requests
import notify2
import random
url = requests.get("https://www.brainyquote.com/topics/daily-quotes").text

soup = BeautifulSoup(url, 'lxml')

tag = soup.find('div',class_="grid-item qb clearfix bqQt b-qt-lg",id=f"pos_1_{random.randint(1,2)}").a.text

notify2.init("Daily Quote")

n = notify2.Notification(None,message=tag)
n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(10000)
n.show()