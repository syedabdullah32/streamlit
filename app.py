from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    # Get user input from the form
    url = request.form['url']
    element_tag = request.form['element_tag']
    element_class = request.form['element_class']

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

        # Render the results template with the scraped data
        return render_template('results.html', scraped_data=scraped_data)
    else:
        error_message = f"Failed to retrieve the webpage. Status code: {response.status_code}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run()
