if __name__ == '__main__':
    # example 1:
    # while True:
    #     try:
    #         n = float(input('Give an float number: '))
    #     except TypeError:
    #         print('Try again')
    #     except ValueError:
    #         print("can't convert to float")
    #     else:
    #         result = abs(n)
    #         print(f'absolute value of the {n} is {result}')
    #         break

    # example 2:

    # class oopsException():
    #     pass
    #
    # raise oopsException('error')


# example 2:

    # import time
    # import math
    #
    #
    # def timed_func(func):
    #     def wrapper(*args, **kwargs):
    #         start_time = time.time()
    #
    #         end = time.time()
    #         czas = round(start_time + end, 10)
    #         print("--- %s seconds ---" % (str(time.time() - start_time)))
    #         return czas
    #
    #         # start = time.time()
    #         #
    #         # a = 0
    #         # for i in range(1000):
    #         #     a += (i ** 100)
    #         #
    #         # end = time.time()
    #         #
    #         # print("The time of execution of above program is :", end - start)
    #
    #     return wrapper
    #
    #
    # @timed_func
    # def sumowanie_liczb(*args, stala=math.pi):
    #     return sum(args) + stala
    #
    #
    # if __name__ == '__main__':
    #     sumowanie_liczb(141414,12313)
    #     print(time.time())


# example 2: second
# import math
# import time
# def timed_func(function):
#     def wrap(*args, **kwargs):
#         czas_pocz = time.time()
#         function(*args, **kwargs)
#         czas_konc = time.time()
#         roznica = czas_konc - czas_pocz
#         print(f'Czas pocz: {czas_pocz}')
#         print(f'Czas konc: {czas_konc}')
#         print(f'Czas operacji wynosi: {roznica}')
#     return wrap
#
# @timed_func
# def sumujaca(*args, liczbapi=math.pi):
#     return sum(args) + liczbapi
#
# if __name__ == '__main__':
#     sumujaca(35,55,832415,234,12,8, liczbapi=2235)


# example 3: third
#     import math
#     import time
#
#     def time_func(function):
#         def wrapper(*args, **kwargs):
#             czas_pocz = time.time()
#             function(*args, **kwargs)
#             czas_kon = time.time()
#             roznica = czas_kon - czas_pocz
#             print(f'Czas początkowy wyniósł: {czas_pocz}')
#             print(f'Czas końcowy wyniósł: {czas_kon}')
#             print(f'Czas operacji wyniósł: {roznica}')
#
#         return wrapper
#
#
#     @time_func
#     def sumujaca(*args, liczbapi=math.pi):
#         return sum(args) + liczbapi
#
#
#     if __name__ == '__main__':
#         sumujaca(3, 5, 8, 2, liczbapi=2224390569406)