#!/usr/bin/python3
"""
This Fabric file generates a .tgz archive from the contents  of the
web_static folder
"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """This function generates a .tgz archive"""
    local('mkdir -p versions')

    # generate the .tgz archive
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    a_path = 'versions/web_static_{}.tgz'.format(time)
    result = local('tar -czvf {} web_static'.format(a_path), capture=False)

    # if successful return the archive path
    if result.succeeded:
        return a_path
    else:
        return None
