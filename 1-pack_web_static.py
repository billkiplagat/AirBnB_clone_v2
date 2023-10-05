#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""
from fabric import task
from datetime import datetime
import os


@task
def do_pack(c):
    # Create a directory to store the archives if it doesn't exist
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Create a timestamp for the archive name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Define the archive name
    archive_name = f"web_static_{timestamp}.tgz"

    # Create the .tgz archive from the web_static folder
    result = c.local(f"tar -cvzf versions/{archive_name} web_static")

    # Check if the archive creation was successful
    if result.failed:
        return None

    # Return the path to the created archive
    return f"versions/{archive_name}"
