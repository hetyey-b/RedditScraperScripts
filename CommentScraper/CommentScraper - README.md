# Reddit Comment Scraper

Script that scrapes the top comments from every post on a subreddit into a .txt file. You can enter a subreddit's name, choose to sort by Hot, New, Controversial, or Top, and have the script automatically scrape every top comment from the first `n` post. (maximum of 1000) Every post's comments will be stored in a different `.txt` file, with the post's title, score, and url noted in the first line.

If you want to tailor the script to your personal use case, it is trivial to change the format of the output. (Save comment's scores, format the output differently, etc.)

WARNING! If you enter the name of a quarantined subreddit, the script will automatically opt in to seeing that subreddit. If you are concerned about not visiting quarantined subreddits accidentally, check them from a browser beforehand.

## Getting Started

The script was written in Python 3.7.6. If your Python installation is having problems running the script, I recommend using that particular version.

### Prequisites

* You need a Python 3.x installation (or Python 3.7.6, it's guaranteed to work, if other versions don't)

* You need to have PRAW (Python Reddit API Wrapper) installed. I recommend installing it from the command line:
`pip install praw`

* If you are running Linux, change the shebang line from
`#! python3`
  to
`#! /usr/bin/python3`

* You need to create your own reddit application:
    1. Go the [developed applications](https://www.reddit.com/prefs/apps/ "Reddit developed applications") page, click create an app, choose `script` as the type, add a name, and `http://localhost:8080` as the redirect url
    2. Create the app, and copy the 14 character personal use script and 27 character secret key somewhere safe. Do NOT publish these to anyone!
    3. Open up the `reddit_comment_scraper.py` script in your editor of choice, and add your personal use script, secret key, application name, username, and password as the values of the string variables at the top.

WARNING! These are in no way encrypted (obviously), and you are essentially storing your sensitive data in plain text. Do NOT, under any circumstance give this script to anyone, or upload it to the internet with your data in it.

If you are adept enough, you can store this data somewhere outside the script, I just didn't have the time/patience to set them up in environmental variables, and felt like I personally don't need that for this project.

### Installing

Just clone this repository anywhere on your system, and you are ready to go. I recommend you run this script from the command line.

## Built With

* [Python 3.7.6](https://www.python.org/)
* [Python Reddit API Wrapper](https://praw.readthedocs.io/en/latest/)
