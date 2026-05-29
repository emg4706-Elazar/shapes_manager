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

    def __init__(self, radius, quoter):
        self._id = 0    # To-Do to complete the signature with 'id'
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
            "id": self._id,
            "type": self._shape_type,
            "quoter": self._quoter,
            "radius": self._radius
        }
        return dicti


if __name__ == "__main__":
    c = Circle(4,8)
    c1 = c.to_dict()
    c2 = c.get_area()
    c3 = c.get_perimeter()
    print(c1,"\n",c2,"\n",c3)
