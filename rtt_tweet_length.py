import os

from tqdm import tqdm
import pandas as pd


def export_word_count_all(basedir, file_paths):
    # not enough RAM for all files at the same time,
    # do it file by file
    for idx, file_path in tqdm(
        enumerate(file_paths),
        desc="(computing tweet length)",
        total=len(file_paths),
    ):
        tweet_df = pd.read_csv(os.path.join(basedir, file_path), dtype={"content": str})

        word_count_part_sr = tweet_df["content"].str.len()
        word_count_part_sr.name = "tweet_length"
        word_count_part_sr = word_count_part_sr[~word_count_part_sr.isna()]
        word_count_part_sr = word_count_part_sr.astype(int)

        output_file = os.path.join("data", f"rtt_tweet_length_{idx}.csv")
        word_count_part_sr.to_csv(output_file, index=True, header=True)


if __name__ == "__main__":
    basedir = "/Volumes/opt/russian-troll-tweets"
    file_paths = [
        "IRAhandle_tweets_1.csv",
        "IRAhandle_tweets_2.csv",
        "IRAhandle_tweets_3.csv",
        "IRAhandle_tweets_4.csv",
        "IRAhandle_tweets_5.csv",
        "IRAhandle_tweets_6.csv",
        "IRAhandle_tweets_7.csv",
        "IRAhandle_tweets_8.csv",
        "IRAhandle_tweets_9.csv",
        "IRAhandle_tweets_10.csv",
        "IRAhandle_tweets_11.csv",
        "IRAhandle_tweets_12.csv",
        "IRAhandle_tweets_13.csv",
    ]
    export_word_count_all(basedir, file_paths)
