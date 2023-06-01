import streamlit as st
import requests
import re
from bs4 import BeautifulSoup

def main():
    st.title("My Web Scraper")

    # Get the URL from the user
    url = st.text_input("Enter the URL", "https://www.whatmobile.com.pk/")

    # Make a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the names using regular expressions
    names = soup.find_all('a', class_='aname')

    # Display the extracted names in Streamlit
    for name in names:
        st.write(name.text.strip())

if __name__ == '__main__':
    main()
