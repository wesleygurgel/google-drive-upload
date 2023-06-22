from googleapiclient.http import MediaFileUpload
from google_apis import create_service

CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Upload a file
file_metadata = {
    'name': 'upload.png',
    'parents': ['1MiMfxzQ4zsh-fPKR0J9gbdfJoPWOpSVn']
}

media_content = MediaFileUpload('wsg.png', mimetype='image/png')

file = service.files().create(
    body=file_metadata,
    media_body=media_content
).execute()

print(file)