import requests
from bs4 import BeautifulSoup

# Get user input for the website URL
url = input("https://www.google.com/")

# Get user input for the HTML element and class to scrape
element_tag = input("Enter the HTML element tag (e.g., h2, p, div): ")
element_class = input("Enter the HTML element class (optional, press Enter if none): ")

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all elements with the specified tag and class
    if element_class:
        elements = soup.find_all(element_tag, class_=element_class)
    else:
        elements = soup.find_all(element_tag)

    # Extract the text from the elements
    scraped_data = [element.text.strip() for element in elements]

    # Print the scraped data
    print("Scraped Data:")
    for data in scraped_data:
        print(data)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
