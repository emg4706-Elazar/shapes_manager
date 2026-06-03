from fastapi import FastAPI, HTTPException
import uvicorn
from shape_manager import ShapeManager
from pydantic import BaseModel, validator
from typing import Annotated, Dict



app = FastAPI()

manager = ShapeManager()

class CircleAttributes(BaseModel):
    quoter: float
    radius: float

class SquareAttributes(BaseModel):
    side: float

class RectangleAttributes(BaseModel):
    length: float
    width: float

class Item(BaseModel):
    type: str
    attributes: RectangleAttributes | SquareAttributes | CircleAttributes



# Get all shapes
@app.get("/shapes")
def get_shapes():
    return manager.get_all_shapes()



@app.post("/shapes")
def post_shape(shape: Item):
    new_id = get_new_id()
    new_shape = shape.model_dump()
    try:
        new_shape["attributes"]["_id"] = new_id
        manager.create_shape(new_shape)
        manager.save_to_json()

    # in case the type is not exist
    except NameError as e:
        raise HTTPException(status_code=422, detail=f"There no '{new_shape["type"]}' type")
    # in case attributes doesn't match for type
    except TypeError as e:
        raise HTTPException(status_code=422,
                            detail=f"Attributes doesn't match for '{new_shape["type"]}'")

    return f"new shape was created"



# Update shape by id
@app.put("/shapes")
def put_shape(new_data: Item, shape_id: int):
    all_shapes = manager.get_all_shapes()
    new_data = new_data.model_dump()
    if shape_id not in manager.get_all_id_s():
        raise HTTPException(status_code=404, detail=f"{shape_id} not exist")

    for s in all_shapes:
        if s["attributes"]["_id"] == shape_id:
            try:
                manager.update_shape(shape_id, new_data)
                manager.save_to_json()
                return f"Shape updated"

            # in case the type is not exist
            except NameError:
                raise HTTPException(status_code=422, detail=f"There no '{new_data["type"]}' type")

            # in case attributes doesn't match for type
            except TypeError:
                raise HTTPException(status_code=422,
                                detail=f"Attributes doesn't match for '{new_data["type"]}'")
    return None


# Delete shape
@app.delete("/shapes")
def delete(shape_id: int):
    try:
        manager.delete_shape(shape_id)
        manager.save_to_json()
        return "\nShape was deleted successfully"
    except KeyError:
        raise HTTPException(status_code=404, detail=f"{shape_id} not exist")



# Get shape by id
@app.get("/shapes/{shape_id}")
def get_shape_by_id(shape_id: int):
    all_shapes = manager.get_all_shapes()
    for s in all_shapes:
        if s["attributes"]["_id"] == int(shape_id):
            return s

    raise HTTPException(status_code=404, detail=f"ID '{shape_id}' not exist")






def get_new_id():
    new_id = 0
    if manager.get_all_id_s():
        maxi = max(manager.get_all_id_s())
        new_id = maxi + 1
    return new_id




if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000)


# @app.post("/shapes")
# def post_shape(shape : Item):
#     new_id = get_new_id()
#     shape["attributes"]["_id"] = new_id
#     manager.create_shape(shape)
#     manager.save_to_json()
#     return f"new shape was created"



# query parameter

# @app.get("/shapes")
# def get_shapes(shape_id=None):
#     if shape_id:
#         all_shapes = manager.get_all_shapes()
#         for s in all_shapes:
#             if s["attributes"]["_id"] == int(shape_id):
#                 return s
#     return manager.get_all_shapes()
