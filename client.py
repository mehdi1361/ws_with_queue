from multiprocessing.managers import BaseManager

class QueuedManager(BaseManager):
    pass


QueuedManager.register('queue')
manager = QueuedManager(address=('', 50000), authkey=b'abc')
manager.connect()

m = manager.queue()
m.create_channel("t")
m.enque("t", 1)
m.deque("t")
