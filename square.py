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

    def __init__(self, side):
        self._id = 0
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
            "id": self._id,
            "shape_type": self._shape_type,
            "side": self._side
        }
        return dicti


