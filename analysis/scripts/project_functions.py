import pandas as pd
import numpy as np

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