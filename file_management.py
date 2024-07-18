from collections import deque
class TreeNode:
    def __init__(self, value=0, left= None, right= None):
        self.value=value
        self.left=left
        self.right=right
    
def write_in_file(root):
    queue=deque([root])
    file=open('binary_tree_as_file','w') 
    while queue:
        node=queue.popleft()
        if(node==None):
            file.write('* ')
        else:
            file.write(str(node.value)+' ')
            queue.append(node.left)
            queue.append(node.right)

def read_from_file(file)-> list:
    data = file.read()
    node_values = data.split()
    return node_values

def make_tree(node_values):
    iter_values=iter(node_values) #using iterator
    root=TreeNode(iter_values)
    queue=deque([root])
    while queue:
        node=queue.popleft()
        try:
            left_value=next(iter_values)
            if(left_value=='*'):
                pass
            else:
                node.left=TreeNode(left_value)
                queue.append(node.left)
        except StopIteration:
            break
        try:
            right_value=next(iter_values)
            if(right_value=='*'):
                pass
            else:
                node.right=TreeNode(right_value)
                queue.append(node.right)
        except StopIteration:
            break
    return root


def bfs(root):
    queue=deque([root])
    while queue:
        node=queue.popleft()
        if(node==None):
            print('*',end=' ')
        else:
            print(str(node.value),end=' ')
            queue.append(node.left)
            queue.append(node.right)

#binary_tree_to_file
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
with open('binary_tree_as_file','w') as file:
    write_in_file(root)

# file_to_binary_tree
with open('binary_tree_as_file','r') as file:
    node_values=read_from_file(file)
    root=make_tree(node_values)
bfs(root)