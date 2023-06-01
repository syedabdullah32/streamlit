import streamlit as st
import requests
import re
from bs4 import BeautifulSoup

def main():
    st.title("My Web Scraper")

    # Get the URL from the user
    url = st.text_input("Enter the URL", "https://quotes.toscrape.com/")

    # Make a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the tags using regular expressions
    tags = soup.find_all('a')

    # Display the extracted tags in Streamlit
    for tag in tags:
        st.write(tag.text.strip())

if __name__ == '__main__':
    main()
