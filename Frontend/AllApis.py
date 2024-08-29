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
                "description" : "",

            },
            {
                "linkId" : uuid.uuid1(),
                "title" : "Generate Uniuque Profiles",
                "link" : "https://faker789.vercel.app/generate-profiles/<Number>",
                "description" : "",

            },
            {
                "linkId" : uuid.uuid1(),
                "title" : "Generate Uniuque Profiles",
                "link" : "https://faker789.vercel.app/generate-profiles/{int}",
                "description" : "",

            },
            
        ]
        return(self.apilist)