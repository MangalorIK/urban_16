from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel

# uvicorn module_16_4:app --reload

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_all_users() -> users:
    return users


@app.post("/user/{username}/{age}")
async def create_user(user_data: User) -> str:
    user_data.id = len(users) + 1
    users.append(user_data)
    return f"User {user_data.username} is registered"


def get_user_index(user_id):
    index = 0
    for user in users:
        if user.id == user_id:
            return index
        else:
            index += 1

    return None


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_data: User) -> str:
    try:
        user_index = get_user_index(user_data.id)
        if user_index is not None:
            users[user_index] = user_data
            return f"The user {user_data.username} is updated"
        else:
            raise HTTPException(status_code=404, detail="User was not found")
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1, le=1000, description="user id")]) -> str:
    try:
        user_index = get_user_index(user_id)
        if user_index is not None:
            users.pop(user_index)
            return "User was deleted!"
        else:
            raise HTTPException(status_code=404, detail="User was not found")
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
