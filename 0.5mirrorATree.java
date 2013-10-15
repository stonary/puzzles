// mirror a tree

/*
 * Tree node
 */

public class Node {
    
    public int value = NULL;
    public Node lc = NULL;
    public Node rc = NULL;
    
    public Node(int value, Node lc, Node rc) {
        this.value = value;
        this.lc = lc;
        this.rc = rc;
    }
    
    public void setValue(int value) {
        this.value = value;
    }
    
    public int getValue() {
        return this.value;
    }
    
    public void setlc(Node lc) {
        this.lc = lc;
    }
    
    public void setrc(Node rc) {
        this.rc = rc;
    }
    
    public Node getlc() {
        return this.lc;
    }
    
    public Node getrc() {
        this.rc;
    }
}

/**
 * Return the mirror of a Tree rooted at root
 */
public Node mirrorTree(Node root) {
    if (root == NULL) {
        return NULL
    }
    
    return new Node(root.getvalue(), mirrorTree(root.getrl()), 
                                    mirrorTree(root.getlc())); 
}
    
public static void main() {
    
}
        
    