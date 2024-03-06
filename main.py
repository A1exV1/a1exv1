class Cat:
    def meow(self):
        return 'мяу'


class Dog:
    def meow(self):
        return 'гав'


class CatDog(Dog, Cat):
    pass


catdog = CatDog()

print(CatDog.mro())
print(catdog.meow())
