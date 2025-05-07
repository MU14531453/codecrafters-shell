import sys


def main():

    command_list = ['exit']
    
    sys.stdout.write('$ ')


    while True:
        command = input()

        if ' ' in command:
            temp = command.split(' ')
            identifier  = temp[0]
            arguments = temp[1]
        else:
            identifier = command
            arguments = ''

        if identifier not in command_list:
            print(f'{command}: command not found')
        else:
            match identifier:
                case 'exit':
                    exit(int(arguments))
                case default:
                    return -1

        sys.stdout.write('$ ')


if __name__ == '__main__':
    main()
