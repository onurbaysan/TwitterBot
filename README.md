twtbot
======

twtbot is a python script that sends follow requests to the user who tweets about a specified keyword. It searches users and follow them. 
It uses PIN-based OAuth for authorization. 

Usage
------------
First of all, twtbot requires tweepy library. It can be downloaded from https://github.com/tweepy/tweepy

Change following values in source code:

consumer_key=[YOUR_CONSUMER_KEY]
consumer_secret=[YOUR_CONSUMER_SECRET]
me = [YOUR_MAIL_ADDRESS]         
mail_password = [PASSWORD]      
you = [SENDER_MAIL_ADDRESS]
polling_time = [SET_POLLING_TIME]

Run twtbot.py script 

Features: 
---------
- Searching interval can be changed.
- List of the users started to be followed is sent as mail. 

NOTE:
----
At the moment, only gmail accounts can send mail, you can change mail server and can use your mail other than gmail.

Next Versions:
----------------

- twtbot can write logs into your local in addition to send mail.
- Users can send mail from different known mail providers in addition to Gmail.
- Windows service implementation of twtbot will be added.