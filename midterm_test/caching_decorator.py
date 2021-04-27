import pickle


def my_caching_decorator(caching_filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                with open(caching_filename, 'rb') as f:
                    cache = pickle.load(f)
            except Exception:
                cache = {}

            kwargs_tuple = tuple(kwargs.items())
            if (args, kwargs_tuple) in cache:
                return cache[(args, kwargs_tuple)]
            else:
                result = func(*args, **kwargs)
                cache[(args, kwargs_tuple)] = result
                with open(caching_filename, 'wb') as f:
                    pickle.dump(cache, f)
                return result

        return wrapper
    return decorator


@my_caching_decorator(caching_filename="cache.pickle")
def foo(a, b, bar='baz', baz='baz'):
    return 9


print(foo(1, 2, bar='asdf', baz='asdf'))