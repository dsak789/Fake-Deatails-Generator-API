from fastapi import FastAPI
from routers import profilegenerate
app = FastAPI()

app.include_router(profilegenerate.route)


@app.get('/')
def index():
    return{"message":"Hey Profile Generating API Running... "}