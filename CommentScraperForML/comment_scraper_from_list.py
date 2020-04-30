#! python3
import praw  # Python Reddit API Wrapper
import os

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

#Top 50 most subscribed to subreddits, as of 2020/april/14
#(from http://redditlist.com/)
subreddit_list = ["announcements",
                  "funny",
                  "AskReddit",
                  "gaming",
                  "pics",
                  "aww",
                  "science",
                  "worldnews",
                  "Music",
                  "movies",
                  "videos",
                  "todayilearned",
                  "news",
                  "IAmA",
                  "gifs",
                  "Showerthoughts",
                  "EarthPorn",
                  "askscience",
                  "food",
                  "Jokes",
                  "explainlikeimfive",
                  "books",
                  "LifeProTips",
                  "Art",
                  "mildlyinteresting",
                  "DIY",
                  "sports",
                  "nottheonion",
                  "space",
                  "gadgets",
                  "television",
                  "Documentaries",
                  "photoshopbattles",
                  "GetMotivated",
                  "listentothis",
                  "UpliftingNews",
                  "tifu",
                  "InternetIsBeautiful",
                  "history",
                  "philosophy",
                  "Futurology",
                  "OldSchoolCool",
                  "dataisbeautiful",
                  "WritingPrompts",
                  "personalfinance",
                  "nosleep",
                  "creepy",
                  "TwoXChromosomes",
                  "memes",
                  "technology"
                  ]

print("Connection sucessfull")
print("WARNING! This script automatically opts in to quarantined subreddits! Do NOT run it on quarantined subreddits you do not wish to opt into")

shutdown = input("\nDo you wish to shut down the computer after the script is done running? (type 'yes')\n>>>> ")

max_comments = int(input("\nMax number of comments per post:\n>>>> "))

print("\nWhich posts to get: ")
print("1 - Hot")
print("2 - New")
print("3 - Controversial")
print("4 - Top")
a = int(input(">>>> "))

if not (a == 1 or a == 2 or a == 3 or a == 4):
    print("Wrong command, defaulting to Hot")
    a = 1

print("\nHow many posts to grab (max 1000): ")
n = int(input(">>>> "))
if n < 0:
    print("Number set to 1")
    n = 1
if n > 1000:
    print("Number capped to 1000")
    n = 1000


printmode = False
comment_num_to_print = 0
y = input("Press Y if you want to see a sample of the scraped comments: ")
if y == 'y' or y == 'Y':
    comment_num_to_print = int(input("Print every 'n-th' comment (enter n): "))
    printmode = True

print("Scraping top level comments...\n")

i=1
for subreddit_name in subreddit_list:
    print(f"Scraping r/{subreddit_name}...")
    subreddit = reddit.subreddit(subreddit_name)

    if a == 2:
        scraped = subreddit.new(limit=n)
    elif a == 3:
        scraped = subreddit.controversial(limit=n)
    elif a == 4:
        scraped = subreddit.top(limit=n)
    else:
        scraped = subreddit.hot(limit=n)

    filename = subreddit_name + ".txt"
    f = open(filename, 'w', encoding='utf-8')

    j = 1
    for submission in scraped:
        if j % 100 == 0 :
            print(f"Post {j}/{n}")
        m = 1
        for top_level_comment in submission.comments:
            if n == max_comments :
                break
            
            if isinstance(top_level_comment, MoreComments):
                continue
            
            f.write("\n---------\n")
            f.write(top_level_comment.body + '\n')

            if printmode:
                if i > comment_num_to_print - 1:
                    i = 1
                    print(f'\n---------\n{top_level_comment.body}\n')
                else:
                    i = i + 1
            m += 1
        j += 1
    f.close()
    print(f"Scraping r/{subreddit_name} complete\n")


if shutdown == "yes" :
    os.system("shutdown /s /t 1") 
else :
    print("Exiting...")
