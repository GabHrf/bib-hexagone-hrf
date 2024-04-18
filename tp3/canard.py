from abc import ABC, abstractmethod

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class Fly2Wings(FlyBehavior):
    def fly(self):
        print('2 wings flying')

class FlyNone(FlyBehavior):
    def fly(self):
        print('Never flies')

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class QuackNone(QuackBehavior):
    def quack(self):
        print('quack none')

class QuackLoud(QuackBehavior):
    def quack(self):
        print('quack loud')


class Duck(ABC):

    # dunder __ double underscore

    def __init__(self, name, flybehavior: FlyBehavior, quackbehavior: QuackBehavior):
        self.__name = name
        self.__flybehavior = flybehavior
        self.__quackbehavior = quackbehavior
    
    @property
    def name(self):
        return self.__name

    def fly(self):
        self.__flybehavior.fly()

    @property
    def flybehavior(self):
        return self.__flybehavior

    @flybehavior.setter
    def flybehavior(self, value):
        if (isinstance(value, FlyBehavior)):
            self.__flybehavior = value
        else:
            print('Unable to set new value')

    def quack(self):
        self.__quackbehavior.quack()

class RedKneck(Duck):

    def __init__(self, name):
        if name[0] == 'j':
            super().__init__(name, FlyNone(), QuackNone())
        else:
            raise ValueError('Should start with j')


class GreenKneck(Duck):

    def __init__(self, name):
        super().__init__(name, Fly2Wings(), QuackLoud())
    

if __name__ == '__main__':
    greenDuck = GreenKneck('green duck')
    greenDuck.fly()
    greenDuck.quack()
    redDuck = RedKneck('jaffiduck')
    redDuck.fly()
    redDuck.quack()
    # TODO: break wings...so does not fly anymore
    greenDuck.flybehavior = FlyNone()
    greenDuck.fly()
    greenDuck.flybehavior = QuackNone()
    greenDuck.fly()