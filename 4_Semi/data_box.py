"""
    Napisz klase DataBox, ktorej zadaniem bedzie gromadzenie danych oraz wyliczanie ich najprostszych statystycznych
    parametrow, takich jak srednia arytmetyczna, srednia geometryczna, moda (wartosc najczesciej sie powtarzajaca).
    Klasa powinna miec dwa atrybuty: self.data oraz self.amount_of_data: pierwszy to lista do ktorej beda wrzucane dane
    typu int/float, drugi to pole informujace o tym, ile danych aktualnie przechowuje obiekt klasy.
    Metody jakie nalezy zaimplementowac:
    - count_arithmetic_average: metoda do liczenia sredniej arytmetycznej listy danych,
    - count_geometric_average: metoda do liczenia sredniej geometrycznej danych, ktore przechowuje obiekt klasy,
    - get_amount_of_data: metoda zwracajaca liczbe danych, jaka aktualnie przechowuje obiekt klasy DataBox,
    - get_modal: metoda liczaca mode, czyli ustalajaca wartosc najczesciej powtarzajacej sie danej.
    - add_data: metoda dodajaca jakas dana do obiektu. Jej argumentem moze byc zarowno liczba jak i lista liczb.
    W pierwszym przypadku zostanie do atrybutu self.data dodana liczba, w drugim wszystkie liczby z listy liczb.
    - remove_data: metoda, ktora usuwa WSZYSTKIE dane z listy (z pola self.data).
    - get_data: metoda zwracajaca liste danych, ktore przechowuje aktualnie obiekt.
    Przykladowe wywolanie i stworzenie obiektu:
    >> box = DataBox()
    >> box.add_data([1,2,3,4,5])
    >> print(box.get_data())
    [1,2,3,4,5]
    >> print(box.count_arithmetic_average())
    3
    >> box.get_modal()
    1  # w przypadku kiedy nie mozna ustalic najczesciej pojawiajacej sie wartosci, zwracamy pierwszy element z atrybutu
       # self.data
    >> print(box.get_amount_of_data())
    5  # ilosc elementow w liscie self.data
    >> box.remove_data()
    >> print(box.get_data())
    []  # po usunieciu danych, w atrybucie self.data nie ma zadnej wartosci, jest to pusta lista
    W przypadku kiedy uzytkownik zechce do obiektu dodac dana innego typu niz int czy float (w metodzie add_data),
    nalezy podniesc wyjatek BadDataTypeError - wczesniej trzeba taka klase wyjatku stworzyc.
"""

from functools import reduce
from statistics import mode
class WrongDataType(Exception):
    pass
class DataBox:
    def __init__(self):
        self.data = []
        self.amount_of_data = len(self.data)
    def add_data(self, a):
        if type(a) not in (int, float, list):
            raise WrongDataType ('Wrong data type.')
        if type(a) in (int, float):
            self.data.append(a)
            self.amount_of_data = len(self.data)
        else:
            self.data.extend(a)
            self.amount_of_data = len(self.data)
    def count_arithmetic_average(self):
        try:
            return sum(self.data)/self.amount_of_data
        except ZeroDivisionError:
            print("Brak danych")
    def count_geometric_average(self):
        try:
            return reduce(lambda a, b: a * b, self.data) ** (1/self.amount_of_data)
        except ZeroDivisionError:
            print("Brak danych")
    def get_amount_of_data(self):
        return len(self.data)
    def get_data(self):
        return self.data
    def get_modal(self):
        return mode(self.data)
    def remove_data(self):
        self.data = []
if __name__ == '__main__':
    box = DataBox()
    print(box.amount_of_data)
    lista = [1,2,3,5]
    box.add_data(lista)
    print(len(box.data))
    box.get_amount_of_data()
    print(box.count_arithmetic_average())
    print(box.count_geometric_average())