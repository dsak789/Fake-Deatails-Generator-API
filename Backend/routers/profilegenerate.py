from fastapi import APIRouter
from faker import Faker
route = APIRouter()
faker = Faker()
@route.get('/generate-profile')
def gen_profile():
    try:
        profile = faker.profile()
        profile["imgurl"] = faker.image_url()
        return profile
    except:
        return {
            "Error":404,
            "Message": "Unable to Generate Profile.. Try again some other Time"
        }
@route.get('/generate-profiles/{no}')
def gen_profiles(no : int):
    try:
        profiles = []
        if no <=47:
            for i in range(no):
                profiles = faker.profile()
                profiles["imgurl"] = faker.image_url()
            return profiles
        else:
            return {"Message":"This API will Generate upto 47 Profiles per request "}
    except:
        return {
            "Error":404,
            "Message": "Unable to Generate Profile.. Try again some other Time"
        }
