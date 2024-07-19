#!/bin/bash

SOURCE_DIR="/path/to/source"
DEST_DIR="/path/to/destination"
BACKUP_NAME="backup_$(date +%Y%m%d%H%M%S).tar.gz"

tar -czf $DEST_DIR/$BACKUP_NAME $SOURCE_DIR

if [ $? -eq 0 ]; then
  echo "Backup successful: $DEST_DIR/$BACKUP_NAME"
else
  echo "Backup failed"
fi

