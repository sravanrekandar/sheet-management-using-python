from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

# Opening JSON file
with open('config.json') as json_file:
    config = json.load(json_file)

SERVICE_ACCOUNT_FILE = "token.json"
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = config["heros_spread_sheet_id"]

# specifying only the sheet name
SAMPLE_RANGE_NAME = "heroes_information"


def get_heros_data():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    service = build("sheets", "v4", credentials=credentials)

    # Call the Sheets API
    print("Calling Sheets api to get data...")
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
        return []
    else:
        return values


def main():
    heros = get_heros_data()
    print(heros)


if __name__ == "__main__":
    main()
