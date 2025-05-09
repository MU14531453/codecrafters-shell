import sys
import os
import shutil
import random
import subprocess

def main():

    command_list = ['exit', 'echo', 'type', 'pwd', 'cd']
    
    sys.stdout.write('$ ')

    while True:

        command = input().rstrip()

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

                if identifier := shutil.which(identifier if identifier else ''):
                    print(command_full)
                    subprocess.run(command_full)
                else:
                    sys.stdout.write(f'{command}: command not found')
                
        sys.stdout.write('\n$ ')


if __name__ == '__main__':
    main()
