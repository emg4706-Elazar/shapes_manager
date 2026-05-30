from shape import Shape




class Square(Shape):
    """
        constructor:
            receives one side,
            Attributes:
                1. _side
                super:
                3. _shape_id
                4. _shape_type
            Methods:
                1. get_area(self)
                2. get_perimeter(self)
                3. to_dict(self)
        """

    def __init__(self, side, _id):
        self._id = _id
        self._side = side
        self._shape_type = "Square"


    def get_area(self):
        """
        Calculate the area of self object
        Args:
            1. self
        :return: result of area
        """
        area = self._side * self._side
        return area


    def get_perimeter(self):
        """
        Calculate the perimeter of self object
        Args:
            1. self
        :return: result of perimeter
        """
        perimeter = (4 * self._side)
        return perimeter


    def to_dict(self):
        """
        Create dict with all object's data,
        in order to save it in a JSON file
        :return: the data dict
        """
        dicti = {
            "type": self._shape_type,
            "attributes": {
                "_id": self._id,
                "side": self._side
            }
        }
        return dicti


if __name__ == "__main__":
    s = Square(5)
    s1 = s.to_dict()
    s2 = s.get_area()
    s3 = s.get_perimeter()
    print(s1, "\n", s2, "\n", s3)
