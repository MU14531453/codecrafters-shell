import sys


def main():

    command_list = []
    
    sys.stdout.write('$ ')

    command = input()

    if command not in command_list:
        print(f'{command}: command not found')


if __name__ == '__main__':
    main()
