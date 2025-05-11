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

print(parser('"hello'script'\\n'world"'))