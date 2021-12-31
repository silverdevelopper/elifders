# 0 1 2 3 4 5
# 10 45 67 3 98
"""
my_list = [10,45,67,3,98]
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(my_list[a] // my_list[b])
    
"""
def pow(x,y):
    # base condtional
    if y == 0:
        return 1
    return x*pow(x,y-1)

'''
    pow(3,4)
    
  pow(3,4)= 3*pow(3,3)
  pow(3,3)= 3* pow(3,2)
  pow(3,2)= 3*pow(3,1)
  pow(3,1)= 3*pow(3,0)
  pow(3,0)= 1
'''
def sum(int_list:list):
    if len(int_list) == 0:
        return 0
    return int_list[0] + sum(int_list[1:])

#print(sum([19,5,6]))

def luhn_sum_double(n:int):
    #Return the Luhn sum of n, doubling the last digit. all_but_last, last = split(n)
    last = int(str(n)[-1])*2
    all_but_last = [int(x) for x in str(n)]
    all_but_last.pop()
    x = all_but_last.copy()
    x.push(last)
    luhn_digit = sum(x)
    if n < 10:
        return luhn_digit 
    else:
        return luhn_sum(all_but_last) + luhn_digit

def luhn_sum(n):
#Return the digit sum of n computed by the Luhn algorithm if n < 10:
    if n <10:
        return n 
    else:
        all_but_last, last = int(str(n)[-1]),int(str(n)[:-1])
        return luhn_sum_double(all_but_last) + last
