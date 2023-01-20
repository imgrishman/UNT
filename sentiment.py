import pandas as pd
from textblob import TextBlob

# read the CSV file
df = pd.read_csv(r'https://github.com/imgrishman/UNT/blob/main/Task-1tweets_1000.csv', sep=',', names=['col1', 'col2', 'col3', 'col4', 'col5','col6','col7','col8'])


# create a new column to store the sentiment scores
df['sentiment'] = None

# iterate through each text and perform sentiment analysis
for index, row in df.iterrows():
    pd.options.display.max_rows = None
    text = row['col1']
    sentiment = TextBlob(text).sentiment.polarity
    df.at[index, 'sentiment'] = sentiment

#print the updated dataframe
print(df)
