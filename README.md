# Uber drivers, activists and investors: Community detection and analysis on Twitter

The widespread use and success of platforms of the so-called sharing or gig economy has led to a growing amount of workers whose employment status is often defined by short-term commitments and temporary contracts. Ride sharing companies like Uber and Lyft promote flexible and attractive side-job opportunities, but in reality their drivers are frequently underpaid, bereft of social security, not enrolled in insurance plans, and reporting long hours and mental health problems. As opposed to employees of traditional taxi companies, Uber and Lyft workers also have fewer tools to communicate with each other and are only very recently seeing political support of specialized labor unions and organizations advocating for better conditions. This thesis collects and analyzes publicly available Twitter data using hashtags related to the IPO (Initial Public Offering) of the ridesharing company Uber on May 10, 2019 and the strikes and protests preceding it. Using a combination of dimensionality reduction via PCP (Principal Component Analysis), K-Means Clustering and NLP (Natural Language Processing), this thesis characterizes different communities consisting of news outlets, activists, worker unions, investors or drivers. Further analysis identifies differences in hashtag usage patterns and topics discussed, as well as relation patterns between expressed sentiment and amount of retweets. The goal of this work is to complement existing branches of sociological, legal, and algorithmic fairness literature.


## Content

**`DataCollection.py`**

The script used for collecting the Twitter data.

**`Tweets_Hashtags_Analysis.ipnyb`**

Jupyter notebook for the hashtag analysis part of the data analysis (Section *Tweets over Time*, *Hashtag Occurrences*, and *Hashtag Cooccurrences* of  the *Results* chapter of the thesis)

**`Community_Detection.ipynb`**

Jupyer notebook for the community detection part of the data analysis (Section *Community Detection* of the *Results* chapter of the thesis).
