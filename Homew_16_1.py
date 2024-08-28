from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def glavnay():
    return "Главная страница"


@app.get("/user/admin")
async def administration():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def users(user_id):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def info_users(username: str = "Неизвестный пользователь", age: int = 0):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"