
class A:

    def __init__(self, a, b):
        self.name_a = a
        self.name_b = b

        print('init')

    def plus(self):
        return self.name_a + self.name_b

    def minus(self):
        return self.name_a - self.name_b

    def umnog(self):
        return self.name_a * self.name_b

    def delenie(self):
        return self.name_a / self.name_b


class_a = A(a=10, b=2)

print(class_a.plus())
print('------------')
print(class_a.minus())
print('------------')
print(class_a.umnog())
print('------------')
print(int(class_a.delenie()))
