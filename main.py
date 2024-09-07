from typing import List

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get('/')
def hello():
    return 'Welcome'


@app.get('/movies_by_id/{cinema_id}')
def get_movies(cinema_id: int) -> List[str]:
    movies = ['Movie1', 'Movie2', 'Movie3']
    if cinema_id <= len(movies):
        return [movies[cinema_id - 1]]
    else:
        raise HTTPException(status_code=404, detail='There is no film with this index')
