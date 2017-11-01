
import math

"""
all done:
works!!!!
"""
class Tree(object):
    def __init__(self,root=None,data_to_nodes=None):
        if root == None:
            root = TreeNode(1)
        self.root = root
        data_to_nodes = {1:self.root}
        #this will be useful in traversing the tree to add nodes
        #wait maybe not nvmnd will just traverse down tree
        #will think about it finding each node to add its children each time could be costly
        #could keep hashmap of data to nodes yeah that will help

    def swapNodes(self,k,level_lists):
        #not convinced this will work but might so I'll run it and see
        levels = [i for i in range(1,len(level_lists)) if (i%k == 0)]
        
        for level in levels:
            #print("current level")
            #print([node.data for node in level_lists[level]])
            for node in level_lists[level]:
                if node.data != -1:
                    temp = node.left
                    node.left = node.right
                    node.right = temp
        
        
class TreeNode(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
        #note when populating the tree will actually want to leave left and right as None NOT a node containing none at first will update later 

    def printInOrder(self):
        #node is a treenode
        if self != None and self.data != -1:
            self.left.printInOrder()
            print(self.data),
            self.right.printInOrder()

    def printInOrderToFile(self,file):
        #node is a treenode
        if self != None and self.data != -1:
            self.left.printInOrderToFile(file)
            file.write(str(self.data) + " ")
            self.right.printInOrderToFile(file)

    """
    def StringInOrder(self,input_string=None):
        if input_string == None:
            input_string = ""
        if self == None:
            return input_string
        if self != None and self.data != -1:
            input_string += self.left.StringInOrder(input_string)
            input_string += self.data
            input_string += self.right.StringInOrder(input_string)
            return input_string
    """
    def retStringInOrder(self):
        #imma just do this iteratively
        stack = []
        current = self
        ret = ""
        while (current != None and current.data != -1) or len(stack) > 0:
            if (current != None and current.data != -1):
                stack.append(current)
                current = current.left
            else:
                current = stack.pop(-1)
                ret += str(current.data) + " "
                current = current.right
        return ret

t = Tree()
num_nodes = int(raw_input().strip())
i = 0
current_parent_node_list = [t.root]
cpn_idx = 0
level_lists = [None]
#so that we have our indexing right
while i < num_nodes:
    current_parent = current_parent_node_list[cpn_idx]
    if cpn_idx == 0:
        new_parent_node_list = []
    #print("i")
    #print(i)
    if current_parent.data != -1:
        [l_child_data, r_child_data] = raw_input().strip().split(' ')
        i += 1
        [l_child_data, r_child_data] = [int(l_child_data), int(r_child_data)]
        [l_child,r_child] = [TreeNode(l_child_data), TreeNode(r_child_data)]
        #print("new parent node list before")
        #print([node.data for node in new_parent_node_list])
        new_parent_node_list.append(l_child)
        new_parent_node_list.append(r_child)
        #print("new parent node list after")
        #print([node.data for node in new_parent_node_list])
        current_parent.left = l_child
        current_parent.right = r_child
        
    if cpn_idx < len(current_parent_node_list)-1:
        cpn_idx += 1
    else:
        cpn_idx = 0
        level_lists.append(current_parent_node_list)
        current_parent_node_list = new_parent_node_list
    
num_queries = int(raw_input().strip())
for j in range(num_queries):
    k = int(raw_input().strip())
    t.swapNodes(k,level_lists)
    answer = t.root.retStringInOrder()
    print(answer)
