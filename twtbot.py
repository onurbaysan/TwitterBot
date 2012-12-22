#  Many thanks to "tweepy" library.     |
#  https://github.com/tweepy/tweepy     |
#  -------------------------------------
#  Implemented by Onur BAYSAN |
#  onurbaysan@outlook.com     |
#  ---------------------------

import tweepy
import webbrowser
import time
import logging
import sys
import smtplib
from email.mime.text import MIMEText

## Change consumer_key and consumer_secret with your own values
consumer_key='[YOUR_CONSUMER_KEY]'
consumer_secret='[YOUR_CONSUMER_SECRET]'

#  Mail Settings #-------------------#
me = [YOUR_MAIL_ADDRESS]         
mail_password = [PASSWORD]      
you = [SENDER_MAIL_ADDRESS]
#----------------------------------- #

# Which frequency twtbot search tweets
polling_time = [SET_POLLING_TIME]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# List for the users to be followed
follower_list = []
   
# Open authorization URL in browser
webbrowser.open(auth.get_authorization_url())

# Ask user for verifier pin
pin = raw_input('Enter the verification pin number from twitter.com: ').strip()

try: 
	# Get access token
	token = auth.get_access_token(verifier=pin)
	auth.set_access_token(token.key, token.secret)
	api = tweepy.API(auth)
	print 'Authorization for twtbot is succeeded'
except Exception, e:
	logging.error(e)
	sys.exit(0)
	
keyword = raw_input('Enter specific keyword: ')

try:
	# Tweet about us
	api.update_status('twtbot - https://github.com/pho3nix/twtbot - #twtbot')
except:
	logging.warning('Tweet has already sent.')
	pass
	
while 1: 
	try:
		for tweet in api.search(keyword):
			# Send follow request
			api.get_user(tweet.from_user).follow()
			# Add user end of the the list
			follower_list.append(tweet.from_user)
			
		time.sleep(polling_time)
	except (KeyboardInterrupt, SystemExit):
		msg = MIMEText('\n'.join(follower_list))
		msg['Subject'] = 'List of the following user , twtbot'
		msg['From'] = me
		msg['To'] = you

		sender = smtplib.SMTP("smtp.gmail.com" , 587)
		sender.ehlo()
		sender.starttls()
		sender.ehlo()
		sender.login(me, mail_password)
		sender.sendmail(me, [you], msg.as_string())
		sender.quit()
		
		print 'Mail contains following list has been sent you.'
		sys.exit(0)