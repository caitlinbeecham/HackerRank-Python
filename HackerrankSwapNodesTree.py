"""
does problem outlined in https://www.hackerrank.com/challenges/swap-nodes-algo/problem
works for all but two largest test cases
still debugging for those but just uploading what I have from doing this this morning
"""

class Tree(object):
    def __init__(self,root=None,data_to_nodes=None):
        if root == None:
            root = TreeNode(1)
        self.root = root
        

    def swapNodes(self,k,level_lists):
        #not convinced this will work but might so I'll run it and see
        #does except for two very large test cases
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
        
    def printInOrder(self):
        if self != None and self.data != -1:
            self.left.printInOrder()
            print(self.data),
            self.right.printInOrder()


"""
the below block is constructing our tree given the input
because the input format is weird with some "holes" so to speak 
(i.e. we could not just append stuff to a heap and then turn into a tree)
this is not trivial
what I do is keep a list of parent_nodes (that is updated as we iterate through each level)
that I simulateously iterate through as I get user input which dictates the children of these parent nodes
"""
t = Tree()
num_nodes = int(input().strip())
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
        [l_child_data, r_child_data] = input().strip().split(' ')
        i += 1
        [l_child_data, r_child_data] = [int(l_child_data), int(r_child_data)]
        """
        print()
        print("current parent data != -1")
        print("cpn_idx")
        print(cpn_idx)
        print("current_parent_node_list")
        print([node.data for node in current_parent_node_list])
        print("current_parent.data")
        print(current_parent.data)
        print("left and right childs data")
        print([l_child_data, r_child_data])
        """
        [l_child,r_child] = [TreeNode(l_child_data), TreeNode(r_child_data)]
        #print("new parent node list before")
        #print([node.data for node in new_parent_node_list])
        new_parent_node_list.append(l_child)
        new_parent_node_list.append(r_child)
        #print("new parent node list after")
        #print([node.data for node in new_parent_node_list])
        current_parent.left = l_child
        current_parent.right = r_child
    #else:
        """
        print()
        print("currrent parent data is -1")
        print("cpn_idx")
        print(cpn_idx)
        print("current_parent_node_list")
        print([node.data for node in current_parent_node_list])
        print("current_parent.data")
        print(current_parent.data)
        """
    if cpn_idx < len(current_parent_node_list)-1:
        cpn_idx += 1
    else:
        cpn_idx = 0
        level_lists.append(current_parent_node_list)
        current_parent_node_list = new_parent_node_list
    
num_queries = int(input().strip())
for j in range(num_queries):
    k = int(input().strip())
    t.swapNodes(k,level_lists)
    t.root.printInOrder()
    print()
