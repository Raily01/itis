from abc import abstractmethod, ABC
from math import pi


class GeometricShapes(ABC):
    def __init__(self, radius: float):
        '''
        Constructs Geometric Shapes class
        :param radius:  radius of our shape
        '''
        self.radius = radius
        pass

    @abstractmethod
    def square(self):
        '''
        Calculate a square of our shape
        :return: float
        '''
        pass

    @abstractmethod
    def perimeter(self):
        '''
        Calculate a perimeter of our shape
        :return:
        '''
        pass


class Round(GeometricShapes):
    def square(self):
        return pi * (Round.radius) ** 2

    def perimeter(self):
        return pi * 2 * Round.radius


class AbsQuadrilateral(GeometricShapes, ABC):
    def __init__(self, heigh: float, weigh_first: float):
        '''
        Constructs Quadrilateral class
        :param heigh: heigh of our Quadrilateral
        :param weigh_first: weigh of our Quadrilateral
        '''
        super().__init__(heigh,weigh_first)
        self.heigh = heigh
        self.weigh_first = weigh_first


class Rectangle(AbsQuadrilateral):
    def square(self):
        return self.heigh * self.weigh_first

    def perimeter(self):
        return (self.weigh_first + self.heigh) * 2


class Trapezoid(AbsQuadrilateral):
    def __init__(self, heigh: float, weigh_first: float, weigh_second: float):
        '''
        Constructs Trapezoid class
        :param heigh: heigh of our Trapezoid
        :param weigh_first: first weigh of our Trapezoid
        :param weigh_second: second weigh of our Trapezoid
        '''
        super().__init__(heigh, weigh_first, weigh_second)
        self.weigh_second = weigh_second

    def square(self):
        return (self.weigh_second + self.weigh_second) / 2 * self.heigh


class Parallelogram(AbsQuadrilateral):
    def square(self):
        return self.heigh * self.weigh_first

    def perimeter(self):
        return (self.weigh_first + self.heigh) * 2


'''
Геометрия.
    Создать класс абстрактный Геометрическая фигура
        Абстрактный метод площадь
        Абстрактный метод переметр
Класс круг
Класс абстрактный четырехугольник
    Прямоугольник
    Трапеция
    Параллелограмм'''
par = Parallelogram(2,3)
print(par)
