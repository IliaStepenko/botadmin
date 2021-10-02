from typing import List

from fastapi import APIRouter, Request


from models.request import ChatModel
from db.config import async_session
from db.models.chats import TargetChats, SourceChats, TargetChatManager, SourceChatManager

chat_crud = APIRouter()


@chat_crud.get('/')
async def index(request: Request):
    return {
        "categories":[
            f'{request.url}/target_chat',
            f'{request.url}/source_chat'
        ]
    }


@chat_crud.get('/target_chat')
async def target_chats() -> List[TargetChats]:
    async with async_session() as session:
        async with session.begin():
            trgt_list = await TargetChatManager(session).get_chat_list()
            return trgt_list


@chat_crud.get('/target_chat/{id}')
async def target_chats(id: int) -> TargetChats:
    async with async_session() as session:
        async with session.begin():
            chat = await TargetChatManager(session).get_chat(chat_id=id)
            return chat


@chat_crud.post('/target_chat/{chat_id}')
async def update_chat(chat_id: int, chat: ChatModel):
    async with async_session() as session:
        async with session.begin():
            await TargetChatManager(session).update_chat(
                id=chat_id, chat_id=chat.chat_id, name=chat.name, active=chat.active, tg_link=chat.tg_link)


@chat_crud.put('/target_chat')
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


@chat_crud.delete('/target_chat/{chat_id}')
async def remove_chat(chat_id: int):
    async with async_session() as session:
        async with session.begin():
            await TargetChatManager(session).remove_chat(chat_id)
    return ""


@chat_crud.get('/source_chat')
async def source_chat() -> List[SourceChats]:
    async with async_session() as session:
        async with session.begin():
            src_list = await SourceChatManager(session).get_chat_list()
            return src_list


@chat_crud.get('/source_chat/{id}')
async def source_chats(id: int) -> SourceChats:
    async with async_session() as session:
        async with session.begin():
            chat = await SourceChatManager(session).get_chat(chat_id=id)
            return chat


@chat_crud.post('/source_chat/{chat_id}')
async def update_chat(chat_id: int, chat: ChatModel):
    async with async_session() as session:
        async with session.begin():
            await SourceChatManager(session).update_chat(
                id=chat_id, chat_id=chat.chat_id, name=chat.name, active=chat.active, tg_link=chat.tg_link)


@chat_crud.put('/source_chat')
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


@chat_crud.delete('/source_chat/{chat_id}')
async def remove_chat(chat_id: int):
    async with async_session() as session:
        async with session.begin():
            await SourceChatManager(session).remove_chat(chat_id)
    return ""
