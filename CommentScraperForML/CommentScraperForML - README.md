# Reddit Comment Scraper For Machine Learning

This script is made to grab a big ammount of comments from different subreddits automatically. In the beginning of the script, you may change the `subreddit_list` list's contents, to track on your own chosen subreddits. The output is stored in a different `.txt` file per subreddit.

This script needs constant internet access while it is ran, and also takes quite a long time, especially if you are grabbing a big number of comments. You may need to run it overnight, if you are running it from your regular work PC, which is why it had the option to automatically shut down your computer after the scripts is done.

WARNING! If you enter the name of a quarantined subreddit, the script will automatically opt in to seeing that subreddit. If you are concerned about not visiting quarantined subreddits accidentally, check them from a browser beforehand.
