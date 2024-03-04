import random

from avl_tree import insert

def find_min(root):
    if root is None:
        return root
    
    if not root.left:
        return root
    else:
        return find_min(root.left)


root = None
keys =  [random.randint(-30, 100) for _ in range(20)]
print(keys)

for key in keys:
    root = insert(root, key)
  
    
res = find_min(root)
print(res.val)