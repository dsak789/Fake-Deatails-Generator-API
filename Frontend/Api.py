import streamlit as st
import requests
import json
from AllApis import ALLAPIS
class API:
    @staticmethod
    def header():
        ap =ALLAPIS()
        apilist = ap.apis()
        for api in apilist:
            st.markdown(f"### {api['title']}")
            st.code(f"{api['link']}",language="API LINK")
            res = requests.get(api['res_link']).json()
            if st.toggle("Show Response",key=api['link']):
                st.code(f"{api['res_link']}",language="API LINK")
                st.code(json.dumps(res, indent=4), language="json")
                
                
                

