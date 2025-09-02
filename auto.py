import os
import datetime
import shutil
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from dotenv import load_dotenv

load_dotenv()

sourcedir = os.path.expanduser(os.getenv("SOURCE_DIR"))
backupdir = os.path.expanduser(os.getenv("BACKUP_DIR"))
CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS")
DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")

SCOPES = ['https://www.googleapis.com/auth/drive.file']
TOKEN_PATH = 'token.json'

def authenticate():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token_file:
            token_file.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)

def upload_to_drive(service, filepath, filename_in_drive):
    file_metadata = {
        'name': filename_in_drive,
        'parents': [DRIVE_FOLDER_ID]
    }
    media = MediaFileUpload(filepath, resumable=True)

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"Upload concluído com sucesso. ID no Drive: {file.get('id')}")

def backup_and_upload(sourcedir, backupdir):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder_name = f"backup_{current_time}"
    backup_folder_path = os.path.join(backupdir, backup_folder_name)
    zip_file_path = os.path.join(backupdir, f"{backup_folder_name}.zip")

    try:
        shutil.copytree(sourcedir, backup_folder_path)
        print(f"Backup local criado em: {backup_folder_path}")

        shutil.make_archive(backup_folder_path, 'zip', backup_folder_path)
        print(f"Arquivo compactado: {zip_file_path}")

        service = authenticate()
        upload_to_drive(service, zip_file_path, f"{backup_folder_name}.zip")

    except Exception as e:
        print(f"Erro durante o processo: {e}")

if __name__ == '__main__':
    backup_and_upload(sourcedir, backupdir)