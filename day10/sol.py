num = "1321131112"

valid_rights = ['111','132','311','312']

def look_and_say(num,repeats,repetitions):

    cur_char = num[0]
    cur_count = 0
    i = 0
    new_num = ''
    while True:
        while i < len(num) and num[i] == cur_char:
            cur_count += 1
            i += 1
        new_num = new_num + str(cur_count) + str(cur_char)
        if i >= len(num):
            break
        cur_char = num[i]
        cur_count = 0

    if repeats == repetitions:
        return num

    num_len = int(len(new_num)/2)
    if new_num[num_len-1] == '2' and new_num[num_len : num_len+3] in valid_rights:
        left = look_and_say(new_num[:num_len],repeats+1,repetitions)
        right = look_and_say(new_num[num_len:],repeats+1,repetitions)
        new_num = left+right
    else:
        new_num = look_and_say(new_num,repeats+1,repetitions)

    return new_num

print(len(look_and_say(num,0,50)))