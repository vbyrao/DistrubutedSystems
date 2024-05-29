import xmlrpc.server
import os
from pathlib import Path

DROPBOX_DIR = "./server_files/"

upload_file = lambda x, y: open(DROPBOX_DIR + x, "a").write(y)

download_file = lambda x: (Path(os.path.join(DROPBOX_DIR, x)).read_bytes() if Path(os.path.join(DROPBOX_DIR, x)).is_file() else False)

delete_file = lambda x: (Path(os.path.join(DROPBOX_DIR, x)).unlink() if Path(os.path.join(DROPBOX_DIR, x)).is_file() else False)
try:
    rename_file = lambda old, new: (Path(os.path.join(DROPBOX_DIR, old)).rename(Path(os.path.join(DROPBOX_DIR, new))) if Path(os.path.join(DROPBOX_DIR, old)).is_file() else False)
except:
    print()


def add(a, b):
    return a + b

def sort(lst):
    return sorted(lst)

server = xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000),allow_none=True)
server.register_function(add, "add")
server.register_function(upload_file, "upload")
server.register_function(download_file, "download")
server.register_function(delete_file, "delete")
server.register_function(rename_file, "rename")
server.register_function(sort, "sort")
server.serve_forever()





