from datetime import datetime, timedelta
import orm
import urllib.request
import os
import instaloader
L = instaloader.Instaloader()
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import random
# from create_post import create_post
from create_post_instabot import create_post
from random import shuffle



def upload_posts(bot = 'not passed'):
    posts = orm.select('SELECT inserted_date, username, short_code, caption, is_video, caption_hashtags FROM post WHERE is_posted = false AND is_video = false')
    shuffle(posts)
    for post in posts:

        username = post[1]
        shortCode = post[2]
        caption = post[3]
        isVideo = post[4]
        caption_hashtags = post[5]

        if isVideo:
            frmt = ".mp4"
        else:
            frmt = ".jpg"


        baseStr = """@the_rise_of_success 😉

    Follow ➡️➡️➡️ @the_rise_of_success
    Follow ➡️➡️➡️ @the_rise_of_success
    Follow ➡️➡️➡️ @the_rise_of_success

    منبع : @{0}


    """.format(username)

        caption = baseStr# + caption

        myHashtagList = ['the_rise_of_success', 'طلوع_موفقیت', 'انگیزشی', 'ثروت', 'انرژی_مثبت', 'موفقیت', 'من_میتوانم',
            'تفکر_مثبت', 'انگیزه', 'خودساخته', 'تحول', 'هدف', 'انگیزه_روزانه', 'آرزو', 'رویا', 'رشد', 'فرصت', 'اراده',
            'من_میتونم', 'لیاقت', 'احترام', 'goal', 'تلاش', 'کوشش', 'خوشبختی', 'خفن', 'امید', 'خدا', 'رابرت_کیوساکی',
            'انگیزشی_موفقیت', 'دکتر_آزمندیان', 'پشتکار', 'قدرت_ذهن', 'رشد_فردی', 'موفقیت_شغلی', 'راز_موفقیت',
            'موفقیت_فردی', 'تلاش_سخت', 'just_do_it', 'انگیزشی_موفقیت_هدف']
        
        # print(len(myHashtagList))

        hashtagList = caption_hashtags

        for hashtag in hashtagList:
            if hashtag in myHashtagList:
                myHashtagList.remove(hashtag)
            # if "#"+hashtag + ' ' in caption:
            #     caption = caption.replace("#"+hashtag + ' ', '')
            # else:
            #     caption = caption.replace("#"+hashtag, '')

        random.shuffle(myHashtagList)

        for k in range(len(myHashtagList)):
            if k < 15:
                caption+= " #"+myHashtagList[k]

        result = create_post('./posts' + '/' + username + "/" + shortCode + frmt, caption, bot)
        
        if result:
            orm.insertOrUpdate("UPDATE post SET is_posted = true WHERE short_code = '{0}'".format(shortCode))
            print(username + '  -  ' + shortCode + '   uploaded')
            return True
        else:
            print(username + '  -  ' + shortCode + '   should be deleted')