#Upload the mastodon_topics.csv file which Mo sent
import pandas as pd
import praw
reddit = praw.Reddit(client_id='JEISNEQ9UJHjHA', client_secret='CY4kBtqKfivAxAiFa_9P0YdRhbY', user_agent='Subro')

# #Tester code
# #If this works extract all possible subreddit's data

# posts = []
# ml_subreddit = reddit.subreddit('technology').hot(limit=1000)
# for post in ml_subreddit:
#     posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
# posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
# print(posts)

def generate_reddit_without_user():
  reddit = praw.Reddit(client_id='JEISNEQ9UJHjHA', client_secret='CY4kBtqKfivAxAiFa_9P0YdRhbY', user_agent='Subro')

  filtering = pd.read_csv('mastodon_counts.csv')
  new_filt = filtering.sort_values(by='userCount', ascending=False)
  subreddit_all = list(new_filt['topic'])[33:35]
  # print(subreddit_all)
  #importing our error which we get if the subreddit doesnt exist
  from prawcore.exceptions import Forbidden

  #trying to comment (we may be banned)
  for i in subreddit_all:
    try:
        print(i)
        posts = []
        ml_subreddit = reddit.subreddit(i).hot(limit=10000)
        for post in ml_subreddit:
            posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
        posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
        posts.to_csv('reddit_data_without_users.csv' , mode='a')
    except Forbidden or NotFound: #might have to manually do it sometimes
        continue

def generate_reddit_without_user():
  # reddit = praw.Reddit(client_id='JEISNEQ9UJHjHA', client_secret='CY4kBtqKfivAxAiFa_9P0YdRhbY', user_agent='Subro')
  subreddit_all = list(set(list(pd.read_csv('reddit_data_without_users.csv')['subreddit'])))
  subreddit_all.SentimentText=subreddit_all.SentimentText.astype(str)
# print(subreddit_all)
  user_data = []

  for i in subreddit_all:
    print(i)
    subreddit = reddit.subreddit(i)
    user_data.append([i,subreddit.subscribers,subreddit.accounts_active,subreddit.accounts_active_is_fuzzed,subreddit.active_user_count])
  user_data = pd.DataFrame(user_data, columns=['Subreddit name','Number of subscribers','Active accounts','Active Fuzzed accounts','Active user count'])
  user_data.to_csv('reddit_data_with_user.csv', mode = 'w')