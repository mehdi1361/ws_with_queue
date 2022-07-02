from multiprocessing.managers import BaseManager


class QueuedClass:
    def __init__(self):
        self.__channel = {}

    def create_channel(self, channel_name):
        if channel_name not in self.__channel.keys():
            self.__channel[channel_name] = []

    def deque(self, channel_name):
        return self.__channel[channel_name].pop(0)

    def enque(self, channel_name, value):
        self.__channel[channel_name].append(value)
        return True


class QueuedManager(BaseManager):
    pass


queue = QueuedClass()
QueuedManager.register('queue',  callable=lambda: queue)
manager = QueuedManager(address=('', 50000), authkey=b'abc')
server = manager.get_server()
server.serve_forever()
