from fastapi import FastAPI
import uvicorn
from shape_manager import ShapeManager



app = FastAPI()

manager = ShapeManager()

# Get all shapes
@app.get("/shapes")
def get_shapes():
    return manager.get_all_shapes()


# Create new shape
@app.post("/shapes")
def post_shape(shape: dict):
    new_id = get_new_id()
    shape["attributes"]["_id"] = new_id
    manager.create_shape(shape)
    manager.save_to_json()
    return f"new shape was created"


# Update shape by id
@app.put("/shapes")
def put_shape(new_data: dict,shape_id: int):
    all_shapes = manager.get_all_shapes()
    for s in all_shapes:
        if s["attributes"]["_id"] == shape_id:
            manager.update_shape(shape_id, new_data)
            manager.save_to_json()
            return f"Shape updated"
    return f"{shape_id} not exist"

# Delete shape
@app.delete("/shapes")
def delete(shape_id: int):
    try:
        manager.delete_shape(shape_id)
        manager.save_to_json()
        return "\nShape was deleted successfully"
    except KeyError:
        return f"{shape_id} not exist"


# Get shape by id
@app.get("/shapes/{shape_id}")
def get_shape_by_id(shape_id):
    all_shapes = manager.get_all_shapes()
    for s in all_shapes:
        if s["attributes"]["_id"] == int(shape_id):
            return s
    return f"{shape_id} not exist"





def get_new_id():
    new_id = 0
    if manager.get_all_id_s():
        maxi = max(manager.get_all_id_s())
        new_id = maxi + 1
    return new_id




if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000)




# query parameter

# @app.get("/shapes")
# def get_shapes(shape_id=None):
#     if shape_id:
#         all_shapes = manager.get_all_shapes()
#         for s in all_shapes:
#             if s["attributes"]["_id"] == int(shape_id):
#                 return s
#     return manager.get_all_shapes()
