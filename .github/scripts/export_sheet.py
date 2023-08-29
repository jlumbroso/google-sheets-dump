import csv
import os
import sys

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from loguru import logger


# 📝 Configure logging with loguru
logger.add("export_sheet.log", rotation="10 MB")  # Log to file
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")  # Log to terminal

def get_env_variable(var_name, default=None):
    """Retrieve environment variable safely."""
    try:
        var_value = os.environ[var_name]
        if not var_value:
            if default is not None:
                return default
            logger.error(f"❌ Environment variable {var_name} is empty.")
            exit(1)
        return var_value
    except KeyError:
        if default is not None:
            return default
        logger.error(f"❌ Environment variable {var_name} not set.")
        exit(1)

# 🛠 Load service account credentials from environment variable
try:
    credentials_json = get_env_variable('SERVICE_ACCOUNT_JSON')
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(eval(credentials_json))
except Exception as e:
    logger.error(f"❌ Error loading service account credentials: {e}")
    exit(1)

# 📊 Access the Google Sheet
try:
    gc = gspread.authorize(credentials)
    sheet_id = get_env_variable('SHEET_ID')
    sheet = gc.open_by_key(sheet_id).sheet1
except gspread.SpreadsheetNotFound:
    logger.error(f"❌ Google Sheet with ID {sheet_id} not found.")
    exit(1)
except Exception as e:
    logger.error(f"❌ Error accessing Google Sheet: {e}")
    exit(1)

# 💾 Export to CSV
output_filename = get_env_variable('OUTPUT_FILENAME', default='data.csv')
try:
    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sheet.get_all_values())
    logger.info(f"✅ Exported Google Sheet to {output_filename}")
except Exception as e:
    logger.error(f"❌ Error exporting data to {output_filename}: {e}")
    exit(1)
