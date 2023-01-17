with open('input.txt') as f:
    lines = f.readlines()

forbidden_strings = ['ab','cd','pq','xy']
nice_strings_p1 = 0
nice_strings_p2 = 0
for string in lines:
    string_len = len(string.strip())
    vowel_count = sum([1 for x in range(string_len) if string[x] in 'aeiou'])
    pair_count = sum([string[n] == string[n+1] for n in range(string_len-1)])
    forbidden_count = sum([string[n:n+2] in forbidden_strings for n in range(string_len-1)])
    nice_strings_p1 += 1 if(vowel_count >= 3 and pair_count >= 1 and forbidden_count == 0) else 0

    count_1 = sum([1 for n in range(string_len-2) if string[n:n+2] in string[n+2:]])
    count_2 = sum([1 for n in range(string_len-2) if string[n] == string[n+2]])
    nice_strings_p2 += 1 if (count_1 and count_2) else 0
    
print(nice_strings_p1)
print(nice_strings_p2)
