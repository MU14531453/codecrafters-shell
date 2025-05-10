import sys
import os
import shutil
import random
import subprocess
from pathlib import Path

def parser(string, as_list = False, as_cat = False):

    string_builder = str()
    result = []

    is_single_quoted = False
    is_double_quoted = False

    for x, char in enumerate(string):
        
        if char == "'":
            if is_double_quoted:
                string_builder += char
            elif is_single_quoted:
                #result.append(string_builder)
                #string_builder = str()
                is_single_quoted = False
                continue
            else:
                is_single_quoted = True
                continue

        if char == '"':
            if is_single_quoted:
                string_builder += char
            elif is_double_quoted:
                #result.append(string_builder)
                #string_builder = ''
                is_double_quoted = False
                continue
            else:
                is_double_quoted = True
                continue

        if not any([is_single_quoted, is_double_quoted]):

            if char == ' ' or string == chr(92):
                result.append(string_builder)
                string_builder = str()
            else:
                string_builder += char
        elif is_double_quoted:
            if ord(char) == 92:
                if (len(string) - x):
                    if string[x+1] in ('$', chr(92), '"', '\n'):
                        string_builder += char
            else:
                string_builder += char
        else:
            string_builder += char

    result.append(string_builder)

    while '' in result:
        result.remove('')

    if as_cat:
        for x, element in enumerate(result):
            while result[x][-1] == ' ' or result[x][-1].isnumeric():
                result[x] = result[x][:-1]

    if as_list:
        return result
    else:
        return ' '.join(result)


def main():

    command_list = ['exit', 'echo', 'type', 'pwd', 'cd']
    
    print('$ ', end = '')

    while True:

        command = input().rstrip()

        command_full = command.split(' ', 1)
        identifier = command_full[0]

        command_full[1] = parser(command_full[1])

        match identifier:

            case 'exit':
                exit(int(command_full[1]))

            case 'echo':
                print(parser("'" + command_full[1] + "'"))

            case 'type':
                if command_full[1].strip() in command_list:
                    print(f'{command_full[1]} is a shell builtin')
                elif PATH := shutil.which(command_full[1] if command_full[1] else ''):
                    print(f'{command_full[1]} is {PATH}')
                else:
                    print(f'{command_full[1]}: not found')

            case 'pwd':
                print(os.getcwd())

            case 'cd':
                if command_full[1] == '~':
                    os.chdir(Path.home())
                else:
                    try:
                        os.chdir(command_full[1])
                    except FileNotFoundError:
                        print(f'cd: {command_full[1]}: No such file or directory')

            #case 'cat':
            #    file_list = parser(command_full[1], as_cat = True, as_list = True)
            #    for f in file_list:
            #        subprocess.run(identifier + ' ' + f)

            case default:
                if identifier := shutil.which(identifier if identifier else ''):
                    subprocess.run(command_full)
                else:
                    print(f'{command}: command not found')
                
        print('$ ', end = '')


if __name__ == '__main__':
    main()
