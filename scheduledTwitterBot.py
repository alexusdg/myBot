import time
import schedule
from datetime import datetime, timedelta
from threading import Timer
import myTwitterBot

schedule.every().day.at("13:00").do(myTwitterBot.tweetPin)
schedule.every().day.at("17:00").do(myTwitterBot.tweetPin)

while True:

    schedule.run_pending()
    time.sleep(2)
