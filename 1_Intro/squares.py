if __name__ == '__main__':

    class Rectangle:
        def __init__(self, height, width):
            self.height = height
            self.width = width

        def rec_cir(self):
            return int((self.height * 2) + (self.width * 2))

        def rec_area(self):
            return int(self.height * self.width)


    class Square(Rectangle):
        def __init__(self, bok):
            super().__init__(bok, bok)


    if __name__ == '__main__':
        my_rec = Rectangle(height=4, width=2)
        print(my_rec.rec_area())
        print(my_rec.rec_cir())

        my_square = Square(10)
        print(my_square.rec_area())
        print(my_square.rec_cir())
