import random

from avl_tree import insert

def find_sum(root):
   if not root:
       return 0
   else:
       return (root.val + find_sum(root.left) + find_sum(root.right))
    


root = None
keys =  set(random.randint(-30, 100) for _ in range(105))

for key in keys:
    root = insert(root, key)
    

print(find_sum(root))
print(sum(keys))
