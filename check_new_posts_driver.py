from datetime import datetime, timedelta
from itertools import dropwhile, takewhile

import time


import orm
import urllib.request
import os

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import random

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys

def get_six_first_posts(driver, pageUsername):
    print('6 started')
    url = 'https://www.instagram.com/' + pageUsername
    print(url)

    driver.get(url)
    sleep(5)
    raw_posts = driver.find_elements_by_xpath("//div[contains(@class, 'kIKUG')]")
    posts = []
    print(driver.page_source)
    print(raw_posts)
    for post in raw_posts[0:3]:
        shortCode = post.find_element_by_xpath('./a').get_attribute('href').replace('https://www.instagram.com/p/', '').replace('/', '')
        post.click()
        img = post.find_element_by_xpath("//img[contains(@class, 'FFVAD')]").get_attribute('srcset')
        imgUrl = img.split('480w,')[1].split(' 640w')[0]
        print(2)
        sleep(random.randint(10,35))
        caption = post.find_element_by_xpath("//div[contains(@class, 'C4VMK')]/span").text
        caption_mentions = []
        atsigns = caption.split('@')
        print(3)
        for at in atsigns:
            words = at.split(' ')
            word = words[0].replace('\n', '')
            word = word.split('\\')[0]
            caption_mentions.append(word)

        caption_hashtags = '{'
        hashtags = caption.split('#')
        for at in hashtags:
            words = at.split(' ')
            word = words[0].replace('\n', '').replace("\'", '')
            caption_hashtags += word + ','
        caption_hashtags = caption_hashtags[:-1] + '}'
        try:
            is_video = post.find_element_by_xpath("//span[contains(@class, 'videoSpritePlayButton')]")
            is_video = True
        except:
            is_video = False

        posts.append({'shortcode': shortCode, 'url': imgUrl, 'caption': caption, 'is_video': is_video, 'caption_mentions': caption_mentions, 'caption_hashtags': caption_hashtags})
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        sleep(10)
        print('end 6')
    return posts

def check_new_posts(driver):
    print('new post')
    while True:
        pages = orm.select('SELECT username, last_post_id FROM page')
        for page in pages:
            pageUsername = page[0]
            lastPostId = page[1]

            posts = get_six_first_posts(driver, pageUsername)
            lastShortcode = ''
            i = 0
            for post in posts:
                if i == 0:
                    lastShortcode = post['shortcode']

                if post['shortcode'] == lastPostId or i == 2 or lastPostId == 'n' or pageUsername not in post['caption_mentions']:
                    continue

                elif post['shortcode'] != lastPostId and i < 2:
                    if not os.path.exists('{0}'.format('posts' + '/' + pageUsername)):
                        os.makedirs('{0}'.format('posts' + '/' + pageUsername))
                    
                    if not post['is_video']:
                        isVideo = False
                        fileAddress = 'posts' + '/' + pageUsername + "/" + post['shortcode'] + ".jpg"
                        urllib.request.urlretrieve(post['url'], fileAddress)
                    else:
                        continue
                        # isVideo = True
                        # fileAddress = pageUsername + "\\" + post.shortcode + ".mp4"
                        # urllib.request.urlretrieve(post.url, fileAddress)
                    
                    now = datetime.now()
                    timestamp = int(time.mktime(now.timetuple()))
                    
                    result = orm.select("SELECT * FROM post WHERE short_code = '{0}'".format(post['shortcode']))
                    if len(result) == 0:
                        orm.insertOrUpdate("INSERT INTO post(short_code, username, inserted_date, file_address, caption, caption_hashtags, is_video, is_posted) VALUES ('{0}','{1}',{2},'{3}','{4}','{5}',{6},{7});".format(post['shortcode'], pageUsername, timestamp, fileAddress, post['caption'], post['caption_hashtags'], isVideo, False))

                print('a post added from: ' + pageUsername)
                i+=1
            print('add post')
            orm.insertOrUpdate("UPDATE page SET last_post_id = '{0}' WHERE username = '{1}'".format(lastShortcode, pageUsername))
        break    