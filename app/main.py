import sys
import os
import shutil
import random
import subprocess
from pathlib import Path

def single_quote(string):
    if string[0] == string[-1] == "'":
        return string[1:-2]
    else:
        return string

def main():

    command_list = ['exit', 'echo', 'type', 'pwd', 'cd']
    string_builder = ''
    
    print('$ ', end = '')

    while True:

        command = input().rstrip()

        command_full = command.split(' ')
        identifier = command_full[0]

        for x, argument in enumerate(command_full):
            if x:
                command_full[x] = single_quote(argument)

        match identifier:

            case 'exit':
                exit(int(command_full[1]))

            case 'echo':
                print(command.split(' ', 1)[1])

            case 'type':
                if command_full[1].strip() in command_list:
                    print(f'{command_full[1]} is a shell builtin')
                elif PATH := shutil.which(command_full[1] if command_full[1] else ''):
                    print(f'{command_full[1]} is {PATH}')
                else:
                    print(f'{command_full[1]}: not found')

            case 'pwd':
                print(os.getcwd())

            case 'cd':
                if command_full[1] == '~':
                    os.chdir(Path.home())
                else:
                    try:
                        os.chdir(command_full[1])
                    except FileNotFoundError:
                        print(f'cd: {command_full[1]}: No such file or directory')

            case default:
                if identifier := shutil.which(identifier if identifier else ''):
                    subprocess.run(command_full)
                else:
                    print(f'{command}: command not found')
                
        print('$ ', end = '')


if __name__ == '__main__':
    main()
