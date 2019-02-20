# -*- coding: utf-8 -*-
import praw
#import time
import datetime
import csv

#AUTHENTIFICATION
reddit = praw.Reddit(client_id='**************',
                     client_secret='***************************',
                     redirect_uri='*',
                     user_agent='*')


worldnews = reddit.subreddit("worldnews")
i=0

with open('RedditExtract.csv',newline="", mode='w') as csv_file:
    
    fieldnames = ['Flair','Title', 'Date', 'Hour', 'Gilded', 'Upvotes', 'DownVotes', 'Upvote_ratio', 'url']
    
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';', quotechar='|')
    writer.writeheader()

    for submission in worldnews.new(limit = 100000):
        
        #time.sleep(1.2)
    
        i+=1
        print(i, datetime.datetime.utcfromtimestamp(submission.created).strftime('%d-%m-%Y %H:%M:%S'))
        writer.writerow({'Flair' : submission.link_flair_text,'Title': submission.title, 'Date': datetime.datetime.utcfromtimestamp(submission.created).strftime('%d-%m-%Y'),
                         'Hour':datetime.datetime.utcfromtimestamp(submission.created).strftime('%H:%M:%S'),
                         'Gilded':submission.gilded,
                         'Upvotes' : submission.ups, 'DownVotes' : int(int(submission.ups)/float(submission.upvote_ratio)-int(submission.ups)),
                         'Upvote_ratio' : submission.upvote_ratio, 'url' : submission.url})
        


