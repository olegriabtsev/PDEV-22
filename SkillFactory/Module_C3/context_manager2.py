from datetime import datetime
import time

from contextlib import contextmanager


@contextmanager
def timer():
    start = datetime.utcnow()
    yield
    print(f'Time passed: {(datetime.utcnow() - start).total_seconds()}')


with timer():
    time.sleep(2)
