import os
import tarfile
import datetime

SOURCE_DIR = "/path/to/source"
DEST_DIR = "/path/to/destination"
BACKUP_NAME = f"backup_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.tar.gz"

with tarfile.open(os.path.join(DEST_DIR, BACKUP_NAME), "w:gz") as tar:
    tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))

if os.path.exists(os.path.join(DEST_DIR, BACKUP_NAME)):
    print(f"Backup successful: {os.path.join(DEST_DIR, BACKUP_NAME)}")
else:
    print("Backup failed")

