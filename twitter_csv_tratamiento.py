# pip install tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

consumer_key = 'consumer_key_here'
consumer_secret = 'consumer_secret_here'
access_token = 'access_token_here'
access_token_secret = 'access_token_secret_here'

class MyListener(StreamListener):

	def on_data(self, data):
		try:
			tweet = data.split(',"text":"')[1].split(',"source":"')[0]
			print tweet
			
			saveThis = str(time.time())+' :: '+tweet
			saveFile = open('twitterDB2.csv','a')
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException, e:
			print "Falla de datos,",str(e)
			time.sleep(5)
	
	def on_error(self, status):
		print status


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitterStream = Stream(auth, MyListener())
twitterStream.filter(track = ["#hashtag_here"]) 
