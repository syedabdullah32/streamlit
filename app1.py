import streamlit as st
import requests
from bs4 import BeautifulSoup

def main():
    st.title("My Web Scraper")

    # Get the URL from the user
    url = st.text_input("Enter the URL", "https://www.whatmobile.com.pk/")

    # Make a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the phone listings on the page
    phone_listings = soup.find_all('div', class_='item')

    # Extract the name and price for each phone listing
    for phone in phone_listings:
        name = phone.find('a', class_='aname').text.strip()
        price = phone.find('i', class_='price').text.strip()

        # Display the name and price in Streamlit
        st.write(f"Name: {name}")
        st.write(f"Price: {price}")
        st.write('---')  # Add a separator between listings

if __name__ == '__main__':
    main()
