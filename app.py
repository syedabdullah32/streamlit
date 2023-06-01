import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.goodreads.com/"  # Replace with the actual website URL

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all elements with the book titles
    book_title_elements = soup.find_all("h2", class_="book-title")  # Replace with the actual HTML element and class

    # Extract the book titles from the elements
    book_titles = [element.text.strip() for element in book_title_elements]

    # Print the book titles
    for title in book_titles:
        print(title)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
