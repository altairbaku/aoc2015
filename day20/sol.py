import math as m

puzzle_input = 34000000
 
# Returns sum of all factors of n.
def sumofFactors(n):
    res = 1
    for i in range(2, int(m.sqrt(n) + 1)):
         
        curr_sum = 1
        curr_term = 1
         
        while n % i == 0:
             
            n = n / i
 
            curr_term = curr_term * i
            curr_sum += curr_term
             
        res = res * curr_sum

    if n > 2:
        res = res * (1 + n)
 
    return res

def sumofFactorsp2(n):
    result = 0
    for i in range(2,(int)(m.sqrt(n))+1):
        if n % i == 0:
            if (i == (n/i) and i >= int(n/50)):
                result = result + i
            else:
                left = i
                right = n//i
                if left >= int(n/50):
                    result = result + left
                if right >= int(n/50):
                    result = result + right
    return (result+n) * 11
 
num = 750000
while True:
    sum = sumofFactors(num)
    if sum >= puzzle_input/10:
        print(num)
        break
    num += 1

num = 800000
while True:
    sum = sumofFactorsp2(num)
    if sum >= puzzle_input:
        print(num)
        break
    num += 1
