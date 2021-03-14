import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt

def load_and_process(url_or_path_to_csv_file):

    df4 = (
          pd.read_csv(url_or_path_to_csv_file)
          .rename(columns={"screen name": "Stream Name"})
        .rename(columns={"top count":"Ranking"})
        .rename(columns={"watch time":"Watch Time (Hours)"})
        .rename(columns={"stream time":"Stream Time (Hours)"})
        .rename(columns={"peak viewers":"Viewers (Peak)"})
        .rename(columns={"average viewers":"Viewers (Average)"})
        .rename(columns={"followers":"Followers (Total)"})
        .rename(columns={"followers gained":"Followers (Gained)"})
        .rename(columns={"views gained":"Viewers (Gained)"})
        .rename(columns={"partnered":"Partnered"})
        .rename(columns={"mature":"Audience Type (Mature)"})
        .rename(columns={"language":"Language"})
        .rename(columns={"first category":"Primary Game"})
        .rename(columns={"second category":"Secondary Game"})
        .rename(columns={"third category":"Tertiary Game"})
        .drop("profile picture", axis = 1)
        .drop("completa name", axis = 1)
      )

    df5 = (
    df4.head(20).style.set_table_styles(
        [{'selector': 'th',
        'props': [('background', '#6441A4'),
             ('color', 'white'),
             ('font-family', 'verdana')]},
     
        {'selector': 'td',
        'props': [('font-family', 'verdana')]},
     
         {'selector': 'tr:nth-of-type(odd)',
         'props': [('background', '#DCDCDC')]},
     
         {'selector': 'tr:nth-of-type(even)',
         'props': [('background', 'white')]},
     
         {'selector': 'tr:hover',
         'props': [('background-color', '#F5DEF9')]}
        ]
    
    ).hide_index()
    
    )

    return df5

def test(url):
    
    df7 = (
        pd.read_csv(url)
        .drop("profile picture", axis=1)
        .drop("completa name", axis=1)
        .drop("top count", axis=1)
        .drop("watch time", axis=1)
        .drop("peak viewers", axis=1)
        .drop("stream time", axis=1)
        .drop("average viewers", axis=1)
        .drop("followers", axis=1)
        .drop("partnered", axis=1)
        .drop("mature", axis=1)
        .drop("language", axis=1)
        .drop("followers gained", axis=1)
        .drop("views gained", axis=1)

    )
    
    
    return df7

def most_followers_gained(url):
    
    df1 = (
        pd.read_csv(url)
        .drop("profile picture", axis=1)
        .drop("completa name", axis=1)
        .drop("top count", axis=1)
        .drop("watch time", axis=1)
        .drop("peak viewers", axis=1)
        .drop("stream time", axis=1)
        .drop("average viewers", axis=1)
        .drop("followers", axis=1)
        .drop("partnered", axis=1)
        .drop("mature", axis=1)
        .drop("language", axis=1)
        .drop("first category", axis=1)
        .drop("second category", axis=1)
        .drop("third category", axis=1)
    )
    
    df1.sort_values(by=['followers gained'], ascending=False)
    
    return df1

def watch_stream(url):

    df6 = (
        pd.read_csv(url)
        .drop("profile picture", axis=1)
        .drop("completa name", axis=1)
        .drop("top count", axis=1)
        .drop("watch time", axis=1)
        .drop("peak viewers", axis=1)
        .drop("followers gained", axis=1)
        .drop("views gained", axis=1)
        .drop("followers", axis=1)
        .drop("partnered", axis=1)
        .drop("mature", axis=1)
        .drop("language", axis=1)
        .drop("first category", axis=1)
        .drop("second category", axis=1)
        .drop("third category", axis=1)
    )
    
    df6.sort_values(by=['average viewers'], ascending=False)
    
    return df6



def games_played(url):
    df2 = pd.read_csv('../../data/raw/twitchdataset.csv')
    df8 = (
            pd.DataFrame(df2).rename(columns={"first category":"game"})
            .rename(columns={"second category":"game2"})
            .rename(columns={"third category":"game3"})
        )
    value_counts = df8['game'].value_counts()
    to_remove = value_counts[value_counts <= 142].index
    df9 = df8[~df8.game.isin(to_remove)]
    df10 = df9['game'].value_counts()
    value_counts1 = df8['game2'].value_counts()
    to_remove1 = value_counts1[value_counts1 <= 100].index
    df11 = df8[~df8.game2.isin(to_remove1)]
    df12 = df11['game2'].value_counts()
    value_counts2 = df8['game3'].value_counts()
    to_remove2 = value_counts2[value_counts2 <= 100].index
    df13 = df8[~df8.game3.isin(to_remove2)]
    df14 = df13['game3'].value_counts()
    games = df10.head(15)
    games1 = df12.head(15)
    games2 = df14.head(15)
    vertical_stack = pd.concat([games, games1, games2], axis=0)
    df30 = vertical_stack.rename_axis('games').reset_index(name='counts')
    df31 = df30.groupby(["games"]).counts.sum().reset_index()
    matplotlib.style.use('fivethirtyeight') 
    df32 = (
        df31.plot.bar(x = "games", y = "counts", rot = 90)
    )
    plt.title("All Games Played the Most")
    plt.xlabel("Games")
    plt.ylabel("Occurances of Game Between Streamers")
    return df32