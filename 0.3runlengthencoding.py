'''Run length encoding '''

def runlen(s):
    output = '';
    if not s:
        return output
        
    i = s[0]
    n = 1
    for char in s[0:]:
        if char == i:
            n += 1
        else:
            output += char + str(n)
            i = char
            n = 1
    return output
    
print runlen("") 
print runlen("aaaaaaaaabbbbbbbbccccccdddddddaaaaaaaaeeeeeccccccdddddd")
print runlen("abababdababaabb") 