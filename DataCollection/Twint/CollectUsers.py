import twint
import json

tweets_file = './2019_april_may_#uber_EN.txt'

f = open(tweets_file, 'r')
lines = [l for l in f]
f.close()

tweets = [json.loads(l) for l in lines]

usernames = {t['username'] for t in tweets}
    
c = twint.Config()
c.Store_object = False
c.Store_json = True
c.Hide_output = True
c.Output = tweets_file + '_users' + '.txt'

i = 1
for username in usernames:
    c.Username = username
    print('Looking up user "%s" (%s, %s)' % (username, i, len(usernames))) 
    twint.run.Lookup(c)
    i += 1
