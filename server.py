from fastapi import FastAPI, HTTPException
import uvicorn
from shape_manager import ShapeManager
from pydantic import BaseModel
from logging_config import logger

app = FastAPI()
logger.info("Init Server as 'app'")


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
    logger.info("get shapes done")
    return manager.get_all_shapes()



@app.post("/shapes")
def post_shape(shape: Item):
    logger.info("'post shape' started")
    new_id = manager.get_new_id()
    new_shape = shape.model_dump()
    try:
        new_shape["attributes"]["_id"] = new_id
        manager.create_shape(new_shape)
        manager.save_to_json()
        logger.info(f"Create new '{new_shape["type"]}'")
    # in case the type is not exist
    except NameError as e:
        logger.warning(f"Trying to create wrong 'type'")
        raise HTTPException(status_code=422, detail=f"There no '{new_shape["type"]}' type")
    # in case attributes doesn't match for type
    except TypeError as e:
        logger.warning(f"incorrect attributes for {new_shape["type"]}")
        raise HTTPException(status_code=422,
                            detail=f"Attributes doesn't match for '{new_shape["type"]}'")

    return f"new shape was created"



# Update shape by id
@app.put("/shapes")
def put_shape(new_data: Item, shape_id: int):
    logger.info("'put shape' started")
    all_shapes = manager.get_all_shapes()
    new_data = new_data.model_dump()
    if shape_id not in manager.get_all_id_s():
        logger.warning(f"put shape failed . wrong id")
        raise HTTPException(status_code=404, detail=f"{shape_id} not exist")

    for s in all_shapes:
        if s["attributes"]["_id"] == shape_id:
            try:
                manager.update_shape(shape_id, new_data)
                manager.save_to_json()
                logger.info("success to update shape")
                return f"Shape updated"

            # in case the type is not exist
            except NameError:
                logger.warning(f"Trying to update shape with wrong 'type'")
                raise HTTPException(status_code=422, detail=f"There no '{new_data["type"]}' type")

            # in case attributes doesn't match for type
            except TypeError:
                logger.warning(f"incorrect attributes for {new_data["type"]}")
                raise HTTPException(status_code=422,
                                detail=f"Attributes doesn't match for '{new_data["type"]}'")
    return None


# Delete shape
@app.delete("/shapes")
def delete(shape_id: int):
    logger.info("'delete shape' started")
    try:
        manager.delete_shape(shape_id)
        manager.save_to_json()
        logger.info("shape was deleted successfully")
        return "\nShape was deleted successfully"
    except KeyError:
        logger.warning("delete shape failed. wrong id")
        raise HTTPException(status_code=404, detail=f"{shape_id} not exist")



# Get shape by id
@app.get("/shapes/{shape_id}")
def get_shape_by_id(shape_id: int):
    logger.info("'get shape by id' started")
    all_shapes = manager.get_all_shapes()
    for s in all_shapes:
        if s["attributes"]["_id"] == int(shape_id):
            return s
    logger.warning("'get shape by id' failed. wrong id")
    raise HTTPException(status_code=404, detail=f"id '{shape_id}' not exist")




if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
