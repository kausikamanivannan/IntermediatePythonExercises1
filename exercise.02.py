def get_combined_dict(dict_1, dict_2):
    combined = {}
    for i in dict_1:
        if i in dict_2:
            combined[i] = dict_1[i] + dict_2[i]
    return combined

# Test
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)