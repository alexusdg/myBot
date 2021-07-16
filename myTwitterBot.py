import tweepy
import requests
from bs4 import BeautifulSoup
print('this is my bot')

#create que for urls


url = 'https://www.pinterest.com/aldgore/bomb-nails'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')


CONSUMER_KEY = 'H1mj1FsaQFtK3eJSzViXej7Nu'
CONSUMER_SECRET = 'qGSIPBlCJvHVjc4X5EdkfJDcfETFk9KV9mCptBuZBWmYsQA3mz'
ACCESS_KEY = '1413976412520951808-0a2JQ42fxWDhnbCuYvh9UGrG9MpHsM'
ACCESS_SECRET = 'heqywJMNRz43u4zYFhNptU2Ch2EhJK5EFkoyPPc0rDAKA'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

pin_ids_queue = []
num = 1
for link in soup.find_all('a'):
    ##find the most recent pins from website
    if '/pin/' in link.get('href'):
     print(str(num) + ' - ' + link.get('href'))
     #check if in text file
     with open('alreadyTweeted.txt') as f:
         if link.get('href') in f.read():
             continue
         else:
            pin_ids_queue.append(link.get('href'))
            num += 1

     #check if in text file

#create text file to keep track of pins already posted
linkToPost = pin_ids_queue.pop(0)
api.update_status('https://www.pinterest.com' + linkToPost)
f = open("alreadyTweeted.txt", "a")
f.write(linkToPost + "\n")
f.close()
