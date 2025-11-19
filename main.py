#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from database.user_db import users

#  _______________________


app = FastAPI()


@app.get(path="/")
def get_root() -> dict[str, str]:
    return {"status": "success", "message": "Welcome to the User Management API"}


#  Create a user
@app.post(path="/users")
def create_user(name: str, email: str, password: str) -> dict[str, str | dict[str, str | int]]:
    users.append({"id": len(users) + 1, "name": name, "email": email, "password": password})
    return {
        "status": "success",
        "data": users[len(users) - 1],
    }


#  Get user by id
@app.get(path="/users/(user_id)")
def get_user_by_id(user_id: int) -> dict[str, str | dict[str, str | int]]:
    return {
        "status": "success",
        "data": users[user_id - 1],
    }


#  Get all user
@app.get(path="/users")
def get_users() -> dict[str, str | list[dict[str, str | int]]]:
    return {
        "status": "success",
        "data": users,
    }


#  update user
@app.put(path="/users/{user_id}")
def update_user(
    user_id: int,
    name: str,
    email: str,
    password: str,
) -> dict[str, str | dict[str, str | int]]:
    users[user_id - 1]["name"] = name
    users[user_id - 1]["email"] = email
    users[user_id - 1]["password"] = password
    return {
        "status": "success",
        "data": users[user_id - 1],
    }


# Patch updating user
@app.patch(path="/users/{user_id}")
def patch_user(
    user_id: int,
    name: str,
    email: str,
) -> dict[str, str | dict[str, str | int]]:
    users[user_id - 1]["email"] = email
    users[user_id - 1]["name"] = name
    return {
        "status": "success",
        "data": users[user_id - 1],
    }


# Delete user
@app.delete(path="/users/{user_id}")
def delete_user(user_id: int) -> dict[str, str | None]:
    users.remove(users[user_id - 1])
    return {
        "status": "success",
        "data": None,
    }


#
#  Import LIBRARIES
#  Import FILES
#  _______________________
