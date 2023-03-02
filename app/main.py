from typing import List, Optional
from fastapi import FastAPI, Query

from recommender import item_based_recommendation, user_based_recommendation

#git commit test
#eee

# 2. resolver.py에서 함수 끌어오기
from resolver import random_items, random_genres_items
# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# 1. 실제로 활용할 4개의 엔드포인트를 미리 생성

@app.get("/")
async def root():
    return {"message": "Hello Words"}

@app.get("/all/")
async def all_movies():
    result = random_items()
    return {"result": result}

@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    # return {"message": f"genre: {genre}"}
    result = random_genres_items(genre) # random_items와는 다르게 장르를 받아와야 함
    return {"result": result}

@app.get("/user-based/")
async def user_based(params: Optional[List[str]] = Query(None)):
    input_ratings_dict = dict(
        (int(x.split(":")[0]), float(x.split(":")[1])) for x in params or []
    )
    result = user_based_recommendation(input_ratings_dict)
    return {"result": result}

@app.get("/item-based/{item_id}")
async def item_based(item_id: str):
    # return {"messsage": f"item based: {item_id}"}
    result = item_based_recommendation(item_id)
    return {"result": result}