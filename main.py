from shape_manager import *
from logging_config import get_logger



# ======================================================

def handle_create_shape(manager, logger):
    """
    To Do:
        1. Adding logs.
        2. Input validation
        3. match messages
    Flow:
        1. create dict function for input
        2. print available shapes
        3. receive valid input choice
        4. get attribute  # valid attributes
        5. add new id into attributes dict
        6. call to manager function, create shape

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

    # add new id
    new_id = get_new_id(manager)
    shape["attributes"]["_id"] = new_id

    try:
        manager.create_shape(shape)
        print("The shape was created successfully\n")
    except:
        print("Exception")

    return


def get_input():
    choice = input("Enter your choice: ")
    return choice


def get_valid_input_shape():
    is_valid = False
    user_input = ""
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


def get_new_id(manager):
    new_id = 0
    if manager.get_all_id_s():
        maxi = max(manager.get_all_id_s())
        new_id = maxi + 1
    return new_id


#===============================================================

def handle_display_shapes(manager, logger):
    """
    To Do:
        1. adding logs
        2. design the print shapes
        3. print Match messages
    Flow:
        1. get all shapes from shape_manager.
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

def print_shape(shape):
    print(shape,"\n")


#================================================================
def handle_update_shape(manager, logger):
    """
    To Do:
        1. Adding logs
        2. valid input
        3. match messages
    Flow:
        1. get input for exist id
        2. get all exist shapes from shapes manager
        3. get the type of the exist shape by id
        4. call to input function by type for new data
        5. call to manager function, update with 2,
            arguments (shape_id, new_data)
    args:
        1. shape_manager
        2. logger
    :return: None
    """
    shape_id = int(input("Enter exist id: "))
    all_shapes = manager.get_all_shapes()
    class_name = ""
    for shape in all_shapes:
        if shape["attributes"]["_id"] == shape_id:
            class_name = shape["type"]
    # dict functions, receive attributes per shape by input
    get_attributes = {
        "Rectangle": get_rectangle,
        "Square": get_square,
        "Circle": get_circle
    }
    new_data = get_attributes[class_name]()
    try:
        updated = manager.update_shape(shape_id, new_data)
        if updated:
            print("The update completed")
    except Exception as e:
        print("This shape doesn't exist", e)
    return

#==================================================================
def handle_delete_shape(manager, logger):
    """
    To Do:
        1. Adding logs
        2. valid input
        3. match messages
    Flow:
        1. get input, id_shape
        2. call to manager function, delete with 1,
            arguments (shape_id)
        3. print match message
    args:
        1. shape_manager
        2. logger
    return: None
    """
    shape_id = int(input("\nEnter exist id: "))
    try:
        deleted = manager.delete_shape(shape_id)
        if deleted:
            print("The shape was deleted successfully\n")
    except KeyError:
        print("This ID doesn't exist\n")

    return

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
    user_input = ""
    while not is_valid:
        user_input = get_input()
        if user_input in ("1","2","3","4","5"):
            is_valid = True
        else:
            print("Invalid input")
    return user_input

def to_exit(manager, logger):
    manager.save_to_json()
    print("\nThe data saved\n")
    print("End")
    is_over = True
    return is_over


def main():
    """
    To do:
        1. Adding logs
        2. valid input
    Flow:
        1. init manager
        2. init logger
        3. create dict functions
        loop:
            4. print actions
            5. get input for action
            6. call to match handler with 2,
                arguments (manager, logger)
    Args:
    Returns:
    """
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
            is_over = to_exit(manager, logger)
        else:
            actions[choice](manager, logger)

    return


if __name__ == '__main__':
    main()

