import streamlit as st
import requests

# Function to get country data from the REST Countries API
def get_country_data(country_name):
    response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

# Title of the web app
st.title("Country Information Cards")

# Input box for the user to enter the country name
country_name = st.text_input("Enter a country name:")

# Button to fetch the country data
if st.button("Get Country Info"):
    if country_name:
        country_data = get_country_data(country_name)
        if country_data:
            # Display country information
            st.header(country_data["name"]["common"])
            st.image(country_data["flags"]["png"], width=200)
            st.write(f"**Capital:** {country_data['capital'][0]}")
            st.write(f"**Region:** {country_data['region']}")
            st.write(f"**Subregion:** {country_data['subregion']}")
            st.write(f"**Population:** {country_data['population']}")
            st.write(f"**Area (sq km):** {country_data['area']}")
            st.write(f"**Timezones:** {', '.join(country_data['timezones'])}")
        else:
            st.error("Country not found. Please check the spelling or try another country.")
    else:
        st.warning("Please enter a country name.")