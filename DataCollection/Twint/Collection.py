import twint

c = twint.Config()

file_name = '2019_#uberlyftstrike_april_and_may.txt' # Insert filename

c.Since = '2019-04-01'
c.Until = '2019-05-31'
c.Hide_output = True
c.Store_json = True
c.Search = '#uberlyftstrike' # Enter search terms and hashtags
c.Store_object = True
c.Stats = True
c.Count = True
c.Output = './data/twint/%s.txt' % (file_name)
#c.Near = 'boston' # Uncomment to get tweets around a location

print('Running the search')
twint.run.Search(c)