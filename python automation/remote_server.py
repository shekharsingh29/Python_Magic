import paramiko

# Paramiko is a module used to handle remote operation

ssh  = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.4', port= 22,username='root', password='google')
stdin, stdout, stderr = ssh.exec_command('whoami')
stdin1, stdout1, stderr1 = ssh.exec_command('free -m')

print(f'The user on the remote server is {stdout.readlines()}')
print(f'The remote servers RAM consumption is {stdout1.readlines()}')

# opening sftp connection to transfer file

sftp_client = ssh.open_sftp()
sftp_client.put('git_bash_version.py','/home/ssingh/newFile.py')

#close all connection
sftp_client.close()
ssh.close()