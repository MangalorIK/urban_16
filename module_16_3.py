from fastapi import FastAPI, Path
from typing import Annotated
# uvicorn module_16_3:app --reload

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_all_messages() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_message(username: Annotated[str, Path(min_length=5, max_length=20, description="User Name")],
                         age: Annotated[int, Path(ge=18, le=120, description="Enter your age from 18 to 120")]) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {username} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: Annotated[int, Path(ge=1, le=1000, description="user id")],
                         username: Annotated[str, Path(min_length=5, max_length=20, description="User Name")],
                         age: Annotated[int, Path(ge=18, le=120, description="Enter your age from 18 to 120")]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_message(user_id: Annotated[int, Path(ge=1, le=1000, description="user id")]) -> str:
    users.pop(str(user_id))
    return "User was deleted!"
