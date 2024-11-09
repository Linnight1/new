from fastapi import FastAPI, status, Body, HTTPException
from typing import Annotated
from pydantic import BaseModel
from typing import List
users = []
class User(BaseModel):
    id: int = None
    username: str
    age: int
app = FastAPI()
@app.get("/users")
async def get_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def register_user(username: str, age: int, user: User = Body())-> User:
    users.append(user)
    user.id = len(users)
    user.username = username
    user.age = age

    return user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age:int) -> User:
    try:
        edit_user = users[user_id-1]
        edit_user.username = username
        edit_user.age = age

        return edit_user
    except IndexError:
            raise HTTPException(status_code = 404, detail = "User was not found" )
@app.delete("/user/{user_id}")
async def delete(user_id: int,user: User = Body()) -> User:
    try:
        users.pop(user_id)
        return user
    except IndexError:
        raise HTTPException(status_code = 404, detail = "User was not found" )



