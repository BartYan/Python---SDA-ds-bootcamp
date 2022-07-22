# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
#     cyfry = { 1: "zero", 2: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem", 9: "dziewięć"}
#
#     user_in = input("enter numbers:")
#     output_str = ""
#     for elem in user_in:
#         output_str += cyfry[int(elem)] + " "
#     print(output_str)

#
# zad2
    a_list = [42, 13, 56, 7, 12, 3, 85]
    min_elem = min(a_list)
    check = a_list[0]
    index = 0
    # print(min_elem)
    # print(a_list.index(min_elem))
    for elem in a_list:
        if check > elem:
            check = elem

        print(check)


    for elem in a_list:
        index += 1
        if elem == check:
            elem -= 1;
            break
    print(f'index to {index}')


#
# zad 3
#     # print(min_elem)s
#
#     input = input('wpisz:')
#     def check(n):
#         if n % 2 == 0 or n <= 1:
#             print("liczba pierwsza")
#         else:
#             print("liczba nie pierwsza")
#
#     check(int(input))
#
#     # def czesc(imie, miasto):
#     #     print("Czesc " + imie + "!")
#     #     print("Widze, ze jestes z miasta", miasto)
#     #
#     #
#     # czesc("Wroclaw", "Janusz")

    # Zadanie 1

    # if __name__ == "__main__":
    #     cyfry = {
    #         0: "zero",
    #         1: "jeden",
    #         2: "dwa",
    #         3: "trzy",
    #         4: "cztery",
    #         5: "pięć",
    #         6: "sześć",
    #         7: "siedem",
    #         8: "osiem",
    #         9: "dziewięć"
    #     }
    #
    #     user_input = input("Podaj ciąg cyfr \n")
    #     output_str = ""
    #     for elem in user_input:
    #         output_str += cyfry[int(elem)] + " "
    #     print(output_str)
    #
    #
    # # Zadanie 2
    #
    # def get_min_index(lst):
    #     min_value = lst[0]
    #     min_index = 0
    #
    #     for idx, value in enumerate(int_list):
    #         if value < min_value:
    #             min_value = value
    #             min_index = idx
    #
    #     return min_index, min_value
    #
    #
    # if __name__ == "__main__":
    #     int_list = [343, 53, 43, 2, 566, 90, 64]
    #     idx, value = get_min_index(int_list)
    #     print(f"Najmniejsza wartość listy to: {value}, znajduje się na pozycji: {idx}")
    #
    # # Zadanie 3
    #
    # from math import sqrt
    #
    #
    # def is_prime(n):
    #     for i in range(2, int(sqrt(n)) + 1):
    #         if n % i == 0:
    #             return False
    #     return True
    #
    #
    # if __name__ == "__main__":
    #     print(f"11: {is_prime(11)}")
    #     print(f"12: {is_prime(12)}")
    #
    #
    # # Zadanie 4
    #
    # def is_palindrom(napis):
    #     napis = napis.lower()
    #     return napis == napis[::-1]
    #
    #
    # if __name__ == "__main__":
    #     print(is_palindrom("Madam"))
    #     print(is_palindrom("kajak"))
    #     print(is_palindrom("Ala ma kota"))
    #
    #
    # # Zadanie 5
    #
    # def count_upper_lower_case(sentence):
    #     no_upper_case, no_lower_case = 0, 0
    #
    #     for char in sentence:
    #         if char.islower():
    #             no_lower_case += 1
    #         elif char.isupper():
    #             no_upper_case += 1
    #
    #     return no_upper_case, no_lower_case
    #
    #
    # if __name__ == "__main__":
    #     napis = "The quick Brown Fox"
    #     upper, lower = count_upper_lower_case(napis)
    #     print(f"Liczba wielkich liter: {upper}, liczba małych liter: {lower}")
    #
    #
    # # Zadanie 6
    #
    # def are_anagrams(napis1, napis2):  # można też np. wykorzystać Counter
    #     napis1 = sorted(napis1.lower().replace(" ", ""))
    #     napis2 = sorted(napis2.lower().replace(" ", ""))
    #     return napis1 == napis2
    #
    #
    # if __name__ == "__main__":
    #     print(are_anagrams("Tom Marvolo Riddle", "I am Lord Voldemort"))
    #     print(are_anagrams("Ala ma kota", "Kot ma Alę"))
    #
    #
    # # Zadanie 7
    #
    # def most_common():
    #     words_freq = {}
    #     with open("oda.txt") as file:
    #         for line in file:
    #             words = line.strip().lower().split()
    #             for word in words:
    #                 words_freq[word] = words_freq.get(word, 0) + 1
    #
    #     return sorted(words_freq.items(), key=lambda x: x[1], reverse=True)[:5]
    #
    #
    # if __name__ == "__main__":
    #     print(most_common())
    #
    #
    # # Zadanie 8
    #
    # class Prostokat:
    #     def __init__(self, a, b):
    #         self.a = a
    #         self.b = b
    #
    #     def obwod(self):
    #         return 2 * (self.a + self.b)
    #
    #     def pole(self):
    #         return self.a * self.b
    #
    #
    # class Kwadrat(Prostokat):
    #     def __init__(self, a):
    #         super().__init__(a, a)
    #
    #
    # if __name__ == "__main__":
    #     prostokat = Prostokat(3, 5)
    #     kwadrat = Kwadrat(5)
    #     print(prostokat.obwod())
    #     print(kwadrat.obwod())
    #
    #
    # # Zadanie 9
    #
    # def debug(func):
    #     def wrapper(*args, **kwargs):
    #         argumenty_pozycyjne = ", ".join([str(arg) for arg in args])
    #         argumenty_nazwane = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
    #         result = func(*args, **kwargs)
    #         print(f"Funkcja {func.__name__}({argumenty_pozycyjne}, {argumenty_nazwane}) zwróciła {result}")
    #         return result
    #
    #     return wrapper
    #
    #
    # @debug
    # def func(a, b, c):
    #     return a + b * c
    #
    #
    # if __name__ == "__main__":
    #     print(func(3, b=2, c=4))
    #
    # # Zadanie 10
    #
    # if __name__ == "__main__":
    #     while True:
    #         try:
    #             liczba = float(input("Podaj liczbę\n"))
    #             print(f"Wartość bezwzględna z {liczba} to {abs(liczba)}")
    #             break
    #         except ValueError:
    #             print("Nie można zwrócić wartości bezwzględnej dla podanego wejścia")








