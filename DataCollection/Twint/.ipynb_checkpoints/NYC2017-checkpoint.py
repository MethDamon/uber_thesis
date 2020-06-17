import twint

c = twint.Config()

c.Since = '2019-04-01'
c.Until = '2019-05-31'
c.Hide_output = True
c.Store_json = True
c.Search = '#uberlyftstrike'
c.User_full = True
c.Store_object = True
c.Stats = True
c.Count = True
c.Output = '2019_#uberlyftstrike_april_and_may.txt'
#c.Near = 'boston'

print('Running the search')
twint.run.Search(c)