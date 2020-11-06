from math import sqrt


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_width(self, width: int):
        self.width = width

    def set_height(self, height: int):
        self.height = height

    def get_area(self) -> int:
        return self.height * self.width

    def get_perimeter(self) -> int:
        return 2 * self.height + 2 * self.width

    def get_diagonal(self) -> int:
        return sqrt(self.width ** 2 + self.height ** 2)

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape: 'Rectangle') -> int:
        if shape.height > self.height or shape.width > self.width:
            return 0

        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit

    def __str__(self):
        return 'Rectangle(width={0}, height={1})'.format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, length: int):
        super().__init__(length, length)

    def set_width(self, width: int):
        self.set_side(width)

    def set_height(self, height: int):
        self.set_side(height)

    def set_side(self, side: int):
        self.width = side
        self.height = side

    def __str__(self):
        return 'Square(side={0})'.format(self.width)
