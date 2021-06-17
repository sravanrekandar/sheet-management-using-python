import pandas as pd
import gspread
from googleapiclient.discovery import build
from google.oauth2 import service_account

from .step01_read_data import get_heros_data
from .defending import get_eye_color_based_data
import json

# Opening JSON file
with open('config.json') as json_file:
    config = json.load(json_file)
# from .defending import get_race_based_data

SERVICE_ACCOUNT_FILE = "token.json"
# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
DESTINATION_FOLDER_ID = config["folder_id"]


def main():
    heros = get_heros_data()
    # print(heros)
    columns = heros[0]
    rows = heros[1:]
    print("Data received. Createing a Pandas Data frame")
    df = pd.DataFrame(rows, columns=columns)

    eye_color_df = get_eye_color_based_data(df)
    print(eye_color_df)

    # print(eye_color_df.values.tolist())
    # return
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    service = build("sheets", "v4", credentials=credentials)

    spreadsheet_data = {
        "properties": {"title": "hero_eye_color"},
    }
    spreadsheet = (
        service.spreadsheets()
        .create(body=spreadsheet_data, fields="spreadsheetId")
        .execute()
    )

    spread_sheet_id = spreadsheet.get("spreadsheetId")
    drive_service = build("drive", "v3", credentials=credentials)
    file = drive_service.files().get(fileId=spread_sheet_id, fields="parents").execute()

    previous_parents = ",".join(file.get("parents"))
    file = (
        drive_service.files()
        .update(
            fileId=spread_sheet_id,
            addParents=DESTINATION_FOLDER_ID,
            removeParents=previous_parents,
            fields="id, parents",
        )
        .execute()
    )
    print(file)

    client = gspread.authorize(credentials)
    client.import_csv(spread_sheet_id, data=eye_color_df.to_csv())
    # race_df = get_race_based_data(df)
    # print(race_df)


if __name__ == "__main__":
    main()
