from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from argparse import ArgumentParser

parser = ArgumentParser(prog='list-files',
                        description='List all files with their IDs in your GDrive')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-a', '--all', action='store_true', default=False, help='List all files in all directories')
group.add_argument('-dir', '--dir', action='store', type=str, help='List files in the specified folder')

args = parser.parse_args()

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth) # Create a drive object using gauth object to interact with GDrive

if args.all:
    files = drive.ListFile({'q': "'root' in parents and trashed=False"}).GetList()
    for file in files:
        print(f"title: {file['title']}     ::     id: {file['id']}")
