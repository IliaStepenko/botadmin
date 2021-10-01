import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI

from datasource import DataSource

app = FastAPI()
db = DataSource()


class SourceChatModel(BaseModel):
    id: int
    chat_id: int
    chat_name: str


class TargetChatModel(BaseModel):
    id: int
    chat_id: int
    chat_name: str


class ChatRoute(BaseModel):
    id: int
    source_chat: SourceChatModel
    target_chat: TargetChatModel


source_chats = [SourceChatModel(id=i,chat_id=i,chat_name=str(i)+"src") for i in range(5)]
target_chats = [TargetChatModel(id=i,chat_id=i,chat_name=str(i)+"trgt") for i in range(5)]
chat_routes = [ChatRoute(id=i, source_chat=source_chats[i], target_chat=target_chats[i]) for i in range(5)]

# =======================================  API ========================

#
@app.get('/target_chats')
async def get_target_chats():
    return target_chats


@app.get('/source_chats')
async def get_source_chats():
    return source_chats


@app.get('/chat_routes')
async def get_chats_routes():
    return chat_routes


#
@app.get('/target_chat/{id}')
async def get_target_chats(id:int):
    return target_chats[id]


@app.get('/source_chat/{id}')
async def get_source_chats(id:int):
    return source_chats[id]


@app.get('/chat_route/{id}')
async def get_chats_routes(id:int):
    return chat_routes[id]


@app.post('/add_source_chat')
async def add_source_chat(source_chat:SourceChatModel):
    source_chat.id = len(source_chats)
    source_chats.append(source_chat)
    return source_chats[-1]


@app.post('/add_target_chat')
async def add_target_chat(target_chat:TargetChatModel):
    target_chat.id = len(target_chats)
    source_chats.append(target_chat)
    return source_chats[-1]


if __name__ == '__main__':
    uvicorn.run("__main__:app", port=8000, host='127.0.0.1')
