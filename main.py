class Vector:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        return f'{tuple(self.args)}'

    def __eq__(self, other):
        if len(self.args) != len(other.args):
            raise ValueError('Векторы должны иметь равную длину')
        return self.args == other.args

    def __add__(self, other):
        if len(self.args) != len(other.args):
            raise ValueError('Векторы должны иметь равную длину')
        return Vector(*(sum(i) for i in zip(self.args, other.args)))

    def __sub__(self, other):
        if len(self.args) != len(other.args):
            raise ValueError('Векторы должны иметь равную длину')
        return Vector(*(i[0] - i[1] for i in zip(self.args, other.args)))

    def __mul__(self, other):
        if len(self.args) != len(other.args):
            raise ValueError('Векторы должны иметь равную длину')
        return sum(i[0] * i[1] for i in zip(self.args, other.args))

    def norm(self):
        return sum(i ** 2 for i in self.args) ** 0.5


vector1 = Vector(1, 2, 3)
vector2 = Vector(3, 4, 5)
vector3 = Vector(5, 6, 7, 8)

print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * vector2)
print(vector3.norm())