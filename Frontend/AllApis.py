import uuid

class ALLAPIS():
    def __init__(self) -> None:
        self.apilist = []
        pass
    def apis(self):
        self.apilist = [
            {
                "linkId" : uuid.uuid1(),
                "title" : "Generate Uniuque Profile",
                "link" : "https://faker789.vercel.app/generate-profile",
                "res_link" : "https://faker789.vercel.app/generate-profile",
                "description" : "",

            },
            {
                "linkId" : uuid.uuid1(),
                "title" : "Generate Uniuque Profiles",
                "link" : "https://faker789.vercel.app/generate-profiles/<Number>",
                "res_link" : "https://faker789.vercel.app/generate-profiles/4",
                "description" : "",

            },
            {
                "linkId" : uuid.uuid1(),
                "title" : "Generate Uniuque Profiles",
                "link" : "https://faker789.vercel.app/generate-profiles/{int}",
                "res_link" : "https://faker789.vercel.app/generate-profiles/2",
                "description" : "",

            },
            
        ]
        return(self.apilist)