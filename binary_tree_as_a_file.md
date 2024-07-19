# Logical explanation of file_management.py
* **Writing binary tree in the file**<br>
  1. Passed root node as an argument to the write_in_file() function
  2. Opened the file 'binary_tree_as_file' in the 'w' write mode
  3. Performing BFS on the tree, instead of printing value, writing the value in the file and if node is None the writing '*' in file
* **Creating tree by reading from file**
    1. 'binary_tree_as_file' stores BFS traversal of binary tree, with '*' in place on None
    2. Opened 'binary_tree-as_file' in the 'r' read mode.
    3. Read data from file using file.read()
    4. Using split() to split the string of node values stored in data into a list based on whitespaces
    5. Traversed the BFS traveresed node values in the list to create binary tree from it.
    6. Returned the root node.
    7. Performed BFS traversal of the tree to ensure that the binary tree created is correct.
