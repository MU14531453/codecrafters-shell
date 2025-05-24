import sys
import os
import shutil
import random
import subprocess
from pathlib import Path
from copy import copy
import time
#git statusimport readline

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

def check_for_file_to_write(command):

    write_list = ['>', '1>', '2>', '>>', '1>>', '2>>']

    if any([x for x in command if x in write_list]):
        io_splitter = command.replace('1>', '>').split('>')
        write_command = io_splitter[0]
        output_file = io_splitter[1]
    else:
        return (command, None)

    return (write_command, output_file)


def write_to(file, text, append = False):

    filepath = file[::-1].split(chr(47), 1)[1][::-1]
    file_name = file[::-1].split(chr(47), 1)[0][::-1]

    os.chdir(filepath.strip())

    open(file_name, 'r'*append + 'w').write(str(text))

    return None


def main():

    command_list = ['exit', 'echo', 'type', 'pwd', 'cd']
    string_agg = ''

    print('$ ', end = '')

    while True:

        output_file = None
        string_agg = ''

        command = input().rstrip()
        command_foo = copy(command)

        command, output_file = check_for_file_to_write(command)

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
                if output_file:
                    write_to(output_file, command_full[1])
                else:
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
            
            case 'fdasfdasdfdafdaadfsfdasadfsadfs':
                _a = """
            case 'cat':

                if not output_file:
                    for filename in parser(command[3:], as_list = True):
                        try:
                            #string_agg += (open(filename).read() + '\n')
                            print(open(filename).read())
                        except:
                            pass
                    #string_agg = string_agg.rstrip()
                
                else:
                    for filename in parser(command[3:], as_list = True):
                        try:
                            string_agg += (open(filename).read() + '\n')
                        except:
                            pass
                    string_agg = string_agg.rstrip()
                    write_to(output_file, string_agg)
                    output_file = None

                string_agg = ''
        
            case 'ls':
                if not output_file:
                    subprocess.run([command], shell = True)
                else:
                    call = command.strip().split(' ')
                    file_list = os.listdir(call[-1])
                    file_list = sorted([f for f in file_list], key = lambda x: os.path.getmtime(call[-1] + chr(47) + x))
                    #print('file_list:', file_list)
                    write_to(output_file, '\n'.join(file_list))
                    output_file = None
            """
            case default:
                    
                if identifier := shutil.which(identifier if identifier else ''):
                    
                    if output_file is not None:
                        res = subprocess.run(' '.join(command_full), shell = True, stdout = subprocess.DEVNULL)
                        write_to(output_file, res)
                    else:
                        res = subprocess.run(' '.join(command_full), shell = True)

                else:
                    print(f'{command}: command not found')
                
        print('$ ', end = '')


if __name__ == '__main__':
    main()
