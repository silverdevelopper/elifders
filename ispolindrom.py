'''
    123421
'''
def get_digts_list(n:int):
    l:list = []
    while n//10 != 0:
        l.append(n%10)
        n = n//10
    l.append(n%10)
    l.reverse()
    return l
# 343
# 35444453

def is_polindrom_helper(dig_list:list):
    if len(dig_list) <  2:
        return True
    if dig_list[0] == dig_list[-1]:
        return True and is_polindrom_helper(dig_list[1:-1])
    else:
        return False
def is_polindrom(n:int):
    return is_polindrom_helper(get_digts_list(n))

print(is_polindrom(1233421))

