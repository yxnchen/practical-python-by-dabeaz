import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time for {func.__module__}.{func.__name__}: {(end - start):.4f}s')
        return r
    return wrapper
