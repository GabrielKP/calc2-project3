import math

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def analyze_data(data_path):
    # load data
    word_count_df = pd.read_csv(data_path)

    # get iqr
    q1 = word_count_df["word_count"].quantile(0.25)
    q3 = word_count_df["word_count"].quantile(0.75)
    iqr = q3 - q1
    outlier_boundary = 1.5 * iqr + word_count_df["word_count"].quantile(0.75)
    outlier_boundary_bottom = word_count_df["word_count"].quantile(0.25) - 1.5 * iqr
    print(f"Outlier boundary upper at: {outlier_boundary}")
    print(f"Outlier boundary bottom at: {outlier_boundary_bottom}")

    # remove outliers
    word_count_df = word_count_df[word_count_df["word_count"] < outlier_boundary]

    # compute within std calculations
    wc_mean = word_count_df["word_count"].mean()
    wc_std = word_count_df["word_count"].std()

    # compute statistics
    word_count_stats = word_count_df["word_count"].describe()
    print(word_count_stats)
    print(word_count_df["word_count"].mean())

    # part 1 - 4
    # compute within std
    within_1_std = word_count_df[
        (word_count_df["word_count"] > wc_mean - wc_std)
        & (word_count_df["word_count"] < wc_mean + wc_std)
    ]
    within_2_std = word_count_df[
        (word_count_df["word_count"] > wc_mean - 2 * wc_std)
        & (word_count_df["word_count"] < wc_mean + 2 * wc_std)
    ]
    within_3_std = word_count_df[
        (word_count_df["word_count"] > wc_mean - 3 * wc_std)
        & (word_count_df["word_count"] < wc_mean + 3 * wc_std)
    ]
    print(f"% Within 1 std: {within_1_std.count() / word_count_df.count()}")
    print(f"% Within 2 std: {within_2_std.count() / word_count_df.count()}")
    print(f"% Within 3 std: {within_3_std.count() / word_count_df.count()}")

    # part 2 - 2
    a = 0
    b = 36
    m = 50
    bin_size = (b - a) / m
    xs = list()
    cdf = list()
    for bin in range(m + 1):
        xs.append(round(bin * bin_size, 2))
        cdf.append(
            round(
                (
                    word_count_df[word_count_df["word_count"] < bin * bin_size].count()
                    / word_count_df.count()
                ).item(),
                2,
            )
        )
    print(xs)
    print(cdf)

    # part 2 - 3
    fig = px.line(x=xs, y=cdf)
    fig.update_layout(
        title="",  # Word Count of Russian Troll Tweets
        xaxis_title="",  # Number of Tweets
        yaxis_title="",  # Word Count
        plot_bgcolor="rgba(0, 0, 0, 0)",
        xaxis=dict(
            showline=True,
            linewidth=3,
            linecolor="black",
            tickfont=dict(size=33),
        ),
        yaxis=dict(
            ticks="outside",
            tickwidth=6,
            showline=True,
            linewidth=3,
            linecolor="black",
            tickfont=dict(size=33),
        ),
    )
    # fig.show()
    fig.write_image("cdf.png", width=1000, height=1000)

    # part 2 - 4
    pdf = list()
    for idx in range(m - 1):
        pdf.append(round((cdf[idx + 2] - cdf[idx]) / (2 * bin_size), 2))

    print(pdf)

    # part 2 - 5
    fig = px.line(x=xs[0:-2], y=pdf)
    fig.update_layout(
        title="",  # Word Count of Russian Troll Tweets
        xaxis_title="",  # Number of Tweets
        yaxis_title="",  # Word Count
        plot_bgcolor="rgba(0, 0, 0, 0)",
        xaxis=dict(
            showline=True,
            linewidth=3,
            linecolor="black",
            tickfont=dict(size=33),
        ),
        yaxis=dict(
            ticks="outside",
            tickwidth=6,
            showline=True,
            linewidth=3,
            linecolor="black",
            tickfont=dict(size=33),
        ),
    )
    # fig.show()
    fig.write_image("pdf.png", width=1000, height=500)

    # part 2 - 6
    def normal_fct(x, mean, std):
        return (1 / (std * (2 * math.pi) ** (1 / 2))) * math.exp(
            -(1 / 2) * ((x - mean) / std) ** 2
        )

    normal = list()
    for x in xs[:-1]:
        normal.append(normal_fct(x, wc_mean, wc_std))
    print(normal)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs[:-2], y=pdf, mode="lines", name="PDF"))
    fig.add_trace(
        go.Scatter(x=xs[:-1], y=normal, mode="lines", name="Normal Distribution")
    )
    fig.update_layout(
        title="",  # Word Count of Russian Troll Tweets
        xaxis_title="",  # Number of Tweets
        yaxis_title="",  # Word Count
        plot_bgcolor="rgba(0, 0, 0, 0)",
        xaxis=dict(
            showline=True,
            linewidth=3,
            linecolor="black",
            tickfont=dict(size=33),
        ),
        yaxis=dict(
            ticks="outside",
            tickwidth=6,
            showline=True,
            linewidth=3,
            linecolor="black",
            tickfont=dict(size=33),
        ),
        legend=dict(title_font_family="Times New Roman", font=dict(size=42)),
    )
    # fig.show()
    fig.write_image("pdf&normal.png", width=1300, height=500)

    # visualize
    fig = px.histogram(
        word_count_df,
        x="word_count",
        nbins=100,
        color_discrete_sequence=["#156082"],
    )
    fig.update_layout(
        title="",  # Word Count of Russian Troll Tweets
        xaxis_title="",  # Number of Tweets
        yaxis_title="",  # Word Count
        plot_bgcolor="rgba(0, 0, 0, 0)",
        xaxis=dict(
            showline=True,
            linewidth=3,
            linecolor="black",
            tickfont=dict(size=33),
        ),
        yaxis=dict(
            ticks="outside",
            tickwidth=6,
            showline=True,
            linewidth=3,
            linecolor="black",
            tickfont=dict(size=33),
        ),
        bargap=0.2,
    )
    # fig.show()
    fig.write_image("word_count_histogram.png", width=2000, height=1400)


if __name__ == "__main__":
    data_path = "data/rtt_word_count_final.csv"
    analyze_data(data_path)
