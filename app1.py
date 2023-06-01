import streamlit as st
import requests
import re

def main():
    st.title(" My Web Scraper")

    # Get the URL from the user
    url = st.text_input("Enter the URL", "https://quotes.toscrape.com/")

    # Make a GET request to the website
    response = requests.get(url)

    # Extract the links using regular expressions
    links = re.findall(r'<a\s+href=[\'"]?([^\'" >]+)', response.text)

    # Display the extracted links in Streamlit
    for link in links:
        st.write(link)

if __name__ == '__main__':
    main()
