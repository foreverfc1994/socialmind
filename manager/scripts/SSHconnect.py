import paramiko
from manager.scripts import SSHdata
class SSHsession():

    def __init__(self,vmid,user,pwd):
        if vmid == 'VM01':
            self.address = SSHdata.VM01_ADDR
        elif vmid == 'VM02':
            self.address = SSHdata.VM02_ADDR
        elif vmid == 'VM03':
            self.address = SSHdata.VM03_ADDR
        elif vmid == 'VM04':
            self.address = SSHdata.VM04_ADDR
        elif vmid == 'VM05':
            self.address = SSHdata.VM05_ADDR
        elif vmid == 'VM06':
            self.address = SSHdata.VM06_ADDR
        elif vmid == 'VM07':
            self.address = SSHdata.VM07_ADDR
        elif vmid == 'VM08':
            self.address = SSHdata.VM08_ADDR
        else:
            self.address = SSHdata.TEST_ADDR
        self.port = 22
        if user:
            self.username = user
        else:
            self.username = SSHdata.TEST_USER
        if pwd:
            self.password = pwd
        else:
            self.password = SSHdata.TEST_PWD
        self.session = self.sshconnect()

    def sshconnect(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.address, port=self.port, username=self.username, password=self.password)
        return ssh

    def excecommand(self,command):
        stdin, stdout, stderr = self.session.exec_command(command)
        for i in stdout.readlines():
            print(i)

    def sshclose(self):
        self.session.close()




