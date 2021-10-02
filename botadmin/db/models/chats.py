from sqlalchemy.future import select
from sqlalchemy import Column, Integer, String, Boolean, text
from sqlalchemy.orm import Session
from ..config import Base


class BaseChatsModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    name = Column(String, nullable=True)
    active = Column(Boolean)
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

    async def get_chat(self, chat_id):
        q = await self.db_session.execute(select(self.model).where(self.model.id==chat_id))
        return q.fetchall()


class TargetChatManager(ChatManager):
    model = TargetChats


class SourceChatManager(ChatManager):
    model = SourceChats

