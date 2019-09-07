#Replace all the white spaces with '%20'

#Time complexity O(n)

def fill_spaces(string):
    count = 0
    aux_str = ""

    for char in string:
        if char == " ":
            aux_str += '20%'

        else:
            aux_str += char
            count += 1

    return aux_str, count
