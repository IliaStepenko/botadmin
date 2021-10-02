from pydantic import BaseModel


class ChatModel(BaseModel):
    chat_id : int
    name    : str
    active  : bool  = False
    tg_link : str = None




