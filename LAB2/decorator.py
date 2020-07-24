def cached(func):
    cache = {}

    def save_in_cache(*args, **kwargs):
        arguments=""
        for arg in args:
            arguments+=str(arg)+", "
        for kwarg_key in kwargs:
            arguments += str(kwargs[kwarg_key]) + ", "
        if arguments in cache:
            print("Value from cache")
            return cache[arguments]
        else:
            result=func(*args, **kwargs)
            cache[arguments]=result
            return  result

    return save_in_cache

@cached
def tuple_sum(tpl, control_lst):
    sum=0
    control_lst.append(1)
    for item in tpl:
        sum += item
    return sum

@cached
def prod(a, b):
    return a*b

prod(1,1)
prod(1,b=1)