file_path = 'data/tim_uber_tweet_user_place.rpt'

tweets_path = 'tweets1.csv'

users_path = 'users1.csv'

places_path = 'places1.csv'

tweets2_path = 'tweets2.csv'

users2_path = 'users2.csv'

places2_path = 'places2.csv'

tweets_line_start = 42
tweets_line_end = 32_578
tweets = []

users_line_start = 32_581
users_line_end = 52_385
users = []

places_line_start = 52_388
places_line_end = 56_165
places = []

tweets2_line_start = 56_168
tweets2_line_end = 58_317
tweets2 = []

users2_line_start = 58_320
users2_line_end = 59_272
users2 = []

places2_line_start = 59_275
places2_line_end = 59_762
places2 = []

tweets_file = open(file_path)

for pos, line in enumerate(tweets_file):
    if pos in range(tweets_line_start, tweets_line_end):
        tweets.append(line)
    if pos in range(users_line_start, users_line_end):
        users.append(line)
    if pos in range(places_line_start, places_line_end):
        places.append(line)
    if pos in range(tweets2_line_start, tweets2_line_end):
        tweets2.append(line)
    if pos in range(users2_line_start, users2_line_end):
        users2.append(line)
    if pos in range(places2_line_start, places2_line_end):
        places2.append(line)

with open(tweets_path, 'w') as f:
    for line in tweets:
        f.write(line)

with open(users_path, 'w') as f:
    for line in users:
        f.write(line)

with open(places_path, 'w') as f:
    for line in places:
        f.write(line)

with open(tweets2_path, 'w') as f:
    for line in tweets2:
        f.write(line)

with open(users2_path, 'w') as f:
    for line in users2:
        f.write(line)

with open(places2_path, 'w') as f:
    for line in places2:
        f.write(line)