import tweepy
import requests
import os.path
from bs4 import BeautifulSoup
print('this is my bot')

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()
pin_ids_queue = []

def has_it_been_posted(current_link, pin_ids_queue):
    if os.path.isfile('alreadyTweeted.txt'):
        with open('alreadyTweeted.txt') as f:
            #if already in text file continue else add to queue
            if current_link in f.read():
                print("here")
            else:
                pin_ids_queue.append(current_link)
                #num += 1
    else: #when file is newly created add link to it
         f = open("alreadyTweeted.txt", "x")
         pin_ids_queue.append(current_link)


#create que for urls
def tweetPin():
    url = 'https://www.pinterest.com/aldgore/bomb-nails'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    num = 1
    for link in soup.find_all('a'):
        ##find the most recent pins from website
        if '/pin/' in link.get('href'):
         current_link = link.get('href')
         #print(str(num) + ' - ' + current_link)
         #check if in text file
         has_it_been_posted(current_link, pin_ids_queue)

         #check if in text file

    #create text file to keep track of pins already posted
    linkToPost = pin_ids_queue.pop(0)
    api.update_status('https://www.pinterest.com' + linkToPost)
    f = open("alreadyTweeted.txt", "a")
    f.write(linkToPost + "\n")
    f.close()
