#!/usr/bin/python3
"""
This file contains a scripts that packages and deploys a web_static
to my servers using Fabric
"""


import os
from fabric.api import local, run, put, env, sudo
from datetime import datetime


env.user = 'ubuntu'
env.hosts = ['34.204.95.239', '54.234.17.205']


def do_pack():
    """This function generates a .tgz archive"""
    local('mkdir -p versions')

    # generate the .tgz archive
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    a_path = 'versions/web_static_{}.tgz'.format(time)
    try:
        local('tar -czvf {} web_static'.format(a_path), capture=True)
        return a_path
    except Exception as e:
        print(f"Error: {e}")
        return None


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        # copy archive to server
        put(archive_path, "/tmp/")

        # extract the filename without extension
        filename = archive_path.split("/")[-1]
        name = filename.split(".")[0]

        # define the release directory using the extracted name
        release_dir = f"/data/web_static/releases/{name}/"

        # uncompress the archive to a folder
        run(f"mkdir -p {release_dir}")
        run(f"tar -xzf /tmp/{filename} -C {release_dir}")

        # remove archive
        run(f"rm /tmp/{filename}")

        # move files into the right directory
        run(f"mv {release_dir}/web_static/* {release_dir}")
        run(f"rm -rf {release_dir}/web_static")

        # set appropriate permissions for files and directories
        sudo(f"chmod -R 755 {release_dir}")
        sudo(f"chown -R www-data:www-data {release_dir}")

        # delete symbolic link from web server
        run("rm -rf /data/web_static/current")

        # create a symlink to new version of code
        run(f"ln -s {release_dir} /data/web_static/current")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def deploy():
    """Packs and deploys an archive to the web servers"""
    pack_result = do_pack()
    if not pack_result:
        return False
    return do_deploy(pack_result)
