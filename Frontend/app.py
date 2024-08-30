import streamlit as st
from streamlit_option_menu import option_menu
from Home import Home
from Api import API
from Contact import Contact

st.set_page_config(page_title="Faker 789", page_icon='🤖' ,layout="wide")

color = {
    'base':'#03001C',
    'primary': '#301E67',
    'secondary':'#5B8FB9',
    'action':'#B6EADA'

}


menu = option_menu(
    menu_title="",
    menu_icon='chat',
    options=['Home',"API Documentation","Contact"],
    icons = ['house','book','envelope'],
    default_index = 0,
    orientation='horizontal',
    styles={
        "container":{
            'padding':'5!important',
            'background-color':color['base'],
            'margin':'1px'},
        'icon':{'color':'','font-size':'15px'},
        'nav-link':{
            'font-size':'20px',
            'tex-align':'left',
            'color':color['action'],
            'margin':'5px',
            'font-family':'Times NewRoman',
            '--hover-color':color['secondary']
        },
        'nav-link-selected':{
            'color':color['primary'],
            'background-color':color['action'],
            'font-family':'calibri'
            
        },
    }

)

if menu == "Home":
    Home.header()
    Home.html()
if menu == "API Documentation":
    st.header(":blue[Faker API Documentation]",divider=True)
    API.header()
    API.func_list()
if menu == "Contact":
    st.header(":blue[Faker Contact]",divider=True)
    Contact.show_contact_info()


st.markdown("""
            <div class="footer"> Design and Developed By DSAK789
        &copy; 2024 <strong>Faker789</strong>. All rights reserved.
    </div>
<style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #03001C;
        color: #B6EADA;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        border-top: 1px solid #ddd;
    }
</style>

""",unsafe_allow_html=True)