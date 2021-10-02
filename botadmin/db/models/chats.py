from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import Column, Integer, String, Boolean, text, BigInteger
from sqlalchemy.orm import Session
from ..config import Base


class BaseChatsModel(Base):
    __abstract__ = True

    id      = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger)
    name    = Column(String, nullable=True)
    active  = Column(Boolean)
    tg_link = Column(String, nullable=True)


class TargetChats(BaseChatsModel):
    __tablename__ = '''TargetChats'''


class SourceChats(BaseChatsModel):
    __tablename__ = '''SourceChats'''


class ChatManager:
    model = None

    def __init__(self, db_session:Session):
        self.db_session = db_session

    async def get_chat_list(self):
        q = await self.db_session.execute(select(self.model))
        return q.all()

    async def get_chat(self, chat_id: int):
        q = await self.db_session.execute(select(self.model).where(self.model.id == chat_id))
        return q.first()

    async def create_chat(self, chat_id: int, name:str, active:bool, tg_link:str):
        new_chat = self.model(chat_id=chat_id, name=name, active=active, tg_link=tg_link)
        self.db_session.add(new_chat)
        await self.db_session.flush()
        return new_chat

    async def remove_chat(self, chat_id: int):
        await self.db_session.execute(f'''delete from public."{self.model.__tablename__}" where id={chat_id}''')

    async def update_chat(self, id, chat_id:int, name:str, active:bool, tg_link:str):
        q = update(self.model).where(self.model.id == id)
        if chat_id:
            q = q.values(chat_id=chat_id)
        if name:
            q = q.values(name=name)
        if active:
            q = q.values(active=active)
        if tg_link:
            q = q.values(tg_link=tg_link)
        q.execution_options(synchronize_session="fetch")
        await self.db_session.execute(q)

class TargetChatManager(ChatManager):
    model = TargetChats


class SourceChatManager(ChatManager):
    model = SourceChats

