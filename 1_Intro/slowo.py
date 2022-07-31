"""
    Napisz program, który pobiera od użytkownika słowo, a następnie wyświetla słowo złożone z co drugiego znaku pobranego.
    W drugiej kolejności program powinien wyświetlić słowo z pozostałych liter.
"""

input = input(f'Wpisz słowo: ')

firstWord = ''
secondWord = ''

for letter in range(0, len(input), 2):
    firstWord += input[letter:letter + 2][1]
    secondWord += input[letter:letter + 2][0]

if __name__ == '__main__':
    print(f'Słowo z co odrugiej litery to {firstWord}')
    print(f'Słowo z pozostałych liter to {secondWord}')
