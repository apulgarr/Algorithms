#Determine if a string has all unique characters

#Solution 1
#Time complexity O(n)

def has_unique_characters(string):
    string = string.lower()

    if len(string) == 1 or len(set(string) == 1):
        return string

    chars_unique = {}

    for char in string:
        if char not in chars_unique.keys():
            chars_unique[char] = True

        else:
            return False

    return True


#Solution 2, without data structures
#Time complexity O(n^2)

def has_unique_characters_2(string):
    string = string.lower()

    if len(string) == 1 or len(set(string)) == 1:
        return True

    start_pos = 1

    for char in string:
        for pos_j in range(start_pos, len(string)):
            if char == string[pos_j]:
                return False

        start_pos += 1

    return True
