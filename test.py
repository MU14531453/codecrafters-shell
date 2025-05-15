
import subprocess
import os

def write_foo(command):

    command_sp = command.split('>')

    subprocess.run(command_sp[0])

    return None

os.system('echo cwel')
#subprocess.call('echo cwel')
#subprocess.run(['dir', os.getcwd()], shell = True)