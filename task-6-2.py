# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    _length: int
    _width: int

    def __init__(self, length: int,width: int):
        self._length = length
        self._width = width

    def square(self):
        square_result = self._length*self._width*25*5/1000
        print(f"{self._length}м * {self._width}м * 25кг * 5см = {square_result}т")

road1 = Road(20,5000)
road1.square()