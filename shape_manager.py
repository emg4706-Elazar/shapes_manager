from rectangle import Rectangle
from circle import Circle
from square import Square
import json
from json.decoder import JSONDecodeError
from logging_config import logger


class ShapeManager:
    def __init__(self):
        """
        Attributes:
            1. self.shapes contains list of objects
            2. self.load_from_json(), an Attribute method load into self.shapes.
        """
        self.shapes = []
        self.load_from_json()


    def create_shape(self, shape):
        """
        receives dict with valid values
        call to its constructor
        adds the new object into self.shapes
        save all objects into the JSON file
        Args:
            shape:

        Returns:
                None
        """
        new_object = eval(shape["type"])(**shape["attributes"])
        self.shapes.append(new_object)
        self.save_to_json()
        return


    def get_all_shapes(self):
        """
        go over the 'self.shapes'
        convert all objects to dict
        and return them as list of dicts
        Returns:
            list_of_dicts: (list[dicts])
        """
        list_of_dicts = []
        for shape in self.shapes:
            conv_to_dict = shape.to_dict()
            list_of_dicts.append(conv_to_dict)
        return list_of_dicts


    def update_shape(self, shape_id, new_data):
        """
        delete old shape by id,
        and create the updated object
        Args:
            shape_id:
            new_data:
        Returns:
        """
        all_shapes = self.get_all_shapes()
        updated_shape = new_data
        updated_shape["attributes"]["_id"] = shape_id
        self.create_shape(updated_shape)
        updated = False
        for shape in all_shapes:
            if shape["attributes"]["_id"] == shape_id:
                i = all_shapes.index(shape)
                del self.shapes[i]

                updated = True
                return updated
        return updated


    def delete_shape(self, shape_id):
        """
        delete shape by id
        Args:
            shape_id: (int)

        Returns: (bool)

        """
        all_shapes = self.get_all_shapes()
        deleted = False
        for shape in all_shapes:
            if shape["attributes"]["_id"] == shape_id:
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
        except JSONDecodeError:
            self.shapes = []
        return


    def get_all_id_s(self):
        all_shapes = self.get_all_shapes()
        all_id_s = [shape["attributes"]["_id"] for shape in all_shapes]
        return all_id_s


    def get_new_id(self):
        new_id = 0
        if self.get_all_id_s():
            maxi = max(self.get_all_id_s())
            new_id = maxi + 1
        return new_id










if __name__ == "__main__":
    sp = ShapeManager()

    dicti = {"type": "Rectangle",
             "attributes": {"_id": 1, "length": 4, "width": 6}}
    sp.create_shape(dicti)
    print(sp.get_all_shapes())
    sp.update_shape(1,dicti)
    sp.save_to_json()
    sp.load_from_json()
    print(sp.get_all_shapes())
    print(sp.get_new_id())
    sp.delete_shape(1)