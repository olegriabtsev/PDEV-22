from datetime import datetime
import time


class Timer:
    def __init__(self):
        pass

    def __enter__(self):
        self.start = datetime.utcnow()
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Time passed: {(datetime.utcnow() - self.start).total_seconds()}')


with Timer():
    time.sleep(2)
