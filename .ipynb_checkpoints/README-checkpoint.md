# An analysis of UBER worker attitudes and social network connections on Twitter

With the widespread use of technologies that facilitate participation in the so-called sharing economy, there is a growing amount of workers whose employment status is far from being traditional. While companies like Uber, Lyft or Foodora promote themselves as being a flexible and attractive opportunity for a side-job, in reality, workers of these platforms are often underpaid, bereft of social security, and report long hours and mental health problems.

The aim of this project would be to collect and analyze worker attitudes and social connections from publicly available data of the Twitter online social network. First, we aim to collect Uber-related messages, so-called tweets using the API of Twitter. Based on the content and sentiment of the tweets, we characterize the authors, who might e.g. be new outlets, users of platforms, or even drivers. As opposed to traditional taxi companies, Uber and Lyft drivers have much fewer tools to communicate with each other. Therefore, by identifying potential drivers, we try to uncover their social connections and understand the ways in which they utilize Twitter. With this study, we would like to complement existing branches of sociological, legal, and algorithmic fairness literature.

## Content of this repository

### Data Collection

Scripts that are used for the general data collection of this project

#### GeoSearch-Tweepy

The code of this script was gathered from [GeoSearch-Tweepy](https://github.com/Ccantey/GeoSearch-Tweepy/blob/master/GeoTweepy.py). See the folder for a description of its content and the prerequisites.

#### `FilteredStream.py`

##### Prerequisites

- http://mysql-python.sourceforge.net/MySQLdb.html
- 

This script uses the [Twitter Filtered Stream](https://developer.twitter.com/en/docs/labs/filtered-stream/overview) to collect English Tweets containing a variety of UBER related keywords and hashtags and stores them in a MySQL database

#### `TwitterScraping.ipynb`

#### Prerequisites

- [TWINT - Twitter Intelligence Tool](https://github.com/twintproject/twint)

Jupyter Notebook using [TWINT - Twitter Intelligence Tool](https://github.com/twintproject/twint) for social network analysis.