import streamlit as st
import requests
import pandas as pd
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
            if st.toggle("Show Example Response",key=api['link']):
                try:
                    res = requests.get(api['res_link']).json()
                    st.caption("Used Link and Response")
                    st.code(f"{api['res_link']}",language="API LINK")
                    st.code(json.dumps(res, indent=4), language="json")
                except:
                    st.info("Response Not Avaibale at the moment")
    def func_list():
        st.title("Attributes List and Usage")
        st.warning('Some Attributes may not get result... They are still in Development')
        try:
            data = requests.get('https://faker789.vercel.app/functions')
            data = data.json()
            table = pd.DataFrame(data)
            st.table(table)
        except:
            st.warning("If Error in Attributes Displaying. Please inform through Contact")

                
                
                

