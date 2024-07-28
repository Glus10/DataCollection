# Description: This file is used to collect data from the web and store it in a csv file
import requests                       # for making HTTP requests
from bs4 import BeautifulSoup         # for parsing HTML
import pandas as pd                   # for data manipulation

# Function to get the data from the web
def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table')
            if table is None:
                print("No table found on the web page.")
                return None
            rows = table.find_all('tr')
            data = []
            for row in rows:
                cols = row.find_all(['td', 'th'])
                cols = [col.text.strip() for col in cols]
                data.append(cols)
            return data
        else:
            print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to save the data to a csv file
def save_data(data, filename):
    # Print the data to check its structure
    for row in data:
        print(row)
    
    # Assuming the first row is the header
    df = pd.DataFrame(data[1:], columns=data[0])
    print(df.head())
    df.to_csv(filename, index=False)

# Main function to get data from the web and save it to a csv file
if __name__ == '__main__':
    url = 'https://www.w3schools.com/html/html_tables.asp'
    data = get_data(url)
    if data is not None:
        save_data(data, 'data.csv')
        print('Data saved to data.csv')
    else:
        print('Failed to get data from the web')
