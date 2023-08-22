# TaiyoAI
Taiyo Web scraping assignment this code automates the process of gathering e-tendering data from a webpage and organizes it into a structured CSV file for further analysis and reference
The provided code is a Python script that performs web scraping using the BeautifulSoup and requests libraries. It extracts specific information from a webpage, particularly from the URL "https://etenders.gov.in/eprocure/app", which seems to be a portal for e-tendering. The script targets a table within the webpage and extracts data about tender opportunities. Here's a brief description of the code's functionality:

The script uses the BeautifulSoup library to parse the HTML content of the webpage fetched using the requests library.
It defines a class named Web_Scraping that contains a method called Beautiful_Soup.
Inside the method:
The script creates empty lists to store data related to tender titles, reference numbers, closing dates, and bid opening dates.
It locates the <tbody> element within the HTML structure of the webpage, where the tabular data is present.
It iterates through each row in the table and extracts the relevant data (tender title, reference number, closing date, and bid opening date) from the respective <td> elements.
The extracted data is then added to their respective lists.
After extracting data from the webpage, the script uses the pandas library to create a DataFrame with columns "Tender Title", "Reference No", "Closing Date", and "Bid Opening Date", and populates it with the extracted data.
The script saves the DataFrame into a CSV file named "Tender_Data.csv" in the same directory where the script is executed.
A message is printed indicating that the data extraction and CSV saving were successful.
In summary, this code automates the process of gathering e-tendering data from a webpage and organizes it into a structured CSV file for further analysis and reference.
