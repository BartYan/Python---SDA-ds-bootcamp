"""
    Stwórz pusty plik tekstowy.
    Napisz program, który pobiera od użytkownika listę słów i zapisuje je w pliku.
"""

with open(r'/path..', 'w') as file:
    input = input('Podaj słowo: ')
    file.write(input)
