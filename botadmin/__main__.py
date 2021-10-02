from typing import List

import uvicorn
from fastapi import FastAPI, Request


from models.request import ChatModel
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
            src_list = await SourceChatManager(session).get_chat_list()
            return src_list


@app.get('/target_chat/{id}')
async def target_chats(id: int) -> TargetChats:
    async with async_session() as session:
        async with session.begin():
            chat = await TargetChatManager(session).get_chat(chat_id=id)
            return chat


@app.get('/source_chat/{id}')
async def source_chats(id: int) -> SourceChats:
    async with async_session() as session:
        async with session.begin():
            chat = await SourceChatManager(session).get_chat(chat_id=id)
            return chat


@app.put('/source_chat')
async def create_source_chat(chat: ChatModel) -> ChatModel:
    async with async_session() as session:
        async with session.begin():
            new_chat = await SourceChatManager(session).create_chat(
                chat_id =chat.chat_id,
                name    =chat.name,
                active  =chat.active,
                tg_link =chat.tg_link
            )
            return new_chat


@app.put('/target_chat')
async def create_target_chat(chat: ChatModel) -> ChatModel:

    async with async_session() as session:
        async with session.begin():
            new_chat = await SourceChatManager(session).create_chat(
                chat_id =chat.chat_id,
                name    =chat.name,
                active  =chat.active,
                tg_link =chat.tg_link
            )
            return new_chat


@app.delete('/target_chat/{chat_id}')
async def remove_chat(chat_id: int):
    async with async_session() as session:
        async with session.begin():
            await TargetChatManager(session).remove_chat(chat_id)


@app.delete('/source_chat/{chat_id}')
async def remove_chat(chat_id: int):
    async with async_session() as session:
        async with session.begin():
            await SourceChatManager(session).remove_chat(chat_id)


@app.post('/target_chat/{chat_id}')
async def update_chat(chat_id: int, chat: ChatModel):
    async with async_session() as session:
        async with session.begin():
            await TargetChatManager(session).update_chat(
                id=chat_id, chat_id=chat.chat_id, name=chat.name, active=chat.active, tg_link=chat.tg_link)


@app.post('/source_chat/{chat_id}')
async def update_chat(chat_id: int, chat: ChatModel):
    async with async_session() as session:
        async with session.begin():
            await SourceChatManager(session).update_chat(
                id=chat_id, chat_id=chat.chat_id, name=chat.name, active=chat.active, tg_link=chat.tg_link)


if __name__ == '__main__':
    uvicorn.run("__main__:app", port=8000, host='127.0.0.1')
