from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import requests 
from bs4 import BeautifulSoup 
import csv  
import time 
  

def get_table(league_name):
    URL = "https://www.theguardian.com/football/{league}/table"
    
    r = requests.get(URL.format(league=league_name)) 
       
    soup = BeautifulSoup(r.content, 'html5lib') 
    teams = soup.findAll("a", {"class": "team-name__long"})
    points = soup.findAll("b")  
    table=""
    line= "{rank}. {team} {point} \n"
    n=len(teams)
    for i in range(0,n):
        name=teams[i].text
        name=name.strip()
        table+=line.format(rank=str(i+1),team=name,point=points[i].text)
    return table

contact = "Group/person name"


driver = webdriver.Chrome()
  
driver.get("https://web.whatsapp.com") 
print("Scan QR Code, And then Enter")
input()
print("Logged In")
user=driver.find_element_by_xpath('//span[@title="{}"]'.format(contact))
user.click()
prev=""
valid=["laliga","bundesliga","seriea","league1","premierleague"]
while(1):
	flag=0
	incoming = driver.find_elements_by_xpath('//div[@class="eRacY" and starts-with(.,"!")]')
	if len(incoming)!= 0:
		query=incoming[-1].text[1:]
		if query!=prev and query in valid:
			prev=query
			if query != "premierleague"
				query=query+"football"
	
			message_box= driver.find_element_by_xpath('//div[@class="_3uMse"]')
			table=get_table(query)
			for i in table.split('\n'):
				message_box.send_keys(i)
				ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
			time.sleep(2)
			message_box.send_keys(Keys.ENTER)

print("close")
input()
driver.close()