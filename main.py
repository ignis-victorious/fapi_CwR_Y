#
#  Import FILES LIBRARIOES
from fastapi import FastAPI

#  _______________________


app = FastAPI()


@app.get(path="/")
def get_root() -> dict[str, str]:
    return {"message": "Hello World"}
