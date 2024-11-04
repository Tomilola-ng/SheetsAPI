"""
    Google Sheets API Samples
    
    This code is to automate some of the tasks in Google Sheets.
"""

from typing import Union

import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

credentials = Credentials.from_service_account_file("client_secret.json", scopes=scopes)
client = gspread.authorize(credentials)

SHEET_ID = "1rfQZ5YxpF-_tGAtCKjczT2tYY3C1H5MRBxaEiU2-mUU"
MAIN_SHEET = client.open_by_key(SHEET_ID)

def get_column(worksheet : gspread.worksheet, title : str, column_id : Union[int, list[int]]):
    """
        A Function that receives a title: string and column_id: number, worksheet: gspread.worksheet
        It gets the column with the given column_id
        IF YES It checks if the matching column's header is same as the given title
        IF YES, return the rest of the column's values in an array starting from the second column
        ELSE return error message "Column not found"
    """
    column = worksheet.col_values(column_id)
    for index, value in enumerate(column):
        if column[value] == title:
            return column[index + 1:]
        return "Column not found"

ip_addresses = get_column(MAIN_SHEET.sheet1, "IP Address", 1)
print(ip_addresses)
