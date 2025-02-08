class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def inorder_traversal(root, elements):
    if root:
        inorder_traversal(root.left, elements)
        elements.append(root.val)
        inorder_traversal(root.right, elements)

def merge_bsts(root1, root2):
    elements1 = []
    elements2 = []
    
    inorder_traversal(root1, elements1)
    inorder_traversal(root2, elements2)

    return merge_sorted_lists(elements1, elements2)

def merge_sorted_lists(list1, list2):
    merged = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# Test cases
root1 = TreeNode(1)
root1.right = TreeNode(3)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(4)

merged_list = merge_bsts(root1, root2)
print("Merged BST:", merged_list)  # Output: [1, 1, 2, 3, 4]

