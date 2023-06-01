import requests
from bs4 import BeautifulSoup

# Set the title for your app
app_title = "Web Scraper"

# Function to get user input
def get_user_input():
    url = input("Enter the website URL: ")
    element_tag = input("Enter the HTML element tag (e.g., h2, p, div): ")
    element_class = input("Enter the HTML element class (optional, press Enter if none): ")
    return url, element_tag, element_class

# Function to scrape the website
def scrape_website(url, element_tag, element_class):
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
        return scraped_data
    else:
        error_message = f"Failed to retrieve the webpage. Status code: {response.status_code}"
        print(error_message)
        return None

# Main function
def main():
    print(app_title)
    print("")

    # Get user input
    url, element_tag, element_class = get_user_input()

    # Scrape the website
    scraped_data = scrape_website(url, element_tag, element_class)

    # Print the scraped data
    if scraped_data:
        print("Scraped Data:")
        for data in scraped_data:
            print(data)

if __name__ == "__main__":
    main()
