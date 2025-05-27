
def check_for_file_to_write(command):

    write_list = ['>', '1>', '2>', '>>', '1>>', '2>>']

    append = bool(command.count('>') - 1)

    for x, symbol in enumerate(command):
        if symbol == '>' and x:
            if command[x-1] == '2':
                err_flag = True
                break
            else:
                err_flag = False
    
    if any([x for x in command if x in write_list]):
        io_splitter = command.replace('1>', '>').replace('2>', '>').replace('>>', '>').split('>')
        write_command = io_splitter[0]
        output_file = io_splitter[1]
    else:
        return (command, None, False, False)

    return (write_command, output_file, append, err_flag)

print(check_for_file_to_write('ls -1 nonexistent 2>> /tmp/quz/foo.md'))