# Reddit Scraper Scripts

Scripts to scrape data from Reddit. Can be used for any kind of project that needs big amount of data off of Reddit. (e.g. Machine Learning)

WARNING! A lot of the scripts automatically opt into quarantined subreddits! If you don't want that to happen, be careful which subreddits you run the scripts on!

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

### Installing

Just clone this repository anywhere on your system, and you are ready to go. I recommend you run this script from the command line.

## Built With

* [Python 3.7.6](https://www.python.org/)
* [Python Reddit API Wrapper](https://praw.readthedocs.io/en/latest/)
