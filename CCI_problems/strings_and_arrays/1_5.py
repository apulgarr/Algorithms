#Given two string, write a function to check if they are one edit or zero edit

#Time complexity: O(min(a,b))

def check_edits(s_1, s_2):
    edits = abs(len(s_1) -  len(s_2))

    if edits >= 2:
        return False

    long_s = s_1.lower() if len(s_1) >= len(s_2) else s_2.lower()
    short_s = s_2.lower() if len(s_2) < len(s_1) else s_1.lower()
    index = 0

    while index < len(short_s):
        if long_s[index] != short_s[index]:
            edits += 1

            if edits >= 2:
                return False

        index += 1


    return True
