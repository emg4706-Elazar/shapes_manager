from shape import Shape
from math import pi



class Circle(Shape):
    """
        constructor:
            receives radius and quoter,
            Object Attributes:
                1. radius
                2. quoter
                super:
                3. _shape_id
                4. _shape_type
            Methods:
                1. get_area(self)
                2. get_perimeter(self)
                3. to_dict(self)
        """

    def __init__(self, radius, quoter, _id):
        self._id = _id
        self._radius = radius
        self._quoter = quoter
        self._shape_type = "Circle"

    def get_area(self):
        """
        Calculate the area of self object
        Args:
            1. self
        :return: result of area
        """
        area = round(pi * (self._radius ** 2), 2)
        return area


    def get_perimeter(self):
        """
        Calculate the perimeter of self object
        Args:
            1. self
        :return: result of perimeter
        """
        perimeter = round(self._quoter * pi, 2)
        return perimeter


    def to_dict(self):
        """
        Create dict with all object's attributes,
        in order to save it in a JSON file
        :return: the data dict
        """
        dicti = {
            "type": self._shape_type,
            "attributes": {
                "_id": self._id,
                "quoter": self._quoter,
                "radius": self._radius
            }
        }
        return dicti


if __name__ == "__main__":
    class_name = "Circle"
    c4 = eval(class_name)(4,5)
    # c = Circle(4,8)
    c1 = c4.to_dict()
    c2 = c4.get_area()
    c3 = c4.get_perimeter()
    print(c1,"\n",c2,"\n",c3)
