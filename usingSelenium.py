from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Go to the website
driver.get("http://www.python.org")

# Find the search box element by its name
search_box = driver.find_element(By.NAME, "q")

# Clear the search box in case there's anything already in there
search_box.clear()

# Type in the search query
search_box.send_keys("getting started with python")

# Submit the query (like hitting return)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(2)

# Find the first search result and print it
result = driver.find_element(By.CSS_SELECTOR, "ul.menu li h3 a")
print(result.text)

# Close the browser
driver.quit()
