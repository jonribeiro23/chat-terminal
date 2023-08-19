from queue import Queue

class ThreadEmulator:
    def __init__(self):
        self.queue = Queue()

    def create_thread(self, data):
        self.queue.put(data)

    def run_threads(self):
        while not self.queue.empty():
            data = self.queue.get()
            data['func'](data['arg'])


