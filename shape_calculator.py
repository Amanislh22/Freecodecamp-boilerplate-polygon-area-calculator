class Rectangle:
    #width and height attributes.
    def __init__(self, width=0, heigth=0):
        self.width = width
        self.height = heigth
    def __str__(self):
      return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**.5)

    def get_picture(self):
        if (self.height > 50 or self.width > 50):
            return "Too big for picture."
        else:
            for i in range(self.height):
                for j in range(self.width):
                    print("*", end="")
                print("\n")

    def get_amount_inside(self, s):
        return int(self.get_area() / s.get_area())


#class square
class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side
    def __str__(self):
      return f'Square(side={self.width})'

    def set_side(self, side):
        self.height = side
        self.width = side
