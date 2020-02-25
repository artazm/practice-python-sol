# Remove Duplicates


def remove_dup(new_list):
    return(set(new_list))

def remove_dups(dup_list):
    new_list = []
    for element in dup_list:
        if element not in new_list:
            new_list.append(element)
    return new_list

a = [1, 1, 1, 1, 1, 8, 8, 21, 21, 55, 89]

print(a[::-1])
print(remove_dup(a))

print(remove_dups(a))
