from fastapi import FastAPI, Path
from typing import Annotated
users = {"1": "Имя: Example, возраст: 18"}
app = FastAPI()
@app.get("/users")
async def get() -> dict:
    return  users

@app.post("/user/{username}/{age}")
async def register_user(username: Annotated[str, Path(min_length=5, max_length=20, description ="Enter username",
                                   example = "UrbanUser")], age: Annotated[int, Path(ge=18, le=120, description ="Enter age",
                                   example = "19")]) -> str:
    current_index = str(int(max(users, key=int))+ 1)
    users[current_index] = f"{username}: {age}"
    return f"User {current_index} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path( ge=1, le=100, description ="Enter User ID", example="1")],
                      username: Annotated[str, Path(min_length=5, max_length=20, description ="Enter username",
                                   example = "UrbanUser")], age: Annotated[int, Path(ge=18, le=120, description ="Enter age",
                                   example = "19")]) -> str:
    users[user_id] = "Имя: {username}, возраст: {age}"
    return f"The user {user_id} is registered"

@app.delete("/user/{user_id}")
async def delete(user_id: Annotated[str, Path( min_length=1, max_length=5, description ='Enter User ID', example="1")]) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"


