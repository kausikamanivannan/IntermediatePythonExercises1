def return_letter_count(string):
    letter_amt = {}
    for letter in string.lower():
        if letter.isalpha():
            if letter in letter_amt:
                letter_amt[letter] += 1
            else:
                letter_amt[letter] = 1
    return letter_amt

user_string = str(input("Enter a string; "))
letter_count = return_letter_count(user_string)
print(letter_count)