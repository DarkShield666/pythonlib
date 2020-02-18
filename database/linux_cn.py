#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko


class LinuxCn:
    def __init__(self, hostname: str, port: int, username: str, password: str):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname,
            port,
            username,
            password
        )

    def close_connect(self):
        self.client.close()

    def cmd_exec(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        print(stderr.read().decode())
        result = stdout.read().decode()
        print(result)


if __name__ == '__main__':
    t = LinuxCn('192.168.1.1', 22, 'root', '123456')
    command = "ls -al"
    t.cmd_exec(command)