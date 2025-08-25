def partial(func, *args, **kwargs):
    def new_func(*more_args, **more_kwargs):
        return func(*args, *more_args, **kwargs, **more_kwargs)
    return new_func

print("first")
print(int("CAFE", base=16))
hex_to_int = partial(int, base=16)
print("second")
print(hex_to_int("CAFE"))
