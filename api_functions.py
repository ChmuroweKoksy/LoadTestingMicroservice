from fastapi.responses import JSONResponse
from pydantic import BaseModel


# success response model
def ResponseModel(data):
    return JSONResponse(
        status_code=200, 
        content=data
    )    


# errors response model
def ErrorResponseModel(code, message):
    return JSONResponse(
        status_code=code, 
        content={"code": code, "message": message}
    )


class Info(BaseModel):
    id: str
    secret: str
    method: str
    url: str
    quantity: int
    body: dict