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
                "title" : "Generate Uniuque Profiles Upto :red[15]",
                "link" : "https://faker789.vercel.app/generate-profiles/<Number>",
                "res_link" : "https://faker789.vercel.app/generate-profiles/4",
                "description" : "",

            },
            {
                "linkId" : uuid.uuid1(),
                "title" : "Generate Fake Details of Various Labels",
                "link" : "https://faker789.vercel.app/generate/<attribute>",
                "res_link" : "https://faker789.vercel.app/generate/paragraphs/",
                "description" : "",

            },
            {
                "linkId" : uuid.uuid1(),
                "title" : "Generate Fake Details of Various Labels upto :red[15]",
                "link" : "https://faker789.vercel.app/generate/<attribute>/<no>",
                "res_link" : "https://faker789.vercel.app/generate/paragraphs/3",
                "description" : "",

            },
            {
                "linkId" : uuid.uuid1(),
                "title" : "Generate Fake Details on :blue[20] various Custom Labels",
                "link" : "https://faker789.vercel.app/generate-custom/<attribute1>,<atribute2><attribute3>/",
                "res_link" : "https://faker789.vercel.app/generate-custom/name,email,iban/",
                "description" : "",

            },
            {
                "linkId" : uuid.uuid1(),
                "title" : "Generate Fake Details on :blue[20] various Custom Labels upto :red[15]",
                "link" : "https://faker789.vercel.app/generate-custom/<attribute1>,<atribute2><attribute3>/<no>",
                "res_link" : "https://faker789.vercel.app/generate-custom/name,email,iban,image_url/3",
                "description" : "",

            },
            
        ]
        return(self.apilist)