import streamlit as st

class Home:
    @staticmethod
    def header():
        st.title(" :rainbow[Welcome to Faker789!]")
        st.write("Faker789 is a powerful API service designed to help developers and testers by providing easy access to realistic and random fake user details.")

    @staticmethod
    def html():
        st.markdown("""
                    <p style='color: #5B8FB9;'>
                    Faker789 generates random, yet realistic, data for various fields like names, addresses, emails, and much more, helping you test and develop your applications efficiently without the need to input real data.
                    </p>
                    """, unsafe_allow_html=True)
        
        # Brief overview of features
        st.subheader(" Key Features")
        st.markdown("""
        - **Easy Integration**: Simply integrate with our API and start generating fake data with minimal setup.
        - **Variety of Data**: Generate a wide range of data types including names, addresses, email addresses, phone numbers, and more.
        - **Flexible and Scalable**: Whether you need a few records or thousands, Faker789 can handle it efficiently.
        - **Secure and Private**: Since all data is randomly generated, there's no risk of exposing real personal information.
        """)

        # Use cases and examples
        st.subheader(" Use Cases")
        st.markdown("""
        - **Testing**: Populate your test database with realistic data to simulate user scenarios.
        - **Prototyping**: Use generated data in your prototypes to visualize how your application will behave with real data.
        - **Data Privacy**: Avoid using sensitive real-world data by substituting with realistic fake data.
        """)

        # Sample API request example
        st.subheader(" Sample API Request")
        st.markdown("""
        Here’s a quick example of how to use the Faker789 API to generate a fake user profile:

        ```python
        import requests

        response = requests.get('https://faker789.vercel.app/api/profile')
        print(response.json())
        ```

        This will return a JSON object containing random user details like name, email, address, etc.
        """)
        
        st.markdown("<hr>", unsafe_allow_html=True)

        # Footer with more information
        st.header(" Learn More")
        st.markdown("""
        Explore the API Documentation Tab for a full list of available endpoints, details on each, and sample responses. 
        If you have any questions or need further assistance, feel free to reach out via the Contact Tab.
        """)

        st.markdown("<br>", unsafe_allow_html=True)
        # st.header("🌐 Visit our Website")
        # st.markdown("[Faker789 API Documentation](https://faker789.streamlit.app) for more details.")
