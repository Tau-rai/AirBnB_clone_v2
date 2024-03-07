#!/usr/bin/python3
"""
This file contains a script that distribute an archive to my web servers
using the function do_deploy
"""


import os
from fabric.api import put, run, env, sudo


env.user = 'ubuntu'
env.hosts = ['34.204.95.239', '54.234.17.205']


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
        run(f"mv -n {release_dir}/web_static/* {release_dir}")
        run(f"rm -rf {release_dir}/web_static")

        # set appropriate permissions for files and directories
        sudo(f"chmod -R 755 {release_dir}")
        sudo(f"chown -R www-data:www-data {release_dir}")

        # delete symbolic link from web server
        run("rm -rf /data/web_static/current")

        # create a symlink to new version of code
        run(f"ln -s {release_dir} /data/web_static/current")
        return True
    except:
        return False
