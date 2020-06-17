import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="supersecurepassword",
  database="eszter_tweets"
)

mycursor = mydb.cursor()

sql = """INSERT INTO tweets1 (run_id, tweet_id, lon, lat, place_id, created_at, user_id, text) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

with open('tweets1.csv') as f:
    reader = csv.reader(f)
    for line in reader:
        line = [None if val == 'NULL' else val for val in line]
        print(line)
        mycursor.execute(sql, tuple(line))
        mydb.commit()