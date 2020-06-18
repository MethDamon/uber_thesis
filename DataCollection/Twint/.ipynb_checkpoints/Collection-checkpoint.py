import twint

c = twint.Config()

c.Since = '2019-01-01'
c.Until = '2019-08-31'
c.Hide_output = True
c.Store_json = True
c.Search = '#uberlyftstrike'
c.User_full = True
c.Store_object = True
c.Stats = True
c.Count = True
c.Output = '../data/twint/schubidu.txt'
#c.Near = 'boston'

print('Running the search')
twint.run.Search(c)