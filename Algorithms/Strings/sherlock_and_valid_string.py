def are_occ_equal(occ: dict):
    all_values = list(occ.values())
    for index in range(len(all_values) - 1):
        if all_values[index] != all_values[index + 1]:
            return False
    return True


def occ_state(occ: dict, check_el):
    if occ[check_el] == 0:
        del occ[check_el]
        return occ
    return occ


given_string = input()

occurrences = {}

for char in set(given_string):
    occurrences[char] = given_string.count(char)

if are_occ_equal(occurrences):
    print('YES')

else:
    max_element_data = tuple(
        {char: value for char, value in occurrences.items() if value == max(occurrences.values())}.keys())
    min_element_data = tuple(
        {char: value for char, value in occurrences.items() if value == min(occurrences.values())}.keys())

    occurrences[max_element_data[0]] -= 1
    if are_occ_equal(occ_state(occurrences, max_element_data[0])):
        print('YES')
        exit(0)

    occurrences[max_element_data[0]] += 1
    occurrences[min_element_data[0]] -= 1
    if are_occ_equal(occ_state(occurrences, min_element_data[0])):
        print('YES')
        exit(0)

    print('NO')
