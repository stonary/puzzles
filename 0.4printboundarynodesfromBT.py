'''0.4 print boundary nodes in Binary Tree'''


# recursion? not working

class Node:
    
    def __init__(self, value, lc=None, rc=None):
        self.value = value
        self.lc = lc
        self.rc = rc
    

def boundary(node):
    print node.value
    l = node.lc
    r = node.rc
    while l != None:
        print l.value
        l = l.lc
    while r != None:
        print r.value
        r = r.rc
    return;
    
root = Node(7, Node(6, Node(4, Node(3), Node(5))), 
                Node(10, Node(8, Node(7)), Node(11, Node(9))))

