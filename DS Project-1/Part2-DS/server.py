import os


def sync_folder(src, dst):
    source_files = set(os.listdir(src))
    dest_files = set(os.listdir(dst))

    for item in source_files:
        src = os.path.join(src, item)
        dest = os.path.join(dst, item)
        if os.path.isdir(src):
            if not os.path.exists(dest):
                os.makedirs(dest)
            sync_folder(src, dest)
        else:
            if not os.path.exists(dest) or os.stat(src).st_mtime - os.stat(dest).st_mtime > 1:
                with open(src, 'rb') as fsrc:
                    with open(dest, 'wb') as fdst:
                        fdst.write(fsrc.read())

    for item in dest_files - source_files:
        dest = os.path.join(dst, item)
        if os.path.isfile(dest):
            os.remove(dest)
        elif os.path.isdir(dest):
            os.rmdir(dest)
