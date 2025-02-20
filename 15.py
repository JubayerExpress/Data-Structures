class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    result = []
    def helper(node):
        if node:
            helper(node.left)
            result.append(node.value)
            helper(node.right)
    helper(root)
    return result

# Example usage:
root = TreeNode(1)
root.right = TreeNode(2, TreeNode(3))
print(inorder_traversal(root))  # Output: [1, 3, 2]
