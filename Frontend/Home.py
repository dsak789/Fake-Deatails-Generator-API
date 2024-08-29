import streamlit as st

class Home:
    @staticmethod
    def header():
        st.markdown("# :rainbow[Welcome to Faker789!]")
        st.write("Faker789 is an API service for generating fake user details.")

    @staticmethod
    def html():
        st.markdown("<p style='color: #5B8FB9;'>This is a sample application to demonstrate the usage of Faker789 APIs.</p>", unsafe_allow_html=True)
