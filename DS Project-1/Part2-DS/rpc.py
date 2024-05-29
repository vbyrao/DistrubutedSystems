import threading
from xmlrpc.server import SimpleXMLRPCServer
from server import sync_folder


def server_thread():
    serv = SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True)
    serv.register_function(sync_folder, "sync_folder")
    serv.serve_forever()


serv_thread = threading.Thread(target=server_thread)
serv_thread.start()
