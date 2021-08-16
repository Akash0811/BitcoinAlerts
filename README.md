# Welcome
This is a simple web-scraper that downloads bitcoin price information for sending price alerts via email

## Libraries

- requests
- BeautifulSoup
- Python `__builtin__` re
- Python `__builtin__` time
- Python `__builtin__` sys
- Python `__builtin__` smtplib


## Usage

- Prints the bitcoin **price** and 24 hr **percent** change on `stdout`
- Configured to send **Email Alerts** and **SMS Alerts** 
- **Password** to be given as an argument on *prompt*
- Timestamp, Price Data Stored in **csv file** at *hardcoded* location
- SQLite Database stores Price Data and Investor Information
- Uses Strategy Behavioral Pattern


## Websites 

- Uses Real-Time Data from [Coindesk](https://www.coindesk.com/price/bitcoin) 


## Last Updated

- August 17 2021
