import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start
        print(f"Время выполнения: {elapsed:.2f} сек")
        return False
with Timer():
    time.sleep(1.5)