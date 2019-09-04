def string_compression(string):
    if len(string) == 0:
        return 0

    if len(string) == 1:
        return string + "1"

    count = 1
    curr_char = string[0]
    new_str = ""

    for pos in range(1,len(string)):
        if curr_char == string[pos]:
            count += 1

            if pos == len(string) - 1:
                new_str += "%s%d" % (curr_char, count)

        else:
            new_str += "%s%d" % (curr_char, count)
            count = 1
            curr_char = string[pos]


    if len(new_str) < len(string):
        return new_str

    return string

print(string_compression(''))
