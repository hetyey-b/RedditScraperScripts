#! python3
import praw  # Python Reddit API Wrapper
import pandas as pd
import datetime as dt

from praw.models import MoreComments

import io

#Visit this page: https://www.reddit.com/prefs/apps
#To create an app (create a personal use script)
#And fill out the data under here:
PERSONAL_USE_SCRIPT_14_CHARS = "**************"
SECRET_KEY_27_CHARS = "***************************"
YOUR_APP_NAME = "..."
YOUR_REDDIT_USER_NAME = "..."
YOUR_REDDIT_LOGIN_PASSWORD = "..."

print("Connecting to Reddit...")
print(f"App {YOUR_APP_NAME} as user {YOUR_REDDIT_USER_NAME}")

reddit = praw.Reddit(client_id=PERSONAL_USE_SCRIPT_14_CHARS,
                     client_secret=SECRET_KEY_27_CHARS,
                     user_agent=YOUR_APP_NAME,
                     username=YOUR_REDDIT_USER_NAME,
                     password=YOUR_REDDIT_LOGIN_PASSWORD)

print("Connection sucessfull")
print("WARNING! This script automatically opts in to quarantined subreddits! Do NOT run it on quarantined subreddits you do not wish to opt into")
sreddit = input("Enter subreddit name (without r/): ")
print(f"Connecting to subreddit r/{sreddit}\n")

subreddit = reddit.subreddit(sreddit)

#Opt in if it's quarantined
try:
    subreddit.quaran.opt_in()
    print("Opted into quarantined subreddit")
except:
    print("Subreddit not quarantined")

print(f"Connected to r/{sreddit}\n")

print("Which posts to get: ")
print("1 - Hot")
print("2 - New")
print("3 - Controversial")
print("4 - Top")
a = int(input(">>>> "))

print("How many posts to grab (max 1000): ")
n = int(input(">>>> "))
if n < 0:
    print("Number set to 1")
    n = 1
if n > 1000:
    print("Number capped to 1000")
    n = 1000

scraped = subreddit.top(limit=1)

if a == 1:
    scraped = subreddit.hot(limit=n)
elif a == 2:
    scraped = subreddit.new(limit=n)
elif a == 3:
    scraped = subreddit.controversial(limit=n)
elif a == 4:
    scraped = subreddit.top(limit=n)
else:
    print("Wrong command")

print("\nScraping complete")

printmode = False
comment_num_to_print = 0
y = input("Press Y if you want to see a sample of the scraped comments: ")
if y == 'y' or y == 'Y' :
    comment_num_to_print = int(input("Print every 'n-th' comment (enter n): "))
    printmode = True

print("Scraping top level comments...\n")

j = 1
for submission in scraped :
    filename =  sreddit + str(j) + ".txt"
    print(f'Post {j} / {n}')
    f = open(filename, 'w', encoding='utf-8')
    header_line = submission.title + ' - Score: ' + str(submission.score)  + ' - url: ' + submission.url + '\n'
    f.write(header_line)
    f.write("------------------\n\n")

    i = 1
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        f.write("\n---------\n")
        f.write(top_level_comment.body)

        if printmode :
            if i > comment_num_to_print - 1 :
                i = 1
                print(f'\n{i}. comment\n{top_level_comment.body}\n')
            else : 
                i = i + 1
    
    j += 1
    f.close()

print("---------------------------------------\nScraping done")
