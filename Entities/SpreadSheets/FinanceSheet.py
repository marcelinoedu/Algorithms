from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1PmqYF0nrA8qkVmR2_kz5TXEGJGWtpx75PJ9zMz5E9ko'
SAMPLE_RANGE_NAME = 'A1:Z1000'

def load_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'financeProjectAuth.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds


def load_finance_sheet():
    creds = load_credentials()

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()

        if not result:
            print('No data found.')
            return None

        return result

    except HttpError as err:
        print(err)
        return None


def update_finance_sheet(cell_updates):
    creds = load_credentials()

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        data_to_update = []
        for cell_range, new_value in cell_updates:
            data_to_update.append({
                'range': cell_range,
                'values': [[new_value]],
            })

        body = {
            'valueInputOption': 'RAW',
            'data': data_to_update,
        }

        sheet.values().batchUpdate(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            body=body
        ).execute()

    except HttpError as err:
        print(err)
