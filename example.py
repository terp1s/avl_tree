from AVLstromy import *

def main():
    """An example how to use each function."""

    avl = AVLTree()   
    keys = [50, 25, 75, 15, 35, 60, 120, 10, 68, 90, 125, 83, 100]
    
    """Insert function returns root of the new tree, so inserting is done as rewriting the root"""
    for key in keys:
        avl.root = avl.insert(avl.root, key)

    """printing a tree"""
    print_tree(avl.root)

    """searching for a value"""
    avl.search(125)
    avl.search(1)

    avl.root = avl.delete(avl.root, 120)
    print('\nAfter deleting 120:')
    print_tree(avl.root)

    avl.root = avl.delete(avl.root, 10)
    print('After deleting 10:')
    print_tree(avl.root)


main()