import os
import requests
import json
import time
from pprint import pprint
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
import MySQLdb

# DB variables
db_host = ''
db_user = ''
db_pw = ''
db_name = ''

# Twitter API Auth keys
consumer_key = ""
consumer_secret = ""

# Twitter API endpoints
stream_url = "https://api.twitter.com/labs/1/tweets/stream/filter"
rules_url = "https://api.twitter.com/labs/1/tweets/stream/filter/rules"

sample_rules = [
    {'value': '(uber OR #uber OR uberdriver OR #uberdriver OR (uber driver) OR uberx OR #uberx OR uberride OR #uberride OR (uber ride)) lang:en'},
]

db = MySQLdb.connect(host=db_host, user=db_user,
                     passwd=db_pw, db=db_name)
curr = db.cursor()

# Gets a bearer token
class BearerTokenAuth(AuthBase):
    def __init__(self, consumer_key, consumer_secret):
        self.bearer_token_url = "https://api.twitter.com/oauth2/token"
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.bearer_token = self.get_bearer_token()

    def get_bearer_token(self):
        response = requests.post(
            self.bearer_token_url,
            auth=(self.consumer_key, self.consumer_secret),
            data={'grant_type': 'client_credentials'},
            headers={'User-Agent': 'TwitterDevFilteredStreamQuickStartPython'})

        if response.status_code is not 200:
            raise Exception(f"Cannot get a Bearer token (HTTP %d): %s" % (
                response.status_code, response.text))

        body = response.json()
        return body['access_token']

    def __call__(self, r):
        r.headers['Authorization'] = f"Bearer %s" % self.bearer_token
        r.headers['User-Agent'] = 'TwitterDevFilteredStreamQuickStartPython'
        return r


def get_all_rules(auth):
    response = requests.get(rules_url, auth=auth)

    if response.status_code is not 200:
        raise Exception(f"Cannot get rules (HTTP %d): %s" %
                        (response.status_code, response.text))

    return response.json()


def delete_all_rules(rules, auth):
    if rules is None or 'data' not in rules:
        return None

    ids = list(map(lambda rule: rule['id'], rules['data']))

    payload = {
        'delete': {
            'ids': ids
        }
    }

    response = requests.post(rules_url, auth=auth, json=payload)

    if response.status_code is not 200:
        raise Exception(f"Cannot delete rules (HTTP %d): %s" %
                        (response.status_code, response.text))


def set_rules(rules, auth):
    if rules is None:
        return

    payload = {
        'add': rules
    }

    response = requests.post(rules_url, auth=auth, json=payload)

    if response.status_code is not 201:
        raise Exception(f"Cannot create rules (HTTP %d): %s" %
                        (response.status_code, response.text))


def stream_connect(auth):
    response = requests.get(stream_url, auth=auth, stream=True)
    for response_line in response.iter_lines():
        if response_line:
            json_data = json.loads(response_line)
            pprint(json_data)
            data = json_data['data']
            curr.execute(u"""INSERT INTO FilteredStream (ID, AuthorID, Date, Text, Data) VALUES
                                    (%s, %s, %s, %s, %s);""",
                     (data['id'], data['author_id'], data['created_at'], data['text'], str(json_data)))
            db.commit()


bearer_token = BearerTokenAuth(consumer_key, consumer_secret)


def setup_rules(auth):
    current_rules = get_all_rules(auth)
    delete_all_rules(current_rules, auth)
    set_rules(sample_rules, auth)


# Comment this line if you already setup rules and want to keep them
setup_rules(bearer_token)

# Listen to the stream.
# This reconnection logic will attempt to reconnect when a disconnection is detected.
# To avoid rate limites, this logic implements exponential backoff, so the wait time
# will increase if the client cannot reconnect to the stream.
timeout = 0
while True:
    stream_connect(bearer_token)
    time.sleep(2 ** timeout)
    timeout += 1