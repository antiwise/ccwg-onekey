import paramiko
import os

ip = '远程服务器ip'
port = 端口
username = '帐号'
password = '密码'

cwd = os.getcwd()

def sftp(src, dest):
	"""
	上传压缩包到服务端
	"""
	transport = paramiko.Transport((ip, port))
	transport.connect(username = username, password = password)
	sftp = paramiko.SFTPClient.from_transport(transport)
	sftp.put(src, dest)
	sftp.close()
	return True

def ssh_exec_command(commands):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname = ip, port = port, username = username, password = password)

	for command in commands:
		stdin, stdout, stderr = ssh.exec_command(command)
		print(stdout.read().decode())
		print(stderr.read().decode())
	ssh.close()

# 先上传文件到服务端
# 然后解压缩文件
resPath = os.path.join(cwd, "res.zip")
if sftp(resPath, '/home/game/gameres/res.zip'):
	ssh_exec_command(['cd /home/game/gameres; sh unzip.sh'])
	print('success')

"""
unzip.sh
rm -rf res
unzip res.zip -d .
"""