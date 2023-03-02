import pandas as pd
import requests

# 영화 상세페이지 주소를 movies_df 데이터 프레임에 붙히기
def add_url(row):
    return f"http://www.imdb.com/title/tt{row}/"

# 영화의 레이팅 추가하기
def add_rating(df):
    ratings_df = pd.read_csv('data/ratings.csv')
    ratings_df['movieId'] = ratings_df['movieId'].astype(str)
    agg_df = ratings_df.groupby('movieId').agg(
        rating_count=('rating', 'count'),
        rating_avg=('rating', 'mean')
    ).reset_index()

    rating_added_df = df.merge(agg_df, on='movieId')
    return rating_added_df

if __name__ == "__main__":
    movies_df = pd.read_csv('data/movies.csv')
    # print(movies_df)
    # id를 문자로 인식할 수 있도록 type을 변경
    movies_df['movieId'] = movies_df['movieId'].astype(str)
    links_df = pd.read_csv('data/links.csv', dtype=str)
    merged_df = movies_df.merge(links_df, on='movieId', how='left')
    # print(merged_df)
    # print(merged_df.columns)
    merged_df['url'] = merged_df['imdbId'].apply(lambda x: add_url(x))
    result_df = add_rating(merged_df)
    # print(merged_df)
    # print(merged_df.iloc[1,:])
    print(result_df)

