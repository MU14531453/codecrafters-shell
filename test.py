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


print(parser("cat '/tmp/qux/f   15' '/tmp/qux/f   10' '/tmp/qux/f   70'", as_cat = True, as_list = True))