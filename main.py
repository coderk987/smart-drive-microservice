from fastapi import FastAPI
from pydantic import BaseModel
import config

app = FastAPI()
print(config.API_KEY)

@app.get('/')
def root():
    return {"body": "wowww"}

todos = []
id = 1

class TodoCreate(BaseModel):
    title: str

@app.get('/todo')
def get_todos():
    return {"body": todos}

@app.post('/todo')
def create_todos(todo: TodoCreate):
    global id
    todos.append({
        'title': todo.title,
        'id': id
    })
    id+=1
    return {"Created a todo"}