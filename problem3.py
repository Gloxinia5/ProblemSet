alpha_order = "abcdefghijklmnopqrstuvwxyz"
s = 'asldkfjlaskdjf'
curr_string = ""
substrings = []
char_index = 0

for i in range(len(s)):
    if i < len(s)-1:
        if alpha_order.index(s[i]) >= char_index and not(alpha_order.index(s[i]) > alpha_order.index(s[i + 1])):
            char_index = alpha_order.index(s[i])
            curr_string += s[i]
        elif alpha_order.index(s[i + 1]) < alpha_order.index(s[i]):
            char_index = 0
            curr_string += s[i]
            substrings.append(curr_string)
            curr_string = ""
        else:
            char_index = 0
            substrings.append(curr_string)
            curr_string = ""
    else:
        curr_string += s[i]
        substrings.append(curr_string)
        break
long = substrings[0]
for j in range(len(substrings)):

    if j < len(substrings) - 1:
        if len(long) < len(substrings[j]):
            long = substrings[j]
        else:
            long = long
    else:
        if len(long) < len(substrings[j]):
            long = substrings[j]
        else:
            long = long
            break
print("Longest substring in alphabetical order is: ", long)
