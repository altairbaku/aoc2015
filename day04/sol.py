from hashlib import md5

def find_hash(leading_zeroes,key):
    leading_string = '0' * leading_zeroes
    i = 1
    while True:
        str2hash = key + str(i)
        result =  md5(str2hash.encode())
        if result.hexdigest()[:leading_zeroes] == leading_string:
            break
        i+=1
    return i

secret_key = 'bgvyzdsv'
print(find_hash(5,secret_key))
print(find_hash(6,secret_key))



