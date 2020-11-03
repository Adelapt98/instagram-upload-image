from check_new_posts_igbot import check_new_posts
from upload_posts import upload_posts
from time import sleep
import random
from login.main import *
from instabot import Bot 
  
bot = Bot() 
  
bot.login(username = "username", password = "pass") 

driver = full_login()
# driver = get_loggedin_driver()

while(True):
    try:
        check_new_posts(driver)
        upload_posts(bot)
        sleep(random.randint(5*3600,7*3600))
    except Exception as e:
        print(e)
        exit()
