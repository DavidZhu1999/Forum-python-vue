import os
import base64


def upload_file(username, filename, file):
    if not os.path.exists(f'../netdisk/{username}'):
        os.mkdir(f'../netdisk/{username}')
    with open(f'../netdisk/{username}/{filename}', 'wb') as f:
        f.write(base64.b64decode(file))
    return 1


def download_file(username, filename):
    return base64.b64encode(open(f'../netdisk/{username}/{filename}', 'rb').read())
