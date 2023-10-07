#!/usr/bin/python3
import paramiko
import os

local_project_path = '/home/bill/Dev/personal BnB/AirBnB_clone_v2/web_static/103-index.html'
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


def upload_project_to_server(server_config):
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

        # Upload the project folder to the server
        sftp.put(local_project_path, os.path.join(remote_project_path, os.path.basename(local_project_path)))

        # Close the SFTP and SSH connections
        sftp.close()
        ssh.close()

        print(f"Uploaded project to {server_config['hostname']} successfully.")
    except Exception as e:
        print(f"Error uploading to {server_config['hostname']}: {str(e)}")


if __name__ == "__main__":
    for server_config in server_configs:
        upload_project_to_server(server_config)
