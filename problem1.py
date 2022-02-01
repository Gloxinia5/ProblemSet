# Paste your code into this box
vowel = "aeiou"
s = "asdfasdfasdf"
vowel_count = 0
for i in range(len(vowel)):
    for j in range(len(s)):
        if vowel[i] == s[j]:
            vowel_count += 1
print("Number of vowels:", vowel_count)