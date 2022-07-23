def decoration(func):
    def wrapper(*args, **kwargs):
        print(f"Argumeenty pozycyjne to: {' ,'.join([str(arg)for arg in args])}")
        print(f"Argumeenty nazwane to: {' ,'.join([str(arg) for arg in kwargs])}")
        result = func(*args, **kwargs)
        print(f"Zwrócony wynik to: {result}")
        return result
    return wrapper

@decoration
def square_numbers(*args, potega = 2):
    square = []
    for arg in args:
       square.append(arg**potega)

    return square


if __name__ == '__main__':
    square_numbers(10, 2, potega=3)

