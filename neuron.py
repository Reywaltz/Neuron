import numpy as np
class Neuron:
    """
    Класс нейрона или перцептрона основанного на методах активации через пограничное значение и смещения
    """
    def __init__(self, weigth, bias):
        """
        Метод инициализации объекта класса

        :param weight: list(list()) 
        :param bias: Значение смещения
        :type bias: inf, float
        """
        self.weigth = np.array(weigth)
        self.bias = bias

    def compute_with_bias(self, x):
        """
        Метод вычисления результата через смещение, а так же активация функции.

        Для получения результата происходит перемножение матрицы весов каждого из входящих значений
        на матрицу входных данных. К получившейся матрице добавляется значение смещения.
        """
        return 1 if np.dot(self.weigth, x) + self.bias > 0 else 0

    def calc_with_threshold(self, x):
        """
        Метод вычисления результата через пограничное значение, а так же активация функции.

        Для получения результата происходит перемножение матрицы весов каждого из входящих значений
        на матрицу входных данных. Получившаяся матрица сравнивается со пограничным значением равным
        значению смещения взятым с противопложным знаком
        """
        return 1 if np.dot(self.weigth, x) > -self.bias else 0