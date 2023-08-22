from bs4 import BeautifulSoup
import requests
import pandas as pd

class Web_Scraping:
    
    def Beautiful_Soup(self):
        # Fetch the webpage and store in a response.
        response = requests.get("https://etenders.gov.in/eprocure/app")
        html_data = response.text
        # Parse the page using BeautifulSoup
        data = BeautifulSoup(html_data,"html.parser")

        # Create lists to store the extracted data
        tender_titles = []
        reference_numbers = []
        closing_dates = []
        bid_opening_dates = []

        tbody = data.find("tbody")
        if tbody:
            a = tbody.find_all("tr")
            for row in a:
                columns = row.find_all("td")
                tender_titles.append(columns[1].text)
                reference_numbers.append(columns[0].text)
                closing_dates.append(columns[2].contents[0])
                bid_opening_dates.append(columns[3].contents[0])

        # Create a DataFrame
        df = pd.DataFrame({
            "Tender Title": tender_titles,
            "Reference No": reference_numbers,
            "Closing Date": closing_dates,
            "Bid Opening Date": bid_opening_dates
        })

        # Store data in a CSV file
        df.to_csv('Tender_Data.csv', index=False)
        print("Data extracted and saved in Tender_Data.csv")

obj = Web_Scraping()
obj.Beautiful_Soup()
