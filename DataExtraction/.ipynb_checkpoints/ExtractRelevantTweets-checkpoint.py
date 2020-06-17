from sqlalchemy import create_engine
import pymysql
import pandas as pd
from pprint import pprint

keywords = ['@uber', '#uber']

output_path = 'relevant_tweets_twitterfeed.csv'

db_user = 'tim'
db_password = 'supersecurepassword'
db_host = 'localhost'
db_name = 'tweets'

chunksize = 30_000

sql_engine = create_engine(
    'mysql+pymysql://%s:%s@%s/%s' % (db_user, db_password, db_host, db_name))
db_connection = sql_engine.connect()
generator = pd.read_sql('select id, text from TwitterFeed;', con=db_connection, chunksize=chunksize)

new_df = pd.DataFrame()

i = 1
for df in generator:
    print(">>> Processing chunk %d" % (i))
    i += 1
    for index, row in df.iterrows():
        text = row['text'].lower()
        match = [keyword in text for keyword in keywords]
        if any(match):
            new_df = new_df.append(row)

print('>>> Found %d relevant tweets' % len(new_df.index))

new_df.to_csv(output_path, header='column_names')