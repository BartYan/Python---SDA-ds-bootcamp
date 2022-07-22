"""
    Stwórz klasę Notebook, która będzie zawierała pola: producenta, cenę netto oraz pamięć RAM.
    Dopisz metody do obliczenia ceny brutto (+23% VAT) oraz zwiększenia ilości RAM-u.
"""

class Notebook:
    def __init__(self, producent, netto, ram):
        self.producent = producent
        self.netto = netto
        self.ram = ram

    def oblicz_brutto(self):
        return self.netto * 1.23

    def zwieksz_ram(self, ilosc):
        self.ram += ilosc
        return self.ram

if __name__ == '__main__':
    laptop = Notebook('apple', 2500, 9,)
    print(laptop.oblicz_brutto())
    print(laptop.zwieksz_ram(2))