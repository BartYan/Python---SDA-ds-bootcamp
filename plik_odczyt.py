"""
    Napisz program, który wczytuje plik tekstowy, a następnie wypisuje go z ponumerowanymi liniami.
"""

with open(r'/path..', 'r') as file:
    i = 0
    for line in file:
        i +=1
        print(f'{i}. {line}')

