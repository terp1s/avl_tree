class AVLNode:
    """
    A class representing a node in an AVL tree.
    
    Attributes
    ----------
    value : int
        value of the node
    left : AVLNode
        the left child of the node, or root of the left subtree (default None)
    right : AVLNode
        the right child of the node, or root of the right subtree (default None)
    height : int
        height of the node. Leaves have height 1. Height of nodes with asymetrical subtrees are one
        larger than the height of the higher subtree. (default 1)
    """

    def __init__(self, val):
        """
        Parameters
        ----------
        value : int
            value of the node"""
        
        self.value = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """
    A class representing AVL tree, which is a type of self-balancing tree.
    
    Attributes
    ----------
    root : AVLNode
        root of the tree

    Methods
    -------
    get_height(node): 
        Returns height of a node.

    get_balance(self, node):
        Retrurns balance of a node. Balance is the difference between height od left and right subtree.

    get_min_node(self, root):
        Returns the smallest (=leftmost) node of a tree.

    insert(self, root, value):
        Inserts value into tree, then returns its root. Duplicates are exluded.

    delete(self, root, value):
        Deletes value from tree, then returns its root.

    rebalance(self, root):
        Rebalances tree and returns its root.

    search(self, value):
        Searches for a value in tree using binary tree traversal. Returns text result of the search.
    
    right_rotation(self, y):
        Performs right rotation of the root y, then returns the new root.
    
    left_rotation(self, x):
        Performs left rotation of a root x, then returns the new root, y.
    
    print_tree(root):
        Gets a list of lines representing the tree and prints them.
    
    print_vertical(root):
        Returns a list of lines creating vertical visual representation of the tree.    
    """
    def __init__(self):
        self.root = None

    def get_height(node):
        """Returns height of a node."""
        return 0 if not node else node.height
    
    def get_balance(self, node):
        """Retrurns balance of a node. Balance is the difference between height od left and right subtree."""
        return 0 if node == None else self.get_height(node.left) - self.get_height(node.right)
    
    def get_min_node(self, root):
        """Returns the smallest (=leftmost) node of a tree."""
        return root if not root or not root.left else self.get_min_node(root.left)

    def insert(self, root, value):
        """Inserts value into tree, then returns its root. Duplicates are exluded.

        First, using binary tree traversal, finds the position to insert the node.
        While exiting recursion updates height of every parent and returns root of a rebalanced tree.
        
        Parameters
        ----------
        root : AVLNode
            root of the tree
        value : int
            value of a node the users wishes to insert
        """

        if(root == None):
            return AVLNode(value)
        elif(value < root.value):
            root.left = self.insert(root.left, value)
        elif(value > root.value):
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        return self.rebalance(root)

    def delete(self, root, value):
        """Deletes value from tree, then returns its root.

        First finds the node. If it is not in the tree, then its root is returned without changes.

        The node is deleted in the same manner as from a regular binary tree. If it has no children,
        the node is simply deleted. If it has one child, it is placed in the position of the deleted node.
        In the unfortunate occrance it has two children, the next succesor of the node is found and switched
        with the original node, making it a leaf, which then gets deleted.

        After deleting the node it recalculates height for every parent, rebalances the tree and returns its root.

        Parameters
        ----------
        root : AVLNode
            root of the tree
        value : int
            value of a node the users wishes to delete
        """
        
        if(root == None):
            return root
        elif(value > root.value):
            root.right = self.delete(root.right, value)
        elif(value < root.value):
            root.left = self.delete(root.left, value)
        else:
            if(root.left == None):
                temp = root.right
                root = None
                return temp
            elif(root.right == None):
                temp = root.left
                root = None
                return temp
            else:
                minmax = self.get_min_node(root.right)
                root.value = minmax.value
                root.right = self.delete(root.right, minmax.value)
                return root
            
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
            
        return self.rebalance(root)
            
    def rebalance(self, root):
        """Rebalances tree and returns its root.

        First gets balances of the root and left and right subtree. According to whether it is left/right heavy
        it performs according rotation.

        Parameters
        ----------
        root : AVLNode
            root of the tree
        """

        b_root = self.get_balance(root)
        b_left = self.get_balance(root.left)
        b_right = self.get_balance(root.right)

        if b_root < -1 and b_right <= 0:
            return self.left_rotation(root)
        if b_root > 1 and b_left >= 0:
            return self.right_rotation(root)
        if b_root < -1 and b_right > 0:
            root.right = self.right_rotation(root.right)
            return self.left_rotation(root)
        if b_root > 1 and b_right < 0:
            root.left = self.left_rotation(root.left)
            return self.right_rotation(root)
        
        return root

    def search(self, value):
        """Searches for a value in tree using binary tree traversal. Returns text result of the search.

        Parameters
        ----------
        value : int
            value of the node to be found"""
        
        node = self.root

        while(node != None):
            if(value > node.value):
                node = node.right
            elif(value < node.value):
                node = node.left
            elif(value == node.value):
                break

        print(f'{value} found' if node else f'{value} not found')

    def right_rotation(self, y):
        """Performs right rotation of the root y, then returns the new root, x.
        
        T1, T2 and T3 are subtrees of the tree, rooted with y (on the left side) or x (on the right side)     
      
            y                               x
           / \     Right Rotation          /  \\
          x   T3   - - - - - - - >        T1   y 
         / \       < - - - - - - -            / \\
        T1  T2     Left Rotation            T2  T3
        
        Then height of both roots is updates.
        
        Parameters
        ----------
        y : AVLNode
            roof of the tree to be rotated"""

        x = y.left
        right_x = x.right
        x.right = y
        y.left = right_x

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.left))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.left))

        return x

    def left_rotation(self, x):
        """Performs left rotation of a root x, then returns the new root, y.
        
        T1, T2 and T3 are subtrees of the tree, rooted with y (on the left side) or x (on the right side)     
      
            y                               x
           / \     Right Rotation          /  \\
          x   T3   - - - - - - - >        T1   y 
         / \       < - - - - - - -            / \\
        T1  T2     Left Rotation            T2  T3
        
        Then height of both roots is updates.
        
        Parameters
        ----------
        x : AVLNode
            roof of the tree to be rotated"""

        y = x.right
        left_y = y.left
        y.left = x
        x.right = left_y

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.left))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.left))

        return y

def print_tree(root):
        """Gets a list of lines representing the tree and prints them.

        Parameters
        ----------
        root : AVLNode
            root of the tree to be printed"""
        tree = print_vertical(root)

        for line in tree:
            print(line)

def print_vertical(root):
        """Returns a list of lines creating vertical visual representation of the tree.

        For each node get left and right subtree and creates the representation of the node, which may
        look like ths:  +-(125) or +-(125)+, depending on whether it is a leaf.

        Then right subtree, root and left subtree, respectively, are added to a common list that is representing
        the whole tree. Subtrees are connected to its root using '|'. It is added to a line, if it
        is below (to the left of the) root of the right subtree. And in the same manner for the left subtree.
        
        The printed tree may look like this:

               +-(125)
        +-(120)+
               |     +-(100)
               +-(90)+
                     +-(83)

        Parameters
        ----------
        root : AVLNode
            root of the tree to be printed"""
        
        if(not root):
            return [' ']
        else:
            key = str(root.value)
            right_tree = print_vertical(root.right)
            left_tree = print_vertical(root.left)

            if(not root.left and not root.right):
                line_root = '+-(' + key + ')'
            else:
                line_root = '+-(' + key + ')+'
            
            tree_out = []
            before_root = True

            for i in range(len(right_tree)):
                if(before_root):
                    if(right_tree[i][0] == '+'):
                        tree_out.append(' '*(4+len(key))+ right_tree[i])
                        before_root = False
                    else:
                        tree_out.append(' '*(4+len(key)) + right_tree[i])
                elif(right_tree[i][-1] != ' '):
                    tree_out.append(' '*(4+len(key)) + '|' + right_tree[i][1:])

            tree_out.append(line_root)
            before_root = True

            for i in range(len(left_tree)):
                if(before_root):
                    if(left_tree[i][0] == '+'):
                        tree_out.append(' '*(4+len(key)) + left_tree[i])
                        before_root = False
                    elif(left_tree[i][-1] != ' '):
                        tree_out.append(' '*(4+len(key)) + '|'+ left_tree[i][1:])
                else:
                    tree_out.append(' '*(4+len(key))  + left_tree[i])     
                
        return tree_out
        
def main():
    avl = AVLTree()   
    keys = [50, 25, 75, 15, 35, 60, 120, 10, 68, 90, 125, 83, 100]
    
    for key in keys:
        avl.root = avl.insert(avl.root, key)

    print_tree(avl.root)

    avl.search(125)
    avl.search(1)

    avl.root = avl.delete(avl.root, 120)
    print('\nAfter deleting 120:')
    print_tree(avl.root)

    avl.root = avl.delete(avl.root, 10)
    print('After deleting 10:')
    print_tree(avl.root)


main()