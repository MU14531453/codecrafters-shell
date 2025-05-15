
import subprocess
import os

def write_foo(command):

    command_sp = command.split('>')

    os.system(command_sp[0])

    return None

subprocess.run(['echo', 'csadcad'])