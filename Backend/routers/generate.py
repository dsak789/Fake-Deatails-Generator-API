from faker import Faker
from fastapi import APIRouter
from routers.Attributes import functions  

route = APIRouter()
faker = Faker()

  
    
@route.get('/generate/{fun}')
def gen(fun: str):
    if fun in functions:
        try:
            faker_function = getattr(faker, fun)
            result = faker_function()
            return {fun:result}
        except AttributeError:
            return {"error": "Attribute not found in Faker library",
                    'Suggestion':"Goto API Documentation at https://faker789.streamlit.app"}
    else:
        return {"error": "Attribute not found in provided Attributes",
                'Suggestion':"Goto API Documentation at https://faker789.streamlit.app"}
    

@route.get('/generate/{fun}/{no}')
def gen(fun: str, no: int):
    res= []
    if fun in functions:
        try:
            if no<=15:
                for i in range(no):
                    faker_function = getattr(faker, fun)
                    result = faker_function()
                    res.append(result)
                return res
            else:
                return {
                    "error": "This Generator API can generate upto 15 responses per request",
                    'Suggestion':"Goto API Documentation at https://faker789.streamlit.app"
                    }

        except AttributeError:
            return {
                "error": "Attribute not found in Faker library",
                'Suggestion':"Goto API Documentation at https://faker789.streamlit.app"
                }
    else:
        return {"error": "Attribute not found in provided Attributes",
                'Suggestion':"Goto API Documentation at https://faker789.streamlit.app"}
    
# @route.get('/generate/{fun}/{no}')
# def gen(fun: str, no: int):
#     res= []
#     if fun in functions:
#         try:
#             for i in range(no):
#                 faker_function = getattr(faker, fun)
#                 result = faker_function()
#                 res.append({fun+str(i+1):result})
#             return res
#         except AttributeError:
#             return {"error": "Function not found in Faker library"}
#     else:
#         return {"error": "Function not found in provided functions"}



@route.get('/generate-custom/{fun_list}')
def gen(fun_list: str):
    fun_list = fun_list.split(",")
    try:
        response = {}
        for fun in fun_list:
            if fun in functions:
                faker_func = getattr(faker, fun)
                response.update({fun:faker_func()})
            else:
                response.update({fun:"Not generated or Attribute not working"})
        return {'Custom':response}

    except:
        return {"error":"Somenthing Went Wrong"}
    
@route.get('/generate-custom/{fun_list}/{no}')
def gen(fun_list: str,no : int):
    fun_list = fun_list.split(",")
    res =[]
    try:
        if no<=15:
            for i in range(no):
                response = {}
                for fun in fun_list:
                    if fun in functions:
                        faker_func = getattr(faker, fun)
                        response.update({fun:faker_func()})
                    else:
                        response.update({
                            fun:{
                                'error':"Not generated or Attribute not working",
                                'Suggestion':"Goto API Documentation at https://faker789.streamlit.app"
                                }
                                })
                res.append(response)
            return res
        else:
            return {"Message":"This Custom Generate API can generate upto 15 responses per request"}


    except:
        return {"error":"Faker789 Facing Internal Issue... Don't worry we will be back in less time"}







    


