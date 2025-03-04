def fn1(s):
    rev = ""
    for char in s:
        rev = char + rev  
    return rev

def fn2(s):
    return s == fn1(s) 

def fn3(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
