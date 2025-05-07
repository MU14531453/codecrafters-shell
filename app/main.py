import sys


def main():

    command_list = ['exit']
    
    sys.stdout.write('$ ')


    while True:
        command = input()

        if command not in command_list:
            print(f'{command}: command not found')
        else:
            match command[:command.index(' ')]:
                case 'exit':
                    exit(int(command[command.index(' ')+1:]))
                case default:
                    return -1

        sys.stdout.write('$ ')


if __name__ == '__main__':
    main()
