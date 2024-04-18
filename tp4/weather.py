from abc import ABC, abstractmethod

class TempDisplay(ABC):
    @abstractmethod
    def update(self):
        pass

class PressureDisplay(ABC):
    @abstractmethod
    def update(self):
        pass

class HumidityDisplay(ABC):
    @abstractmethod
    def update(self):
        pass


class WeatherData(ABC):

    def __init__(self, temperatureDisplay: TempDisplay, humidityDisplay: HumidityDisplay, pressureDisplay: PressureDisplay):
        self.__temperatureDisplay = temperatureDisplay
        self.__humidityDisplay = humidityDisplay
        self.__pressureDisplay = pressureDisplay
     
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