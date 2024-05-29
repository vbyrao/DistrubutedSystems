import xmlrpc.client


def client_thread(source, dest):
    client = xmlrpc.client.ServerProxy("http://localhost:8000/")
    client.sync_folder(source, dest)


while 1:
    client_thread("./src", "./dst")
