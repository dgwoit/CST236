

PerformanceFuncs = []


def performance():
    def wrapper(func):
        def add_perf_info(*args, **kwargs):
            PerformanceFuncs.append(func.__name__)
            return func(*args, **kwargs)

        return add_perf_info
    return wrapper

