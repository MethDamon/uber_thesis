import twint

c = twint.Config()
c.Since = '2019-04-01'
c.Until = '2019-05-31'
c.Debug = True
c.Lang = 'en'
c.Hide_output = False
c.Store_json = True
c.Search = """
    #uberride OR #uberdriver OR #uber OR #uberlyftstrike
    OR #uberstrike OR #ubershutdown OR #lyft OR #lyftstrike
    OR #uberipo OR #driversunite OR #strikeuberlyft OR
    #driverslivesmattertoo"""
c.Store_object = False
c.Stats = True
c.Count = True
c.Filter_retweets = True
c.User_full = True
c.Output = 'data.txt'

twint.run.Search(c)