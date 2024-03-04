import random

from avl_tree import insert

def find_max(root):
    if root is None:
        return root
    
    if not root.right:
        return root
    else:
        return find_max(root.right)


root = None
keys =  [random.randint(-30, 100) for _ in range(20)]
print(keys)

for key in keys:
    root = insert(root, key)
    
res = find_max(root)
print(res.val)