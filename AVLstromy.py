
class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return 0 if not node else node.height

    def insert(self, root, value):
        if(root == None):
            return AVLNode(value)
        elif(value < root.value):
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        return self.rebalance(root)

    def get_balance(self, node):
        return 0 if node == None else self.get_height(node.left) - self.get_height(node.right)
    
    def minmax(self, node):
        return node if not node or not node.left else self.get_min_node(node.left)

    def delete(self, root, value):
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
                minmax = self.minmax(root.right)
                root.value = minmax.value
                root.right = self.delete(root.right, minmax.value)
                return root
            
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
            
        return self.rebalance(root)
            
    def rebalance(self, root):
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
        x = y.left
        right_x = x.right
        x.right = y
        y.left = right_x

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.left))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.left))

        return x

    def left_rotation(self, x):
        y = x.right
        left_y = y.left
        y.left = x
        x.right = left_y

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.left))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.left))

        return y

def print_tree2(root):
        tree = print_horizontal(root)

        for line in tree:
            print(line)

def print_horizontal(root):
        if(not root):
            return [' ']
        else:
            key = str(root.value)
            right_tree = print_horizontal(root.right)
            left_tree = print_horizontal(root.left)

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

class AVLNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.height = 1
        
def main():
    avl = AVLTree()   
    keys = [50, 25, 75, 15, 35, 60, 120, 10, 68, 90, 125, 83, 100]
    
    for key in keys:
        avl.root = avl.insert(avl.root, key)

    print_tree2(avl.root)

    avl.search(125)
    avl.search(1)

    avl.root = avl.delete(avl.root, 120)
    print('\nAfter deleting 120:')
    print_tree2(avl.root)

    avl.root = avl.delete(avl.root, 10)
    print('After deleting 10:')
    print_tree2(avl.root)


main()