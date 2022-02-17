from __future__ import print_function

import os.path
import pandas as pd

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1EL6D5Usfhf5rX2-AVz2dzgWdZnkLNcwr6EKVyKDdl94'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

sheet_id = '1EL6D5Usfhf5rX2-AVz2dzgWdZnkLNcwr6EKVyKDdl94'
sheet_name = 'export'
url = 'https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}'.format(sheet_id, sheet_name)

class GoogleAPI():
    def __init__(self) -> None:
        pass

    def read_spreadsheet(self, sheet_id=sheet_id):
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        url = 'https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}'.format(sheet_id, sheet_name)
        return pd.read_csv(url, usecols = ['URL Hidden'])