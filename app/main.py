import sys
import shutil

def get_command_name(command, command_list):

    pass

def main():

    command_list = ['exit', 'echo', 'type', 'PATH']
    PATH = []
    
    sys.stdout.write('$ ')


    while True:

        command = input()

        command_full = command.split(' ')
        identifier  = command_full[0]

        if identifier not in command_list:
            sys.stdout.write(f'{command}: command not found')
        else:
            match identifier:

                case 'exit':
                    exit(int(command_full[1]))

                case 'echo':
                    sys.stdout.write(command_full[1])

                case 'type':
                    if command_full[1].strip() in command_list:
                        sys.stdout.write(f'{command_full[1]} is a shell builtin')
                    elif PATH and PATH in shutil.which(command_full[1]):
                        sys.stdout.write(f'{command_full[1]} is {PATH}')
                    else:
                        sys.stdout.write(f'{command_full[1]}: not found')
                
                case 'PATH':
                    PATH.append(command_full[1])

                case default:
                    return -1

        sys.stdout.write('\n$ ')


if __name__ == '__main__':
    main()
