from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome1() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def welcome2() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def welcome3(user_id: str) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def welcome4(username="Billy", age=35) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

