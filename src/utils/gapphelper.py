from os import path,getenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import get_env

class GappHelper():
    def __init__(self):
        """init"""
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        json_file_path = path.join(path.dirname(__file__), '../../', get_env('CLIENT_SECRET_FILE'))
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_path, self.scope)
        self.client = gspread.authorize(self.credentials)

    def open_sheet(self):
        """open the google sheet"""
        sheet = self.client.open(get_env('GAPPS_SHEET_NAME')).sheet1
        return sheet.get_all_records(empty2zero=False, head=1, default_blank='')