from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from argparse import ArgumentParser
import os
import sys

def valid_file_path(loc):
    if os.path.exists(loc):
        return loc
    else:
        print('Path specified doesn\'t exist')
        sys.exit()

parser = ArgumentParser(prog='mkfile',
                        description='Creates a new file in Google Drive from the given content or local file',
                        )
parser.add_argument('file_name', type=str, help='File name of the new file')

group = parser.add_mutually_exclusive_group()
group.add_argument('--content', type=str, help='Content of the new file')
group.add_argument('--local_file', type=valid_file_path, action='store', help='Path to the local file to upload to Drive')
args = parser.parse_args()

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

new_file = drive.CreateFile({'title': args.file_name})
if args.content:
    new_file.SetContentString(args.content)
if args.local_file:
    new_file.SetContentFile(args.local_file)

new_file.Upload()
