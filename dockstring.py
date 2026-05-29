import json


"""
Structure files:

    shape_crud/
    │
    ├── main.py
    ├── shape.py
    ├── rectangle.py
    ├── square.py
    ├── circle.py
    ├── shape_manager.py
    └── shapes.json


User actions:
    1. Add shape
    2. Show all shapes
    3. Update shape
    4. Delete shape
    5. Exit


Classes:
    1. Shape
    2. Rectangle
    3. Square
    4. Circle
    5. Shape_manager

======================================
main.py
======================================
"""
def handle_create_shape(manager, logger):
    """
    1. print available shapes.
    2. get valid input from user
    3. get input for attributes shape,   | To do validation for attributes
        call to match function that,
        creates a dict with all attributes
    4. create this  shape
    args:
        1. shape manager
        2. logger
    :return
        None
    """


def handle_display_shapes(manager, logger):
    """
    1. get all shapes from shape_manager
    2. print all shapes with loop,
    args:
        1. shape_manager
        2. logger
    :return:
        None
    """


def handle_update_shape(manager, logger):
    """
    1. get valid input
        a. id_shape
        b. new_data
    2. get all shapes
    3. change the shape by id_shape(try/except),
        It's a function with condition to check,
        if this shapes exist.
    4. print match message
    args:
        1. shape_manager
        2. logger
    :return: None
    """


def handle_delete_shape(manager, logger):
    """
    1. get valid input, id_shape
    2. get all shapes from shape manager
    3. delete the shape by id_shape(try/except),
        It's a function with condition to check,
        if this shapes exist.
    4. print match message
    args:
        1. shape_manager
        2. logger
    return: None
    """


def main():
    """
    initialize:
        create shape manager
        create logger
    loop:
        print actions
        get valid input
        call to match action
        if loop is over:
            exit
    args:
        None
    return:
        None
    """

"""
================================================
shape.py
================================================

Base class
    produce the id for each shape
    has a method get area,
    get_perimeter,
    to_dict that convert the data to dict,
    for dumping into json file.
    
    
class Shape:
    Class_attributes:
        1. id_producer = 0
        
    

    
===================================================
rectangle.py
===================================================

class Rectangle
    constructor:
        receives length and width 

"""

# dict for tests
d = [
    {"id": 0, "type": "Rectangle", "length": 4, "width": 7},
    {"id": 1, "type": "Square", "side": 4}
]





