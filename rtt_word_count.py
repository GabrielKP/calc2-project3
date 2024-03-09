import os

from nltk.tokenize import word_tokenize
import pandas as pd

# make sure nltk data is downloaded
# pip3 install --user nltk

try:
    word_tokenize("test this")
except LookupError:
    import nltk

    nltk.download("punkt")

# load file
path_to_file = "/Volumes/opt/russian-troll-tweets/IRAhandle_tweets_1.csv"  # path will be different!
tweet_df = pd.read_csv(path_to_file)
print(tweet_df["content"])


# # compute word count for each tweet
def _word_count(text):
    return len(word_tokenize(text))


word_count_sr = tweet_df["content"].apply(_word_count)
print(word_count_sr)
word_count_sr.name = "word_count"

# save
word_count_sr.to_csv("rtt_word_count_2.csv", index=True, header=True)
