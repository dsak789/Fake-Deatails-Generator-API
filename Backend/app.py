from fastapi import FastAPI
from routers import profilegenerate
from routers import generate
app = FastAPI(docs_url=None,redoc_url=None)

app.include_router(profilegenerate.route)
app.include_router(generate.route)


@app.get('/')
def index():
    try:
        return{
            "Status":200,
            "message":"Hey! Welcome to Faker789 Deatails Generating...",
            "Goto":"https://faker789.streamlit.app"
            }
    except:
        return{
            "Status":500,
            "message":"Something went wrong don't worry we will be back in less time",
            "Goto":"https://faker789.streamlit.app"
            }
