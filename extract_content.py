from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from urllib.request import urlretrieve
option = webdriver.ChromeOptions()
import json
import time
from selenium.webdriver.common.by import By
import os

## Change these parameters to extract from different accounts
LIMIT = 20 ## Number of images to extract
TAG_LIST = ["williethelabrador"] ## List of usernames to extract from
USERNAME = "" ## Your Instagram username
PASSWORD = "" ## Your Instagram password


def get_username_images(tag, limit=20):
    driver.get("https://www.instagram.com/explore/tags/{}/".format(tag))
    time.sleep(2)
    scrolldown=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    match=False
    scroll_count = 0
    while(match==False and scroll_count<limit//4):
        scroll_count += 1
        last_count = scrolldown
        time.sleep(3)
        scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    if last_count==scrolldown:
        match=True
    posts = []
    photos = driver.find_elements(By.TAG_NAME,'img')
    for photo in photos:
        posts.append(photo.get_attribute('src'))
    posts = posts[4:]
    posts = posts[:limit]

    cnt = 0
    if not os.path.exists(f"images/{username}"):
        os.makedirs(f"images/{username}")
    for post in posts:
        cnt += 1
        try:
            urlretrieve(post, f'images/{username}/img_{cnt}.jpg')
        except:
            print("Error in downloading image")

if __name__ == "_main_":
    s = Service()
    driver = webdriver.Chrome(service=s, options=option)
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    username=driver.find_element("name","username")
    password=driver.find_element("name","password")
    username.clear()
    password.clear()
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    login = driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    time.sleep(5)

    for tag in TAG_LIST:
        get_username_images(tag, limit=20)
        print("{} images extracted from {}".format(LIMIT, tag))
    driver.close()


    