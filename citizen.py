"""
    Napisz klasę Citizen, która implementuje metodę __init__, przyjmującą dwa argumenty: first name i last name.
    Stwórz obiekt tej klasy, a następnie wyświetl imię i nazwisko obywatela.

    Dodaj metodę klasową set_nationality do klasy Citizen (a wraz z nią pole klasowe nationality
    o wybranej wartości domyślnej).
    Wywołaj tę metodę. Stwórz drugi obiekt klasy i zobacz, jaką wartość będzie miało pole nationality w obu obiektach.

    Dodatkowo możesz spróbować dodać atrybut klasowy total_number_of_citizens będący liczbą.
    Zwiększaj ją za każdym razem, kiedy tworzony będzie nowy obywatel.
"""

class Citizen:
    total_number_of_citizens = 0
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Citizen.total_number_of_citizens +=1

    def set_nationality(self, nationality = 'Polska'):
        self.nationality = nationality

if __name__ == '__main__':
    czlowiek = Citizen('Adam', 'Adam')
    czlowiek2 = Citizen('Mom', 'mommy')
    print(czlowiek.last_name, czlowiek.first_name)
    czlowiek.set_nationality('Niemcy')
    print(czlowiek.nationality)
    print(Citizen.total_number_of_citizens)