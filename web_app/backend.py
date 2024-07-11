import gspread
from google.oauth2.service_account import Credentials
from env import SHEET_ID

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = SHEET_ID
workbook = client.open_by_key(sheet_id)

worksheet = workbook.worksheet("Sheet1")