import tweepy 
from random import seed
from random import randint
import time
import schedule

consumer_key ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
seed(1)
def Spam():
    status_message = str(randint(0, 100000000)) + "#CancelTNSemesterExams #CancelTNSemesterExams #cancelfinalyearexams #CancelAUExamsTN #CoronavirusIndia #COVID19 #StopOnlineClass #FailedLockdown #PromoteStudentsSaveFuture #ClearArrearsToo"
    print(status_message)
    api.update_status(status = status_message)

schedule.every(1).minutes.do(Spam)

while 1:
    schedule.run_pending()
    time.sleep(1)
    
