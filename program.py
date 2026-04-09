def plus_one(digits):
    n =len(digits)
    for i in range(n- 1,-1,-1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
    
num =[1, 2, 3]
result = plus_one(num)
print(result)