import twint

c = twint.Config()

file_name = '2019_april_may_#uber_EN' # Insert filename

c.Since = '2019-04-01'
c.Until = '2019-05-31'

c.Lang = 'en'

c.Hide_output = False
c.Store_json = True

c.Search = '#uber' # Enter search terms and hashtags
c.Store_object = False

c.Stats = True
c.Count = True

c.Filter_retweets = True

c.User_full = True

c.Output = file_name + '.txt'

print('Running the search')

twint.run.Search(c)

print('done')
