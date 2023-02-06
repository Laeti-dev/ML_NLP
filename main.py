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

print(tweets.head(100))
