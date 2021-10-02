from fastapi import FastAPI

from routers.chat_crud_router import chat_crud

app = FastAPI()

app.include_router(chat_crud, prefix='/api/v1')