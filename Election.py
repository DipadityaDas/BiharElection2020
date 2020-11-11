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

# Scaning the Entire HTML and finding <table border="1"></table> and returns the result in HTML format
BE_table = soup.find("table", attrs={"border": "1"})

# Scaning all the tr tags inside the table tag
BE_table_data = BE_table.tbody.find_all("tr")

data = []
row = []

# Fetching all the Heading of the table
for th in BE_table_data[2].find_all("th"):
    row.append(th.text)

data.append(row)
