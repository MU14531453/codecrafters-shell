import sys
import os
import shutil
import random
import subprocess

def get_command_name(command, command_list):

    pass

def main():

    command_list = ['exit', 'echo', 'type', 'PATH', 'pwd', 'cd']
    
    sys.stdout.write('$ ')


    while True:

        command = input()

        command_full = command.split(' ')
        identifier = command_full[0]

        match identifier:

            case 'exit':
                exit(int(command_full[1]))

            case 'echo':
                sys.stdout.write(command.split(' ', 1)[1])

            case 'type':
                if command_full[1].strip() in command_list:
                    sys.stdout.write(f'{command_full[1]} is a shell builtin')
                elif PATH := shutil.which(command_full[1] if command_full[1] else ''):
                    sys.stdout.write(f'{command_full[1]} is {PATH}')
                else:
                    sys.stdout.write(f'{command_full[1]}: not found')

            case 'pwd':
                sys.stdout.write(os.getcwd())

            case 'cd':
                pass

            case default:

                if command := shutil.which(command_full[1] if command_full[1] else ''):
                    ret = subprocess.run(command)
                    sys.stdout.write(ret.stdout)
                else:
                    sys.stdout.write(f'{command}: command not found')
                
        sys.stdout.write('\n$ ')


if __name__ == '__main__':
    main()
