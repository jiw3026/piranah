#!/usr/bin/env python
# coding: utf-8

# In[34]:


from selenium import webdriver 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup


# In[35]:


browser = webdriver.Chrome('./chromedriver.exe')
url = 'https://www.fss.or.kr/fss/bbs/B0000207/list.do?menuNo=200691&bbsId=&cl1Cd=&pageIndex=16&sdate=&edate=&searchCnd=1&searchWrd='
browser.get(url)


# In[36]:


act = ActionChains(browser)
lst = []


# In[37]:


from selenium.webdriver.common.by import By

for i in range(1, 10):
    try:
        element = browser.find_element(By.CSS_SELECTOR, f'#content > div.bd-list > table > tbody > tr:nth-child({i}) > td.title > a')
        act.click(element).perform()
        time.sleep(2)
        target_element = browser.find_element(By.CSS_SELECTOR, '#content > div.bd-view > div > video')
        audio_url = target_element.get_attribute("src")
        lst.append(audio_url)
    except NoSuchElementException:
        print(f"Element not found for row {i}. Skipping...")
    finally:
        browser.back()
        time.sleep(2)


# Print the collected URLs
print(lst)


i = 1
for url in lst:
    response = requests.get(url)
    with open(f'{i}.mp3','wb') as file:
        file.write(response.content)
        i+=1

browser.quit()


# In[ ]:





# In[ ]:





# In[ ]:




