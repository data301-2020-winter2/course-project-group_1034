import pandas as pd
import numpy as np
import seaborn as sns

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

def count(url):
    df8 = (
        def unique('first category'):
        seen = set()
        return [x for x in sequence if not (x in seen or seen.add(x))]
        def print_count(pr):
        for item in unique(pr):  
        print(item, pr.count(item))
    )

    return df8