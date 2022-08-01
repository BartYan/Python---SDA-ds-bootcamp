#1 Given a list, write a Python program to swap first and last element of the list.
listExample = ['one', 'two', 'three', 'four', 'five'];

def swapItems(list):
    listLenght = len(list)
    first = list[0]

    list[0] = list[listLenght-1]
    list[listLenght-1] = first
    return list

print(swapItems(listExample))

#
# def swapList(newList):
#     newList[0], newList[-1] = newList[-1], newList[0]
#
#     return newList
#
# # Driver code
# someList = [12, 35, 9, 56, 24]
# someList2 = [12, 35, 9, 56, 29]
# print(swapList(someList2))




