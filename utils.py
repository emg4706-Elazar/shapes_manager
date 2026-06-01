

def get_valid_input(options):
    is_valid = False
    while not is_valid:
        user_input = input("Type here: ")
        if is_valid_input(user_input, options):
            is_valid = True
            return user_input
        else:
            print("\nInvalid input")
    return


def in_options(user_input ,options):
    lst = []
    for k in options:
        lst.append(k)
    return user_input in lst

def is_valid_input(user_input, options):
    return user_input.isdigit() and in_options(user_input, options)


# def get_valid_attribute():
#     is_valid = False
#     while not is_valid:
#         user_input = input("Type here: ")
#         try:
#             valid_attribute(user_input)
#         except:
#             print("\nInvalid input")
#     return int(user_input)
#
#
def valid_attribute(shape):
    is_valid = False
    attributes = shape["attributes"]
    for a in attributes.values():
        if a >= 0:
            is_valid = True
            return is_valid
    return is_valid



# def get_valid_attribute():
#     is_valid = False
#     while not is_valid:
#
#         try:
#             is_valid = valid_attribute(user_input)
#         except:
#             print("\nInvalid Input")
