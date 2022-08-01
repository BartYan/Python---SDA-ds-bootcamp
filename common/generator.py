# print((x*2 for x in range(10)))



# def func_with_generator(x):
#     x -=1
#     yield x




# def all_even(max):
#     n = 0
#     while n < max:
#         yield n #przekuzje to w ktorym dokladnie moemncie jestes
#         n += 2
#
# print(sum(all_even(91)))




# print(sum(x**2 for x in range(10)))



# def flatten_list(lista):
#     for element in lista:
#         if isinstance(element, list):
#             yield from flatten_list(element)
#         else:
#             yield element
#
# for i in flatten_list([[1,2],1,2,3,[4,5,6,[7,8]]]):
#     print(i)



# flatten_a_list = [1,2,3,[4,5,6,[7,8,9]]];
# def flatten2(lista):
#     try:
#         for sublist in lista:
#             for element in flatten2(sublist):
#                 yield element
#     except TypeError:
#         yield lista
#
# print(list(flatten2(flatten_a_list)))



# my_list = [[1], [2, 3], [4, 5, 6, 7]]
# flatList = [item for elem in my_list for item in elem]
# print('Flat List : ', flatList)