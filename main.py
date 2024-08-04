"""
    Google Sheets API Samples
    
    This code is to automate some of the tasks in Google Sheets.
"""

import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

credentials = Credentials.from_service_account_file("client_secret.json", scopes=scopes)
client = gspread.authorize(credentials)

SHEET_ID = "1rfQZ5YxpF-_tGAtCKjczT2tYY3C1H5MRBxaEiU2-mUU"
sheet = client.open_by_key(SHEET_ID)

values_list = sheet.sheet1.row_values(1)
print(values_list)
