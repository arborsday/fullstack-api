# /all 엔드포인트에서 사용되는 random_items 함수를 정의 > main.py에서는 이 함수를 import하여 사용
# pandas에서 제공되는 함수 중 sample이라는 함수를 이용해서 랜덤하게 10개의 데이터를 반환(return)하도록 만들기

import pandas as pd

item_fname = 'data/movies_final.csv'

def random_items():
    movies_df = pd.read_csv(item_fname)
    movies_df = movies_df.fillna('') # 공백을 채워줍니다.
    result_items = movies_df.sample(n=10).to_dict("records")
    return result_items

def random_genres_items(genre):
    movies_df = pd.read_csv(item_fname)
    genre_df = movies_df[movies_df['genres'].apply(lambda x:genre in x.lower())]
    genre_df = genre_df.fillna('')
    result_items = genre_df.sample(n=10).to_dict("records")
    return result_items