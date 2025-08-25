def memoize(func):
    cache = {}
    def wrapper(args):
        print(args)
        if args in cache:
            print(f"Cached: {cache}")
            return cache[args]
        result = func(args)
        print(f"Put into cache: {args}")
        cache[args] = result
        return result
    return wrapper

@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
## fib = memoize(fib)

print(fib(4))
