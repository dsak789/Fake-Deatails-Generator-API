from fastapi import FastAPI
from routers import profilegenerate
app = FastAPI()

app.include_router(profilegenerate.route)


@app.get('/')
def index():
    try:
        return{"message":"Hey Profile Generating API Running... "}
    except:
        return{"message":"Something went wrong don't worry we will be back in less time"}
