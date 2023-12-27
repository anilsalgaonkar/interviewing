import binarytree
import math

print(binarytree.bst)


def validate(node, low, high):
    # Empty trees are valid BSTs.
    if node is None:
        return True

    print( low, node.val, high)
    # The current node's value must be between low and high.
    if node.val <= low  or node.val >= high:
        return False

    # The left and right subtree must also be valid.
    return validate(node.left,low, node.val) and validate(node.right,node.val, high)


validate(binarytree.bst, -math.inf, math.inf)