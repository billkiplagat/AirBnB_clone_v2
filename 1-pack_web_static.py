#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Create a .tgz archive from web_static folder.
    """
    try:
        current_time = datetime.utcnow()
        file_name = "web_static_{}.tgz".format(current_time.strftime(
            "%Y%m%d%H%M%S"))
        local("mkdir -p versions")
        local("tar -czvf versions/{} web_static".format(file_name))
        return "versions/{}".format(file_name)
    except Exception as e:
        return None


if __name__ == "__main__":
    do_pack()
