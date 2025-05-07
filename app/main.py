import sys
import shutil

def get_command_name(command, command_list):

    pass

def main():

    command_list = ['exit', 'echo', 'type', 'PATH']
    PATH = ''
    
    sys.stdout.write('$ ')


    while True:
        command = input()

        identifier  = command[:4]
        arguments = command[4:]

        if identifier not in command_list:
            sys.stdout.write(f'{command}: command not found')
        else:
            match identifier:

                case 'exit':
                    exit(int(arguments))

                case 'echo':
                    sys.stdout.write(arguments)

                case 'type':
                    if arguments.strip() in command_list:
                        sys.stdout.write(f'{arguments} is a shell builtin')
                    elif PATH and PATH in shutil.which(arguments):
                        sys.stdout.write(f'{arguments} is {PATH}')
                    else:
                        sys.stdout.write(f'{arguments}: not found')
                
                case 'PATH':
                    PATH = arguments

                case default:
                    return -1

        sys.stdout.write('\n$ ')


if __name__ == '__main__':
    main()
