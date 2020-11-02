from instabot import Bot 
  

# Recommended to put the photo 
# you want to upload in the same 
# directory where this Python code 
# is located else you will have  
# to provide full path for the photo 
# bot.upload_photo("p1.jpg", caption ="..") 

def create_post(filePath, caption, bot):
    try:
        bot.upload_photo(filePath, caption =caption)
        return True
    except Exception as e:
        print(e)
        if 'No such file or directory' in e.strerror:
            print(filePath)
            return False
        else:
            exit()