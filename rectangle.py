from shape import Shape



class Rectangle(Shape):
    """
    constructor:
        receives length and width,
        Attributes:
            1. _length
            2. _width
            super:
            3. _shape_id
            4. _shape_type
        Methods:
            1. get_area(self)
            2. get_perimeter(self)
            3. to_dict(self)
    """

    def __init__(self, length, width):
        self._id = 0  # To-Do to complete the signature with 'id'
        self._length = length
        self._width = width
        self._shape_type = "Rectangle"


    def get_area(self):
        """
        Calculate the area of self object
        Args:
            1. self
        :return: result of area
        """
        area = self._length * self._width
        return area


    def get_perimeter(self):
        """
        Calculate the perimeter of self object
        Args:
            1. self
        :return: result of perimeter
        """
        perimeter = (2 * self._length) + (2 * self._width)
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
            "length": self._length,
            "width": self._width
        }
        return dicti

rec = Rectangle(3,4)