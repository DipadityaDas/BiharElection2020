from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Official Website of Election Commission of India 
url = "https://results.eci.gov.in/ACTRENDS2020/partywiseresult-S04.htm"

# Make a GET request to fetch the raw HTML content
htm_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(htm_content, "html.parser")

# print the parsed data of html
# print(soup.prettify())
