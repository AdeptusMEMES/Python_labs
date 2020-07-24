import  math
from functools import reduce

class Errors(Exception):
    def __init__(self, text="ERROR! WRONG VECTOR!"):
        self.txt = text

class Vector:
    def __init__(self, *coordinates):
        coordinates_lst=[]
        for i in range(len(coordinates)):
            coordinates_lst.append(float(coordinates[i]))
        self.coordinates = tuple(coordinates_lst)

    def __str__(self):
        return "vector({})".format(", ".join(str(coordinate) for coordinate in self.coordinates))

    def __eq__(self, other):
        if len(self.coordinates) == len(other.coordinates):
            if(self.coordinates==other.coordinates):
                return True
            else:
                return False
        else:
            raise Errors("ERROR! DIFFERENT DIMENSIONAL VECTORS!")

    def __getitem__(self, index):
        if index < len(self.coordinates) and index>=0:
            return self.coordinates[index]
        else:
            raise Errors("ERROR! INDEX OUT OF VECTOR DIMENSION!")

    def __abs__(self):
        return math.sqrt(reduce((lambda x, y: x + y ** 2 ), (0,) + self.coordinates))

    def __add__(self, other):
        if len(self.coordinates)==len(other.coordinates):
            res_lst=[]
            for i in range(len(self.coordinates)):
                res_lst.append(self.coordinates[i] + other.coordinates[i])
            res=Vector()
            res.coordinates=tuple(res_lst)
            return res
        else:
            raise Errors("ERROR! DIFFERENT DIMENSIONAL VECTORS!")

    def __sub__(self, other):
        if len(self.coordinates) == len(other.coordinates):
            res_lst = []
            for i in range(len(self.coordinates)):
                res_lst.append(self.coordinates[i] - other.coordinates[i])
            res = Vector()
            res.coordinates = tuple(res_lst)
            return res
        else:
            raise Errors("ERROR! DIFFERENT DIMENSIONAL VECTORS!")

    def __mul__(self, other):
        if len(self.coordinates) == len(other.coordinates):
            return reduce((lambda x, y: x + y), (res_elem[0]*res_elem[1] for res_elem in zip(self.coordinates,other.coordinates)))
        else:
            raise Errors("ERROR! DIFFERENT DIMENSIONAL VECTORS!")

    def __imul__(self, const):
        coordinates_lst=list(self.coordinates)
        for i in range(len(self.coordinates)):
            coordinates_lst[i] *= const
        self.coordinates=tuple(coordinates_lst)
        return self

    def __itruediv__(self, const):
        if const!=0.0:
            const = 1/const
            return self.__imul__(const)
        else:
            raise Errors("ERROR! DIVIDING BY ZERO!")