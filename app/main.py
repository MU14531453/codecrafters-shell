import sys
import os
import shutil
import random
import subprocess

def main():

    command_list = ['exit', 'echo', 'type', 'pwd', 'cd']
    
    print('$ ')

    while True:

        command = input().rstrip()

        command_full = command.split(' ')
        identifier = command_full[0]

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
                pass

            case 'cd':
                pass

            case default:

                if identifier := shutil.which(identifier if identifier else ''):
                    subprocess.run(command_full)
                    #print('test')
                else:
                    print(f'{command}: command not found')
                
        print('$  ')


if __name__ == '__main__':
    main()
