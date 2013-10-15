'''

input: a digit number
output: find the next palindrome

'''

def nextpal(n):
    s = str(n);
    
    if (n < 9):
        return n + 1
    if (n == 9):
        return 11
    front = s[0: len(s) / 2]
    mid = s[len(s)/2: len(s)/2 + len(s) % 2]
    end = s[len(s)/2 + len(s) % 2 :]
    
    if (end <= front[::-1]):
        return int(front + mid + front[::-1])
    
    if (mid != "" and mid != "9"):
        return int(front + str(int(mid) + 1) + front[::-1])
    
    front = str(int(front) + 1)
    if (mid):
        return int(front + "0" + front[::-1])
    return int(front + front[::-1])
    

print nextpal(1)
print nextpal(12)
print nextpal(10)
print nextpal(12345)
print nextpal(12456)
print nextpal(12410)
print nextpal(1234)
print nextpal(100000000)
print nextpal(100000100)
            
        
        
        