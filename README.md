# Faker789

## Overview
**Faker789** is a simple API service for generating fake user details and other random data, ideal for testing and development purposes. The application is built using Streamlit and provides a web interface for exploring and interacting with various Faker APIs.

## Features
- **Home Page:** Introduction to Faker789, including details about the service and how it can be used.
- **API Documentation:** A detailed list of available APIs with descriptions and examples.
- **Contact Page:** Information on how to get in touch with the developer or contribute to the project.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Streamlit
- Requests
- Pandas
- `streamlit-option-menu` for a styled menu interface

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dsak789/https://github.com/dsak789/Fake-Details-Generator-API.git
   cd Faker789
2. **Dependencies:** 

To run this application, you will need the following Python packages:

- **streamlit**: A library for building interactive web applications.
- **requests**: A library for making HTTP requests.
- **pandas**: A library for data manipulation and analysis.
- **streamlit-option-menu**: A library for creating styled menu options in Streamlit.

You can install all the necessary dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
## Running the Application

To run the Faker789 application locally, follow these steps:

1. **Ensure Dependencies are Installed**: Make sure you have installed all necessary dependencies listed in the `requirements.txt` file. You can install them using pip:
    bash
    pip install -r requirements.txt

2. **Run the Application**: Start the Streamlit server with the following command:
    bash
    streamlit run app.py
    

3. **Access the Application**: After running the command, Streamlit will open the application in your default web browser. If it doesn’t open automatically, you can navigate to `http://localhost:8501` in your browser.

## File Structure

Here’s an overview of the file structure for the application:

- **app.py**: The main entry point of the Streamlit application. This file manages page navigation and displays content based on the selected menu option.

- **Home.py**: Contains the content and layout for the Home page. It provides an introduction to the Faker789 application and its features.

- **API.py**: Provides the API documentation page. It includes an embedded iframe for the API profile generation service and displays relevant links and details.

- **Contact.py**: Displays contact information and communication details for the application.

- **requirements.txt**: Lists the Python packages required to run the application. This file is used for setting up the environment with the necessary dependencies.
