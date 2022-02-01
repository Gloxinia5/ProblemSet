s = "askdjfhlkjshadbobkjashdfbob"
y = "bob"
temp_word = ""
bob_count = 0
for i in range(len(s)):
    if i <= (len(s) - len(y)):
        temp_word = ""
        for j in range(len(y)):
            temp_word += s[i+j]
        if temp_word == y:
            bob_count += 1
    else:
        i -= 2
print("Number of times bob occurs is: ", bob_count)