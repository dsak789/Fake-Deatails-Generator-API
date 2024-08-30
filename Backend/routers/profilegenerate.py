from fastapi import APIRouter
from faker import Faker
from routers.Attributes import functions, details
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
        if no <=15:
            for i in range(no):
                profile = faker.profile()
                profile["imgurl"] = faker.image_url()
                profiles.append(profile)
            return profiles
        else:
            return {"Message":"This API will Generate upto 47 Profiles per request "}
    except:
        return {
            "Error":404,
            "Message": "Unable to Generate Profile.. Try again some other Time"
        }
    

@route.get('/functions')
def gen_profiles():
    func_info =[]
    try:
        for fun in functions:
            if fun in functions and fun in details:
                func_info.append({
                    'Attribute':fun,
                    "About":details[fun],
                    # "link":f"https://faker789.vercel.app/generate/{fun}"
                    })
            else:
                func_info.append({
                    'Attribute':fun,
                    "About": f"So Inforamtion Not Available. {fun} Attribute still in develpoment..  But Once Try if developed it return response ",
                    # "link":f"https://faker789.vercel.app/generate/{fun}"
                    })

        return func_info
    except:
        return {
            "Error":404,
            "Message": "Unable to Generate Functions Inforamtion.. Try again some other Time"
        }
    
@route.get('/functions/atributes')
def gen_profiles():
    try:
        return functions
    except:
        return {
            "Error":404,
            "Message": "Unable to Generate Functions Inforamtion.. Try again some other Time"
        }
    
@route.get('/functions/information')
def gen_profiles():
    try:
        return details
    except:
        return {
            "Error":404,
            "Message": "Unable to Generate Functions Inforamtion.. Try again some other Time"
        }
