import sys


def main():

    command_list = []
    
    sys.stdout.write('$ ')


    while True:
        command = input()

        if command not in command_list:
            print(f'{command}: command not found')
        else:
            pass

        sys.stdout.write('$ ')


if __name__ == '__main__':
    main()
