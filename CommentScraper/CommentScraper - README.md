# Reddit Comment Scraper

Script that scrapes the top comments from every post on a subreddit into a .txt file. You can enter a subreddit's name, choose to sort by Hot, New, Controversial, or Top, and have the script automatically scrape every top comment from the first `n` post. (maximum of 1000) Every post's comments will be stored in a different `.txt` file, with the post's title, score, and url noted in the first line.

If you want to tailor the script to your personal use case, it is trivial to change the format of the output. (Save comment's scores, format the output differently, etc.)

WARNING! If you enter the name of a quarantined subreddit, the script will automatically opt in to seeing that subreddit. If you are concerned about not visiting quarantined subreddits accidentally, check them from a browser beforehand.
