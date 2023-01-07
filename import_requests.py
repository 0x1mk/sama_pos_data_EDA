import requests
from bs4 import BeautifulSoup

session = requests.Session()

# Make a request to the webpage using the session
url = 'https://www.sama.gov.sa/ar-sa/Indices/pages/pos.aspx'
response = session.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
                                     })


# Parse the HTML of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the `tr` elements with class "gridalter"
rows = soup.find_all('tr', class_='gridalter')

# Extract the href values from the rows
for row in rows:
    # Find all the `a` elements within the row
    links = row.find_all('a', href=True)

    # Print the `href` attribute of each link
    for link in links:
        print(link['href'])
