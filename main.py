from shape_manager import *
from logging_config import get_logger


def get_input():
    choice = input("Enter your choice: ")
    return choice


def get_valid_input_shape():
    is_valid = False
    while not is_valid:
        user_input = get_input()
        if user_input in ("1","2","3"):
            is_valid = True
        else:
            print("Invalid input")
    return user_input


def print_available_shapes():
    print(
        "\n ==== All Shapes ====\n",
        "1. Rectangle\n",
        "2. Square\n",
        "3. Circle\n"
    )
    return


def get_rectangle():
    shape = {
        "type": "Rectangle",
        "attributes": {
            "length": input("Enter length: "),
            "width": input("Enter width: ")
        }
    }
    return shape


def get_square():
    shape = {
        "type": "Square",
        "attributes": {
            "side": input("Enter side: ")
        }
    }
    return shape


def get_circle():
    shape = {
        "type": "Circle",
        "attributes": {
            "radius": input("Enter radius: "),
            "quoter": input("Enter quoter: ")
        }
    }
    return shape



def handle_create_shape(manager, logger):
    """
    To Do:
        1. Adding logs.
        2. Input validation
    :param manager:
    :param logger:
    :return:
    """


    # dict functions, receive attributes per shape by input
    get_attributes = {
        "1": get_rectangle,
        "2": get_square,
        "3": get_circle
    }
    print_available_shapes()

    # get available choice from user
    choice = get_valid_input_shape()

    # get match attributes per shape from user
    shape = get_attributes[choice]()

    try:
        manager.create_shape(shape)
        print("The shape was created successfully\n")
    except:
        print("Exception")

    return







#===============================================================

def print_shape(shape):
    print(shape)


def handle_display_shapes(manager, logger):
    """
    1. get all shapes from shape_manager,
        the shape should be as an object.
    2. print all shapes with loop,
    args:
        1. shape_manager
        2. logger
    :return:
        None
    """

    for shape in manager.get_all_shapes():
        print_shape(shape)
    return

#================================================================
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
    pass

#==================================================================
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
    pass

#===============================================================================
def print_actions():
    print(
        "====== Actions ======\n",
        "1. Create new shape\n",
        "2. Update exist shape\n",
        "3. Delete exist shape\n",
        "4. Display all shapes\n",
        "5. Exit\n"
    )
    return


def get_valid_input_action():
    is_valid = False
    while not is_valid:
        user_input = get_input()
        if user_input in ("1","2","3","4","5"):
            is_valid = True
        else:
            print("Invalid input")
    return user_input



def main():
    manager = ShapeManager()
    logger = get_logger()

    actions = {
        "1": handle_create_shape,
        "2": handle_update_shape,
        "3": handle_delete_shape,
        "4": handle_display_shapes
    }

    is_over = False
    while not is_over:
        print_actions()
        choice = get_valid_input_action()
        if choice == "5":
            is_over = True
            manager.save_to_json()
            print("\n the data saved")
            print("End")
        else:
            actions[choice](manager, logger)

    return


if __name__ == '__main__':
    main()














    # def get_shape_attributes():
    #     input_att = {
    #         "1": {
    #             "shape_type": "Square",
    #             "side": input("Enter side: ")
    #         },
    #         "2": {
    #             "shape_type": "Circle",
    #             "radius": input("Enter radius: "),
    #             "quoter": input("Enter quoter: ")
    #         },
    #         "3": {
    #             "shape_type": "Circle",
    #             "radius": input("Enter radius: "),
    #             "quoter": input("Enter quoter: ")
    #         }
    #     }




