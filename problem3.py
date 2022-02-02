max_len = 0
s = 'ujiedfjfrbhzamdwjjpgepd'
curr_string = s[0]
substrings = []
for i in range(len(s)):
    if i != 0 and i < len(s) - 1:
        if curr_string[-1] <= s[i]:
            curr_string += s[i]
        elif curr_string[-1] > s[i]:
            substrings.append(curr_string)
            curr_string = s[i]
    elif i == 0:
        continue
    elif i == len(s) - 1 and s[-1] < curr_string[-1]:
        substrings.append(curr_string)
    else:
        curr_string += s[i]
        substrings.append(curr_string)
for word in substrings:
    if len(word) > max_len:
        max_len = len(word)
        long_word = word
print("Longest substring in alphabetical order is:", long_word)