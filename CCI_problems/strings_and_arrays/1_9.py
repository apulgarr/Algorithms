#String rotation: check if s_1 is a rotation of s_2 ej: (waterbottle is a rotation of terbottlewa)

#Time complexity: O(n)

def is_rotation(s_1, s_2):
    if len(s_1) == 0 and len(s_2):
        return 0

    if len(s_1) != len(s_2):
        return False

    s_2 = s_2 * 2

    return s_1 in s_2
