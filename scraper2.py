import requests
from bs4 import BeautifulSoup

# Function to scrape data from the website
def scrape_website():
    # Make a request to the website
    make = input("Enter the car make: ")
    url = f'https://charm.li/{make}'
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.content
        # Parse HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract data from the website
        data = []
        # Example: Scraping titles and descriptions
        for item in soup.find_all('li'):
            title = item.find('a').text.strip()
            
            data.append({'title': title})
        return data
    else:
        print("Failed to fetch the webpage")
        return None

# Call the function to scrape data
scraped_data = scrape_website()

# Check if data is scraped successfully
if scraped_data:
    # Print scraped data for verification
    print(scraped_data)

    # Now you can use scraped_data for further processing (e.g., storing in a file or database)
    # Replace the sample data with scraped_data
    data = scraped_data
import sqlite3

# Function to save data to an SQLite database
def save_to_sqlite(data):
    # Connect to SQLite database (or create if it doesn't exist)
    conn = sqlite3.connect('scraped_data2.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create a table to store the scraped data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scraped_data (
            id INTEGER PRIMARY KEY,
            title TEXT
        )
    ''')

    # Insert data into the table
    for item in data:
        cursor.execute('''
            INSERT INTO scraped_data2 (title) VALUES (?)
        ''', (item['title'],))

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Call the function to save data to the SQLite database
save_to_sqlite(scraped_data)