def debug(func):
    def wrapper(*args, **kwargs):
        arguments = " ,".join([str(arg)for arg in args]);
        kwarguments = " ,".join([str(arg)for arg in kwargs]);
        result = func(*args,**kwargs)

        print(f'funkcja o nazwie {func.__name__}, argumenty pozycyjne {arguments}, argumenty nazwane: {kwarguments}')
        return result

    return wrapper



@debug
def example(a,b,c):
    return (a + b * c)


if __name__ == '__main__':
    print(example(2, b=3, c=4))

