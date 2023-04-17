def get_unique_list(input):
    output = []
    for i in input:
        if i not in output:
            output.append(i)
    return output

# Test
my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)