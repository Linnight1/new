from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel
users = []
class User(BaseModel):
    id: int = None
    username: str
    age: int
app = FastAPI()
@app.get("/users")
async def get() -> list[User]:
    return users

@app.post("/user/{username}/{age}")
async def register_user(username: Annotated[str, Path(min_length=5, max_length=20, description ="Enter username",
                                   example = "UrbanUser")], age: Annotated[int, Path(ge=18, le=120, description ="Enter age",
                                   example = "19")]) -> User:

    users.id = len(users) + 1
    users.append(username)
    user.username = username
    user.age = age
    return User

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path( ge=1, le=100, description ="Enter User ID", example="1")],
                      username: Annotated[str, Path(min_length=5, max_length=20, description ="Enter username",
                                   example = "UrbanUser")], age: Annotated[int, Path(ge=18, le=120, description ="Enter age",
                                                                                     example = "19")]) -> User:
    for user in users:
        if user_id == user.id:
            user.username = username
            user.age = age
            return User
        else:
            raise HTTPException(status_code = 404, detail = "User was not found" )
@app.delete("/user/{user_id}")
async def delete(user_id: Annotated[int, Path( ge=1, le=100, description ='Enter User ID', example="1")]) -> User:
    for user in users:
        if user_id == user.id:
            users.pop(user)
            return user
        else:
            raise HTTPException(status_code = 404, detail = "User was not found" )


