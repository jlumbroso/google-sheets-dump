import os
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Load service account credentials from environment variable
credentials_json = os.environ['SERVICE_ACCOUNT_JSON']
credentials = ServiceAccountCredentials.from_json_keyfile_dict(eval(credentials_json))

# Access the Google Sheet
gc = gspread.authorize(credentials)
sheet = gc.open_by_key(os.environ['SHEET_ID']).sheet1

# Export to CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sheet.get_all_values())

print("Exported Google Sheet to data.csv")
