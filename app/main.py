import sys
import os
import shutil
import random
import subprocess
from pathlib import Path

def parser(string, as_list = False):

    string_builder = str()
    result = []

    is_single_quoted = False
    is_double_quoted = False
    is_escaped = False

    for x, char in enumerate(string):

        if is_escaped:
            is_escaped = False
            continue
        
        if char == "'":
            if is_double_quoted:
                string_builder += char
            elif is_single_quoted:
                is_single_quoted = False
            else:
                is_single_quoted = True
            continue

        if char == '"':
            if is_single_quoted:
                string_builder += char
            elif is_double_quoted:
                is_double_quoted = False
            else:
                is_double_quoted = True
            continue

        if ord(char) == 92:
            if is_single_quoted:
                string_builder += char
            elif is_double_quoted:
                if string[x+1] in (chr(92), '$', '"'):
                    string_builder += string[x+1]
                    is_escaped = True
                else:
                    string_builder += char
            else:
                string_builder += string[x+1]
                is_escaped = True
            continue

        if not any([is_single_quoted, is_double_quoted]):

            if char == ' ':
                result.append(string_builder)
                string_builder = str()
            else:
                string_builder += char
        else:
            string_builder += char

    result.append(string_builder)

    while '' in result:
        result.remove('')

    if as_list:
        return result
    else:
        return ' '.join(result)


def main():

    command_list = ['exit', 'echo', 'type', 'pwd', 'cd']
    string_builder = ''
    is_redirecting = False

    print('$ ', end = '')

    while True:

        command = input().rstrip()

        command_full = parser(command).split(' ', 1)
        identifier = command_full[0]

        if command[0] in ("'", '"'):
            command_full = parser(command, as_list = True)
            command_full[0] = 'cat '
            command = ''.join(command_full)
            identifier = 'cat'

        match identifier:

            case 'exit':
                exit(int(command_full[1]))

            case 'echo':
                print(command_full[1])

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

            case 'cat':
                for filename in parser(command[3:], as_list = True):
                    try:
                        string_builder += open(filename).read()
                    except:
                        pass
                print(string_builder.rstrip())
                string_builder = ''

            case default:

                if '>' in command_full[1] or '1>' in command_full[1]:

                    command_full[1].replace('1>', '')
                    io = command_full[1].split('>')
                    input_file = io[0].strip()
                    output_file = io[1].strip()

                    if input_file[0] in ('"', '"'):
                        input_file = input_file[1:-1]
                        open(output_file, 'w').write(input_file)
                    else:
                        open(output_file, 'w').write(open(input_file, 'r').read())
                    
                elif identifier := shutil.which(identifier if identifier else ''):
                    subprocess.run(command_full)

                else:
                    print(f'{command}: command not found')
                
        print('$ ', end = '')


if __name__ == '__main__':
    main()
