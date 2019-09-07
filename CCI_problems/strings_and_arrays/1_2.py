#Given two strings, determine if one is permutation of the other

#Time complexity O(n)

def check_permutation(s_1, s_2):
    if len(s_1) != len(s_2):
        return False

    set_1 = set(s_1)
    set_2 = set(s_2)

    difference = set_1.difference(set_2)

    return len(difference) == 0
