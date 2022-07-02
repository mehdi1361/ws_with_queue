from fastapi import APIRouter, Request
from schema import MessageSchema
from collections import deque

router = APIRouter(
    tags=['items'],
    responses={404: {"description": "Page not found"}}
)


@router.post('/send-message')
async def send_message(payload: MessageSchema, request: Request):
    request.app.pika_client.send_message(
        {"message": payload.message}
    )
    return {"status": "ok"}

@router.get('/get-message')
async def get_message(request: Request):
    a = request.app.pika_client.send_message()
    return {"status": "ok"}

@router.get('/get-test')
async def get_test(request: Request):
    data = 0
    return {"status": data}
