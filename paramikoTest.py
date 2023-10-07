#!/usr/bin/python3
import paramiko
import os

local_project_path = '/home/bill/Dev/AirBnB_clone_v2/web_static'
remote_project_path = '/data/web_static/current'
# Define server information
# "nginx_config_path": "/etc/nginx/sites-available/default"
server_configs = [
    {
        'hostname': '35.175.130.26',
        'port': 22,
        'username': 'ubuntu',
        'password': '/home/bill/.ssh/id_rsa',
    },

    {
        'hostname': '54.158.191.169',
        'port': 22,
        'username': 'ubuntu',
        'password': '/home/bill/.ssh/id_rsa',
    },
]


def upload_folder_contents(local_path, remote_path, sftp):
    for item in os.listdir(local_path):
        local_item_path = os.path.join(local_path, item)
        remote_item_path = os.path.join(remote_path, item)
        if os.path.isfile(local_item_path):
            sftp.put(local_item_path, remote_item_path)
            print(f"Uploaded {item} to {remote_item_path}")
        elif os.path.isdir(local_item_path):
            sftp.mkdir(remote_item_path)
            upload_folder_contents(local_item_path, remote_item_path, sftp)


def upload_folder_to_server(server_config):
    try:
        # Create an SSH client instance
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        ssh.connect(
            server_config["hostname"],
            port=server_config["port"],
            username=server_config["username"],
            password=server_config["password"],
        )

        # Create an SFTP client instance
        sftp = ssh.open_sftp()

        # Upload the entire local folder and its contents to the remote directory
        upload_folder_contents(local_project_path, remote_project_path, sftp)

        # Close the SFTP and SSH connections
        sftp.close()
        ssh.close()

        print(f"Uploaded folder and its contents to {server_config['hostname']} successfully.")
    except Exception as e:
        print(f"Error uploading to {server_config['hostname']}: {str(e)}")


if __name__ == "__main__":
    for server_config in server_configs:
        upload_folder_to_server(server_config)
