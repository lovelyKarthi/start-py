"""Inheritance and duck-typing / protocols example"""
class Animal:
    def speak(self): raise NotImplementedError

class Dog(Animal):
    def speak(self): return 'woof'

class Cat(Animal):
    def speak(self): return 'meow'

def let_speak(a):
    print(a.speak())

if __name__ == '__main__':
    let_speak(Dog()); let_speak(Cat())
