import paramiko
client = paramiko.SSHClient()
client.connect('51.79.203.153', username='Administrator', password='Hk@hjjhejh878')
stdin, stdout, stderr = client.exec_command('ls -l')