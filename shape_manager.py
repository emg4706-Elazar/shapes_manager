
from rectangle import Rectangle
from circle import Circle
from square import Square
import json
from json.decoder import JSONDecodeError



class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):

        new_object = eval(shape["type"])(**shape["attributes"])
        self.shapes.append(new_object)
        return



    def get_all_shapes(self):
        list_of_dicts = []
        for shape in self.shapes:
            conv_to_dict = shape.to_dict()
            list_of_dicts.append(conv_to_dict)
        return list_of_dicts

    def update_shape(self, shape_id, new_data):
        pass

    def delete_shape(self, shape_id):
        all_shapes = self.get_all_shapes()
        deleted = False
        for shape in all_shapes:
            if shape["id"] == shape_id:
                i = all_shapes.index(shape)
                del self.shapes[i]
                deleted = True
                break
        if deleted:
            return deleted
        else:
            raise KeyError



    def save_to_json(self):
        shapes = self.get_all_shapes()
        with open("shapes.json", "w", encoding="utf-8") as f:
            json.dump(shapes, f, indent=2)
        return



    def load_from_json(self):
        try:
            with open("shapes.json", "r", encoding="utf-8") as f:
                shapes_as_dicts = json.load(f)
            # convert to objects
            for d in shapes_as_dicts:
                self.create_shape(d)
                # How to convert dict to object
        except JSONDecodeError:
            self.shapes = []
        return



if __name__ == "__main__":
    sp = ShapeManager()
    # all_shapes = sp.get_all_shapes()
    # print(all_shapes)
    # dicti = {"type": Rectangle,
    #          "attributes": {"length": 4, "width": 6}}
    for s in sp.shapes:
        print(type(s))
    else:
        print("empty")



