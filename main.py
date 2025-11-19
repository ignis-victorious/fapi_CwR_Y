#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES

#  _______________________


app = FastAPI()


@app.get(path="/")
def get_root() -> dict[str, str]:
    return {"status": "success", "message": "Welcome to the User Management API"}
