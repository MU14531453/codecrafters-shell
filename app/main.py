import sys


def main():

    command_list = ['exit', 'echo', 'type']
    
    sys.stdout.write('$ ')


    while True:
        command = input()

        if ' ' in command:
            temp = command.split(' ', 1)
            identifier  = temp[0]
            arguments = temp[1]
        else:
            identifier = command
            arguments = ''

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
                    else:
                        sys.stdout.write(f'{arguments}: not found')
                case default:
                    return -1

        sys.stdout.write('\n$ ')


if __name__ == '__main__':
    main()
