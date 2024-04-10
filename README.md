# webscraping1
webscraping in python

# Website Data Scraper

This Python script scrapes data from the Wikipedia page listing the most visited websites and saves it into an Excel file.

## Overview

This script utilizes the `requests` library to send HTTP GET requests to the Wikipedia page and the `BeautifulSoup` library to parse the HTML content. It then extracts relevant data from the page, including website names, domain names, ranks from SimilarWeb and Semrush, website types, company names, and countries. The extracted data is stored in a pandas DataFrame and saved to an Excel file.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library

## Installation

1. Clone the repository:
git clone https://github.com/jamil2021/webscraping1.git


2. Install the required dependencies:
pip install requests beautifulsoup4 pandas


## Usage

1. Navigate to the project directory:
cd webscraping1

2. Run the script:
python popularSites.py


3. The scraped data will be saved to `website_data.xlsx` in the project directory.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script was inspired by the need to extract data from the Wikipedia page on most visited websites.
- Special thanks to the developers of the `requests`, `beautifulsoup4`, and `pandas` libraries for their contributions to the Python community.


## Additions
# 1. COVID-19 Data Scraper

The `coronaVirus.py` script collects data related to the COVID-19 pandemic from https://www.worldometers.info/coronavirus/. It scrapes information such as total cases, new cases, total deaths, new deaths, total recovered, new recovered, active cases, serious critical cases, total cases per 1M population, deaths per 1M population, total tests conducted, tests per 1M population, and population. The extracted data is stored in an Excel file named `corona_data.xlsx`.

# 2. Python Selenium Web Scraper
This Python script uses Selenium WebDriver to perform a web scraping task. Here’s a brief summary of what the script does:

Launches a web browser: The script starts by launching a new instance of the Firefox web browser using Selenium WebDriver.

Navigates to a website: The script then navigates to the Python.org website.

Searches for a query: It finds the search box element on the website by its name, clears it, and types in the search query “getting started with python”. It then submits the query.

Waits for results: The script waits for two seconds to allow the search results to load.

Prints the first result: It finds the first search result and prints its text to the console.

Closes the browser: Finally, the script closes the web browser.

Please note that this script requires the Selenium WebDriver and a compatible web browser to be installed on your system. You may need to replace webdriver.Chrome() with the driver of the browser you are using (e.g., webdriver.Firefox() for Firefox).
