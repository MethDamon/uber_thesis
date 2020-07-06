import twint
import json

c = twint.Config()

file_name = '2019_april_may_uber' # Insert filename

c.Since = '2019-04-01'
c.Until = '2019-05-31'

c.Hide_output = False
c.Store_json = True

c.Search = 'uber' # Enter search terms and hashtags
c.Store_object = False

c.Stats = True
c.Count = True

c.Filter_retweets = True

c.User_full = True

c.Output = file_name + '.txt'

print('Running the search')
twint.run.Search(c)

# Getting the users

with open(file_name + '.txt', 'r') as tweets_file:
    usernames = []
    for line in tweets_file:
        tweet = json.loads(line)
        username = tweet['username']
        usernames.append(username)
    unique_usernames = list(set(usernames))
    tweets_file.close()

c = twint.Config()
c.Store_object = False
c.Store_json = True
c.Output = file_name + '_users' + '.txt'
for username in unique_usernames:
    c.Username = username
    print('Looking up user "%s"' % username)
    twint.run.Lookup(c)
