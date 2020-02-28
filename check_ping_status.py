#!/bin/python3
import subprocess
import platform

operating_sys = platform.system()
IP_ADDRESS = '172.217.160.14'


def ping(ip):

    ping_command = ['ping', ip, '-n', '1'
                    ] if operating_sys == 'Windows' else ['ping', ip, '-c 1']
    shell_needed = True if operating_sys == 'Windows' else False

    ping_output = subprocess.run(ping_command,
                                 shell=shell_needed,
                                 stdout=subprocess.PIPE)
    success = ping_output.returncode
    return True if success == 0 else False


result = ping(IP_ADDRESS)

if result:
    print("Server is up.")
else:
    print("Server is down.")
