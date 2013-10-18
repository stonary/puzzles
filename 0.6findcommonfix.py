'''Given two String, s1 and s2. to find the longest substring which is prefix 
of s1, as well as suffix of s2'''

from datetime import datetime

def findfix_exhaust(s1, s2):
    begin = datetime.now()
    l = []
    i = 1
    while (i < max(len(s1), len(s2))):
        if (s1[:i] == s2[-(i):]):
            l.append(i)
        i += 1
    end = datetime.now()
    return (s1[: max(l)], end-begin)
    
def findfix_back(s1, s2):
    begin = datetime.now()  
    i = len(s1)
    while (i > 0 and s1[:i] != s2[-i:]):
        i -= 1
    end = datetime.now()
    return (s1[:i], end-begin)
    
# this java answer is much better (from career cup):

'''
public String findLongestSubstring(String s1, String s2) {
        List<Integer> occurs = new ArrayList<>();
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) == s2.charAt(s2.length()-1)) {
                occurs.add(i);
            }
        }
        
        Collections.reverse(occurs);
        
        for(int index : occurs) {
            boolean equals = true;
            for(int i = index; i >= 0; i--) {
                if (s1.charAt(index-i) != s2.charAt(s2.length() - i - 1)) {
                    equals = false;
                    break;
                }
            }
            if(equals) {
                return s1.substring(0,index+1);
            }
        }
        
        return null;
    }

'''


a = findfix_exhaust("abcdefgabcdefgabcdefgabcdefgabcdefgadsffewighhhhhhhhkdsanvvvsdvdsaggggadddsggcc", 
                    "granbdafdagranbdafdagranbdafdagranbdafdagranbdafdagranbda" + 
                    "fgranbdafdagranbdafdagranbdafdagranbdafdagranbdafdagranbda" + 
                    "fdagranbdafdagranbdafdagranbdafdadagranbdafdagranbdafdagra" +
                    "nbdafdagranbdafdagranbdafdagranbdafdagranbdafdagranbdafdagranbdafdagranbdafdabcdfabcdeabcdefgabcdefgabcdefgabcdefgabcdefg")
b = findfix_back("abcdefgabcdefgabcdefgabcdefgabcdefgadsffewighhhhhhhhkdsanvvvsdvdsaggggadddsggcc", 
                    "granbdafdagranbdafdagranbdafdagranbdafdagranbdafdagranbda" + 
                    "fgranbdafdagranbdafdagranbdafdagranbdafdagranbdafdagranbda" + 
                    "fdagranbdafdagranbdafdagranbdafdadagranbdafdagranbdafdagra" +
                    "nbdafdagranbdafdagranbdafdagranbdafdagranbdafdagranbdafdagranbdafdagranbdafdabcdfabcdeabcdefgabcdefgabcdefgabcdefgabcdefg")
assert a[0] == b[0]
print "findfix_exhaust vs. findfix_back /n"
print "{0}\t{1}\n".format(a[1], b[1])

        

