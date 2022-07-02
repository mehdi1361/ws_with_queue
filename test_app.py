import logging
import asyncio
from fastapi import FastAPI
from pike_client import PikaClient
from router import router


class FooApp(FastAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pika_client = PikaClient(self.log_incoming_message)

    @classmethod
    def log_incoming_message(cls, message: dict):
        """Method to do something meaningful with the incoming message"""
        logging.info('Here we got incoming message %s', message)

foo_app = FooApp()
foo_app.include_router(router)


@foo_app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(foo_app.pika_client.consume(loop))
    await task
