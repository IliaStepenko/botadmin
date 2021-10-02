from typing import List

import uvicorn
from fastapi import FastAPI
from db.config import async_session
from db.models.chats import TargetChats, SourceChats, TargetChatManager, SourceChatManager


app = FastAPI()


@app.get('/')
async def index():
    return "hello"


@app.get('/target_chat')
async def target_chats() -> List[TargetChats]:
    async with async_session() as session:
        async with session.begin():
            trgt_list = await TargetChatManager(session).get_chat_list()
            return trgt_list


@app.get('/source_chat')
async def target_chats() -> List[SourceChats]:
    async with async_session() as session:
        async with session.begin():
            src_list = await TargetChatManager(session).get_chat_list()
            return src_list


@app.get('/target_chat/{id}')
async def target_chats(id: int) -> TargetChats:
    async with async_session() as session:
        async with session.begin():
            chat = await SourceChatManager(session).get_chat(chat_id=id)
            return chat


@app.get('/source_chat/{id}')
async def target_chats(id: int) -> SourceChats:
    async with async_session() as session:
        async with session.begin():
            chat = await TargetChatManager(session).get_chat(chat_id=id)
            return chat


if __name__ == '__main__':
    uvicorn.run("__main__:app", port=8000, host='127.0.0.1')
