# Import some libraries to prepare the project
# Dwl NLTK (Natural language tool kit - all pckg), numpy, pandas, scikit-learn

# OPEN CSV WITH PANDAS
import pandas as pd

tweets = pd.read_csv('./datas/rechauffementClimatique.csv', delimiter=';')

# Discovering our datas
print(tweets.shape)
print(tweets.head(5))

# change CROYANCE feature to numeric values yes = 1 no = 0
tweets['CROYANCE'] = (tweets['CROYANCE'] == 'Yes').astype(int)

print(tweets.head(11))

# NORMALIZE TEXT
import re

# Create a function
def normalize(tweet):
    tweet =re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+','USER', tweet)
    tweet = tweet.lower().replace('ë', 'e')
    tweet = re.sub('[^a-zA-Z1-9]', ' ', tweet)
    tweet = re.sub(' +', ' ', tweet)
    return tweet.strip()

tweets['TWEET'] = tweets['TWEET'].apply(normalize)

print(tweets.head(50))