def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

# 2
# def square(nums):
#     for num in nums:
#         yield num**2
#
# print(sum(square(fibonacci_numbers(10))))

# 3
# def fib(n):
#     if n < 1:
#         return 0
#     if n < 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# print(fib(10));


