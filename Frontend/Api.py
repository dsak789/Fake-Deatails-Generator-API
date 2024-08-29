import streamlit as st
from AllApis import ALLAPIS
class API:
    @staticmethod
    def header():
        ap =ALLAPIS()
        apilist = ap.apis()
        for api in apilist:
            st.markdown(f"### {api['title']}")
            st.code(f"{api['link']}",language="API LINK")
            if st.toggle("Show Response",key=api['link']):
                ifr = f'''
                <iframe src="{api['link']}" width="70%" height="200px" frameborder="0"></iframe>
                '''
                st.markdown(ifr, unsafe_allow_html=True)
                

